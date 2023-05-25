from src.database.models import Ihtiyac
from src.schemas.ihtiyac import IhtiyacOutSchema
from .crud import Crud

Crud_Ihtiyac = Crud(Ihtiyac, IhtiyacOutSchema)