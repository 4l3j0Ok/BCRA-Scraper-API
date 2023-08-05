from pydantic import BaseModel
from typing_extensions import TypedDict
from bson import ObjectId


class Bank(BaseModel):
    id: str | None
    label: str
    bcra_id: str

    def __init__(self, **user):
        if "_id" in user and isinstance(user["_id"], ObjectId):
            user["id"] = str(user["_id"])
        super().__init__(**user)


class Detail(TypedDict):
    payload: dict | list | Bank | list[Bank] | None
    message: str | None


class Success(BaseModel):
    input: str | int | dict | None
    detail: Detail


class Failed(BaseModel):
    input: str | int | dict | None
    detail: Detail


class Result(BaseModel):
    success: list[Success] | list
    failed: list[Failed] | list
