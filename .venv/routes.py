# routes.py
from app import app
from flask import render_template

@app.route('/')
def home():
    return render_template('home.html')

# Other route definitions...

from flask import Blueprint, request, jsonify
from .bot.koded import Koded
from .bot.guido import Guido
from .bot.sentinel import Sentinel

routes = Blueprint('routes', __name__)

koded = Koded()
guido = Guido()
sentinel = Sentinel()

@routes.route('/ask-koded', methods=['POST'])
def ask_koded():
    data = request.json
    question = data.get('question')
    response = koded.answer_question(question)
    return jsonify({'response': response})

# Add more routes for other functionalities...


# routes.py (or within your Flask app's route definitions)

from flask import Blueprint, request, jsonify
from bot.koded import Koded
from bot.guido import Guido
from bot.sentinel import Sentinel

routes = Blueprint('routes', __name__)

koded = Koded()
guido = Guido()
sentinel = Sentinel()

@routes.route('/ask-koded', methods=['POST'])
def ask_koded():
    data = request.json
    question = data.get('question')
    response = koded.answer_question(question)
    return jsonify({'response': response})

# Add more routes for other functionalities...

# Remember to register your Blueprint in the main app.py if you haven't already.

from flask import request, jsonify
from .bot.koded import scrape_website  # Ensure correct import path

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.json.get('url')
    result = scrape_website(url)
    return jsonify({'result': result})
