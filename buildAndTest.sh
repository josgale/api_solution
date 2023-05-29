#!/bin/bash


docker-compose up --build -d
sleep 10
docker exec -it flask-app /bin/bash -c "cd tests && python test_user_api.py"