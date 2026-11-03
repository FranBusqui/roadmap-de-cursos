# Roadmap de Cursos

> WebApp de gestión de comunidad de cursos: catálogo comunitario de cursos gratuitos
> de cualquier plataforma + roadmaps personales de aprendizaje.
>
> **Estado:** Instancia B en curso — scaffold mínimo (tickets pre-clase T1–T5). Ver [CHANGELOG](CHANGELOG.md).

**Stack:** React 19 + Vite + pnpm · FastAPI + uv · PostgreSQL 18.6 · Docker Compose (dev)

## Cómo levantar

> Se completa en el ticket T4 (Docker Compose de desarrollo). Requisitos: Git y Docker con Docker Compose.

```bash
git clone https://github.com/FranBusqui/roadmap-de-cursos.git
cd roadmap-de-cursos
cp .env.example .env
docker compose up
```

---

## Qué hace

Roadmap de Cursos es para estudiantes y autodidactas que aprenden con cursos gratuitos
repartidos en decenas de plataformas y no tienen dónde compararlos ni ordenarlos.
Cualquier persona registrada puede **aportar** un curso gratuito (con su enlace activo y sus
metadatos: categoría, versión, año, docentes, si tiene cuestionarios, examen, certificado o aval
institucional) y declarar si ella misma lo tomó. Un **validador** de la comunidad revisa el aporte;
si lo aprueba, el curso pasa al **catálogo comunitario**, visible para todos (incluso sin cuenta).
Desde el catálogo, cada usuario arma su **roadmap personal y privado**: elige cursos, los ordena
y marca su progreso (pendiente · en curso · completado).

## Documentación

| Documento | Responde la pregunta | Link |
|-----------|----------------------|------|
| SPEC | ¿Qué nos pidieron construir y qué decidimos nosotros? | [docs/SPEC.md](docs/SPEC.md) |
| PRD | ¿Para quién, qué problema resuelve, qué hace y qué NO hace? | [docs/PRD.md](docs/PRD.md) |
| TRD | ¿Cómo lo construimos técnicamente y por qué? | [docs/TRD.md](docs/TRD.md) |
| UX-UI | ¿Cómo se ve, se siente y se comporta? | [docs/UX-UI.md](docs/UX-UI.md) |
| APPFlow | ¿Qué pantallas hay y cómo se navega? | [docs/APPFlow.md](docs/APPFlow.md) |
| BackendSchema | ¿Qué datos persistimos y qué API expone? | [docs/BackendSchema.md](docs/BackendSchema.md) |
| Implementation Plan | ¿En qué orden construimos y qué significa "hecho"? | [docs/IMPLEMENTATION_PLAN.md](docs/IMPLEMENTATION_PLAN.md) |

> La SPEC de clase original se conserva sin modificar en el primer commit del repo
> (`docs/SPEC.md`); el archivo actual es su versión refinada.

## Cómo revisar este repo

- Los `.md` se renderizan solos en GitHub.
- Los diagramas Mermaid (`erDiagram`, `flowchart`, `stateDiagram`) también: si los ves como
  texto crudo, falta el bloque ` ```mermaid `.
- Preview local: VS Code con `Ctrl+Shift+V` (extensión "Markdown All in One" recomendada).
- Orden de lectura sugerido: SPEC → PRD → UX-UI → APPFlow → BackendSchema → TRD → Implementation Plan.

## Estado del trabajo

| Instancia | Contenido | Estado |
|-----------|-----------|--------|
| A — Documentación | repo + 7 documentos | Enviada el 23/10/2026. No se recibió devolución; el docente envió los tickets de desarrollo, que se toman como habilitación para avanzar. |
| B — Desarrollo del MVP | scaffold (tickets pre-clase T1–T5) → módulos P0 del Implementation Plan | En curso |
| C — Clase 27/10 | testing, Docker multi-stage, gestión del cambio (tickets de clase T1–T11) | Pendiente |

## Versionado

- **Flujo de Git: `main` / `dev` / ramas de trabajo** (fijado por el ticket pre-clase del docente; detalle en [TRD §4.1](docs/TRD.md#41-flujo-de-git-main--dev--ramas-de-trabajo)).
  - `main` solo recibe el merge de `dev` en cada release, con tag anotado `vX.Y.Z`. Nunca commits directos.
  - `dev` es la rama de integración.
  - Las ramas de trabajo nacen de `dev` y vuelven a `dev`: `feat/T{N}-descripcion-corta` o `fix/descripcion-corta`.
- **Convención de commits:** [Conventional Commits](https://www.conventionalcommits.org/) —
  `feat:`, `fix:`, `docs:`, `test:`, `refactor:`, `chore:`, `docker:`.
- **Releases:** SemVer `0.y.z`, registrados en el [CHANGELOG](CHANGELOG.md). `v0.1.0` = scaffold mínimo.

---

## Referencias de aprendizaje

### Markdown (para escribir los 6 documentos bien)

| Recurso | Para qué |
|---------|----------|
| [Markdown Guide — sintaxis básica](https://www.markdownguide.org/basic-syntax/) | encabezados, listas, énfasis, imágenes |
| [Markdown Guide — cheat sheet](https://www.markdownguide.org/cheat-sheet/) | tablas, task lists, bloques de código |
| [CommonMark — referencia](https://commonmark.org/help/) | la especificación cuando hay dudas |
| [GitHub — Writing on GitHub](https://docs.github.com/en/get-started/writing-on-github) | GFM, tablas, checklists |
| [GitHub — Mermaid en Markdown](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams) | diagramas que renderizan en tu repo |

### Por tipo de documento

| Documento | Recurso |
|-----------|---------|
| PRD | [Atlassian — Plantilla PRD](https://www.atlassian.com/software/confluence/templates/product-requirements) · [Lenny Rachitsky — plantilla](https://www.atlassian.com/software/confluence/templates/requirements) |
| TRD | [Design Docs at Google](https://www.industrialempathy.com/posts/design-docs-at-google/) — el clásico: contexto, goals/non-goals, trade-offs |
| UX-UI | [NN/g — Front-End Style-Guides](https://www.nngroup.com/articles/front-end-style-guides/) · [NN/g — Design Systems 101](https://www.nngroup.com/articles/design-systems-101/) · [Material Design 3 (la inspiración)](https://m3.material.io/) · [Material Symbols (iconos)](https://fonts.google.com/icons) |
| APPFlow | [NN/g — IA vs. Sitemaps](https://www.nngroup.com/articles/information-architecture-sitemaps/) · [NN/g — User Journeys vs. User Flows](https://www.nngroup.com/articles/user-journeys-vs-user-flows/) |
| BackendSchema | [Mermaid — ER Diagrams](https://mermaid.js.org/syntax/entityRelationshipDiagram.html) · [PostgreSQL — Conceptual Model](https://www.postgresql.org/docs/current/datamodel.html) |
| Implementation Plan | [Atlassian — Plantilla de plan de proyecto](https://www.atlassian.com/software/confluence/templates/project-plan) · [Shape Up](https://basecamp.com/shapeup/) — scopes y ciclos |

---

## Licencia / uso

Trabajo Práctico — Desarrollo de Software, UTN FR La Plata, 2026.
Autor: BUSCAGLIA, Francisco Nicolás.
