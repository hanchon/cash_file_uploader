# RAW=$(curl -X POST "http://electrum:electrumpassword@127.0.0.1:8000" \
#      -H "accept: application/json" \
#      -H "Content-Type: application/json" \
#      -d "{\"method\":\"payto\",\"params\":{\"destination\" : \"qzs9aq2ag6yxnt987ayhy6lc4cn7xw6svsn04rdud8\", \"amount\": 0.1, \"op_return\":\"HOLA\"}, \"id\": 1}" | jq .result.hex)


RAW=\"010000000147fcebf7f99097ad35f2383b24afe93ec330b2aea9e4a030e5fc9dd215a2d685000000006441a9faea40cb49a38cdca48da3494adef245a2b7785c1093066654cb268aa6dc30294a496f2ce6b032b34ab36cb9f601a0fdc92290adf48f632e54885861638ca64121024fd7d72189a28e7dd75092c7c4ad8ee76b1e5bf7fb9027466d8d365a1b19833efeffffff030000000000000000676a4c643133656532636639313230386330306138346230663063653736666439323361656662353865663530303432613235666233636530373430353566306561343939393265636565322d313036302d346161372d626630662d31343235326563616237326210270000000000001976a914a05e815d468869aca7f749726bf8ae27e33b506488aca5b8f505000000001976a91437a975dcd17abeb1ee2896710c8c4ef393f5aaa588aca3131500\"

curl -X POST "http://electrum:electrumpassword@127.0.0.1:8000" \
     -H "accept: application/json" \
     -H "Content-Type: application/json" \
     -d "{\"method\":\"deserialize\",\"params\":[$RAW], \"id\": 1}" | jq



     