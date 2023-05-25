from src.database.models import Iletisim
from src.schemas.iletisim import IletisimOutSchema
from .crud import Crud

Crud_Iletisim = Crud(Iletisim, IletisimOutSchema)