from src.service.postgresql import Postgresql
from src.model.dto.userDto import UserDtoGetById

db = Postgresql()


class UserModel:

    list_fields = [
        "user_id",
        "name",
        "email",
        "login",
        "password",
        "activated",
        "age",
        "description",
        "city",
    ]

    def get_all(self):
        sql_query = """SELECT * FROM public.user"""
        db_result = db.fetch_all(sql_query)
        if not db_result:
            return None

        payload_users = []
        for user in db_result:
            dict_fields_and_user = dict(zip(self.list_fields, list(user)))
            user_dict = (UserDtoGetById(**dict_fields_and_user)).dict()
            payload_users.append(user_dict)

        return payload_users

    def get_by_id(self, id):
        # "," convert from string to tuple
        sql_query = """SELECT * FROM public.user WHERE user_id = %s"""
        id_to_fetch = (id,)

        db_result = db.fetch_one(sql_query, id_to_fetch)
        if not db_result:
            return None

        # zip creates dict union of the two lists
        dict_fields_and_db_result = dict(zip(self.list_fields, list(db_result)))
        data_result = UserDtoGetById(**dict_fields_and_db_result)

        return data_result

    def add(self, payload):
        sql_query = """INSERT INTO public.user (name, age, email, city, login, password, description, activated) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
        data_to_insert = (
            payload.name,
            payload.age,
            payload.email,
            payload.city,
            payload.login,
            payload.password,
            payload.description,
            payload.activated,
        )
        data_result = db.execute_modify(sql_query, data_to_insert)
        return data_result

    def update(self, id, payload):
        sql_query = """UPDATE public.user SET name=%s, age=%s, email=%s, city=%s, description=%s, activated=%s WHERE user_id=%s"""
        data_to_updade = (
            payload.name,
            payload.age,
            payload.email,
            payload.city,
            payload.description,
            payload.activated,
            id,
        )
        data_result = db.execute_modify(sql_query, data_to_updade)
        return data_result

    def delete(self, id):
        sql_query = """DELETE FROM public.user WHERE user_id = %s"""
        id_to_delete = (id,)
        data_result = db.execute_modify(sql_query, id_to_delete)
        return data_result
