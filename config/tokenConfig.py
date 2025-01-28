import os
import datetime
from dotenv import load_dotenv

expired = datetime.timedelta(minutes=3)
refresh_token = datetime.timedelta(minutes=10)
public_key = open("oauth-public.key").read()
private_key = open("oauth-private.key").read()

load_dotenv()

class TokenConfig:
    SECRET_KEY = "mxA/YunwbxIhc1K7ZNhbsO9vNWJHhVs5CSb4kSQOh8I="
    CLIENT_KEY = os.getenv("CLIENT_ID")
    ENCRYPTION_KEY = "200af68706880879a7d30ecd5ad8bc407b15a7e38eb6a0bba8cc12283418656c"
    IV = "e0dadba31ca191db7b81f97a6436bc68"
    JWT_PUBLIC_KEY = public_key
    JWT_PRIVATE_KEY = private_key
    TOKEN_EXPIRED = expired
    TOKEN_REFRESH = refresh_token