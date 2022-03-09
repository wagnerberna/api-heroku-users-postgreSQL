from src.service.postgresql import Postgresql


db = Postgresql()

connection = Postgresql().postgresql_connect()


class LoginModel:
    def find_login(self, login):
        # "," converte de string para tupla
        sql_query = """SELECT * FROM public.user WHERE login = %s"""
        login_to_fetch = (login,)
        
        data_result = db.fetch_one(sql_query, login_to_fetch)
        # print(data_result)
        return data_result

    def update_status(self, login, status):
        sql_query = """UPDATE public.user SET activated=%s WHERE login=%s"""
        data_update = (status, login)
        data_result = db.execute_modify(sql_query, data_update)
        return data_result
