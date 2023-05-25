from fastapi import HTTPException


def valid_zip(uszip: str):
    if not uszip:
        raise HTTPException(status_code=400, detail='Zip is null')
    if uszip.strip() == '':
        raise HTTPException(status_code=400, detail='Zip is null')
    if len(uszip) > 5:
        raise HTTPException(status_code=400, detail='Incorrect zip')


def valid_miles(miles: int):
    if not miles:
        raise HTTPException(status_code=400, detail='Miles is null')
    if miles < 0:
        raise HTTPException(status_code=400, detail='Incorrect miles')


def valid_weight(weight: int):
    if not weight:
        raise HTTPException(status_code=400, detail='Weight is null')
    if weight <= 0:
        raise HTTPException(status_code=400, detail='Incorrect weight')
    if weight > 1000:
        raise HTTPException(status_code=400, detail='Incorrect weight')


def valid_description(description: str):
    if not description:
        raise HTTPException(status_code=400, detail='Description is null')
    if description.strip() == '':
        raise HTTPException(status_code=400, detail='Description is null')
    if len(description) > 255:
        raise HTTPException(status_code=400, detail='Description is too long')


def valid_location(latitude: float, longitude: float):
    if latitude == 0:
        latitude = 0.99999999
    if longitude == 0:
        longitude = 0.99999999
    if not latitude:
        raise HTTPException(status_code=400, detail='Latitude is null')
    if latitude < -90:
        raise HTTPException(status_code=400, detail='Incorrect latitude')
    if latitude > 90:
        raise HTTPException(status_code=400, detail='Incorrect latitude')
    if not longitude:
        raise HTTPException(status_code=400, detail='Longitude is null')
    if longitude < -180:
        raise HTTPException(status_code=400, detail='Incorrect longitude')
    if longitude > 180:
        raise HTTPException(status_code=400, detail='Incorrect longitude')
