import logging

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException

log = logging.getLogger("app.errores")


class ErrorDeDominio(Exception):
    """Error que lanzan los services; main.py lo convierte al envelope (TRD §2.3)."""

    def __init__(self, status: int, code: str, message: str, meta: dict | None = None):
        super().__init__(message)
        self.status, self.code, self.message, self.meta = status, code, message, meta


def respuesta_error(request: Request, status: int, code: str, message: str, details=None, meta=None):
    request_id = getattr(request.state, "request_id", None)
    error = {"code": code, "message": message}
    if details:
        error["details"] = details
    if meta:
        error["meta"] = meta
    error["request_id"] = request_id
    headers = {"X-Request-ID": request_id} if request_id else None
    return JSONResponse({"error": error}, status_code=status, headers=headers)


def registrar_manejadores(app: FastAPI):
    @app.exception_handler(ErrorDeDominio)
    async def dominio(request: Request, exc: ErrorDeDominio):
        return respuesta_error(request, exc.status, exc.code, exc.message, meta=exc.meta)

    @app.exception_handler(RequestValidationError)
    async def validacion(request: Request, exc: RequestValidationError):
        # shortcut: code y message por campo salen tal cual de Pydantic (en inglés), traducirlos cuando el frontend muestre errores por campo (M1)
        details = [
            {"field": ".".join(str(p) for p in e["loc"][1:]), "code": e["type"], "message": e["msg"]}
            for e in exc.errors()
        ]
        return respuesta_error(request, 422, "validacion_fallida", "Hay campos con errores.", details=details)

    @app.exception_handler(HTTPException)
    async def http(request: Request, exc: HTTPException):
        # solo llegan los del ruteo de Starlette: los services nunca lanzan HTTPException
        code, message = {
            404: ("no_encontrado", "El recurso no existe."),
            405: ("metodo_no_permitido", "El método no está permitido en esta ruta."),
        }.get(exc.status_code, ("error_http", str(exc.detail)))
        return respuesta_error(request, exc.status_code, code, message)

    @app.exception_handler(Exception)
    async def no_controlada(request: Request, exc: Exception):
        log.exception("error no controlado", extra={"request_id": getattr(request.state, "request_id", None)})
        return respuesta_error(request, 500, "error_interno", "Ocurrió un error inesperado.")
