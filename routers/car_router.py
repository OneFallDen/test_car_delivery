from fastapi import routing, Depends
from sqlalchemy.orm import Session


from sql.db import get_db
from models import schemas
from controllers.car_controller import car_update


router = routing.APIRouter()


@router.put('/car/{carId}', tags=['car'])
async def update_car(carId: int, loc: schemas.UpdateCarLoc, db: Session = Depends(get_db)):
    return car_update(carId, loc.loc, db)
