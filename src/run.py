import uuid
from typing import List
from pathlib import Path

from uploader.functions import save_upload_file
from zip_helpers.functions import create_zip
from crypto.utils import get_hash_from_file

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.post("/files/")
async def create_files(files: List[bytes] = File(...)):
    return {"file_sizes": [len(file) for file in files]}


@app.post("/uploadfiles/")
async def create_upload_files(files: List[UploadFile] = File(...)):
    unique_id = uuid.uuid4()
    path = f"/home/hanchon/devel/cash_file_uploader/src/tmp/{str(unique_id)}/"
    Path(path).mkdir(parents=True, exist_ok=True)
    paths = []
    for file in files:
        path_actual = path + file.filename
        paths.append(path_actual)
        save_upload_file(file, Path(path_actual))

    zip_path = f"{str(unique_id)}.zip"
    create_zip(paths, zip_path)
    print(get_hash_from_file(zip_path))

    return {"filenames": [file.filename for file in files]}


@app.get("/")
async def main():
    content = """
        <body>
        <form action="/files/" enctype="multipart/form-data" method="post">
        <input name="files" type="file" multiple>
        <input type="submit">
        </form>
        <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
        <input name="files" type="file" multiple>
        <input type="submit">
        </form>
        </body>
    """
    return HTMLResponse(content=content)