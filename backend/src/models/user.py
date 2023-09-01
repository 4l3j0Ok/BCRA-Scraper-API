from pydantic import BaseModel
from bson import ObjectId


class User(BaseModel):
    id: str | None
    name: str
    surname: str
    username: str

    def __init__(self, **user):
        if "_id" in user and isinstance(user["_id"], ObjectId):
            user["id"] = str(user["_id"])
        super().__init__(**user)