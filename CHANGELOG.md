# Changelog

Todos los cambios relevantes del proyecto se registran en este archivo.

El formato sigue [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/) y el proyecto usa
[Versionado Semántico](https://semver.org/lang/es/) (`0.y.z` mientras el producto sea inestable).
Solo `main` recibe versiones: cada release es un merge de `dev` con su tag anotado `vX.Y.Z`
(flujo en [TRD §4.1](docs/TRD.md#41-flujo-de-git-main--dev--ramas-de-trabajo)).

## [Unreleased]

### Added

- Workflow de Git `main` / `dev` / `feat/*` y este CHANGELOG (ticket pre-clase T1).
- Estructura de carpetas por dominio según TRD §3.2 (Screaming Architecture) y `.env.example` con las variables del TRD §4.4.

### Changed

- El flujo de Git pasa de GitHub Flow a `main` / `dev` / ramas de trabajo, según el ticket pre-clase del docente (TRD §4.1, SPEC §9).
