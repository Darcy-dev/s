from http import server
from turtle import title
from flask import Flask
from flask_restplus import Api

class Servidor():
    def __init__(self,  ):
        self.app = Flask(__name__)
        self.api = Api(self.app,
        version='1.0',
        title='Sample API',
        description='Gotta deploy it on HEROKU AND AWS',
        doc='/docs'
        )

    def run(self, ):
        self.app.run(
            debug=True
        )

server = Servidor()

if __name__ == "__main__":
    app.run(debug=True)