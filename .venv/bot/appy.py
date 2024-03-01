from flask import Flask, render_template, request, jsonify
import subprocess
from importlib_metadata import version, PackageNotFoundError

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/run-code', methods=['POST'])
def run_code():
    code = request.form.get('code')

    # Save the code to a file
    with open('user_code.py', 'w') as file:
        file.write(code)

    # Execute the code and capture the output
    process = subprocess.Popen(['python', 'user_code.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    # Return the output as a JSON response
    response = {
        'output': output.decode('utf-8'),
        'error': error.decode('utf-8') if error else None
    }
    return jsonify(response), 400 if error else 200

def check_library(library_name):  # <--- function rewritten
    try:
        return version(library_name)
    except PackageNotFoundError:
        return None

def install_library(library_name):
    if not check_library(library_name):
        try:
            subprocess.check_call(["pip", "install", library_name])
            print(f"{library_name} has been successfully installed.")
        except subprocess.CalledProcessError:
            print(f"Installation of {library_name} failed.")

if __name__ == '__main__':
    app.run(debug=True)

    from flask import Flask, send_from_directory

    app = Flask(__name__, static_url_path='/bot/static')


    @app.route('/bot/static/<path:path>')
    def send_static(path):
        return send_from_directory('static', path)


    if __name__ == "__main__":
        app.run(debug=True)