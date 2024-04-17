task1

sudo docker run --name hw03_db -p 5432:5432 -e POSTGRES_PASSWORD=123456 -d postgres

python create_tables.py

python seed.py

python execute_queries.py

task2

sudo docker run --name hw03_mongodb -d -p 27017:27017 mongo

python create_db.py

python main.py