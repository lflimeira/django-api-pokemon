import graphene
import graphql_jwt

import trainers.schema
import users.schema
import pokemons.schema

class Query(
        users.schema.Query, 
        trainers.schema.Query, 
        pokemons.schema.Query, 
        graphene.ObjectType
    ):
    pass

class Mutation(users.schema.Mutation, trainers.schema.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)