from flask import Flask, jsonify, request
from ..managers.ingestion_manager import extract_text

app = Flask(__name__)  # Define or import the app object

@app.route('/extract', methods=['GET'])
def extract():
    file_path = request.args.get('file_path')
    if not file_path:
        return jsonify({"error": "file_path parameter is required"}), 400

    try:
        text = extract_text(file_path)
        return jsonify({"extracted_text": text}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
