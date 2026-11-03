from fastapi import APIRouter, Query

router = APIRouter(prefix="/api/v1/cursos", tags=["catalogo"])


@router.get("")
def listar_cursos(
    page: int = Query(1, ge=1),
    page_size: int = Query(12, ge=1, le=50),
):
    # shortcut: página vacía hasta tener la tabla cursos (tarea 2.3 del plan)
    return {"items": [], "total": 0, "page": page, "page_size": page_size}
