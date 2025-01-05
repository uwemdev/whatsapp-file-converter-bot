from flask import Flask
from dotenv import load_dotenv
import os
from app.routes import routes

load_dotenv()

app = Flask(__name__)
app.register_blueprint(routes)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, port=port)
