import graphene
import pokepy
from graphene_django import DjangoObjectType

class PokemonType(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()
    height = graphene.Int()
    weight = graphene.Int()
    location_area_encounters = graphene.String()

class Query(graphene.ObjectType):
    pokemon = graphene.Field(
        PokemonType, 
        id=graphene.ID(required=False),
        name=graphene.String(required=False)
    )

    def resolve_pokemon(self, info, **args):
        id = args.get('id', None)
        name = args.get('name', None)
        try:
            query_arg = id
            if query_arg == None:
                query_arg = name
            print(query_arg)
            pokemon = pokepy.V2Client()
            return pokemon.get_pokemon(query_arg)[0]
        except:
            raise Exception('A valid ID or Name must be provide.')
