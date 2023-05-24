from fastapi import HTTPException
from sqlalchemy.orm import Session

from sql.crud import add_crg
from models import schemas
from controllers.validation_controller import valid_zip, valid_weight, valid_description


def cargo_add(cargo: schemas.NewCargo, db: Session):
    valid_zip(cargo.delivery)
    valid_zip(cargo.pick_up)
    valid_weight(cargo.weight)
    valid_description(cargo.description)
    return add_crg(cargo, db)
