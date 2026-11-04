from fastapi.testclient import TestClient

from app.main import app


@app.get("/_test/explota")
def _explota():
    raise RuntimeError("detalle interno que no debe salir")


client = TestClient(app, raise_server_exceptions=False)


def test_ruta_inexistente_devuelve_404_con_envelope():
    # Arrange
    ruta = "/api/v1/inexistente"

    # Act
    r = client.get(ruta)

    # Assert
    assert r.status_code == 404
    assert r.json()["error"]["code"] == "no_encontrado"
    assert r.json()["error"]["request_id"] == r.headers["X-Request-ID"]


def test_page_size_fuera_de_rango_devuelve_422_con_details():
    # Arrange
    ruta = "/api/v1/cursos?page_size=99"

    # Act
    r = client.get(ruta)

    # Assert
    assert r.status_code == 422
    assert r.json()["error"]["code"] == "validacion_fallida"
    assert [d["field"] for d in r.json()["error"]["details"]] == ["page_size"]


def test_error_no_controlado_devuelve_500_sin_detalle():
    # Arrange
    ruta = "/_test/explota"

    # Act
    r = client.get(ruta)

    # Assert
    assert r.status_code == 500
    assert r.json()["error"]["code"] == "error_interno"
    assert "detalle interno" not in r.text
    assert r.json()["error"]["request_id"] == r.headers["X-Request-ID"]
