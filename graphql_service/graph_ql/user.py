# Imports
from graphql_service.models import User
from ..config import db
import graphene
from graphql_service.graph_ql.schema import UserObject

class CreateUser(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)

    user = graphene.Field(lambda: UserObject)

    def mutate(self, info, username):
        user = User(username=username)

        db.session.add(user)
        db.session.commit()
        return CreateUser(user=user)