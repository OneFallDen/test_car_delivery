from fastapi import HTTPException
from sqlalchemy import select, and_
from sqlalchemy.orm import Session

from sql import models
from models import schemas


"""
    CAR
"""


def get_car_by_id(carId: int, db: Session):
    result = db.execute(select(models.Car).where(models.Car.id == carId)).first()
    return result[0]


def upd_car(carId: int, loc:  str, db: Session):
    db.query(models.Car).filter(models.Car.id == carId).update(
        {
            models.Car.loc: loc
        }
    )
    res = get_car_by_id(carId, db)
    db.commit()
    return {
        'id': carId,
        'number': res.numb,
        'loc': res.loc,
        'tonnage': res.tonnage
    }


"""
    CARGO
"""
