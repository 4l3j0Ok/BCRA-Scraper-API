from pydantic import BaseModel


class Bank(BaseModel):
    label: str
    bcra_id: str


class AdminCredentials(BaseModel):
    username: str
    password: str
