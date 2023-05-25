from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "arac" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "isim" VARCHAR(30) NOT NULL,
    "soyisim" VARCHAR(30) NOT NULL,
    "telefon" VARCHAR(12) NOT NULL,
    "tur" VARCHAR(20) NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "gonullu" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "isim" VARCHAR(30) NOT NULL UNIQUE,
    "soyisim" VARCHAR(30),
    "telefon" VARCHAR(12),
    "postakodu" VARCHAR(6),
    "adres" TEXT NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "ihtiyac" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "isim" VARCHAR(30) NOT NULL UNIQUE,
    "soyisim" VARCHAR(30),
    "telefon" VARCHAR(12),
    "tur" VARCHAR(50) NOT NULL,
    "aciklama" TEXT NOT NULL,
    "adres" TEXT NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "iletisim" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "isim" VARCHAR(30) NOT NULL UNIQUE,
    "soyisim" VARCHAR(30),
    "email" VARCHAR(30),
    "mesaj" TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS "yardimsever" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "isim" VARCHAR(30) NOT NULL UNIQUE,
    "soyisim" VARCHAR(30),
    "telefon" VARCHAR(12),
    "tur" VARCHAR(50) NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
