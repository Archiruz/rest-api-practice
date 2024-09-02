# config/database.py

import os
import re

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import configparser

config = configparser.ConfigParser()
config.read("alembic.ini")

SQLALCHEMY_DATABASE_URL = config.get("alembic", "sqlalchemy.url")
# print(SQLALCHEMY_DATABASE_URL)

url_tokens = {
        "DB_USER": os.getenv("DB_USER", ""),
        "DB_HOST": os.getenv("DB_HOST", ""),
        "DB_NAME": os.getenv("DB_NAME", ""),
    }

SQLALCHEMY_DATABASE_URL = re.sub(r"\${(.+?)}", lambda m: url_tokens[m.group(1)], SQLALCHEMY_DATABASE_URL)
# print(SQLALCHEMY_DATABASE_URL)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

conn = engine.connect()
