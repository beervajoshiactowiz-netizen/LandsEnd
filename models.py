from pydantic import BaseModel, HttpUrl,field_validator
from typing import Optional
import re
import json

#products model
class Products(BaseModel):
    prodUrl:str
    product_name:str
    brand:str
    product_id:int
    variants:str

    #json dump
    @field_validator("variants", mode="before")
    @classmethod
    def to_json(cls, v):
        if not v:
            return None
        if isinstance(v, (list, dict)):
            return json.dumps(v)
        return str(v)

    #check url
    @field_validator("prodUrl", mode="before")
    @classmethod
    def url_check(cls, v):
        if v.startswith("https"):
            return v
        else:
            raise ValueError("invalid Url")
