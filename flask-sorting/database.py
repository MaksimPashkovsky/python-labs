import os
from pymongo import MongoClient


class MongodbService:
    _instance = None
    _client = None
    _db = None
    _collection = None

    @classmethod
    def get_instance(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls.__init__(cls._instance)
        return cls._instance

    def __init__(self):
        self._client = MongoClient(host=os.getenv('DB_HOST', default='localhost'),
                                   port=os.getenv('DB_PORT', default=27017))
        self._db = self._client[os.getenv('DB_NAME', default='sortdb')]
        self._collection = self._db[os.getenv('DB_COLLECTION', default='sorted_lists')]

    def save_data(self, data):
        self._collection.insert_one(data)

    def has_hash(self, h: str):
        for _ in self._collection.find(filter={'hash': h}):
            return True
        return False

    def get_by_hash(self, h: str):
        return self._collection.find_one({'hash': h})
