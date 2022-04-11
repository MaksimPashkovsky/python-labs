import pickle
import xxhash


def hash_list(data: list) -> str:
    b = bytearray(pickle.dumps(data))
    h = xxhash.xxh32(b)
    return h.hexdigest()
