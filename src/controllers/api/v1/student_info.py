from fastapi import APIRouter
from src.schemas.v1.student_info_check import Check

router = APIRouter()

@router.post("/")
def student_info(data : Check):
    return{"data" : data}
