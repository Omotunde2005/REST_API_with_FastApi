from pydantic import BaseModel
from uuid import UUID, uuid4
from typing import Optional, List
from enum import Enum
from database import Base
from sqlalchemy import Boolean, Column, Integer, String


class Gender(str, Enum):
    male = "male"
    female = "female"


class Status(str, Enum):
    married = "married"
    divorced = "divorced"
    single = "single"


class User(BaseModel):
    first_name: str
    last_name: str
    age: int
    gender: Gender
    status: Status


class UpdateUserInfo(BaseModel):
    first_name: Optional[str]
    second_name: Optional[str]
    age: Optional[int]
    gender: Optional[str]
    status: Optional[Status]


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    second_name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)
    key = Column(String, nullable=False)
    status = Column(String, nullable=False)