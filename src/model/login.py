from src.service.postgresql import Postgresql

db = Postgresql()

connection = Postgresql().postgresql_connect()


class LoginModel:
    def find_login(self, login):
        # "," convert from string to tuple
        sql_query = """SELECT * FROM public.user WHERE login = %s"""
        login_to_fetch = (login,)

        db_result = db.fetch_one(sql_query, login_to_fetch)
        if db_result == None:
            return False

        payload_result = {
            "login": db_result[3],
            "password": db_result[4],
            "activated": db_result[5],
        }
        return payload_result

    def update_status(self, login, status):
        sql_query = """UPDATE public.user SET activated=%s WHERE login=%s"""
        data_update = (status, login)
        data_result = db.execute_modify(sql_query, data_update)
        return data_result
