from fastapi import APIRouter
from src.controllers.api.v1 import bike_controllers
from src.controllers.api.v1 import car_controllers
from src.controllers.api.v1 import election_controllers
from src.controllers.api.v1 import home_controllers
from src.controllers.api.v1 import laptop_controllers
from src.controllers.api.v1 import mobile_controllers
from src.controllers.api.v1 import student_info
from src.controllers.api.v1 import teachers_info


router = APIRouter()


router.include_router(bike_controllers.router, prefix="/bike")
router.include_router(car_controllers.router, prefix="/car")
router.include_router(election_controllers.router, prefix="/election")
router.include_router(home_controllers.router, prefix="/home")
router.include_router(laptop_controllers.router, prefix="/laptop")
router.include_router(mobile_controllers.router, prefix="/mobile")
router.include_router(student_info.router, prefix="/student")
router.include_router(teachers_info.router, prefix="/teacher")



