from pydantic import BaseModel
from typing import Optional


class PokemonPayloadSchema(BaseModel):
    name: str
    type: str
    team_id: int


class PokemonResponseSchema(PokemonPayloadSchema):
    id: int
