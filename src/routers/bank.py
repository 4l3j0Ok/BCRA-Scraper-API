from fastapi import APIRouter, HTTPException
import modules.bank as functions
from models.response import Success, Detail
from modules import messages
from models.bank import Bank, AdminCredentials


router = APIRouter()


@router.get("/")
async def get(bank_id: str = None) -> Success:
    "Retorna la lista de bancos o un usuario concreto en base al id."
    success, result = functions.get_banks(bank_id, as_dict=True)
    if not success:
        raise HTTPException(
            status_code=404,
            detail=Detail(
                payload=None,
                message=result
            )
        )
    return Success(
        input=bank_id if bank_id else None,
        detail=Detail(
            payload=result,
            message=messages.MSG_SUCCESS_GENERIC
        )
    )


@router.post("/update")
async def update_banks_list(credentials: AdminCredentials) -> Success:
    "Actualiza la lista de bancos en la base de datos usando Web Scraping."
    if not functions.validate_admin(credentials):
        raise HTTPException(
            status_code=401,
            detail=Detail(
                payload=None,
                message=messages.MSG_ERROR_UNAUTHORIZED
            )
        )
    success, result = functions.update_banks()
    if not success:
        raise HTTPException(
            status_code=400,
            detail=Detail(
                payload=None,
                message=result
            )
        )
    return Success(
        detail=Detail(
            payload={"ids": result},
            message=messages.MSG_SUCCESS_SAVE
        )
    )


@router.post("/add")
def add_bank(bank: Bank, credentials: AdminCredentials) -> Success:
    "Agrega el banco indicado."
    if not functions.validate_admin(credentials):
        raise HTTPException(
            status_code=401,
            detail=Detail(
                payload=None,
                message=messages.MSG_ERROR_UNAUTHORIZED
            )
        )
    success, result = functions.add_bank(bank)
    if not success:
        raise HTTPException(
            status_code=400,
            detail=Detail(
                payload=None,
                message=result
            )
        )
    return Success(
        detail=Detail(
            payload={"id": result},
            message=messages.MSG_SUCCESS_SAVE
        )
    )
