# StarWarsDatalake
A datalake of star wars data retrieved from the swapi API

# Setup Postgres with Docker
-Download latest docker desktop release

-Pull the postgres image with command:  > docker pull postgres:latest

# Create new container 

-start a new postgres instance
 docker run --name StarWarsDriven -e POSTGRES_PASSWORD=maytheforcebewithyou -d postgres

-password = "maytheforcebewithyou"

-Start up docker in desktop by pressing the run button

-Verify you docker instance is running with: >docker ps

-Enter postgres shell through docker: > docker exec -it StarWarsDriven bash

-Connect to postgres Db with: > psql -h localhost -U postgres

-Create DB tab: >CREATE DATABASE StarWarsDriven

-Display DB: >

# Run Container