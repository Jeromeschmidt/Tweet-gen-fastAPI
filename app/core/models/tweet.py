from pydantic import BaseModel, Field
from typing import Optional
import datetime


class TweetSchema(BaseModel):
    _id: str = Field(...)
    tweet: str = Field(...)
    created_at: Optional[datetime.datetime]

    class Config:
        schema_extra = {
            "example": {
                "_id": "1234",
                "tweet": "Test Tweet Content",
                "created_at": "2032-04-23T10:20:30.400+02:30",
            }
        }



def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
