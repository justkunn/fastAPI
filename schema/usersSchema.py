from pydantic import BaseModel
from typing import List, Optional


class responseData(BaseModel):
    id: int
    name: str
    job: str
    salary: float
    role: str
    
    class Config:
        from_attributes = True
        
class createResponseUsers(BaseModel):
    name: str
    job: str
    salary: float
    role: str
    
    class Config:
        from_attributes = True
        
class responseUsers(BaseModel):
    message: str
    status: str 
    data: List[responseData]
    
    class Config:
        from_attributes = True
        
class updateDataUsers(BaseModel):
    name: Optional[str]
    job: Optional[str]
    salary: Optional[float]
    job: Optional[str]
    
    class Config:
        from_attributes = True
        
class responseDelete(BaseModel):
    message: str
    status: str 
    data: List[responseData]
    
    class Config:
        from_attributes = True