from fastapi import HTTPException
from sqlalchemy.orm import Session
from geopy import distance

from sql.crud import add_crg, get_cargo_by_id, upd_cargo, dlt_cargo, get_all_cargos, get_all_cars, get_location, \
    get_cargos_by_weight
from models import schemas
from controllers.validation_controller import valid_zip, valid_weight, valid_description, valid_miles


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


def cargo_delete(cargoId: int, db: Session):
    try:
        get_cargo_by_id(cargoId, db)
    except:
        raise HTTPException(status_code=404, detail=f'Cargo with id={cargoId} not found')
    return dlt_cargo(cargoId, db)


def get_cargo_list(miles: int, cargos, db: Session):
    cargos_to_send = []
    cars = get_all_cars(db)
    to_skip = []
    count = 0
    for cargo in cargos:
        cargo_loc = get_location(cargo.pick_up, db)
        for car in cars:
            if car.loc in to_skip:
                pass
            elif car.loc == cargo.pick_up:
                count += 1
            else:
                car_loc = get_location(car.loc, db)
                dists = distance.distance((cargo_loc.lat, cargo_loc.lng), (car_loc.lat, car_loc.lng)).miles
                if dists > miles:
                    to_skip.append(car.loc)
                else:
                    count += 1
        cargos_to_send.append(
            {
                'id': cargo.id,
                'pick_up': cargo.pick_up,
                'delivery': cargo.delivery,
                'weight': cargo.weight,
                'description': cargo.description,
                'cars': count
            }
        )
        to_skip.clear()
        count = 0
    return cargos_to_send


def cargos_get(db: Session):
    cargos = get_all_cargos(db)
    if not cargos:
        raise HTTPException(status_code=404, detail='Cargos not found')
    return get_cargo_list(450, cargos, db)


def cargo_filtered(weight: int, miles: int, db: Session):
    valid_miles(miles)
    valid_weight(weight)
    cargos = get_cargos_by_weight(weight, db)
    if not cargos:
        raise HTTPException(status_code=404, detail=f'Cargos with weight={weight} not found')
    return get_cargo_list(miles, cargos, db)


def cargo_get_by_id(cargoId: int, db: Session):
    try:
        cargo = get_cargo_by_id(cargoId, db)
    except:
        raise HTTPException(status_code=404, detail='Cargo not found')
    cargo_loc = get_location(cargo.pick_up, db)
    cars = get_all_cars(db)
    cars_to_send = []
    for car in cars:
        car_loc = get_location(car.loc, db)
        dists = distance.distance((cargo_loc.lat, cargo_loc.lng), (car_loc.lat, car_loc.lng)).miles
        cars_to_send.append(
            {
                car.numb: dists
            }
        )
    return {
        'id': cargoId,
        'pick_up': cargo.pick_up,
        'delivery': cargo.delivery,
        'weight': cargo.weight,
        'description': cargo.description,
        'cars': cars_to_send
    }
