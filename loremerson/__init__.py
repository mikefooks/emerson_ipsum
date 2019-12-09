import os
from random import shuffle
from flask import Flask
from flask_restful import Resource, Api

from loremerson.sentence_gen import SentenceGen


application = Flask(__name__)
api = Api(application)

data_path = os.environ['LOREMERSON_DATA_PATH']
sent_gen = SentenceGen(data_path)


class Emerson(Resource):
    def get(self):
        return {'cool': sent_gen() }

api.add_resource(Emerson, '/')
