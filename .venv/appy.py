from flask import Flask, render_template, request, jsonify
import subprocess
from importlib_resources import files

data_path = files('example').joinpath('data/data_file')

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

def check_library(library_name):
    try:
        dist = pkg_resources.get_distribution(library_name)
        print(f"{library_name} version {dist.version} is already installed.")
        return True
    except pkg_resources.DistributionNotFound:
        print(f"{library_name} is not installed.")
        return False

def install_library(library_name):
    if not check_library(library_name):
        try:
            subprocess.check_call(["pip", "install", library_name])
            print(f"{library_name} has been successfully installed.")
        except subprocess.CalledProcessError:
            print(f"Installation of {library_name} failed.")

if __name__ == '__main__':
    app.run(debug=True)