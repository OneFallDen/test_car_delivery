from fastapi import routing, Depends
from sqlalchemy.orm import Session

from sql.db import get_db
from models import schemas
from controllers.cargo_controller import cargo_add, cargo_update


router = routing.APIRouter()


@router.post('/cargo', tags=['cargo'], status_code=201)
async def add_cargo(cargo: schemas.NewCargo, db: Session = Depends(get_db)):
    return cargo_add(cargo, db)


@router.get('/cargo/{cargoId}', tags=['cargo'])
async def get_cargo_by_id(cargoId: int, db: Session = Depends(get_db)):
    return 0


@router.get('/cargo', tags=['cargo'])
async def get_cargos(db: Session = Depends(get_db)):
    return 0


@router.put('/cargo/{cargoId}', tags=['cargo'])
async def update_cargo(cargoId: int, cargo: schemas.UpdateCargo, db: Session = Depends(get_db)):
    return cargo_update(cargoId, cargo, db)


@router.delete('/cargo/{cargoId}', tags=['cargo'])
async def delete_cargo(cargoId: int, db: Session = Depends(get_db)):
    return 0
