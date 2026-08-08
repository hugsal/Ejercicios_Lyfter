from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from config import DB_NAME, USER, PASSWORD, HOST

url = f"postgresql://{USER}:{PASSWORD}@{HOST}/{DB_NAME}"

engine = create_engine(url, echo=False)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

class BaseDb(DeclarativeBase):
    pass