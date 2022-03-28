from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class TeamModel(models.Model):
    name = fields.TextField()

    def __str__(self):
        return self.name


TeamSchema = pydantic_model_creator(TeamModel)
