from pydantic import BaseModel

class StudentSchema(BaseModel):
    id : int
    name : str
    department : str