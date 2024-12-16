from flask import request, jsonify
from ..controllers.upload_controller import app
from ..managers.chunk_manager import create_chunks

@app.route('/chunk', methods=['POST'])
def chunk():
    # Parse JSON request data
    data = request.get_json()

    # Validate required fields
    text = data.get('text', '')
    if not isinstance(text, str) or not text.strip():
        return jsonify({"error": "Invalid or missing 'text' in request body"}), 400

    max_chunk_size = data.get('max_chunk_size', 512)
    overlap = data.get('overlap', 50)

    try:
        # Generate chunks
        chunks = create_chunks(text, max_chunk_size, overlap)
        return jsonify({"chunks": chunks}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
