from src.service.postgresql import Postgresql


db = Postgresql()


class UserModel:
    def get_all(self):
        sql_query = """SELECT * FROM db.user"""
        data_result = db.fetch_all(sql_query)
        return data_result

    def get_by_id(self, id):
        # "," converte de string para tupla
        # print("---typer of login 1:::", type(id))
        sql_query = """SELECT * FROM db.user WHERE user_id = %s"""
        id_to_fetch = (id,)
        # print("---typer of login 2:::", type(id))

        data_result = db.fetch_one(sql_query, id_to_fetch)
        return data_result

    def add(self, activated, name, email, login, password):
        sql_query = """INSERT INTO db.user (name, email, login, password, activated) VALUES (%s,%s,%s,%s,%s)"""
        data_to_insert = (name, email, login, password, activated)
        data_result = db.execute_modify(sql_query, data_to_insert)
        return data_result

    def update(self, id, name, email, login, password, activated):
        sql_query = """UPDATE db.user SET name=%s, email=%s, login=%s, password=%s, activated=%s WHERE user_id=%s"""
        data_to_updade = (name, email, login, password, activated, id)
        data_result = db.execute_modify(sql_query, data_to_updade)
        return data_result

    def delete(self, id):
        sql_query = """DELETE FROM db.user WHERE user_id = %s"""
        id_to_delete = (id,)
        data_result = db.execute_modify(sql_query, id_to_delete)
        return data_result
