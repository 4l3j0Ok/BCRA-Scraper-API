from modules import soup, messages, config
from models.banks import Bank
from pydantic import ValidationError
from db.client import client
from bson import ObjectId


db = client.local.banks


def get_banks(id: str = None):
    if id:
        if not ObjectId.is_valid(id):
            return False, messages.ERR_SCHEMA.format(err_args="id")
    result = list(db.find({"_id":ObjectId(id)} if id else None))
    if not result:
        return False, messages.ERR_BANK_NOT_FOUND
    banks = [Bank(**bank) for bank in result]
    return True, banks if len(banks) != 1 else banks[0]


def update_banks():
    data = soup.get_table_from_page(config.BCRA_URL)
    result = db.insert_many(data)
    return True, result
