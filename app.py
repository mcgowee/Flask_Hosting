from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes   

@app.route('/api/submit', methods=['POST'])
def submit_data():
    data = request.json
    letters = data.get('letters')
    colors = data.get('colors')
    return jsonify({'status': 'success', 'message': 'Data received!'})

if __name__ == "__main__":
    app.run(host="45.132.241.60", port=5000)
