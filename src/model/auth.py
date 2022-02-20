from src.service.mongo import Mongo
from bson.objectid import ObjectId

db = Mongo().mongo_connect()


class AuthModel:
    def find_login(self, login):
        find_user = db.users.find_one({'login': login})
        if find_user:
            return find_user
        return None
    
    def update_status(self, login, status):
        data = db.users.update_one({'login':login}, {'$set': {'activated': status}})

        if data:
            return data
        return None