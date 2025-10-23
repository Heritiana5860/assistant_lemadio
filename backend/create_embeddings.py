"""
Script pour créer les embeddings de la documentation ADES
et les stocker dans FAISS pour la recherche sémantique
"""

from sentence_transformers import SentenceTransformer
import faiss
import pickle
import numpy as np
import os

# ============== CONFIGURATION ==============

# Chemin vers la documentation
DOC_PATH = 'docs/ADES_DOCUMENTATION.md'

# Dossier de sortie pour les fichiers générés
OUTPUT_DIR = 'rag/data'

# Modèle d'embedding (multilangue, bon pour français/malagasy)
EMBEDDING_MODEL = 'all-MiniLM-L6-v2'

# Taille des chunks (en caractères approximatif)
CHUNK_SIZE = 500

# ============== FONCTIONS ==============

def load_documentation(file_path):
    """
    Charge la documentation depuis le fichier Markdown
    """
    print(f"📖 Chargement de la documentation depuis {file_path}...")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        print(f"✅ Documentation chargée ({len(content)} caractères)")
        return content
    except FileNotFoundError:
        print(f"❌ Erreur : Fichier {file_path} introuvable")
        return None
    except Exception as e:
        print(f"❌ Erreur lors du chargement : {e}")
        return None

def split_into_chunks(text, chunk_size=500):
    """
    Découpe le texte en chunks intelligents
    
    Stratégie :
    1. D'abord par sections (## ou ###)
    2. Puis par paragraphes si trop grand
    3. Garde un peu de contexte entre chunks
    """
    print(f"✂️  Découpage en chunks de ~{chunk_size} caractères...")
    
    chunks = []
    
    # Séparer par les titres de sections
    sections = text.split('\n## ')
    
    for i, section in enumerate(sections):
        if i > 0:  # Rajouter ## sauf pour le premier
            section = '## ' + section
        
        # Si la section est trop grande, la découper par paragraphes
        if len(section) > chunk_size * 2:
            paragraphs = section.split('\n\n')
            current_chunk = ""
            
            for para in paragraphs:
                # Si ajouter ce paragraphe dépasse la limite
                if len(current_chunk) + len(para) > chunk_size and current_chunk:
                    chunks.append(current_chunk.strip())
                    # Garder un peu de contexte (overlap)
                    current_chunk = para
                else:
                    current_chunk += "\n\n" + para if current_chunk else para
            
            # Ajouter le dernier chunk
            if current_chunk:
                chunks.append(current_chunk.strip())
        else:
            # La section est assez petite, on la garde entière
            if section.strip():
                chunks.append(section.strip())
    
    # Filtrer les chunks trop petits (moins de 50 caractères)
    chunks = [c for c in chunks if len(c) > 50]
    
    print(f"✅ {len(chunks)} chunks créés")
    
    # Afficher quelques exemples
    print("\n📝 Exemples de chunks créés :")
    for i, chunk in enumerate(chunks[:3]):
        preview = chunk[:100].replace('\n', ' ')
        print(f"  Chunk {i+1}: {preview}...")
    
    return chunks

def create_embeddings(chunks, model_name):
    """
    Crée les embeddings pour chaque chunk
    """
    print(f"\n🤖 Chargement du modèle d'embedding : {model_name}...")
    
    try:
        model = SentenceTransformer(model_name)
        print(f"✅ Modèle chargé")
    except Exception as e:
        print(f"❌ Erreur lors du chargement du modèle : {e}")
        return None, None
    
    print(f"🔢 Création des embeddings pour {len(chunks)} chunks...")
    print("⏳ Cela peut prendre 1-2 minutes...")
    
    try:
        # Encoder tous les chunks en une fois
        embeddings = model.encode(chunks, show_progress_bar=True)
        
        print(f"✅ Embeddings créés : {embeddings.shape}")
        print(f"   - Nombre de chunks : {embeddings.shape[0]}")
        print(f"   - Dimension des vecteurs : {embeddings.shape[1]}")
        
        return embeddings, model
    except Exception as e:
        print(f"❌ Erreur lors de la création des embeddings : {e}")
        return None, None

def create_faiss_index(embeddings):
    """
    Crée un index FAISS pour la recherche rapide
    """
    print(f"\n🗄️  Création de l'index FAISS...")
    
    try:
        # Dimension des vecteurs
        dimension = embeddings.shape[1]
        
        # Créer un index simple (L2 distance)
        index = faiss.IndexFlatL2(dimension)
        
        # Ajouter les embeddings à l'index
        index.add(embeddings.astype('float32'))
        
        print(f"✅ Index FAISS créé avec {index.ntotal} vecteurs")
        
        return index
    except Exception as e:
        print(f"❌ Erreur lors de la création de l'index : {e}")
        return None

def save_artifacts(index, chunks, output_dir):
    """
    Sauvegarde l'index FAISS et les chunks
    """
    print(f"\n💾 Sauvegarde des fichiers dans {output_dir}...")
    
    # Créer le dossier s'il n'existe pas
    os.makedirs(output_dir, exist_ok=True)
    
    try:
        # Sauvegarder l'index FAISS
        index_path = os.path.join(output_dir, 'faiss_index.index')
        faiss.write_index(index, index_path)
        print(f"✅ Index FAISS sauvegardé : {index_path}")
        
        # Sauvegarder les chunks
        chunks_path = os.path.join(output_dir, 'chunks.pkl')
        with open(chunks_path, 'wb') as f:
            pickle.dump(chunks, f)
        print(f"✅ Chunks sauvegardés : {chunks_path}")
        
        # Sauvegarder les métadonnées
        metadata = {
            'num_chunks': len(chunks),
            'embedding_model': EMBEDDING_MODEL,
            'chunk_size': CHUNK_SIZE,
            'dimension': index.d
        }
        
        metadata_path = os.path.join(output_dir, 'metadata.pkl')
        with open(metadata_path, 'wb') as f:
            pickle.dump(metadata, f)
        print(f"✅ Métadonnées sauvegardées : {metadata_path}")
        
        return True
    except Exception as e:
        print(f"❌ Erreur lors de la sauvegarde : {e}")
        return False

def test_search(index, chunks, model, test_query="Comment créer une vente?"):
    """
    Teste la recherche avec une question exemple
    """
    print(f"\n🔍 Test de recherche avec : '{test_query}'")
    
    try:
        # Encoder la question
        query_embedding = model.encode([test_query])
        
        # Rechercher les 3 chunks les plus similaires
        distances, indices = index.search(query_embedding.astype('float32'), 3)
        
        print(f"\n📊 Résultats de la recherche :")
        for i, (dist, idx) in enumerate(zip(distances[0], indices[0])):
            print(f"\n  Résultat {i+1} (distance: {dist:.4f}):")
            chunk_preview = chunks[idx][:200].replace('\n', ' ')
            print(f"  {chunk_preview}...")
        
        return True
    except Exception as e:
        print(f"❌ Erreur lors du test : {e}")
        return False

# ============== MAIN ==============

def main():
    """
    Fonction principale
    """
    print("=" * 60)
    print("🚀 CRÉATION DES EMBEDDINGS POUR ADES CHATBOT")
    print("=" * 60)
    
    # 1. Charger la documentation
    documentation = load_documentation(DOC_PATH)
    if documentation is None:
        return
    
    # 2. Découper en chunks
    chunks = split_into_chunks(documentation, CHUNK_SIZE)
    if not chunks:
        print("❌ Aucun chunk créé")
        return
    
    # 3. Créer les embeddings
    embeddings, model = create_embeddings(chunks, EMBEDDING_MODEL)
    if embeddings is None:
        return
    
    # 4. Créer l'index FAISS
    index = create_faiss_index(embeddings)
    if index is None:
        return
    
    # 5. Sauvegarder
    success = save_artifacts(index, chunks, OUTPUT_DIR)
    if not success:
        return
    
    # 6. Tester
    test_search(index, chunks, model)
    
    print("\n" + "=" * 60)
    print("✅ TERMINÉ AVEC SUCCÈS !")
    print("=" * 60)
    print(f"\n📁 Fichiers créés dans {OUTPUT_DIR}/")
    print("  - faiss_index.index (index de recherche)")
    print("  - chunks.pkl (morceaux de documentation)")
    print("  - metadata.pkl (informations)")
    print("\n🎉 Vous pouvez maintenant passer à l'intégration dans app.py")

if __name__ == "__main__":
    main()