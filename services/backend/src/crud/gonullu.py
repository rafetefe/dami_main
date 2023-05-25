from src.database.models import Gonullu
from src.schemas.gonullu import GonulluOutSchema
from .crud import Crud

Crud_Gonullu = Crud(Gonullu, GonulluOutSchema)