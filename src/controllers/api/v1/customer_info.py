from fastapi import APIRouter
from src.schemas.v1.check import Customer_info_check
from src.database_connection.connection import cursor, connection

router = APIRouter()

#Create 
@router.post("/")
def create_customer(data : Customer_info_check):
    cursor.execute(
        f"""
            insert into
            "customer_info" (id,name, address, contact)
            values(%s,%s,%s,%s)
            returning *
        """,
        (
            data.id,
            data.name,
            data.address,
            data.contact
        )
    )
    connection.commit()
    returning_data = cursor.fetchone()
    return{"data" : returning_data}


#Read
@router.get("/")
def read():
    cursor.execute(
        """
            select
                *
            from "customer_info"
        """
    )
    data = cursor.fetchall()
    return{"data" : data}

#Read by id
@router.get("/{id}")
def read_by_id(id : int):
    cursor.execute(
        f"""
            select
                *
            from customer_info
            where id = %s
        """,
        (
            id,
        )
    )
    data = cursor.fetchone()
    return{"data" : data}


#Update
@router.put("/")
def create(data : Customer_info_check):
    cursor.execute(
        f"""
            update "customer_info"
            set name = %s,
                address = %s,
                contact = %s
            where id = %s
            returning *
        """,
        (
            data.name,
            data.address,
            data.contact,
            data.id
        )
    )
    connection.commit()
    updated_data = cursor.fetchone()
    return{"data" : updated_data}


#Delete
@router.delete("/{id}")
def delete(id : int):
    cursor.execute(
        f"""   
            delete 
            from customer_info
            where id = %s
        """,
        (
            id,
        )
    )
    connection.commit()
    return{"status" : "data deleted successfully"}

    