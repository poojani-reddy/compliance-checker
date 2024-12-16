from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def generate_embeddings(chunks):
    try:
        embeddings = model.encode(chunks, convert_to_tensor=True)
        return embeddings.tolist()
    except Exception as e:
        raise Exception(f"Error generating embeddings: {e}")
