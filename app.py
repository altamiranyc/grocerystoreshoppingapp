from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({"message": "Grocery Store Shopping App Backend is running!"})

@app.route('/api/test')
def test():
    return jsonify({"status": "success", "message": "API is working!"})

# Add more routes as needed

if __name__ == '__main__':
    app.run()
