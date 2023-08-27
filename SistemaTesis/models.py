from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'Students'
    INum = Column(Integer, primary_key=True)
    FirstName = Column(String(15))
    MidName = Column(String(15))
    SurName = Column(String(15))
    SecSurName = Column(String(15))
