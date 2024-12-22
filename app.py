from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/submit', methods=['POST'])
def submit_data():
    data = request.json
    letters = data.get('letters')
    colors = data.get('colors')

    print(f"Received letters: {letters}")
    print(f"Received colors: {colors}")

    # Perform backend processing here

    return jsonify({'status': 'success', 'message': 'Data received!'})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
