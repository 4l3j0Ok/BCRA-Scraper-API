from fastapi import APIRouter, HTTPException
import modules.banks as functions
from models.banks import Bank, Success, Detail
from modules import messages


router = APIRouter()


@router.get("/")
async def get_banks(id: str = None) -> Success:
    "Retorna la lista de bancos o un usuario concreto en base al id."
    success, result = functions.get_banks(id)
    if not success:
        raise HTTPException(
            status_code=404,
            detail=Detail(
                payload=None,
                message=result
            )
        )
    return Success(
        input=id if id else None,
        detail=Detail(
            payload=result,
            message=messages.MSG_SUCCESS_GENERIC
        )
    )


@router.post("/update_banks_list")
async def update_banks_list() -> Success:
    "Actualiza la lista de bancos en la base de datos usando Web Scraping."
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
        input=None,
        detail=Detail(
            payload={"ids": result},
            message=messages.MSG_SUCCESS_SAVE
        )
    )
