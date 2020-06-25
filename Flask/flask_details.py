from flask import Flask, jsonify, request
#from mysql_object
from werkzeug.routing import BaseConverter, ValidationError

from Flask import mysql_import_data

_USERS = {'1': 'Tarek', '2' : 'Freya'}
_IDS = {val: id for id, val in _USERS.items()}

class RegisteredUser(BaseConverter):
    def to_python(self, value):
        if value in _USERS:
            return _USERS[value]
        raise ValidationError

    def to_url(self, value):
        return _IDS[value]

app = Flask(__name__)
app.url_map.converters['registered'] = RegisteredUser

@app.route('/api/person/<registered:person_id>')
def person(person_id):
    response = jsonify({'Hello' : person_id})
    return response

@app.route('/api')
def my_microservice():
    print(request)
    print(request.environ)
    response = jsonify({'Hello' : 'World'})
    print(response)
    print(response.data)
    return response
if __name__ == '__main__':
   # mysql_import_data.write_db()
    app.run()
