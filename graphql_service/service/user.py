from graphql_service.graph_ql import schema
from graphql_service.models import User
import json

class _User(object):

    @classmethod
    def all_user(cls):
        query_string = '''
            query allUsers {
                allUsers{
                edges{
                node{
                    uuid
                    username
                        }
                    }
                }
            }
        '''
        result = schema.execute(
            query_string,
            operation_name='allUsers'
        )
        res = result.data
        return res