from lib import bcrypt
from bcrypt import hashpw, checkpw


def crypt_password(password):
    try:
        print("service password")
        salt = bcrypt.gensalt()
        print("-pass salt:::", salt)
        password_hashed = bcrypt.hashpw(password.encode("utf8"), salt)
        print("-pass hash:::", password_hashed)
        return password_hashed
    except Exception as error:
        print(error)


def compare_password(password, password_hashed):
    try:
        if bcrypt.checkpw(password.encode("utf8"), password_hashed.encode("utf8")):
            print("Password ok")
            return True
        return False
    except Exception as error:
        print(error)
