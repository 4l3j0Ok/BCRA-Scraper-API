from fastapi import APIRouter, HTTPException, Depends, status
from typing import Annotated
import modules.bank as functions
from models.response import Success, Detail
from modules import messages, security
from models.bank import Bank


router = APIRouter()


@router.get("/")
async def get(bcra_id: str = None) -> Success:
    "Retorna la lista de bancos o un usuario concreto en base al id."
    success, result = functions.get_banks(bcra_id, as_dict=True)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=Detail(
                payload=None,
                message=result
            )
        )
    return Success(
        detail=Detail(
            payload=result,
            message=messages.MSG_SUCCESS_GENERIC
        )
    )


@router.post("/update")
async def update_banks_list(authorized: Annotated[str, Depends(security.validate_admin)]) -> Success:
    "Actualiza la lista de bancos en la base de datos usando Web Scraping."
    if not authorized:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario o contraseña incorrectos.",
            headers={"WWW-Authenticate": "Basic"},
        )
    success, result = functions.update_banks()
    if not success:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=Detail(
                payload=None,
                message=result
            )
        )
    return Success(
        detail=Detail(
            payload=None,
            message=messages.MSG_SUCCESS_SAVE
        )
    )


@router.post("/add")
def add_bank(bank: Bank, authorized: Annotated[str, Depends(security.validate_admin)]) -> Success:
    "Agrega el banco indicado."
    if not authorized:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario o contraseña incorrectos.",
            headers={"WWW-Authenticate": "Basic"},
        )
    success, result = functions.add_bank(bank)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=Detail(
                payload=None,
                message=result
            )
        )
    return Success(
        detail=Detail(
            payload=None,
            message=messages.MSG_SUCCESS_SAVE
        )
    )
