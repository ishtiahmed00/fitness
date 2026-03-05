from fastapi import APIRouter
from src.schemas.v1.teacher_schema import TeacherSchema 

router = APIRouter()

@router.post("/")
def teachers_info(data : TeacherSchema):
    return{"data" : data}