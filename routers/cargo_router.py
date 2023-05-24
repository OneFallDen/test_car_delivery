from fastapi import routing, HTTPException

from models import schemas


router = routing.APIRouter()


@router.post('/cargo', tags=['cargo'], status_code=201)
async def add_cargo(cargo: schemas.NewCargo):
    return 0


@router.get('/cargo/{cargoId}', tags=['cargo'])
async def get_cargo_by_id(cargoId: int):
    return 0


@router.get('/cargo', tags=['cargo'])
async def get_cargos():
    return 0


@router.put('/cargo/{cargoId}', tags=['cargo'])
async def update_cargo(cargoId: int, cargo: schemas.UpdateCargo):
    return 0


@router.delete('/cargo/{cargoId}', tags=['cargo'])
async def delete_cargo(cargoId: int):
    return 0
