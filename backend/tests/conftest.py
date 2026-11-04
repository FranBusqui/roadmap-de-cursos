import os

# valores por defecto para correr pytest fuera de Docker; en el contenedor ya vienen del .env
os.environ.setdefault("APP_ENV", "test")
os.environ.setdefault("DATABASE_URL", "postgresql+psycopg://roadmap:roadmap_dev@localhost:5432/roadmap")
