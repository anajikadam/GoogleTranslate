from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List, Optional, Union

from dataclasses import dataclass
from fastapi import FastAPI, Form, Depends, Query, File, UploadFile, Response
from fastapi.responses import HTMLResponse
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from fastapi.middleware.cors import CORSMiddleware

# Import files
from Gtrans import lang,translation, GetLanguages

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=["*"],
    allow_headers=["*"],
)


class SourceEng(BaseModel):
    sourceLang: Optional[str] = 'en'
    destLang: str
    Sentence: str

# {
#     "destLang": "sagar",
#     "Sentence": "Kadam"
# }

class Translate(BaseModel):
    sourceLang: str
    destLang: str
    Sentence: str

# {
#     "sourceLang":"en",
#     "destLang": "sagar",
#     "Sentence": "Kadam"
# }

@app.get("/")
@app.get("/root")
def read_root():
    return {"Key": "Hello World",
        "Get languages": "http://127.0.0.1:8000/languages",
        "Home Page----": "http://127.0.0.1:8000/translate-Home"
        }


laShort = [(i) for i,j in lang.items()]
laFull = [(j) for i,j in lang.items()]

@app.get("/translate-Home/")
async def uploadImage(request: Request, ):
    templates = Jinja2Templates(directory="templates")
    return templates.TemplateResponse("index.html", {"request": request, "dest":laFull})


@app.get("/languages",)
def get_languages():
    result =GetLanguages()
    return JSONResponse(status_code=200, content={"Data": result})

@app.post("/Eng-translate/")
async def translate1(item: SourceEng):
    result = translation(item)
    return JSONResponse(status_code=200, content={"Data": result})

@app.post("/translate/")
async def translate2(item: Translate):
    result = translation(item)
    return JSONResponse(status_code=200, content={"Data": result})


@dataclass
class SimpleModel:
    sourceLang: Optional[str] = 'en'
    destLang: str = Form(...)
    Sentence: str = Form(...)


@app.post("/Eng-translator/")
async def translate11(item: SimpleModel = Depends()):
    # print(item)
    result = translation(item)
    return JSONResponse(status_code=200, content={"Data": result})

@dataclass
class SimpleModel2:
    sourceLang: str = Form(...)
    destLang: str = Form(...)
    Sentence: str = Form(...)


@app.post("/translator/")
async def translate12(item: SimpleModel = Depends()):
    # print(item)
    result = translation(item)
    return JSONResponse(status_code=200, content={"Data": result})

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

# @app.get("/foo",)
# def read_item():
#     item_id = 'foo'
#     if item_id == "foo":
#         return {"id": "foo", "value": "there goes my hero", 'tags':["sjhsj"]}
#     else:
#         return JSONResponse(status_code=201, content={"message": "Item not found........."})

