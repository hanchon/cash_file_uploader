import os

# ELECTRUM
ELECTRUM_USER = os.environ.get('ELECTRUM_USER') or "electrum"
ELECTRUM_PASSWORD = os.environ.get('ELECTRUM_PASSWORD') or "electrumpassword"
ELECTRUM_ADDRESS = os.environ.get('ELECTRUM_ADDRESS') or "127.0.0.1"
ELECTRUM_PORT = os.environ.get('ELECTRUM_PORT') or "8000"
