#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    id = Column(Integer(),primary_key=true)
    name = Column(string())
    pass

if __name__ == '__main__':
    pass