from pymongo import MongoClient
from config import Config


class MongodbService:
    _instance = None
    _client = None
    _db = None
    _collection = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls.__init__(cls._instance)
        return cls._instance

    def __init__(self):
        self._client = MongoClient(host=Config.DB_HOST, port=Config.DB_PORT)
        self._db = self._client[Config.DB_NAME]
        self._collection = self._db[Config.DB_COLLECTION]

    def save_data(self, data):
        self._collection.insert_one(data)

    def get_by_hash(self, h: str):
        return self._collection.find_one(filter={'hash': h})

    def get_all(self):
        return list(self._collection.find())

    def clear_all(self):
        self._collection.delete_many({})