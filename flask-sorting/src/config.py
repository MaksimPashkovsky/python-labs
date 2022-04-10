import os


class Config:
    SERVER_HOST = os.getenv('SERVER_HOST', default='0.0.0.0')
    SERVER_PORT = int(os.getenv('SERVER_PORT', default=9999))
    WORKER_PROCESSES = int(os.getenv('WORKER_PROCESSES', default=4))
    DB_HOST = os.getenv('DB_HOST', default='localhost')
    DB_PORT = int(os.getenv('DB_PORT', default=27017))
    DB_NAME = os.getenv('DB_NAME', default='sortdb')
    DB_COLLECTION = os.getenv('DB_COLLECTION', default='sorted_lists')