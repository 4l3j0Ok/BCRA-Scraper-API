from modules import config
from pymongo import MongoClient

client = None

if config.MONGO_URI:
    client = MongoClient(config.MONGO_URI)

else:
    client = MongoClient(
        host = config.MONGO_HOST,
        port = config.MONGO_PORT,
        username = config.MONGO_USER,
        password = config.MONGO_PASS
    )
