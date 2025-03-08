import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv(
    override=True
)

TOKEN = os.environ.get("TOKEN")

REDIS_HOST = os.environ.get("REDIS_HOST")
REDIS_PORT = int(os.environ.get("REDIS_PORT"))
REDIS_DB = os.environ.get("REDIS_DB")

PSQL_USER = os.environ.get("PSQL_USER") 
PSQL_PASS = os.environ.get("PSQL_PASS") 
PSQL_HOST = os.environ.get("PSQL_HOST") 
PSQL_PORT = int(os.environ.get("PSQL_PORT")) 
PSQL_NAME = os.environ.get("PSQL_NAME")
DB_ENGINE = os.environ.get("DB_ENGINE")

DATABASE_URL = f"{DB_ENGINE}://{PSQL_USER}:{PSQL_PASS}@{PSQL_HOST}:{PSQL_PORT}/{PSQL_NAME}"
# @property
# def DATABASE_URL_asyncpg(self):
#     # postgresql+asyncpg://postgres: postgres@localhost:5433/postgre
#     return f"postgresql+asyncpg://{self.DB_USER}: {self.DB_PASS }@{ self.DB_HOST}: { self.DB_PORT}/{self}"
    
# model_config = SettingsConfigDict(env_file=".env")

