"""
This app returns the length of a given string.

"""
from flask import Flask, request
from flask_restful import Resource, Api
import requests

app = Flask(__name__)
api = Api(app)

class ReturnLength(Resource):
	def get(self):
		return "Greetings planet"

	def post(self):
		str_received = request.form['usr_input']
		return len(str_received)

api.add_resource(ReturnLength, '/')

if __name__ == '__main__':
	app.run(debug=True, host="localhost", port=5000)

