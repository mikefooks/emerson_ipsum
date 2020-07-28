import sys
import os
import json

from flask import Flask, request, make_response
from flask_restful import Resource, Api, reqparse
from flask_restful.utils import unpack

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

# Define different mimetype representations
@api.representation('application/json')
def json_response (data, code, headers):
    resp = make_response(json.dumps(data), code)
    resp.headers.extend(headers or {})
    return resp

@api.representation('text/html')
def html_response (data, code, headers):
    data = [ '<p>' + p + '</p>' for p in data ]
    data = '\n'.join(data['text'])
    resp = make_response(data, code)
    resp.headers.extend(headers or {})
    return resp

@api.representation('text/plain')
def text_response (data, code, headers):
    data = '\n'.join(data['text'])
    resp = make_response(data, code)
    resp.headers.extend(headers or {})
    return resp

# Define the resource.
@api.resource("/")
class EmersonResource (Resource):
    def get (self):
        args = parser.parse_args()
        paras = args['paras'] or 1
        sentences = args['sentences'] or 4
        headings = args['headings'] or 0

        return {
            'text': [ sentence_gen(count=sentences)
                      for _ in range(paras) ]
        }
