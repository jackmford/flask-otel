import requests
from flask import Flask
app = Flask(__name__)

app.route("/")
def main():
    response = requests.get('https://jackmitchellfordyce.com')
    print(response)

    return response.status_code

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')