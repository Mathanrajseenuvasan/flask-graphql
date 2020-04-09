from flask_restplus import Resource
from graphql_service import api
from graphql_service.service.user import _User

ns = api.namespace("user",
           description="sample user api")

@ns.route('/')
class User(Resource):
    def get(self):
        res = _User.all_user()
        return res