from typing import List

from fastapi import APIRouter, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist

#from src.crud.arac import Crud_Arac as crud
import src.crud.arac as crud  
from src.schemas.arac import AracOutSchema, AracInSchema

router = APIRouter()

#Tüm nesneleri döndür
@router.get("/arac",response_model=List[AracOutSchema])
async def get_arac():
    return await crud.get_all()

#Verilen ID deki nesneyi döndür
@router.get("/arac/{arac_id}",response_model=AracOutSchema)
async def get_arac(arac_id: int) -> AracOutSchema:
    try:
        return await crud.get(arac_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="ID'si verilen araç bulunamadi.",
        )

#Ekle
@router.post("/arac", response_model=AracOutSchema)
async def create_arac(arac: AracInSchema) -> AracOutSchema:
    return await crud.create(arac)

#Sil
@router.delete(
    "/arac/{arac_id}",
    response_model=AracOutSchema,
    responses={404: {"model": HTTPNotFoundError}}
)
async def delete_arac(_id: int):
    return await crud.delete(_id)
