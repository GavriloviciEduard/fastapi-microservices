from typing import List, Optional

from app.models.pydantic import TeamPayloadSchema
from models.team import TeamModel


async def get(id: int) -> Optional[dict]:
    team = await TeamModel.filter(id=id).first().values()
    if team:
        return team[0]
    return None


async def get_all() -> List:
    return await TeamModel.all().values()


async def post(payload: TeamPayloadSchema) -> int:
    team = TeamModel(name=payload.name)
    await team.save()
    return team.id


async def delete(id: int) -> int:
    team = await TeamModel.filter(id=id).first().delete()
    return team


async def put(id: int, payload: TeamPayloadSchema) -> Optional[dict]:
    team = await TeamModel.filter(id=id).update(name=payload.name)
    if team:
        return await get(id)
    return None
