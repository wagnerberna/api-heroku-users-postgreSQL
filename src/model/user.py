from src.service.mongo import Mongo
from bson.objectid import ObjectId

db = Mongo().mongo_connect()


class UserModel:
    def get_all(self):
        data = list(db.users.find())
        if data:
            return data
        return None

    def get_by_id(self, id):
        data = db.users.find_one({'_id': ObjectId(id)})
        if data:
            return data
        return None

    def add(self, activated, name, email, login, password):
        print('Model')
        print(activated, name, email, login, password)
        new_user = {'name': name, 'email': email, 'login': login, 'password': password, 'activated': activated}
        print(new_user)
        data = db.users.insert_one(new_user)
        if data:
            return data
        return None

    def update(self, id, name, email, login, password, activated):
        data = db.users.update_one(
            {'_id': ObjectId(id)}, {'$set': {'name': name, 'email': email, 'login': login, 'password': password, 'activated': activated}}
        )
        if data:
            return data
        return None

    def delete(self, id):
        data = db.users.delete_one({'_id': ObjectId(id)})
        if data:
            return data
        return None
