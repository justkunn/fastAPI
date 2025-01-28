import os
import base64
from pydantic import BaseModel
from fastapi_jwt_auth import AuthJWT
from config.tokenConfig import TokenConfig
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

class SettingJWT(BaseModel):
    authjwt_secret_key: str = TokenConfig.SECRET_KEY
    print(authjwt_secret_key)
    authjwt_algoryhtm: str = "HS256"
    authjwt_public_key: str = TokenConfig.JWT_PUBLIC_KEY
    authjwt_private_key: str = TokenConfig.JWT_PRIVATE_KEY
    authjwt_acces_token_expire: int = TokenConfig.TOKEN_EXPIRED
    authjwt_refresh_token: int = TokenConfig.TOKEN_REFRESH
    authjwt_token_handle: list = ["headers"]
    authjwt_cookie_csrf_protect: bool = True
    authjwt_cookie_samesite: str = "lax"
    
@AuthJWT.load_config
def get_config():
    return SettingJWT()
    
    
class TokenSetting():
    def __init__(self):
        # inisialisai variabel
        self.key: bytes = self.generate_encrypt_key()
        self.iv: bytes = self.generate_encrypt_iv()
        
    def generate_encrypt_key(self) -> bytes:
        # generate random 32 char
        return os.urandom(32)
    
    def generate_encrypt_iv(self) -> bytes:
        # generate random 16 char
        return os.urandom(16)
    
    def encrypt_token(self, tokens: str) -> bytes:
        # padding data agar panjangnya kelipatan 16
        padder = padding.PKCS7(128).padder()
        padded_token = padder.update(tokens.encode()) + padder.finalize()
        
        # buat chipper menggunakan algoritma AES dan mode CBC
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(self.iv), backend=default_backend())
        encryptor = cipher.encryptor()
        
        # enkripsi token
        encryption_token = encryptor.update(padded_token) + encryptor.finalize()
        
        # gabungkan IV dengan token yg terenkripsi
        result = base64.b64encode(self.iv + encryption_token)
        return result
    
    def decrypt_token(self, decryot_tokens: str) -> bytes:
        decode_token = base64.b64decode(decryot_tokens)
        iv = decode_token[:16]
        encyrpt_message = decode_token[16:]
        
        # buat cipher
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(self.iv), backend=default_backend())
        decryptor = cipher.decryptor()
        
        # dekripsi token
        padded_token = decryptor.update(encyrpt_message) + decryptor.finalize()
        
        unpadder = padding.PKCS7(128).unpadder()
        token = unpadder.update(padded_token) + unpadder.finalize()
        return token.decode()        
    