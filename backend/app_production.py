from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import json
import datetime
import os
from dotenv import load_dotenv
from rag_search import RAGSearcher

# Charger les variables d'environnement
load_dotenv()

# Créer l'application Flask
app = Flask(__name__)
CORS(app)

# ============== CONFIGURATION ==============

# Mode de déploiement : utilise HuggingFace au lieu d'Ollama
USE_HUGGINGFACE = os.getenv('USE_HUGGINGFACE', 'false').lower() == 'true'
HUGGINGFACE_API_KEY = os.getenv('HUGGINGFACE_API_KEY', '')
HUGGINGFACE_MODEL = "mistralai/Mistral-7B-Instruct-v0.2"

# Ollama (pour développement local)
OLLAMA_URL = os.getenv('OLLAMA_URL', 'http://localhost:11434')
OLLAMA_MODEL = 'mistral'

# System prompt
SYSTEM_PROMPT = """Tu es un assistant d'aide pour l'application mobile Lemadio d'ADES.
Tu aides les vendeurs à utiliser l'application de vente.

RÈGLES IMPORTANTES :
- Base tes réponses UNIQUEMENT sur la documentation fournie ci-dessous
- Sois précis, clair et concis
- Réponds en français ou malagasy selon la question
- Si tu ne trouves pas l'information dans la documentation, dis-le honnêtement
- Donne des instructions étape par étape quand c'est approprié"""

# Créer le dossier logs s'il n'existe pas
if not os.path.exists('logs'):
    os.makedirs('logs')

# ============== INITIALISATION RAG ==============

print("\n" + "="*60)
print("🚀 DÉMARRAGE DU BACKEND ADES CHATBOT")
print("="*60)
print(f"Mode: {'Production (HuggingFace)' if USE_HUGGINGFACE else 'Développement (Ollama)'}")

# Initialiser le RAG Searcher
try:
    rag_searcher = RAGSearcher(data_dir='rag/data')
    RAG_ENABLED = True
    print("✅ RAG activé et prêt")
except Exception as e:
    print(f"⚠️  RAG désactivé : {e}")
    rag_searcher = None
    RAG_ENABLED = False

print("="*60 + "\n")

# ============== FONCTIONS UTILITAIRES ==============

def log_conversation(user_message, bot_response, context_used=None):
    """Sauvegarde chaque conversation"""
    timestamp = datetime.datetime.now().isoformat()
    log_entry = {
        'timestamp': timestamp,
        'user': user_message,
        'bot': bot_response,
        'context_used': context_used is not None,
        'rag_enabled': RAG_ENABLED
    }
    
    log_file = 'logs/conversations.jsonl'
    
    try:
        with open(log_file, 'a', encoding='utf-8') as f:
            f.write(json.dumps(log_entry, ensure_ascii=False) + '\n')
    except Exception as e:
        print(f"Erreur lors du logging: {e}")

def call_huggingface(prompt):
    """Appelle HuggingFace Inference API"""
    try:
        headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
        
        payload = {
            "inputs": prompt,
            "parameters": {
                "max_new_tokens": 512,
                "temperature": 0.3,
                "top_p": 0.95,
                "return_full_text": False
            }
        }
        
        response = requests.post(
            f"https://api-inference.huggingface.co/models/{HUGGINGFACE_MODEL}",
            headers=headers,
            json=payload,
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            if isinstance(result, list) and len(result) > 0:
                return result[0].get('generated_text', 'Erreur: pas de réponse')
            return 'Erreur: format de réponse invalide'
        else:
            return f'Erreur HuggingFace: {response.status_code}'
            
    except Exception as e:
        return f'Erreur: {str(e)}'

def call_ollama(prompt):
    """Appelle Ollama (développement local)"""
    try:
        payload = {
            'model': OLLAMA_MODEL,
            'prompt': prompt,
            'stream': False,
            'temperature': 0.3
        }
        
        response = requests.post(
            f'{OLLAMA_URL}/api/generate',
            json=payload,
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            return result.get('response', 'Erreur: pas de réponse')
        else:
            return f'Erreur Ollama: {response.status_code}'
            
    except Exception as e:
        return f'Erreur: {str(e)}'

def call_llm(prompt):
    """Appelle le LLM approprié selon l'environnement"""
    if USE_HUGGINGFACE:
        return call_huggingface(prompt)
    else:
        return call_ollama(prompt)

def create_prompt_with_context(user_message, context):
    """Crée le prompt complet avec le contexte RAG"""
    prompt = f"""{SYSTEM_PROMPT}

DOCUMENTATION LEMADIO (extraits pertinents) :
---
{context}
---

QUESTION DU VENDEUR : {user_message}

RÉPONSE (basée uniquement sur la documentation ci-dessus) :"""
    
    return prompt

# ============== ROUTES API ==============

@app.route('/', methods=['GET'])
def home():
    """Route simple pour vérifier que le serveur fonctionne"""
    return jsonify({
        'status': 'ok',
        'message': 'Backend ADES ChatBot Lemadio fonctionne!',
        'version': '2.0.0',
        'rag_enabled': RAG_ENABLED,
        'mode': 'production' if USE_HUGGINGFACE else 'development'
    })

@app.route('/api/health', methods=['GET'])
def health():
    """Vérifie la santé du serveur"""
    llm_status = 'connected'
    
    if not USE_HUGGINGFACE:
        try:
            response = requests.get(f'{OLLAMA_URL}/api/tags', timeout=5)
            llm_status = 'connected' if response.status_code == 200 else 'disconnected'
        except:
            llm_status = 'disconnected'
    
    rag_status = 'disabled'
    if RAG_ENABLED and rag_searcher:
        rag_health = rag_searcher.health_check()
        rag_status = rag_health.get('status', 'error')
    
    return jsonify({
        'backend': 'running',
        'llm': llm_status,
        'rag': rag_status,
        'mode': 'production' if USE_HUGGINGFACE else 'development',
        'timestamp': datetime.datetime.now().isoformat()
    })

@app.route('/api/chat', methods=['POST'])
def chat():
    """Route principale pour le chatbot avec RAG"""
    try:
        data = request.get_json()
        user_message = data.get('message', '')
        
        if not user_message or len(user_message.strip()) == 0:
            return jsonify({
                'error': 'Le message ne peut pas être vide'
            }), 400
        
        context_used = None
        
        # Créer le prompt avec ou sans RAG
        if RAG_ENABLED and rag_searcher:
            print(f"🔍 Recherche RAG pour : {user_message[:50]}...")
            context = rag_searcher.get_context(user_message, top_k=3, max_length=2000)
            context_used = context
            
            full_prompt = create_prompt_with_context(user_message, context)
            print(f"✅ Contexte trouvé ({len(context)} caractères)")
        else:
            full_prompt = f"{SYSTEM_PROMPT}\n\nQUESTION: {user_message}\n\nRÉPONSE:"
            print(f"⚠️  Pas de RAG")
        
        # Appeler le LLM
        print(f"🤖 Appel au LLM...")
        bot_response = call_llm(full_prompt)
        print(f"✅ Réponse reçue")
        
        # Logger la conversation
        log_conversation(user_message, bot_response, context_used)
        
        return jsonify({
            'status': 'success',
            'user_message': user_message,
            'reply': bot_response,
            'rag_used': RAG_ENABLED and context_used is not None,
            'timestamp': datetime.datetime.now().isoformat()
        })
        
    except Exception as e:
        print(f"❌ Erreur dans /api/chat : {e}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/api/search', methods=['POST'])
def search():
    """Route pour tester la recherche RAG directement"""
    try:
        if not RAG_ENABLED or not rag_searcher:
            return jsonify({
                'error': 'RAG non disponible'
            }), 503
        
        data = request.get_json()
        query = data.get('query', '')
        top_k = data.get('top_k', 3)
        
        if not query:
            return jsonify({
                'error': 'Query manquante'
            }), 400
        
        results = rag_searcher.get_detailed_results(query, top_k=top_k)
        
        return jsonify({
            'query': query,
            'results': results,
            'count': len(results)
        })
        
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500

@app.route('/api/logs', methods=['GET'])
def get_logs():
    """Route pour récupérer les logs de conversation"""
    try:
        logs = []
        log_file = 'logs/conversations.jsonl'
        
        if os.path.exists(log_file):
            with open(log_file, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.strip():
                        logs.append(json.loads(line))
        
        return jsonify({
            'total': len(logs),
            'logs': logs[-50:]
        })
        
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500

# ============== GESTION ERREURS ==============

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'error': 'Route non trouvée',
        'path': request.path
    }), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({
        'error': 'Erreur du serveur',
        'message': str(error)
    }), 500

# ============== MAIN ==============

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    print(f"🚀 Serveur démarrant sur le port {port}")
    app.run(debug=False, host='0.0.0.0', port=port)