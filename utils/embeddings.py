from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

def create_embeddings(chunks):
    embeddings = model.encode(chunks)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings, dtype='float32'))
    return index, embeddings

def search_index(query, index, chunks, top_k=3):
    q_vec = model.encode([query])
    D, I = index.search(np.array(q_vec, dtype='float32'), top_k)
    return [chunks[i] for i in I[0]]
