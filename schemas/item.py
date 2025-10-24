from typing import Optional
from pydantic import BaseModel,Field

class NewsItem(BaseModel):
    id:str = Field(...,alias="_id")
    title:str
    link:str
    published:str
    summary:Optional[str] = None
    content: Optional[str] = None