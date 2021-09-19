import ast
import pandas as pd
import random
import requests
from data import *
from flask import Flask
from flask_restful import Api, reqparse, Resource
from random import randint

app = Flask(__name__)
api = Api(app)

class nums(Resource):
    def get(self):
        data = randint(1, 10)
        return {'data': data}, 200

class names(Resource):
    def get(self):
        data = ticket[randint(0,len(ticket) - 1)]
        return {'data': data}, 200

class getDelInfo(Resource):
    def get(self):
        headers = {
            'Content-Type': 'application/json',
        }
        response = requests.get('http://<server-ip>/users', headers=headers)
        for i in range(len(response.json())):
            requests.delete(str('http://<server-ip>/users/' + response.json()[i]['id']), headers=headers)
        return response.json(), 200

class getPersonInfo(Resource):
    def get(self):
        headers = {
            'Content-Type': 'application/json',
        }
        response = requests.get('http://<server-ip>/users', headers=headers)
        number = randint(0, len(response.json()) - 1)
        name = response.json()[number]['name']
        num = response.json()[number]['num']
        return {'name': name, 'num': num}, 200

api.add_resource(nums, '/nums')
api.add_resource(names, '/names')
api.add_resource(getDelInfo, '/getDelInfo')
api.add_resource(getPersonInfo, '/getPersonInfo')

if __name__ == '__main__':
    app.run(host="<local-ip>")
