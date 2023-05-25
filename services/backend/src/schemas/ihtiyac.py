from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import Ihtiyac

#Yeni Araç Girdisi
IhtiyacInSchema = pydantic_model_creator(
    Ihtiyac, name="IhtiyacIn", exclude=['id'], exclude_readonly=True
)
#API dıs çağrı Arac Okuma
IhtiyacOutSchema = pydantic_model_creator(
    #exclude: okunmasına gerek olmayan satırlar
    Ihtiyac, name="IhtiyacOut", exclude=["id", "created_at", "modified_at"]
)
#Uygulamaiçi okuma
IhtiyacDatabaseSchema = pydantic_model_creator(
    Ihtiyac, name="Ihtiyac", exclude=["created_at", "modified_at"]
)
