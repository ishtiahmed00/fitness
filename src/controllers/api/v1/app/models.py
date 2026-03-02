from . database import Base
from sqlalchemy import Integer,String
from sqlalchemy.orm import Mapped,mapped_column

class Subscriber(Base):
    __tablename__ = "subscriber"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
