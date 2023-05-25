from src.database.models import Yardimsever
from src.schemas.yardimsever import YardimseverOutSchema
from .crud import Crud

Crud_Yardimsever = Crud(Yardimsever, YardimseverOutSchema)