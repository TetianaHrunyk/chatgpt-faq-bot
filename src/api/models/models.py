from pydantic import BaseModel


class FAQRequest(BaseModel):
    query: str


class FAQResponse(BaseModel):
    query: str
    response: str
