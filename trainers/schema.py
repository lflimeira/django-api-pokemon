import graphene
from graphene_django import DjangoObjectType

from .models import Trainer
from users.schema import UserType

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
    created_by = graphene.Field(UserType)

    class Arguments:
        name = graphene.String()
        age = graphene.Date()

    def mutate(self, info, name, age):
        user = info.context.user or None
        trainer = Trainer(
            name=name,
            age=age,
            created_by=user,
        )
        trainer.save()

        return CreateTrainer(
            id=trainer.id,
            name=trainer.name,
            age=trainer.age,
            created_by=trainer.created_by,
        )

class Mutation(graphene.ObjectType):
    create_trainer = CreateTrainer.Field()