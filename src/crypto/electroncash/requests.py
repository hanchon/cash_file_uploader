import requests
from config import ELECTRUM_USER, ELECTRUM_PASSWORD
from config import ELECTRUM_PORT, ELECTRUM_ADDRESS

import logging
logging.getLogger("urllib3").setLevel(logging.INFO)


def run_command(command, params={}):
    # TODO: return error if request fails
    data = {"id": "1", "method": command, "params": params}
    # print("Sending electrum request: %s", data)
    r = requests.post('http://' + ELECTRUM_ADDRESS + ':' + ELECTRUM_PORT,
                      auth=(ELECTRUM_USER, ELECTRUM_PASSWORD),
                      json=data)
    # print("Electrum request resp: %s", r.text)
    parsed = r.json().get('result')
    return parsed is not None, parsed


def list_of_addresses():
    return run_command("listaddresses")


def get_balance():
    return run_command("getbalance")


def broadcast(
    raw="0200000001b0c8e048037a9972bac8b0f3a3f367a87dee313d734e204dee5c38b27406ec4801000000d90047304402207d769bd7ed635a954cebea37fb9e1c632235182280ec6e2c0e23f08f7178f3d302204ec9e2a8b38f42cd33f00ebfb8101049822d55e4dc5438db6c8b26841df054440147304402204f094956880a9f7dc37099727e482667cba73234244fc48a6cb65ae8ed83cbcb0220682810d48f7ab893094f01b5784052d198cc430ca76a7150e46535b72c9c6ea0014752210319ae6c407cb8e26d1d778d3e69653edcb736c9960251b8d636aab9820d93600821039f7c82e2d4e943e04ab0572c361a47b2804121be7479b2f7b6bd4a611faf516b52aefdffffff0240420f00000000002200206d19d1d012279e07c612dc698bc247ac5f5e774c2feca3700e11dc5ef13c15c58f2116000000000017a9147108882546549bffa4c283a8722ba5ceb53c369c87d13b1a00"  # noqa
):
    # NOTE: result is none if already sent
    # NOTE: result = 235026f114b54a58bca17ec0f983cfbe99cdfff723fac54b0ee439002eb2e747
    return run_command("broadcast", [raw])


def help():
    return run_command("help")


def pay_to(destination="", amount="", op_return=None):
    # NOTE: returns{'hex': '4555..', 'complete': False, 'final': False}
    if op_return:
        return run_command("payto", {"destination": destination, "amount": amount, "op_return": op_return})

    return run_command("payto", [destination, amount])


def history():
    return run_command("history")


def get_address_history(wallet="2N4KGN3HNzYcSgxZ5Ff6Map2J7Rb2soRk33"):
    return run_command("getaddresshistory", [wallet])


def get_tx_status(hash="bc41258f0051ebcd23fdddb408dffadafc67a81cb55445599e44e69d4af85955"):
    return run_command("get_tx_status", [hash])


def deserialize(
    raw="02000000000101bc9df515e1dd009a468ef4aa0eae88bf7d9dc1e27b4bbb7044b946c1afd23b1f0000000000feffffff02102700000000000017a914796d07b52e07daa2defd9914291292b06e27702587d2a16e3f0900000017a914c56c605e4f4da4ac4b112a4d09ba369d37bd72ce87024730440220271f2805b1441c9445e0567788c32ca30c509492c40c3d57fd6267ba8c1e57fa02204a580a495a38d281b220a4b75cfdf0bd85f554e46ddb44657cab570f32d5567901210281801bee766cfb7ee7bb9868df1465a0b8a73e350e78f1861c4eaa14cce0df90d87f1900"  # noqa
):
    return run_command("deserialize", [raw])


def get_transaction(tx="bc41258f0051ebcd23fdddb408dffadafc67a81cb55445599e44e69d4af85955"):
    return run_command("gettransaction", [tx])


def listaddresses():
    return run_command("listaddresses")


def validate_address(address="tb1qd5var5qjy70q03sjm35chsj84304ua6v9lk2xuqwz8w9aufuzhzsx64hd4"):
    # NOTE: returns True or False not a json
    return run_command("validateaddress", [address])
