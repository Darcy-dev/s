from flask import Flask
from flask_restplus import Api, Resource

from src.server.istance import Servidor

app, api = server.app, server.api

books_db = [
    {"id": 0, 'title': 'Die Stimme'},
    {"id": 1, "title": "Clean Code"}
]

@api.route('/t')
class BookList(Resource):
    def get(self, ):
        return books_db