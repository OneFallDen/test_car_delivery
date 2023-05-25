from fastapi import routing, Depends
from sqlalchemy.orm import Session

from sql.db import get_db
from models import schemas
from controllers.cargo_controller import cargo_add, cargo_update, cargo_delete, cargos_get, cargo_get_by_id, \
    cargo_filtered


router = routing.APIRouter()


@router.post('/cargo', tags=['cargo'], status_code=201)
async def add_cargo(cargo: schemas.NewCargo, db: Session = Depends(get_db)):
    return cargo_add(cargo, db)


@router.get('/cargo/{cargoId}', tags=['cargo'])
async def get_cargo_by_id(cargoId: int, db: Session = Depends(get_db)):
    return cargo_get_by_id(cargoId, db)


@router.get('/cargo/filter/{weight}/{miles}', tags=['cargo'])
async def get_cargo_filtered(weight: int, miles: int, db: Session = Depends(get_db)):
    return cargo_filtered(weight, miles, db)


@router.get('/cargo', tags=['cargo'])
async def get_cargos(db: Session = Depends(get_db)):
    return cargos_get(db)


@router.put('/cargo/{cargoId}', tags=['cargo'])
async def update_cargo(cargoId: int, cargo: schemas.UpdateCargo, db: Session = Depends(get_db)):
    return cargo_update(cargoId, cargo, db)


@router.delete('/cargo/{cargoId}', tags=['cargo'])
async def delete_cargo(cargoId: int, db: Session = Depends(get_db)):
    return cargo_delete(cargoId, db)
