# Import necessary modules
from flask import Flask, render_template, request, jsonify, send_from_directory
import subprocess
from importlib_metadata import version, PackageNotFoundError

# Define app
app = Flask(__name__, static_url_path='/bot/static')

# Define route to send static files
@app.route('/bot/static/<path:path>')
def send_static(path):
    return send_from_directory('../static', path)

# Define route to run code
@app.route('/run-code', methods=['POST'])
def run_code():
    # remaining code
    pass  # Placeholder. Replace 'pass' with your actual code.

# Define home route
@app.route('/')
def home():
    return render_template('home.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)