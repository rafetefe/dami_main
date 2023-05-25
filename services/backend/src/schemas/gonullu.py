from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import Gonullu

#Yeni Araç Girdisi
GonulluInSchema = pydantic_model_creator(
    Gonullu, name="GonulluIn", exclude=['id'], exclude_readonly=True
)
#API dıs çağrı Arac Okuma
GonulluOutSchema = pydantic_model_creator(
    #exclude: okunmasına gerek olmayan satırlar
    Gonullu, name="GonulluOut", exclude=["id", "created_at", "modified_at"]
)
#Uygulamaiçi okuma
GonulluDatabaseSchema = pydantic_model_creator(
    Gonullu, name="Gonullu", exclude=["created_at", "modified_at"]
)
