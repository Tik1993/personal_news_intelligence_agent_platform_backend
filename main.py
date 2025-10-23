from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from db.mongodb import news_collection

app = FastAPI()

@app.get("/")
def read_root():
    return {"Message": "Welcome to the news intelligence agent backend server"}

@app.get("/test-db")
async def test_db():
    try:
        result = await news_collection.find_one()
        result["_id"] = str(result["_id"])
        if result:
            return {"status":"connected","sample":result}
        else:
            return {"status":"connected", "message":"No documents found yet"}
    except Exception as e:
        return {"status":"error","detail":str(e)}