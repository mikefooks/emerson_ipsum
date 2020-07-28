import sys
import os
import json

from flask import Flask
from flask_restful import Resource, Api, reqparse

from loremerson.generators import StringGen


DATA_PATH = os.environ["EMERSON_DATA_PATH"]

# Instantiate the sentence and heading generators.
sentence_gen = StringGen(os.path.join(DATA_PATH, "sentences.dat"))
heading_gen = StringGen(os.path.join(DATA_PATH, "headings.dat"))

# Initialize the application.
application = Flask(__name__)

# Define query parameters.
parser = reqparse.RequestParser()
parser.add_argument('paras',
                    type=int,
                    help='numbers of paragraphs')
parser.add_argument('sentences',
                    type=int,
                    help='number of sentences')
parser.add_argument('headings',
                    type=int,
                    help='number of headings')

api = Api(application)

# Define the resource.
@api.resource("/")
class EmersonResource (Resource):
    def get (self):
        args = parser.parse_args()
        paras = args['paras'] or 1
        sentences = args['sentences'] or 4
        headings = args['headings'] or 0

        output = {
            'data': [ sentence_gen(count=sentences)
                      for _ in range(paras) ]
        }

        return output, 200, { "Access-Control-Allow-Origin": "*" }
