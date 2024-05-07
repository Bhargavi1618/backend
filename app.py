from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
#CORS(app, resources={r"/receive_response": {"origins": "https://magnificent-salamander-454500.netlify.app"}})
#CORS(app, resources={r"/*": {"origins": "*"}})  # Allow CORS for all origins
CORS(app)
@app.route('/receive_response', methods=['POST'])
@cross_origin()  # Allow CORS for this route
def receive_response():
    print("Received a request!")
    response_data = request.json
    print("Response Data:", response_data)
    # Your processing logic here
    response = jsonify({"message": "Response received"})
    response.headers.add('Access-Control-Allow-Origin', '*')  # Add CORS header
    return response, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
