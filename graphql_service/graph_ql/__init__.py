# Imports
import graphene
from graphene_sqlalchemy import SQLAlchemyConnectionField
from graphql_service.graph_ql.schema import PostObject, UserObject
from graphql_service.graph_ql.user import CreateUser
from graphql_service.graph_ql.post import CreatePost
from graphql_service.models import User


class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    all_posts = SQLAlchemyConnectionField(PostObject)
    all_users = SQLAlchemyConnectionField(UserObject)

class Mutation(graphene.ObjectType):
    create_post = CreatePost.Field()
    create_user = CreateUser.Field( )


schema = graphene.Schema(query=Query, mutation=Mutation)


