from fastapi import APIRouter,Depends
from pydantic import BaseModel
from . database import engine, Base, get_db
from . import models
from sqlalchemy.orm import Session

router = APIRouter()

models.Base.metadata.create_all(bind=engine)


#Base Model
class Check(BaseModel):
    name : str
    age : int

# Create
@router.post("/")
def create(data: Check, db: Session = Depends(get_db)):
    new_data = models.Subscriber(
        name = data.name,
        age = data.age
    )

    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return {"data": new_data}


# Read All
@router.get("/")
def read(db: Session = Depends(get_db)):
    data = db.query(models.Subscriber).all()
    return {"data": data}


#Read by id
@router.get("/{id}")
def read_by_id(id:int, db : Session = Depends(get_db)):
    data = db.query(models.Subscriber).filter(models.Subscriber.id == id).first()
    return {"data" : data}


#Update
@router.put("/{id}")
def update(id: int,data : Check, db : Session = Depends(get_db)):
    selected_data = db.query(models.Subscriber).filter(models.Subscriber.id == id).first()
    
    setattr(selected_data, "name", data.name)
    setattr(selected_data, "age", data.age)

    db.commit()
    db.refresh(selected_data)
    return {"data" : data}


#Delete
@router.delete("/{id}")
def delete(id : int, db : Session = Depends(get_db)):
    data = db.query(models.Subscriber).filter(models.Subscriber.id == id).first()
    
    db.delete(data)
    db.commit()
    return {"status" : "Data successfully Deleted"}

