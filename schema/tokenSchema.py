from pydantic import BaseModel

class TokenSchema(BaseModel):
    username: str
    password: str
    
class ResponseLoginBearear(BaseModel):
    access_token: str
    refresh_token: str
    
class ResponseProtected(BaseModel):
    message: str
    
class ResponseRefreshToken(BaseModel):
    access_token: str