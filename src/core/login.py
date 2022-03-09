from src.model.login import LoginModel
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token

login_model = LoginModel()


class LoginCore:
    def find_login(self, login_received):
        # retorna uma tupla
        login_db = login_model.find_login(login_received)
        if login_db == None:
            return False
        data = {'login': login_db[3], 'password': login_db[4], 'activated': login_db[5]}
        return data

    def check_password(self, password_db, password_received):
        # safe método seguro de comparar string de password retorna boolean
        return safe_str_cmp(password_db, password_received)

    def create_token(self, login):
        # token gerado baseado no login
        return create_access_token(identity=login)
