# routes.py
from flask import render_template, Blueprint, request, jsonify
from bot.koded import Koded, scrape_website
from bot.guido import Guido
from bot.sentinel import Sentinel

routes = Blueprint('routes', __name__)

koded = Koded()
guido = Guido()
sentinel = Sentinel()

@routes.route('/')
def home():
    return render_template('home.html')

@routes.route('/ask-koded', methods=['POST'])
def ask_koded():
    data = request.json
    question = data.get('question')
    response = koded.answer_question(question)
    return jsonify({'response': response})

@routes.route('/scrape', methods=['POST'])
def scrape():
    url = request.json.get('url')
    result = scrape_website(url)
    return jsonify({'result': result})

# Add more routes for other functionalities...