import os

from flask import Flask
from flask_restful import Resource, Api, reqparse

from loremerson.generators import StringGen


data_path = os.environ['LOREMERSON_DATA_PATH']

# Instantiate the sentence and heading generators.
sentence_gen = StringGen(os.path.join(data_path, "all_gentext.dat"))
heading_gen = StringGen(os.path.join(data_path, "headings.dat"))

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
parser.add_argument('headings',
                    type=int,
                    help='number of headings')

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
