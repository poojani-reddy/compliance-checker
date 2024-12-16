from flask import Flask
from src.configuration.config import Config

# Initialize the Flask application
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = Config.UPLOAD_FOLDER

# Import all routes/controllers
from src.models.controllers.upload_controller import *
from src.models.controllers.ingestion_controller import *
from src.models.controllers.chunk_controller import *
from src.models.controllers.embedding_controller import *

if __name__ == "__main__":
    app.run(debug=True)




