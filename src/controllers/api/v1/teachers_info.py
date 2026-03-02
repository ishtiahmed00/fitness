from fastapi import APIRouter
from src.schemas.v1.teachers_info_check import Check

router = APIRouter()

@router.post("/")
def teachers_info(data : Check):
    return{"data" : data}
