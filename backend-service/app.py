from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def get():
    SERVICE_NAME = os.environ.get("SERVICE_NAME")
    return f'Hello from {SERVICE_NAME}'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')