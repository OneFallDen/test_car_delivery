from fastapi import routing, HTTPException

from models import schemas


router = routing.APIRouter()


@router.put('/car/{carId}', tags=['car'])
async def update_car(carId: int, loc: schemas.UpdateCarLoc):
    return 0
