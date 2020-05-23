import os


def cast_to_number(id):
    temp = os.environ.get(id)
    if temp is not None:
        return float(temp)
    return None


# ELECTRUM
ELECTRUM_USER = os.environ.get('ELECTRUM_USER') or "electrum"
ELECTRUM_PASSWORD = os.environ.get('ELECTRUM_PASSWORD') or "electrumpassword"
ELECTRUM_ADDRESS = os.environ.get('ELECTRUM_ADDRESS') or "127.0.0.1"
ELECTRUM_PORT = os.environ.get('ELECTRUM_PORT') or "8000"

# DATABASE
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'postgres://postgres:mysecretpassword@127.0.0.1:5432'
POOL_SIZE = cast_to_number('POOL_SIZE') or 10
MAX_OVERFLOW = cast_to_number('MAX_OVERFLOW') or 20
