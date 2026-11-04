# Changelog

Todos los cambios relevantes del proyecto se registran en este archivo.

El formato sigue [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/) y el proyecto usa
[Versionado Semántico](https://semver.org/lang/es/) (`0.y.z` mientras el producto sea inestable).
Solo `main` recibe versiones: cada release es un merge de `dev` con su tag anotado `vX.Y.Z`
(flujo en [TRD §4.1](docs/TRD.md#41-flujo-de-git-main--dev--ramas-de-trabajo)).

## [Unreleased]

### Added

- Configuración del backend con `pydantic-settings` y conexión a PostgreSQL con SQLAlchemy 2.1 + psycopg 3 (tarea 0.3).
- Envelope de errores del TRD §2.2 para 404, 405, 422 y 500, con el código nuevo `metodo_no_permitido` (tarea 0.3).
- Log JSON de una línea por request y header `X-Request-ID` en todas las respuestas (tarea 0.3).
- Primeros tests del backend (pytest) sobre el envelope de errores (tarea 0.3).

### Changed

- `GET /health` informa el estado de la base: `{"status":"ok","db":"ok"}` o `503 degraded` si PostgreSQL no responde (tarea 0.3).
- `/docs` y `/openapi.json` solo se sirven con `APP_ENV=dev` (tarea 0.3).

## [v0.1.0] - 2026-11-03

Scaffold mínimo del proyecto (tickets pre-clase T1–T5).

### Added

- Workflow de Git `main` / `dev` / `feat/*` y este CHANGELOG (T1).
- Estructura de carpetas por dominio según TRD §3.2 (Screaming Architecture) y `.env.example` con las variables del TRD §4.4 (T1).
- Backend mínimo: FastAPI 0.158.2 + uv con `GET /health` y `GET /api/v1/cursos` (página vacía con el contrato de paginación del BackendSchema) (T2).
- Frontend mínimo: React 19 + Vite + pnpm con la pantalla del catálogo consumiendo `GET /api/v1/cursos` (estados de carga, error y vacío) y proxy `/api` hacia el backend (T3).
- Docker Compose de desarrollo con `postgres:18.6` (volumen `pgdata`), backend y frontend, y Dockerfiles simples (T4).
- README con instrucciones verificables para levantar el entorno (T4).

### Changed

- El flujo de Git pasa de GitHub Flow a `main` / `dev` / ramas de trabajo, según el ticket pre-clase del docente (TRD §4.1, SPEC §9).
- Las versiones exactas instaladas quedan registradas en SPEC §6 y TRD §1 (T5).

[Unreleased]: https://github.com/FranBusqui/roadmap-de-cursos/compare/v0.1.0...dev
[v0.1.0]: https://github.com/FranBusqui/roadmap-de-cursos/releases/tag/v0.1.0
