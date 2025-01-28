from fastapi import APIRouter, Depends, HTTPException
from fastapi_jwt_auth import AuthJWT
from tokens.tokenUtilities import TokenSetting
from schema.tokenSchema import (ResponseLoginBearear, ResponseProtected, ResponseRefreshToken,
    TokenSchema)

tokenRoute = APIRouter()
db_dummy = {"admin": {"username": "admin", "password": "password"}}
TOKENS = TokenSetting()

@tokenRoute.get(path="/token", summary="Generate Token")
def generateToken(dec: str):
    return TOKENS.encrypt_token(dec)


@tokenRoute.get(path="/decryptToken", summary="decrypt token")
def decryptToken(enc: str):
    return TOKENS.decrypt_token(enc)


@tokenRoute.post(path="/loginBearear", summary="login Bearear")
def login(user: TokenSchema, Authorize: AuthJWT = Depends()):
    try:
        if user.username not in db_dummy or db_dummy[user.username]["password"] != user.password:
                raise HTTPException(status_code=401, detail="invalid users")

        access_token = Authorize.create_access_token(subject=user.username)
        refresh_token = Authorize.create_refresh_token(subject=user.username)
        return ResponseLoginBearear(access_token=access_token, refresh_token=refresh_token)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@tokenRoute.get(path="protected")
def protected(Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
        current_user = Authorize.get_jwt_subject()
        return ResponseProtected(message=f"Hello {current_user} welcome to the portal's")
    except Exception as e:
        raise HTTPException(status_code=404, detail=(e))
    
@tokenRoute.get(path="refresh token")
def refreshToken(Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_refresh_token_required()
        current_users = Authorize.get_jwt_subject()
        new_access_token = Authorize.create_access_token(subject=current_users)
        return ResponseRefreshToken(access_token=new_access_token)
    except Exception as e:
        raise HTTPException(status_code=500, detail=(e))