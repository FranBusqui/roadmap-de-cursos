import json
import logging
import sys
import time
import uuid
from datetime import UTC, datetime

from fastapi import Request

log = logging.getLogger("app.request")

# atributos propios de LogRecord: todo lo demás llega por extra= y va al JSON
_ESTANDAR = set(vars(logging.LogRecord("", 0, "", 0, "", None, None))) | {"message", "taskName"}


class FormatoJSON(logging.Formatter):
    def format(self, record):
        linea = {
            "ts": datetime.fromtimestamp(record.created, UTC).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "msg": record.getMessage(),
        }
        linea.update({k: v for k, v in vars(record).items() if k not in _ESTANDAR})
        if record.exc_info:
            linea["exc"] = self.formatException(record.exc_info)
        return json.dumps(linea, ensure_ascii=False, default=str)


def configurar_logging(nivel: str):
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(FormatoJSON())
    logging.basicConfig(level=nivel, handlers=[handler], force=True)
    # uvicorn trae sus propios handlers: los mandamos al nuestro y apagamos su access log (lo reemplaza el middleware)
    for nombre in ("uvicorn", "uvicorn.error", "uvicorn.access"):
        logging.getLogger(nombre).handlers.clear()
        logging.getLogger(nombre).propagate = True
    logging.getLogger("uvicorn.access").disabled = True


async def middleware_request_id(request: Request, call_next):
    request.state.request_id = request_id = str(uuid.uuid4())
    inicio = time.perf_counter()
    estado = 500  # si call_next lanza, la respuesta la arma el manejador de errores no controlados
    try:
        response = await call_next(request)
        estado = response.status_code
        response.headers["X-Request-ID"] = request_id
        return response
    finally:
        # solo método, ruta y estado: nunca cookies, headers ni cuerpos (RNF-012)
        log.info(
            "request",
            extra={
                "request_id": request_id,
                "metodo": request.method,
                "ruta": request.url.path,
                "estado": estado,
                "duracion_ms": round((time.perf_counter() - inicio) * 1000, 1),
            },
        )
