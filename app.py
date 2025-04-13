from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This allows your frontend to communicate with this backend

@app.route('/')
def home():
    return jsonify({"message": "Grocery Store Shopping App Backend is running!"})

@app.route('/api/test')
def test():
    return jsonify({"status": "success", "message": "API is working!"})

# Add more routes as needed for your application

if __name__ == '__main__':
    app.run(debug=True)
