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

    response_data = request.json
    if 'response' in response_data:
        user_response = response_data['response']
        print("User Response:", user_response)
        # Process the user response here
        # For example, you can save it to a database or perform other actions based on the response
        response_message = {"message": "Response received", "data": user_response}
        return jsonify(response_message), 200
    else:
        return jsonify({"error": "Invalid request format"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
