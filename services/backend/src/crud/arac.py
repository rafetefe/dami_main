from src.database.models import Arac
from src.schemas.arac import AracOutSchema

async def get_all():
    return await AracOutSchema.from_queryset(Arac.all())

async def get(_id):
    return await AracOutSchema.from_queryset_single(Arac.get(id=_id))

async def create(_obj):
    obj_dict = _obj.dict(exclude_unset=True)
    f_obj = await Arac.create(**obj_dict)
    return await AracOutSchema.from_tortoise_orm(f_obj)

async def delete(_id):
    from fastapi import HTTPException
    from tortoise.exceptions import DoesNotExist

    try:
        db_entry = await AracOutSchema.from_queryset_single(Arac.get(id=_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"{_id} not found")

    _deleted = await Arac.filter(id=_id).delete()
    if not _deleted:
        raise HTTPException(status_code=404, detail=f"{_id} not found")
    return f"Deleted: {_id}"