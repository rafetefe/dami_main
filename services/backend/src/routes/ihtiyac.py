from typing import List

from fastapi import APIRouter, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist

import src.crud.ihtiyac as crud
from src.schemas.ihtiyac import IhtiyacOutSchema, IhtiyacInSchema

router = APIRouter()

#Tüm nesneleri döndür
@router.get("/ihtiyac",response_model=List[IhtiyacOutSchema])
async def get_ihtiyac():
    return await crud.get_all()

#Verilen ID deki nesneyi döndür
@router.get("/ihtiyac/{ihtiyac_id}",response_model=IhtiyacOutSchema)
async def get_ihtiyac(ihtiyac_id: int) -> IhtiyacOutSchema:
    try:
        return await crud.get(ihtiyac_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="ID'si verilen araç bulunamadi.",
        )

#Ekle
@router.post("/ihtiyac", response_model=IhtiyacOutSchema)
async def create_ihtiyac(ihtiyac: IhtiyacInSchema) -> IhtiyacOutSchema:
    return await crud.create(ihtiyac)

#Sil
@router.delete(
    "/ihtiyac/{ihtiyac_id}",
    response_model=IhtiyacOutSchema,
    responses={404: {"model": HTTPNotFoundError}}
)
async def delete_ihtiyac(_id: int):
    return await crud.delete(_id)
