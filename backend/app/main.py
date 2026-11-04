import logging

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from app.catalogo.router import router as catalogo_router
from app.compartido.db import engine
from app.compartido.errores import registrar_manejadores
from app.compartido.logging import configurar_logging, middleware_request_id
from app.config import settings

configurar_logging(settings.log_level)
log = logging.getLogger("app")

# /docs y el esquema OpenAPI solo en desarrollo (BackendSchema §3)
es_dev = settings.app_env == "dev"
app = FastAPI(
    title="Roadmap de Cursos API",
    docs_url="/docs" if es_dev else None,
    redoc_url=None,
    openapi_url="/openapi.json" if es_dev else None,
)
app.middleware("http")(middleware_request_id)
registrar_manejadores(app)
app.include_router(catalogo_router)


@app.get("/health")
def health():
    try:
        with engine.connect() as conexion:
            conexion.execute(text("select 1"))
    except SQLAlchemyError:
        log.warning("health: sin conexión con PostgreSQL")
        return JSONResponse({"status": "degraded", "db": "error"}, status_code=503)
    return {"status": "ok", "db": "ok"}
