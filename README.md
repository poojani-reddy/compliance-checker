# compliance-checker

This project allows users to upload, extract, process, and store PDF data with functionality for validation, chunking, embedding, and vector search.

## Features:
- **File Upload**: Upload PDFs with validation.
- **Text Extraction**: Extract text from uploaded PDFs.
- **Chunking**: Split text into chunks for processing.
- **Embedding**: Generate embeddings from text chunks.
- **Vector Store**: Store and query embeddings using FAISS.

## Folder Structure:
- **`data/`**: Stores uploaded files and vector data.
- **`src/`**: Core source code for controllers, managers, and utilities.
- **`tests/`**: Contains test scripts and requirements.

## Requirements:
- Flask
- PyPDF2
- sentence-transformers
- faiss-cpu
- werkzeug

## Setup:
1. Install dependencies:  
   `pip install -r requirements.txt`
   
2. Run the Flask app:  
   `python src/tests/main.py`

## Endpoints:
- **`/upload`** (POST): Upload PDF file.
- **`/extract`** (GET): Extract text from PDF.
- **`/chunk`** (POST): Split extracted text into chunks.
- **`/embed`** (POST): Generate embeddings for text chunks.

## License:
This project is licensed under the MIT License.
