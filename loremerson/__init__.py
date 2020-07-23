import os
from random import shuffle
from flask import Flask
from flask_restful import Resource, Api, reqparse

from loremerson.sentence_gen import SentenceGen

# Instantiate the sentence generator.
data_path = os.environ['LOREMERSON_DATA_PATH']
sent_gen = SentenceGen(data_path)

# Initialize the application.
application = Flask(__name__)
api = Api(application)

# Define query parameters.
parser = reqparse.RequestParser()
parser.add_argument('paras',
                    type=int,
                    help='numbers of paragraphs')
parser.add_argument('sentences',
                    type=int,
                    help='number of sentences')
parser.add_argument('format',
                    type=str,
                    help='output format: one of json, html, text')

# Define the resource.
class EmersonGuest(Resource):
    def get(self):
        args = parser.parse_args()
        paras = args['paras'] or 1
        sentences = args['sentences'] or 4
        format = args['format'] or 'json'

        paragraphs = [ sent_gen(count=sentences)
                       for _ in range(paras) ]

        return paragraphs


api.add_resource(EmersonGuest, '/')
