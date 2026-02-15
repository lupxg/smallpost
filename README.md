# Smallpost
Minimal post application build with Docker. 

## Description
Smallpost is a lightweight post management application that allows creating and retrieving post via a simple API.

# Tech stack
- Backend: Flask v3.1.2 + Python v3.12.
- Database: MySQL.
- Containerization: Docker + Docker compose.

# Requirements.
- Docker.
- Docker compose.

## Development setup using docker
1 - Create a folder named `db`
2 - Inside it, create a file called `password.txt`
3 - Add your database password inside that file.
Then run:
```bash
docker compose -f compose.dev.yaml up --build
```
The application will start in development mode.
