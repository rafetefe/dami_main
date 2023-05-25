from tortoise import fields, models

#Mevcut tablolar
#Gonullu, Ihtiyac, Yardimsever, Arac, Iletisim (5)

class Gonullu(models.Model):
    id = fields.IntField(pk=True)
    isim = fields.CharField(max_length=30, unique=True)
    soyisim = fields.CharField(max_length=30, null=True)
    telefon = fields.CharField(max_length=12, null=True)
    postakodu = fields.CharField(max_length=6, null=True)
    adres = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)


class Ihtiyac(models.Model):
    id = fields.IntField(pk=True)
    isim = fields.CharField(max_length=30, unique=True)
    soyisim = fields.CharField(max_length=30, null=True)
    telefon = fields.CharField(max_length=12, null=True)
    tur = fields.CharField(max_length=50)
    aciklama = fields.TextField()
    adres = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)

class Yardimsever(models.Model):
    id = fields.IntField(pk=True)
    isim = fields.CharField(max_length=30, unique=True)
    soyisim = fields.CharField(max_length=30, null=True)
    telefon = fields.CharField(max_length=12, null=True)
    tur = fields.CharField(max_length=50)
    created_at = fields.DatetimeField(auto_now_add=True)

class Arac(models.Model):
    id = fields.IntField(pk=True)
    isim = fields.CharField(max_length=30, unique=False)
    soyisim = fields.CharField(max_length=30, unique=False)
    telefon = fields.CharField(max_length=12, unique=False)
    tur = fields.CharField(max_length=20, unique=False)
    created_at = fields.DatetimeField(auto_now_add=True)

class Iletisim(models.Model):
    id = fields.IntField(pk=True)
    isim = fields.CharField(max_length=30, unique=True)
    soyisim = fields.CharField(max_length=30, null=True)
    email = fields.CharField(max_length=30, null=True)
    mesaj = fields.TextField()