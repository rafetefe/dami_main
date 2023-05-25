from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import Yardimsever

#Yeni Araç Girdisi
YardimseverInSchema = pydantic_model_creator(
    Yardimsever, name="YardimseverIn",  exclude=['id'], exclude_readonly=True
)
#API dıs çağrı Arac Okuma
YardimseverOutSchema = pydantic_model_creator(
    #exclude: okunmasına gerek olmayan satırlar
    Yardimsever, name="YardimseverOut", exclude=["id", "created_at", "modified_at"]
)
#Uygulamaiçi okuma
YardimseverDatabaseSchema = pydantic_model_creator(
    Yardimsever, name="Yardimsever", exclude=["created_at", "modified_at"]
)
