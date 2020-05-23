#!/usr/bin/env sh
set -ex

# Testnet support
if [ "$TESTNET" = true ]; then
  FLAGS='--testnet'
fi

# Set config
electron-cash $FLAGS setconfig rpcuser ${ELECTRUM_USER}
electron-cash $FLAGS setconfig rpcpassword ${ELECTRUM_PASSWORD}
electron-cash $FLAGS setconfig rpchost 0.0.0.0
electron-cash $FLAGS setconfig rpcport 8000

# XXX: Check load wallet or create

# Run application
electron-cash $FLAGS daemon start

electron-cash $FLAGS -w $WALLET daemon load_wallet

# Wait forever
while true; do
  tail -f /dev/null & wait ${!}
done