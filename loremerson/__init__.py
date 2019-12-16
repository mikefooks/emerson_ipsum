import os
from random import shuffle
from flask import Flask
from flask_restful import Resource, Api, reqparse

from loremerson.sentence_gen import SentenceGen


application = Flask(__name__)
api = Api(application)

parser = reqparse.RequestParser()
parser.add_argument('s', type=int, help='number of sentences')
parser.add_argument('p', type=int, help='numbers of paragraphs')

data_path = os.environ['LOREMERSON_DATA_PATH']
sent_gen = SentenceGen(data_path)


class EmersonGuest(Resource):
    def get(self):
        args = parser.parse_args()

        sentences, paras = args['s'], args['p']
        
        if sentences:
            if paras:
                text = [ sent_gen(count=sentences)
                         for _ in range(paras) ]
                return { 'text': text }
            else:
                return {
                    'text': sent_gen(count=sentences)
                }
        
        if paras:
            text = [ sent_gen(count=1)
                    for _ in range(paras) ]
            return { 'text' : text }

        return { 'text' : sent_gen(count=1) }

        
    def _build_paragraphs (self, sent_counts):
        paragraphs = []
        for n in sent_count_list:
            paragraphs.append(sent_gen(count=n))

        return { 'text': paragraphs }

                      
api.add_resource(EmersonGuest, '/')
