from cryptography.fernet import Fernet, InvalidToken
from os import environ

SALT = environ["SALT"]
ENCRYPTIONKEY = environ["ENCRYPTION_KEY"]
FERNETCRYPT = Fernet(ENCRYPTIONKEY.encode("utf-8") + SALT.encode("utf-8"))

def encrypt(str_to_enc):
    return str(FERNETCRYPT.encrypt(str_to_enc.encode("utf-8")).decode("utf-8")) # i want to return a string
    
def decrypt(enc_str):
    try:
        res = str(FERNETCRYPT.decrypt(enc_str.encode("utf-8")).decode("utf-8")) # again i want to return a string
        return res
    except InvalidToken:
        print("invalid token, skip: ", enc_str)
        raise