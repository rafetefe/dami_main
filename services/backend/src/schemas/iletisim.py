from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import Iletisim

#Yeni Araç Girdisi
IletisimInSchema = pydantic_model_creator(
    Iletisim, name="IletisimIn", exclude=['id'], exclude_readonly=True
)
#API dıs çağrı Arac Okuma
IletisimOutSchema = pydantic_model_creator(
    #exclude: okunmasına gerek olmayan satırlar
    Iletisim, name="IletisimOut", exclude=["id", "created_at", "modified_at"]
)
#Uygulamaiçi okuma
IletisimDatabaseSchema = pydantic_model_creator(
    Iletisim, name="Iletisim", exclude=["created_at", "modified_at"]
)
