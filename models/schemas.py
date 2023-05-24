from pydantic import BaseModel


class NewCargo(BaseModel):
    pick_up: str | None
    delivery: str | None
    weight: int | None
    description: str | None


class UpdateCarLoc(BaseModel):
    loc: str | None


class UpdateCargo(BaseModel):
    weight: int | None
    description: str | None
