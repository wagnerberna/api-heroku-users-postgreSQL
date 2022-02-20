from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
MONGO_HOST = os.getenv('MONGO_HOST')
MONGO_PORT = int(os.getenv('MONGO_PORT'))
# MONGO_SERVER = os.getenv('MONGO_SERVER')

MONGO_SERVER = 'mongodb+srv://wbbackend:pythonflask@cluster0.9ar0u.mongodb.net/wb_db?retryWrites=true&w=majority'

class Mongo:
    def mongo_connect(self):
        try:
            # mongo = MongoClient(host=MONGO_HOST, port=MONGO_PORT, serverSelectionTimeoutMS=1000)
            client = MongoClient(MONGO_SERVER)
            
            # db = client.dcheroes
            db = client['wb_db']

            # conectar direto na collection:
            # collection = db['users']
            
            client.server_info()  # trigger exception if cannot connect to db
            # print (list(db.users.find()))
            return db
            
        except:
            print('ERROR - Cannot connect to db')

Mongo().mongo_connect()