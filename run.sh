sudo docker-compose up -d --build
sudo docker-compose exec backend aerich migrate
sudo docker-compose exec backend aerich upgrade
