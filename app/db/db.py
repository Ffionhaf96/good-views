from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from os import getenv

DATABASE_URI = f"postgresql://{getenv('POSTGRES_USER')}:{getenv('POSTGRES_PASSWORD')}@postgres:5432/{getenv('POSTGRES_DB')}"

engine = create_engine(DATABASE_URI, echo=True)
Session = sessionmaker(bind=engine)
