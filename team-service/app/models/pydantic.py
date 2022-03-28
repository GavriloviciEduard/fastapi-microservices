from pydantic import BaseModel


class TeamPayloadSchema(BaseModel):
    name: str


class TeamResponseSchema(TeamPayloadSchema):
    id: int
