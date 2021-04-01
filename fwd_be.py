"""
This app returns the length of a given string.

"""
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class ReturnLength(Resource):
    def get(self):
    	return "Greetings planet"

    def post(self):
    	data = request.form['num_input']
    	return len(data)

api.add_resource(ReturnLength, '/')

if __name__ == '__main__':
    app.run(debug=True, host="localhost", port=5000)

