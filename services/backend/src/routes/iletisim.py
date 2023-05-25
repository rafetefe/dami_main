from typing import List

from fastapi import APIRouter, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist

import src.crud.iletisim as crud
from src.schemas.iletisim import IletisimOutSchema, IletisimInSchema

router = APIRouter()

#Tüm nesneleri döndür
@router.get("/iletisim",response_model=List[IletisimOutSchema])
async def get_iletisim():
    return await crud.get_all()

#Verilen ID deki nesneyi döndür
@router.get("/iletisim/{iletisim_id}",response_model=IletisimOutSchema)
async def get_iletisim(iletisim_id: int) -> IletisimOutSchema:
    try:
        return await crud.get(iletisim_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="ID'si verilen araç bulunamadi.",
        )

#Ekle
@router.post("/iletisim", response_model=IletisimOutSchema)
async def create_iletisim(iletisim: IletisimInSchema) -> IletisimOutSchema:
    return await crud.create(iletisim)

#Sil
@router.delete(
    "/iletisim/{iletisim_id}",
    response_model=IletisimOutSchema,
    responses={404: {"model": HTTPNotFoundError}}
)
async def delete_iletisim(_id: int):
    return await crud.delete(_id)
