# from sqlalchemy.orm import DeclarativeBase  # Новый импорт для SQLAlchemy 2.0+
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy import create_engine
# import utils.config as config


# DATABASE_URL = f"postgresql+psycopg2://{config.PSQL_USER}:{config.PSQL_PASS}@{config.PSQL_HOST}:{config.PSQL_PORT}/{config.PSQL_NAME}"

# engine = create_engine(DATABASE_URL, echo=True)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# class Base(DeclarativeBase):
#     pass


# def init_db():
#     from sql.model import User
#     Base.metadata.create_all(bind=engine)


import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import URL, create_engine, text
from utils import config
from sqlalchemy.orm import DeclarativeBase


engine = create_async_engine(
        url=config.DATABASE_URL,
        echo = True,
)

class Base(DeclarativeBase):
    __allow_unmapped__ = True

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)