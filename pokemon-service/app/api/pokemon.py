from typing import List
from fastapi import APIRouter, status, Path, HTTPException
from app.api import crud
from app.models.pydantic import PokemonPayloadSchema, PokemonResponseSchema
from app.api.interservice import team_exists

router = APIRouter(prefix="/pokemon")


@router.get("/{id}/", response_model=PokemonResponseSchema)
async def get_pokemon(id: int = Path(..., gt=0)) -> PokemonResponseSchema:
    pokemon = await crud.get(id)
    if not pokemon:
        raise HTTPException(status_code=404, detail="Pokemon not found!")
    return pokemon


@router.get("/", response_model=List[PokemonResponseSchema])
async def get_all_pokemon() -> List[PokemonResponseSchema]:
    return await crud.get_all()


@router.post("/", response_model=PokemonResponseSchema, status_code=status.HTTP_201_CREATED)
async def create_pokemon(payload: PokemonPayloadSchema) -> PokemonResponseSchema:
    if not team_exists(payload.team_id):
        raise HTTPException(
            status_code=404,
            detail=f"Team with id:{payload.team_id} not found!")
    pokemon_id = await crud.post(payload)
    return {"id": pokemon_id,
            "name": payload.name,
            "type": payload.type,
            "team_id": payload.team_id}


@router.delete("/{id}/")
async def delete_pokemon(id: int = Path(..., gt=0)) -> int:
    pokemon = await crud.get(id)
    if not pokemon:
        raise HTTPException(status_code=404, detail="Pokemon not found!")
    await crud.delete(id)
    return id


@router.put("/{id}/", response_model=PokemonResponseSchema)
async def update_pokemon(payload: PokemonPayloadSchema, id: int = Path(..., gt=0)) -> PokemonResponseSchema:
    if not team_exists(payload.team_id):
        raise HTTPException(
            status_code=404,
            detail=f"Team with id:{payload.team_id} not found!")
    pokemon = await crud.put(id, payload)
    if not pokemon:
        raise HTTPException(status_code=404, detail="Pokemon not found!")
    return pokemon
