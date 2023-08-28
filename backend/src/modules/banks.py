from modules import soup, messages, config
from modules.logger import logger
from models.banks import Bank
from pydantic import ValidationError
from db.client import client
from bson import ObjectId


db = client.local.banks


def get_banks(id: str = None):
    logger.info(f"Validando ID {id}.")
    if id:
        if not ObjectId.is_valid(id):
            logger.warning(f"ID {id} inválido.")
            return False, messages.ERR_SCHEMA.format(err_args="id")
    logger.info("Buscando bancos en la DB.")
    result = list(db.find({"_id":ObjectId(id)} if id else None))
    if not result:
        return False, messages.ERR_BANK_NOT_FOUND
    banks = [Bank(**bank) for bank in result]
    return True, banks if len(banks) != 1 else banks[0]


def update_banks():
    logger.info("Actualizando la lista de bancos con SOUP...")
    data = soup.get_table_from_page(config.BCRA_URL)
    db.delete_many({})
    result = db.insert_many(data)
    return True, [str(id) for id in result.inserted_ids]
