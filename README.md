<h1 align="center">
GoEventure Events Backend
</h1>

# ⚒️ Techologies Used

- Alembic: For Database Migrations.
- SQLAlchemy: For ORM.
- Pydantic: For Typing or Serialization.
- Pytests: For TDD or Unit Testing.
- Poetry: Python dependency management and packaging made easy. (Better than pip)
- Docker & docker-compose : For Virtualization.
- postgresSQL: Database.
- PgAdmin: To interact with the Postgres database sessions.
- Loguru: Easiest logging ever done.


# 🚀 Up and run in 5 mins 🕙
Make sure you have docker and docker-compose installed [docker installation guide](https://docs.docker.com/compose/install/)
## Step 1
create **.env** file in root folder or use [Doppler](www.doppler.com) for secrets mgmt.
```
DATABASE_URL=postgresql+psycopg://postgres:password@db:5432/events_db
DB_USER=postgres
DB_PASSWORD=password
DB_NAME=events_db
PGADMIN_EMAIL=admin@admin.com
PGADMIN_PASSWORD=admin
X_TOKEN=12345678910
```

## Step 2
```
docker-compose build
```

## Step 3
```
docker-compose up
```

# 🎉 Your Production Ready FastAPI CRUD backend app is up and running on `localhost:8000`

- Swagger docs on `localhost:8000/docs`

- PgAdmin on `localhost:5050`


# Run Tests Locally

`doppler run -- docker-compose -f docker-compose-test.yml build`

`doppler run -- docker-compose -f docker-compose-test.yml run test`