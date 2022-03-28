from typing import List, Optional

from app.models.pydantic import PokemonPayloadSchema
from models.pokemon import PokemonModel

import logging

log = logging.getLogger("uvicorn")


async def get(id: int) -> Optional[dict]:
    pokemon = await PokemonModel.filter(id=id).first().values()
    if pokemon:
        return pokemon[0]
    return None


async def get_all() -> List:
    return await PokemonModel.all().values()


async def post(payload: PokemonPayloadSchema) -> int:
    pokemon = PokemonModel(
        name=payload.name,
        type=payload.type,
        team_id=payload.team_id,)
    await pokemon.save()
    return pokemon.id


async def delete(id: int) -> int:
    pokemon = await PokemonModel.filter(id=id).first().delete()
    return pokemon


async def put(id: int, payload: PokemonPayloadSchema) -> Optional[dict]:
    pokemon = await PokemonModel.filter(id=id).update(
        name=payload.name,
        type=payload.type,
        team_id=payload.team_id)
    if pokemon:
        return await get(id)
    return None
