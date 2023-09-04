from pydantic import BaseModel
from bson import ObjectId


class Bank(BaseModel):
    label: str
    bcra_id: str


class BankWithID(BaseModel):
    id: str | None
    label: str
    bcra_id: str

    def __init__(self, **bank):
        if "_id" in bank and isinstance(bank["_id"], ObjectId):
            bank["id"] = str(bank["_id"])
        super().__init__(**bank)
