from typing import Dict, Any
from flask import Flask, jsonify, request

app = Flask(__name__)

# Types
Request = Dict[str, Any]
Response = Dict[str, Any]

# Controllers
def index_controller() -> Response:
    return {"message": "Welcome to the API"}

def health_controller() -> Response:
    return {"status": "healthy"}

# Routes
@app.route("/", methods=["GET"])
def index():
    return jsonify(index_controller())

@app.route("/health", methods=["GET"]) 
def health():
    return jsonify(health_controller())

if __name__ == "__main__":
    app.run(port=3000)