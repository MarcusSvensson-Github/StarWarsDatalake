# StarWarsDatalake
A datalake of star wars data retrieved from the swapi API


# Setup Postgres with Docker
-Download latest docker desktop release

-Build images and run them with > docker compose up --build -d

-To shutdown the containers > dcoker compose down

# Create new postgres container 

-Create table: > CREATE TABLE starwars_people(ID SERIAL PRIMARY KEY, NAME TEXT NOT NULL, HEIGHT INT NOT NULL, HAIR_COLOR TEXT NOT NULL,SKIN_COLOR TEXT NOT NULL, EYE_COLOR TEXT NOT NULL, BIRTH_YEAR TEXT NOT NULL, GENDER TEXT NOT NULL);



