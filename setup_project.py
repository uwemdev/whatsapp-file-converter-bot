import os

# Define folder structure
folders = [
    "app",
    "app/converters",
    "app/utils",
    "static"
]

files = {
    ".env": "",
    "requirements.txt": "",
    "README.md": "# WhatsApp File Converter Bot\n\n",
    ".gitignore": "venv/\n__pycache__/\n*.pyc\n.env\nstatic/",
    "app/__init__.py": "",
    "app/routes.py": """from flask import Blueprint

routes = Blueprint('routes', __name__)

@routes.route('/', methods=['GET'])
def home():
    return "WhatsApp File Converter Bot is Running!"
""",
    "app/converters/image_converter.py": "",
    "app/converters/audio_converter.py": "",
    "app/converters/video_converter.py": "",
    "app/utils/storage_handler.py": "",
    "app/utils/file_validator.py": "",
    "app.py": """from flask import Flask
from dotenv import load_dotenv
import os
from app.routes import routes

load_dotenv()

app = Flask(__name__)
app.register_blueprint(routes)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, port=port)
"""
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files
for file_path, content in files.items():
    with open(file_path, "w") as file:
        file.write(content)

print("Project structure created successfully!")
