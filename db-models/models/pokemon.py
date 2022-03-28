from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator
from models.team import TeamModel


class PokemonModel(models.Model):
    name = fields.TextField()
    type = fields.TextField()
    team = fields.ForeignKeyField(
        'models.TeamModel',
        on_delete=fields.CASCADE,)

    def __str__(self):
        return self.name


PokemonSchema = pydantic_model_creator(PokemonModel)
