sudo docker-compose up -d --build
sudo docker-compose exec backend aerich init -t src.database.config.TORTOISE_ORM
sudo docker-compose exec backend aerich init-db
