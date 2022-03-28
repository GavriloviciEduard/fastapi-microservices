from typing import List
from fastapi import APIRouter, status, Path, HTTPException
from app.api import crud
from models.team import TeamSchema
from app.models.pydantic import TeamPayloadSchema, TeamResponseSchema

router = APIRouter(prefix="/teams")


@router.get("/{id}/", response_model=TeamSchema)
async def get_team(id: int = Path(..., gt=0)) -> TeamSchema:
    team = await crud.get(id)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found!")
    return team


@router.get("/", response_model=List[TeamSchema])
async def get_all_teams() -> List[TeamSchema]:
    return await crud.get_all()


@router.post("/", response_model=TeamResponseSchema, status_code=status.HTTP_201_CREATED)
async def create_team(payload: TeamPayloadSchema) -> TeamResponseSchema:
    team_id = await crud.post(payload)
    return {"id": team_id, "name": payload.name}


@router.delete("/{id}/")
async def delete_team(id: int = Path(..., gt=0)) -> int:
    team = await crud.get(id)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found!")
    await crud.delete(id)
    return id


@router.put("/{id}/", response_model=TeamSchema)
async def update_team(payload: TeamPayloadSchema, id: int = Path(..., gt=0)) -> TeamSchema:
    team = await crud.put(id, payload)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found!")
    return team
