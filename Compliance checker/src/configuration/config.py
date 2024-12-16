from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    UPLOAD_FOLDER = "./data/uploads"
    FAISS_INDEX_PATH = "./data/vector_store/faiss_index"
    VECTOR_DB_API_KEY = os.getenv("PINECONE_API_KEY")
    VECTOR_DB_ENV = os.getenv("PINECONE_ENVIRONMENT")
