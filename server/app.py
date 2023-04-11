from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from model import ask

app = Flask(__name__)
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["50 per day", "10 per hour"],
    storage_uri="memory://"
)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

@app.route('/api/ask', methods=['POST'])
def handle_ask():
    payload = request.get_json()
    query = payload['query']
    answer = ask(query)
    print (answer)

    response = make_response(jsonify(answer), 200)
    response.headers['Content-Type'] = 'application/json'
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

if __name__ == '__main__':
    app.run(debug=True)