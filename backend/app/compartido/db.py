from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import settings

# connect_timeout corto: si PostgreSQL no responde, /health contesta 503 rápido en vez de colgarse
engine = create_engine(settings.database_url, pool_pre_ping=True, connect_args={"connect_timeout": 3})
SessionLocal = sessionmaker(engine)


def get_db():
    with SessionLocal() as db:
        yield db
