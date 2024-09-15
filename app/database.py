# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base

# PostgreSQL database connection string
DATABASE_URL = 'postgresql://postgres:postgres@localhost:5432/estacio_python'

# Create the database engine
engine = create_engine(DATABASE_URL)

# Create a local session for database transactions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Function to initialize the database (create tables)
def init_db():
    Base.metadata.create_all(bind=engine)
