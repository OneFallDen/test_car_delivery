from pydantic import BaseModel

from typing import Union


class NewCargo(BaseModel):
    pick_up: Union[str, None]
    delivery: Union[str, None]
    weight: Union[int, None]
    description: Union[str, None]


class UpdateCarLoc(BaseModel):
    loc: Union[str, None]


class UpdateCargo(BaseModel):
    weight: Union[int, None]
    description: Union[str, None]
