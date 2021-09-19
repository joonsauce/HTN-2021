import ast
import pandas as pd
import random
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
        data = ticket[randint(0,3)]
        return {'data': data}, 200

api.add_resource(nums, '/nums')
api.add_resource(names, '/names')

if __name__ == '__main__':
    app.run(host="<your-ip-here>")
