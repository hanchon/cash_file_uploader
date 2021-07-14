from pydantic import BaseModel
from fastapi import FastAPI, Form
from starlette.responses import Response
import uvicorn

from crypto.electroncash.requests import list_of_addresses, pay_to, broadcast

from fastapi.responses import HTMLResponse

app = FastAPI()
addresses = None


class Params(BaseModel):
    value: str


class ReponseValue(BaseModel):
    value: str


@app.post("/hash", response_model=ReponseValue)
async def upload_hash(value: str = Form(...)):
    res, raw = pay_to(addresses[5], 0.0001, value)
    hexa = None
    if res:
        hexa = raw["hex"]
        res2, raw = broadcast(hexa)
        return {'value': raw[1]}
    return {'value': "error"}


@app.get("/address")
async def get_address():
    return addresses[5]


@app.get("/")
async def main():
    content = f"""
        <body>
        <h1>{addresses[5]}</h1>
        <a href="https://explorer.bitcoin.com/tbch/address/{addresses[5]}">Explorer</a>
        <form action="/hash" method="post" enctype="multipart/form-data">
        <input name="value" id="value" type="text" placeholder="Commit..." />
        <input type="submit">
        </form>
        </body>
    """
    return HTMLResponse(content=content)


if __name__ == "__main__":
    res, lista = list_of_addresses()
    if res:
        addresses = lista
    uvicorn.run(app, host='0.0.0.0', port=7000)