from src.service.postgresql import Postgresql


db = Postgresql()


class UserModel:
    def get_all(self):
        sql_query = """SELECT * FROM public.user"""
        data_result = db.fetch_all(sql_query)
        return data_result

    def get_by_id(self, id):
        # "," converte de string para tupla
        # print("---typer of login 1:::", type(id))
        sql_query = """SELECT * FROM public.user WHERE user_id = %s"""
        id_to_fetch = (id,)
        # print("---typer of login 2:::", type(id))

        data_result = db.fetch_one(sql_query, id_to_fetch)
        return data_result

    def add(self, name, age, email, city, login, password, description, activated):
        sql_query = """INSERT INTO public.user (name, age, email, city, login, password, description, activated) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
        data_to_insert = (name, age, email, city, login, password, description, activated)
        data_result = db.execute_modify(sql_query, data_to_insert)
        return data_result

    def update(self, id, name, age, email, city, login, password, description, activated):
        sql_query = """UPDATE public.user SET name=%s, age=%s, email=%s, city=%s, login=%s, password=%s, description=%s, activated=%s WHERE user_id=%s"""
        data_to_updade = (name, age, email, city, login, password, description, activated, id)
        data_result = db.execute_modify(sql_query, data_to_updade)
        return data_result

    def delete(self, id):
        sql_query = """DELETE FROM public.user WHERE user_id = %s"""
        id_to_delete = (id,)
        data_result = db.execute_modify(sql_query, id_to_delete)
        return data_result
