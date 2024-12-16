import os
from flask import request, jsonify
from werkzeug.utils import secure_filename
from ..managers.upload_manager import validate_pdf
from src.configuration.config import Config

# Assume `app` is imported from the main entry point
from flask import current_app as app

@app.route('/upload', methods=['POST'])
def upload_pdf():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    filename = secure_filename(file.filename)
    file_path = os.path.join(Config.UPLOAD_FOLDER, filename)

    # Save file to configured upload folder
    os.makedirs(Config.UPLOAD_FOLDER, exist_ok=True)  # Ensure folder exists
    file.save(file_path)

    if not validate_pdf(file_path):
        return jsonify({"error": "Invalid PDF format"}), 400

    return jsonify({"message": "File uploaded successfully!", "file_path": file_path})


