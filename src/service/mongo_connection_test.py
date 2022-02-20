from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
MONGO_HOST = os.getenv('MONGO_HOST')
MONGO_PORT = int(os.getenv('MONGO_PORT'))


class Mongo:
    def mongo_connect(self):
        
        # print(MONGO_HOST, MONGO_PORT)
        # mongo = MongoClient(host=MONGO_HOST, port=MONGO_PORT, serverSelectionTimeoutMS=1000)
        client = MongoClient('mongodb+srv://wbbackend:pythonflask@cluster0.9ar0u.mongodb.net/wb_db?retryWrites=true&w=majority')
        
        # database
        # db = client.dcheroes
        db = client['wb_db']

        # conexão direto na collection:
        collection = db['users']

        # data = list(collection.find())
        data = list(db.users.find())
        print(data)
            
    #     client.server_info()  # trigger exception if cannot connect to db
    #     return db
            
        # except:
        #     print('ERROR - Cannot connect to db')

Mongo().mongo_connect()

