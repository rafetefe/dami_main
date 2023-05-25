from typing import List

from fastapi import APIRouter, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist

import src.crud.gonullu as crud
from src.schemas.gonullu import GonulluOutSchema, GonulluInSchema

router = APIRouter()

#Tüm nesneleri döndür
@router.get("/gonullu",response_model=List[GonulluOutSchema])
async def get_gonullu():
    return await crud.get_all()

#Verilen ID deki nesneyi döndür
@router.get("/gonullu/{gonullu_id}",response_model=GonulluOutSchema)
async def get_gonullu(gonullu_id: int) -> GonulluOutSchema:
    try:
        return await crud.get(gonullu_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="ID'si verilen araç bulunamadi.",
        )

#Ekle
@router.post("/gonullu", response_model=GonulluOutSchema)
async def create_gonullu(gonullu: GonulluInSchema) -> GonulluOutSchema:
    return await crud.create(gonullu)

#Sil
@router.delete(
    "/gonullu/{gonullu_id}",
    response_model=GonulluOutSchema,
    responses={404: {"model": HTTPNotFoundError}}
)
async def delete_gonullu(_id: int):
    return await crud.delete(_id)
