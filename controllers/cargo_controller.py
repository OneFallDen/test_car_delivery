from fastapi import HTTPException
from sqlalchemy.orm import Session

from sql.crud import add_crg, get_cargo_by_id, upd_cargo
from models import schemas
from controllers.validation_controller import valid_zip, valid_weight, valid_description


def cargo_add(cargo: schemas.NewCargo, db: Session):
    valid_zip(cargo.delivery)
    valid_zip(cargo.pick_up)
    valid_weight(cargo.weight)
    valid_description(cargo.description)
    return add_crg(cargo, db)


def cargo_update(cargoId: int, cargo: schemas.UpdateCargo, db: Session):
    valid_weight(cargo.weight)
    valid_description(cargo.description)
    try:
        get_cargo_by_id(cargoId, db)
    except:
        raise HTTPException(status_code=404, detail=f'Cargo with id={cargoId} not found')
    return upd_cargo(cargoId, cargo, db)
