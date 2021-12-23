from flask import Flask
import os
import requests

app = Flask(__name__)

@app.route("/")
def get():
    SERVICE_URL = os.environ.get("SERVICE_URL")
    response = requests.get(f'{SERVICE_URL}')
    return response.text

@app.route('/config')
def config():
    return os.environ.get("SERVICE_URL")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')