from flask_restplus import Resource
from graphql_service import api

ns = api.namespace("hello world",
           description="sample module api")

@ns.route('/')
class HelloWorld(Resource):
    def get(self):
        return "hello world"