from fastapi import APIRouter
from tokens.tokenUtilities import TokenSetting

tokenRoute = APIRouter()
TOKENS = TokenSetting()

@tokenRoute.get(path="/token", summary="Generate Token")
def generateToken(dec: str):
    return TOKENS.encrypt_token(dec)


@tokenRoute.get(path="/decryptToken", summary="decrypt token")
def decryptToken(enc: str):
    return TOKENS.decrypt_token(enc)