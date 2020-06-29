from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/api/person', methods=["POST"])
def login_person():
    data = request.json
    user_name = data.get('user_name', "")
    age = data.get('age', "1000")
    id = data.get('id', "")
    return "Hello"


app.run(host='0.0.0.0', port=5656)
