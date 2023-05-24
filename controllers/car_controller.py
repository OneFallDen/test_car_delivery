from fastapi import HTTPException
from sqlalchemy.orm import Session

from sql.crud import upd_car, get_car_by_id
from controllers.validation_controller import valid_zip


def car_update(carId: int, loc: str, db: Session):
    valid_zip(loc)
    try:
        get_car_by_id(carId, db)
    except:
        raise HTTPException(status_code=404, detail=f'Car with id={carId} not found')
    return upd_car(carId, loc, db)
