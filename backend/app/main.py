from fastapi import FastAPI

from app.catalogo.router import router as catalogo_router

app = FastAPI(title="Roadmap de Cursos API")
app.include_router(catalogo_router)


@app.get("/health")
def health():
    return {"status": "ok"}
