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

# Activer CORS (permet à Flutter de communiquer)
CORS(app)

# ============== CONFIGURATION ==============

# URL de Ollama (locale par défaut)
OLLAMA_URL = os.getenv('OLLAMA_URL', 'http://localhost:11434')
OLLAMA_MODEL = 'mistral'

# System prompt : c'est les "instructions" qu'on donne à Mistral
SYSTEM_PROMPT = """Tu es un assistant d'aide pour l'application mobile ADES.
Tu aides les vendeurs à utiliser l'application de vente ADES.

RÈGLES IMPORTANTES :
- Base tes réponses UNIQUEMENT sur la documentation fournie ci-dessous
- Sois précis, clair et concis
- Réponds en français ou malagasy selon la question
- Si tu ne trouves pas l'information dans la documentation, dis-le honnêtement
- Donne des instructions étape par étape quand c'est approprié
- Si la question n'est pas sur l'app ADES, dis poliment que tu ne peux pas aider"""

# Créer le dossier logs s'il n'existe pas
if not os.path.exists('logs'):
    os.makedirs('logs')

# ============== INITIALISATION RAG ==============

print("\n" + "="*60)
print("🚀 DÉMARRAGE DU BACKEND ADES CHATBOT")
print("="*60)

# Initialiser le RAG Searcher
try:
    rag_searcher = RAGSearcher(data_dir='rag/data')
    RAG_ENABLED = True
    print("✅ RAG activé et prêt")
except Exception as e:
    print(f"⚠️  RAG désactivé : {e}")
    print("   Le chatbot fonctionnera sans contexte personnalisé")
    rag_searcher = None
    RAG_ENABLED = False

print("="*60 + "\n")

# ============== FONCTIONS UTILITAIRES ==============

def log_conversation(user_message, bot_response, context_used=None):
    """
    Sauvegarde chaque conversation dans un fichier log
    pour pouvoir analyser plus tard
    """
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

def call_ollama(prompt, temperature=0.3):
    """
    Appelle Ollama (Mistral) avec le prompt fourni
    Retourne la réponse
    """
    try:
        # Préparer la requête pour Ollama
        payload = {
            'model': OLLAMA_MODEL,
            'prompt': prompt,
            'stream': False,
            'temperature': temperature
        }
        
        # Appeler l'API Ollama
        response = requests.post(
            f'{OLLAMA_URL}/api/generate',
            json=payload,
            timeout=60  # Timeout après 60 secondes
        )
        
        # Vérifier si l'appel a réussi
        if response.status_code == 200:
            result = response.json()
            return result.get('response', 'Erreur: pas de réponse')
        else:
            return f'Erreur Ollama: {response.status_code}'
            
    except requests.exceptions.ConnectionError:
        return 'Erreur: Impossible de se connecter à Ollama. Vérifiez que Ollama fonctionne (ollama serve)'
    except requests.exceptions.Timeout:
        return 'Erreur: Ollama a mis trop de temps à répondre'
    except Exception as e:
        return f'Erreur: {str(e)}'

def create_prompt_with_context(user_message, context):
    """
    Crée le prompt complet avec le contexte RAG
    """
    prompt = f"""{SYSTEM_PROMPT}

DOCUMENTATION ADES (extraits pertinents) :
---
{context}
---

QUESTION DU VENDEUR : {user_message}

RÉPONSE (basée uniquement sur la documentation ci-dessus) :"""
    
    return prompt

def create_prompt_without_context(user_message):
    """
    Crée le prompt sans contexte (fallback si RAG désactivé)
    """
    prompt = f"""{SYSTEM_PROMPT}

QUESTION : {user_message}

RÉPONSE :"""
    
    return prompt

# ============== ROUTES API ==============

@app.route('/', methods=['GET'])
def home():
    """
    Route simple pour vérifier que le serveur fonctionne
    """
    return jsonify({
        'status': 'ok',
        'message': 'Backend ADES ChatBot fonctionne!',
        'version': '2.0.0',
        'rag_enabled': RAG_ENABLED
    })

@app.route('/api/health', methods=['GET'])
def health():
    """
    Vérifie la santé du serveur et la connexion à Ollama
    """
    try:
        # Essayer de se connecter à Ollama
        response = requests.get(f'{OLLAMA_URL}/api/tags', timeout=5)
        ollama_status = 'connected' if response.status_code == 200 else 'disconnected'
    except:
        ollama_status = 'disconnected'
    
    # Vérifier le statut du RAG
    rag_status = 'disabled'
    if RAG_ENABLED and rag_searcher:
        rag_health = rag_searcher.health_check()
        rag_status = rag_health.get('status', 'error')
    
    return jsonify({
        'backend': 'running',
        'ollama': ollama_status,
        'rag': rag_status,
        'timestamp': datetime.datetime.now().isoformat()
    })

@app.route('/api/chat', methods=['POST'])
def chat():
    """
    Route principale pour le chatbot avec RAG
    Reçoit une question, cherche dans la doc, appelle Mistral, retourne la réponse
    """
    try:
        # Récupérer le message de la requête
        data = request.get_json()
        user_message = data.get('message', '')
        
        # Valider que le message n'est pas vide
        if not user_message or len(user_message.strip()) == 0:
            return jsonify({
                'error': 'Le message ne peut pas être vide'
            }), 400
        
        # Variable pour stocker le contexte utilisé
        context_used = None
        
        # Créer le prompt avec ou sans RAG
        if RAG_ENABLED and rag_searcher:
            # Rechercher le contexte pertinent
            print(f"🔍 Recherche RAG pour : {user_message[:50]}...")
            context = rag_searcher.get_context(user_message, top_k=3, max_length=2000)
            context_used = context
            
            # Créer le prompt avec contexte
            full_prompt = create_prompt_with_context(user_message, context)
            print(f"✅ Contexte trouvé ({len(context)} caractères)")
        else:
            # Fallback sans RAG
            full_prompt = create_prompt_without_context(user_message)
            print(f"⚠️  Pas de RAG, utilisation du prompt basique")
        
        # Appeler Ollama
        print(f"🤖 Appel à Mistral...")
        bot_response = call_ollama(full_prompt)
        print(f"✅ Réponse reçue")
        
        # Logger la conversation
        log_conversation(user_message, bot_response, context_used)
        
        # Préparer la réponse
        response_data = {
            'status': 'success',
            'user_message': user_message,
            'reply': bot_response,
            'rag_used': RAG_ENABLED and context_used is not None,
            'timestamp': datetime.datetime.now().isoformat()
        }
        
        # Ajouter le contexte si demandé (pour déboguer)
        if data.get('include_context', False) and context_used:
            response_data['context'] = context_used
        
        return jsonify(response_data)
        
    except Exception as e:
        print(f"❌ Erreur dans /api/chat : {e}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/api/search', methods=['POST'])
def search():
    """
    Route pour tester la recherche RAG directement
    Utile pour déboguer
    """
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
        
        # Rechercher
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
    """
    Route pour récupérer les logs de conversation
    Utile pour déboguer et analyser
    """
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
            'logs': logs[-50:]  # Retourner les 50 derniers logs
        })
        
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500

# ============== GESTION ERREURS ==============

@app.errorhandler(404)
def not_found(error):
    """Gère les routes non trouvées"""
    return jsonify({
        'error': 'Route non trouvée',
        'path': request.path
    }), 404

@app.errorhandler(500)
def server_error(error):
    """Gère les erreurs du serveur"""
    return jsonify({
        'error': 'Erreur du serveur',
        'message': str(error)
    }), 500

# ============== MAIN ==============

if __name__ == '__main__':
    print("🚀 Démarrage du backend ADES ChatBot...")
    print(f"📡 Connecté à Ollama: {OLLAMA_URL}")
    print(f"🤖 Modèle: {OLLAMA_MODEL}")
    print(f"🔍 RAG: {'Activé' if RAG_ENABLED else 'Désactivé'}")
    print("\nLe serveur démarre sur http://localhost:3000")
    print("Appuyez sur Ctrl+C pour arrêter\n")
    
    # Lancer le serveur
    app.run(debug=True, host='0.0.0.0', port=3000)