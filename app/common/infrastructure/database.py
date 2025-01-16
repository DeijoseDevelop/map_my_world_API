import os

from sqlmodel import Session, SQLModel, create_engine


default_sqlite_url = "sqlite:///./map-my-world.db"
db_url = os.getenv("DATABASE_URL", default_sqlite_url)

if db_url.startswith("sqlite"):
    # Para SQLite
    connect_args = {"check_same_thread": False}
    engine = create_engine(db_url, connect_args=connect_args)
else:
    # Para PostgreSQL (u otro motor)
    engine = create_engine(db_url)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session