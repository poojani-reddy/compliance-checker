from flask import request, jsonify
from ..controllers.upload_controller import app
from ..managers.embedding_manager import generate_embeddings

@app.route('/embed', methods=['POST'])
def embed():
    data = request.get_json()
    chunks = data.get('chunks', [])

    # Validate chunks
    if not isinstance(chunks, list) or not chunks:
        return jsonify({"error": "Invalid or missing 'chunks' in request body"}), 400

    try:
        embeddings = generate_embeddings(chunks)
        return jsonify({"embeddings": embeddings}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
