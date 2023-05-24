from fastapi import FastAPI

from routers import car_router, cargo_router


app = FastAPI()


app.include_router(car_router.router)
app.include_router(cargo_router.router)
