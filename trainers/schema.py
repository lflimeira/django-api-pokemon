import graphene
from graphene_django import DjangoObjectType

from .models import Trainer

class TrainerType(DjangoObjectType):
    class Meta:
        model = Trainer

class Query(graphene.ObjectType):
    trainers = graphene.List(TrainerType)

    def resolve_trainers(self, info, **kwargs):
        return Trainer.objects.all()

