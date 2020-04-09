from flask_restplus import Resource
from graphql_service import api
from graphql_service.service.post import _Post

ns = api.namespace("post",
           description="sample post api")

@ns.route('/')
class User(Resource):
    def get(self):
        res = _Post.all_post()
        return res