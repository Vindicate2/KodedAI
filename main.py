# main.py
from app import app

if __name__ == "__main__":
    app.run(debug=True)

from package_name import print_package_version

print_package_version("numpy")
