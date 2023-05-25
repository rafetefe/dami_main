class Crud:
    def __init__(self, class_model, class_out_schema):
        self.model = class_model
        self.out_schema = class_out_schema

    async def get_all(self):
        return await self.out_schema.from_queryset(self.model.all())
    
    async def get(self, _id):
        return await self.out_schema.from_queryset_single(self.model.get(id=_id))

    async def create(self, _obj):
        obj = await self.model.create(_obj)
        return await self.out_schema.from_tortoise_orm(obj)
    
    async def delete(self, _id):
        from fastapi import HTTPException
        from tortoise.exceptions import DoesNotExist

        try:
            db_entry = await self.out_schema.from_queryset_single(self.model.get(id=_id))
        except DoesNotExist:
            raise HTTPException(status_code=404, detail=f"{_id} not found")

        _deleted = await self.model.filter(id=_id).delete()
        if not _deleted:
            raise HTTPException(status_code=404, detail=f"{_id} not found")
        return f"Deleted: {_id}"