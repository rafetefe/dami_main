from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import Arac

#Yeni Araç Girdisi
AracInSchema = pydantic_model_creator(
    Arac, name="AracIn", exclude_readonly=True
)
#API dıs çağrı Arac Okuma
AracOutSchema = pydantic_model_creator(
    #exclude: okunmasına gerek olmayan satırlar
    Arac, name="AracOut", exclude=["id", "created_at"]
)
#Uygulamaiçi okuma
AracDatabaseSchema = pydantic_model_creator(
    Arac, name="User", exclude=["created_at"]
)
