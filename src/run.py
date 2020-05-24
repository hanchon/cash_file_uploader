import uuid
import uvicorn

from typing import List
from pathlib import Path

from uploader.functions import save_upload_file
from zip_helpers.functions import create_zip
from crypto.utils import get_hash_from_file
from crypto.electroncash.requests import list_of_addresses, pay_to, broadcast

from database.models import Caso
from database.db import create_models, create_session

from fastapi import Form
from fastapi import FastAPI, File, UploadFile, Request, Response
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI()
addresses = None


# TODO: move this to the app start method
@app.get("/start")
async def start():
    global addresses
    res, lista = list_of_addresses()
    if res:
        addresses = lista
    return {"addresses": addresses}


@app.post("/register")
async def register(name):
    return {"this is your new wallet ...."}


@app.post("/files/")
async def create_files(files: List[bytes] = File(...)):
    return {"file_sizes": [len(file) for file in files]}


@app.post("/uploadfiles/")
async def create_upload_files(*, nombre: str = Form(...), files: List[UploadFile] = File(...)):
    # Do something with this
    print(nombre)
    for file in files:
        print(file)

    unique_id = uuid.uuid4()
    path = f"/home/hanchon/devel/cash_file_uploader/tmp/{str(unique_id)}/"
    Path(path).mkdir(parents=True, exist_ok=True)
    paths = []
    for file in files:
        path_actual = path + file.filename
        paths.append(path_actual)
        save_upload_file(file, Path(path_actual))

    zip_path = f"/home/hanchon/devel/cash_file_uploader/zip/{str(unique_id)}.zip"
    create_zip(paths, zip_path)
    x = get_hash_from_file(zip_path)

    data = f"{x}{unique_id}"

    print(data)

    res, raw = pay_to("qzs9aq2ag6yxnt987ayhy6lc4cn7xw6svsn04rdud8", 0.0001, data)
    hexa = None
    if res:
        hexa = raw["hex"]
        print(hexa)
        # broadcast
        # res2, raw = broadcast(hexa)
        # print(raw)
        # caso = Caso(generated_id=str(unique_id), tx_hash=raw[1])
        # session = create_session()
        # session.add(caso)
        # session.commit()

    return {"filenames": [file.filename for file in files]}


@app.get("/")
async def main():
    # TODO: move this to the start program function
    create_models()

    content = """
        <body>
        <form action="/files/" enctype="multipart/form-data" method="post">
        <input name="files" type="file" multiple>
        <input type="submit">
        </form>
        <form id="data" action="/uploadfiles/" enctype="multipart/form-data" method="post">
            <input name="nombre" id="nombre" type="text" value="valor"/>
            <input name="files" type="file" multiple />
            <input type="submit" />
        </form>
        </body>
    """
    return HTMLResponse(content=content)


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=7000)