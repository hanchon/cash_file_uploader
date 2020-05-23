import hashlib

def get_hash_from_file(file):
    with open(file, "rb") as f:
        bytes = f.read()
        return hashlib.sha256(bytes).hexdigest()