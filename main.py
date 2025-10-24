from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from db.mongodb import news_collection
from schemas.item import NewsItem

app = FastAPI()

@app.get("/")
def read_root():
    return {"Message": "Welcome to the news intelligence agent backend server"}

@app.get("/test-db")
def test_db():
    try:
        result =  news_collection.find_one()
        result["_id"] = str(result["_id"])
        if result:
            return {"status":"connected","sample":result}
        else:
            return {"status":"connected", "message":"No documents found yet"}
    except Exception as e:
        return {"status":"error","detail":str(e)}
    
@app.get("/news",response_model=list[NewsItem])
def get_all_news():
    news=[]
    all_news = news_collection.find()
    for doc in all_news:
        doc["_id"]=str(doc["_id"])
        news.append(doc)
    return news