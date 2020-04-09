from graphql_service.graph_ql import schema
from graphql_service.models import Post
import json

class _Post(object):

    @classmethod
    def all_post(cls):
        query_string = '''
            query allPosts{
                allPosts{
                edges{
                node{
                    body
                    title
                    author{
                        uuid
                        username
                    }
                    }
                }
                }
                }
        '''
        result = schema.execute(
            query_string,
            operation_name='allPosts'
        )
        res = result.data
        return res