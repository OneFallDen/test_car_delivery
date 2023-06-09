from sqlalchemy import select
from sqlalchemy.orm import Session

from sql import models
from models import schemas


"""
    CAR
"""


def get_all_cars(db: Session):
    result = db.execute(select(models.Car)).scalars().all()
    return result


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


def get_cargos_by_weight(weight: int, db: Session):
    result = db.execute(select(models.Cargo).where(models.Cargo.weight == weight)).scalars().all()
    return result


def get_all_cargos(db: Session):
    result = db.execute(select(models.Cargo)).scalars().all()
    return result


def get_cargo_by_id(cargoId: int, db: Session):
    result = db.execute(select(models.Cargo).where(models.Cargo.id == cargoId)).first()
    return result[0]


def add_crg(cargo: schemas.NewCargo, db: Session):
    db_cargo = models.Cargo(
        pick_up=cargo.pick_up,
        delivery=cargo.delivery,
        weight=cargo.weight,
        description=cargo.description
    )
    db.add(db_cargo)
    db.commit()
    db.refresh(db_cargo)
    return {
        'id': db_cargo.id,
        'pick_up': db_cargo.pick_up,
        'delivery': db_cargo.delivery,
        'weight': db_cargo.weight,
        'description': db_cargo.description
    }


def upd_cargo(cargoId: int, cargo: schemas.UpdateCargo, db: Session):
    db.query(models.Cargo).filter(models.Cargo.id == cargoId).update(
        {
            models.Cargo.weight: cargo.weight,
            models.Cargo.description: cargo.description
        }
    )
    res = get_cargo_by_id(cargoId, db)
    db.commit()
    return {
        'id': cargoId,
        'pick_up': res.pick_up,
        'delivery': res.delivery,
        'weight': cargo.weight,
        'description': cargo.description
    }


def dlt_cargo(cargoId: int, db: Session):
    db.query(models.Cargo).filter(models.Cargo.id == cargoId).delete()
    db.commit()


"""
    LOCATION
"""


def get_location(uszip: str, db: Session):
    result = db.execute(select(models.Location).where(models.Location.zip == str(int(uszip)))).first()
    return result[0]
