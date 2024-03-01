from flask import Flask

app = Flask(__name__)

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
    return jsonify({'output': output.decode('utf-8'), 'error': error.decode('utf-8')})

from importlib_metadata import version, PackageNotFoundError

def get_package_version(package_name):
    try:
        return version(package_name)
    except PackageNotFoundError:
        return f'No package metadata was found for {package_name}'

print(get_package_version("my_package"))

def check_library(library_name):
    try:
        dist = pkg_resources.get_distribution(library_name)
        print(f"{library_name} version {dist.version} is already installed.")
        return True
    except pkg_resources.DistributionNotFound:
        print(f"{library_name} is not installed.")
        return False

import subprocess

def install_library(library_name):
    try:
        subprocess.check_call(["pip", "install", library_name])
        print(f"{library_name} has been successfully installed.")
        return True
    except subprocess.CalledProcessError:
        print(f"Installation of {library_name} failed.")
        return False

def download_library(library_name):
    if not check_library(library_name):
        install_library(library_name)

        if __name__ == '__main__':
            app.run(debug=True)

# Importing flask module in the project
from flask import Flask

# Initialising the flask app with the name 'app'
app = Flask(__name__)

# Defining a route
@app.route('/')
# Function that will complete this endpoint
def home():
    return "Hello, World!"

# Main driver function
if __name__ == '__main__':

    # The run() method of Flask class runs the application
    # on the local development server.
    app.run(debug=True)