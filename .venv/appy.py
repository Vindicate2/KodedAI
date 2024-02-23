from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the AI Bots' world!"

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template

# ... rest of your Flask app ...

@app.route('/')
def home():
    return render_template('home.html')

from flask import Flask
from yourapplication.routes import routes

app = Flask(__name__)
app.register_blueprint(routes)

# Rest of the file...

from flask import Flask
# Adjust the import path based on your project structure
from routes import routes

app = Flask(__name__)

# Register the Blueprint
app.register_blueprint(routes)

# Other configurations for your Flask app go here

if __name__ == '__main__':
    app.run(debug=True)
