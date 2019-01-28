from pymongo import MongoClient

import configs

'''
    The following are different way of connecting to mongo db.
    client = MongoClient()
    client = MongoClient('mongodb://localhost:27017/')
'''
client = MongoClient(configs.MONGO_HOST, configs.MONGO_PORT)

# Connecting to Database.
db = client[configs.DB_NAME]

# Connecting to Selected Collection and store it in cursor 'cur'.
cur = db[configs.COLLECTION_NAME]
