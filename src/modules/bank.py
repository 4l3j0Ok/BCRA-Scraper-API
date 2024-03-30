from modules import soup, messages, config
from modules.logger import logger
from models.bank import Bank
from db.client import client


db = client.bcra_scraper.banks


def get_banks(bcra_id: str = None, as_dict: bool = False):
    logger.info("Buscando bancos en la DB.")
    result = list(db.find({"bcra_id": bcra_id} if bcra_id else None))
    if not result:
        return False, messages.ERR_BANK_NOT_FOUND
    banks = [Bank(**bank) for bank in result] if not as_dict \
        else [Bank(**bank).model_dump() for bank in result]
    return True, banks if len(banks) != 1 else banks[0]


def update_banks():
    logger.info("Actualizando la lista de bancos con SOUP...")
    data = soup.get_banks_from_url(config.BCRA_URL)
    delete_query = {"bcra_id": {"$in": [bank["bcra_id"] for bank in data]}}
    try:
        db.delete_many(delete_query)
        db.insert_many(data)
    except Exception as ex:
        logger.exception(ex)
        return False, messages.ERR_FAILED_TO_UPDATE
    return True, messages.MSG_SUCCESS_SAVE


def add_bank(bank):
    logger.info("Agregando un nuevo banco...")
    result = db.insert_one(bank.dict())
    return True, messages.MSG_SUCCESS_SAVE
