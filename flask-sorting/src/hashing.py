import hashlib
import pickle


def hash_list(data: list) -> str:
    b = bytearray(pickle.dumps(data))
    h = hashlib.sha256(b)
    return h.hexdigest()
