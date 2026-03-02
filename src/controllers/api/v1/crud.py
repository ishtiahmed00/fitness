from fastapi import APIRouter
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor

router = APIRouter()

#Database Connection
try:
    connection = psycopg2.connect(
        host = 'localhost',
        user = 'postgres',
        database = 'fitness',
        password = 'hello',
        cursor_factory = RealDictCursor
    )
    cursor = connection.cursor()
    print("Database connect successfully")

except Exception as error:
    print("Database not connected")
    print("Error =",error)

#Create
class Check(BaseModel):
    id : int
    name : str
    age : int

@router.post("/")
def create(data : Check):
    cursor.execute(
        f"""
            insert into 
            "user" (id,name, age) 
            values (%s,%s, %s) 
            returning *
        """,
        (   
            data.id,
            data.name,
            data.age
        )
    )
    connection.commit()
    user = cursor.fetchone()
    return{"user" : user}

#Read
@router.get("/")
def read():
    cursor.execute(
        """
            select 
                *
            from "user"
        """
    )

    user = cursor.fetchall()
    return{"user" : user}

#Update
@router.put("/{id}")
def update(data : Check):
    cursor.execute(
        f"""
            update "user"
            set name = %s,
                age = %s
            where id = %s
            returning *
        """,
        (
            data.name,
            data.age,
            data.id
        )
    )
    connection.commit()
    user = cursor.fetchone()
    return{"user" : user}

@router.delete("/{id}")
def delete(id:int):
    cursor.execute(
        f"""
            delete from "user"
            where id = %s
        """,
        (
            id,
        )
    )

    connection.commit()
    return{"status" : "Data successfully deleted"}