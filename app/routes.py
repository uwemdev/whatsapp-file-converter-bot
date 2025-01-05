from flask import Blueprint

routes = Blueprint('routes', __name__)

@routes.route('/', methods=['GET'])
def home():
    return "WhatsApp File Converter Bot is Running!"
