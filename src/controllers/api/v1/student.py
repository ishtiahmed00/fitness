from fastapi import APIRouter
from src.schemas.v1.student_schema import StudentSchema

router = APIRouter()

@router.post("/")
def student_info(data : StudentSchema):
    return{"data" : data}