from fastapi import FastAPI, Request, File, UploadFile, HTTPException, status
import uvicorn
from db.dbWork import database
from dbAPI import InboxRep
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime
import uuid
import shutil
import os
from minio import Minio
import random


client = Minio('127.0.0.1:9001', access_key='admin', secret_key='password', secure=False)
app = FastAPI()
templates = Jinja2Templates(directory="templates")


def randomCode():
    choise = random.randint(1, 3)
    if choise == 1:
        return 111
    elif choise == 2:
        return 222
    elif choise == 3:
        return 333
    else:
        return 444


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/frames")
async def frames(files: list[UploadFile] = File()):
    if len(files) > 15:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="so many files, man!")
    newInbox = InboxRep(database)
    isCreate = False
    dt = datetime.now()
    buckName = str(dt.strftime('%Y%m%d'))
    buckets = client.list_buckets()
    for bucket in buckets:
        if buckName == str(bucket.name):
            isCreate = True
    if not isCreate:
        client.make_bucket(buckName)
    for file in files:
        file.filename = str(uuid.uuid1()) + '.jpg'
        with open("tmp.jpg", "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        client.fput_object(buckName, file.filename, 'tmp.jpg')
        os.remove('tmp.jpg')
        await newInbox.createImg(randomCode(), file.filename, str(datetime.now().strftime('%Y%m%d-%H:%M')))
    return {"files": [file.filename for file in files]}


@app.get("/frames/{code}")
async def framesCode(code: int):
    myInbox = InboxRep(database)
    res = await myInbox.getByCode(code)
    return str(res)


@app.delete("/frames/{code}")
async def framesCodeDel(code: int):
    myInbox = InboxRep(database)
    data = await myInbox.getByCode(code)
    for d in data:
        client.remove_object(d[3].split('-')[0], d[2])
    await myInbox.delImg(code)
    return 'Successful'
