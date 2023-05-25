from typing import List

from fastapi import APIRouter, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist

import src.crud.yardimsever as crud
from src.schemas.yardimsever import YardimseverOutSchema, YardimseverInSchema

router = APIRouter()

#Tüm nesneleri döndür
@router.get("/yardimsever",response_model=List[YardimseverOutSchema])
async def get_yardimsever():
    return await crud.get_all()

#Verilen ID deki nesneyi döndür
@router.get("/yardimsever/{yardimsever_id}",response_model=YardimseverOutSchema)
async def get_yardimsever(yardimsever_id: int) -> YardimseverOutSchema:
    try:
        return await crud.get(yardimsever_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="ID'si verilen araç bulunamadi.",
        )

#Ekle
@router.post("/yardimsever", response_model=YardimseverOutSchema)
async def create_yardimsever(yardimsever: YardimseverInSchema) -> YardimseverOutSchema:
    return await crud.create(yardimsever)

#Sil
@router.delete(
    "/yardimsever/{yardimsever_id}",
    response_model=YardimseverOutSchema,
    responses={404: {"model": HTTPNotFoundError}}
)
async def delete_yardimsever(_id: int):
    return await crud.delete(_id)
