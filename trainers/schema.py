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

class CreateTrainer(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    age = graphene.Date()

    class Arguments:
        name = graphene.String()
        age = graphene.Date()

    def mutate(self, info, name, age):
        trainer = Trainer(name=name, age=age)
        trainer.save()

        return CreateTrainer(
            id=trainer.id,
            name=trainer.name,
            age=trainer.age,
        )

class Mutation(graphene.ObjectType):
    create_trainer = CreateTrainer.Field()