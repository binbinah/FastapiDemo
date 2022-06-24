from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
import os

name = os.environ.get("db_name", "demo")
user = os.environ.get("db_user", "demo")
password = os.environ.get("db_password", "demo")
host = os.environ.get("db_host", "db")
port = os.environ.get("db_port", 3306)

SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{user}:{password}@{host}:{port}/{name}"
engine = create_engine(SQLALCHEMY_DATABASE_URI, poolclass=NullPool)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
