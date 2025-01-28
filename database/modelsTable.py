from .databaseMain import Base
from sqlalchemy import Integer, Column, String

class dataUsers(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    job = Column(String(255))
    salary = Column(Integer)
    role = Column(String(255))