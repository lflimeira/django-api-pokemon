import graphene

import trainers.schema

class Query(trainers.schema.Query, graphene.ObjectType):
    pass

class Mutation(trainers.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)