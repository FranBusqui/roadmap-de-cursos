# SPEC — Roadmap de Cursos

> **Qué es este documento:** la versión refinada de la SPEC de clase.
> El repo empieza con la SPEC de clase **tal cual** (primer commit). Este archivo es su evolución:
> mismos requisitos, ambigüedades resueltas, decisiones incorporadas.
> **Regla:** si la SPEC de clase no lo decía y lo definí yo, queda acá (con el porqué)
> o se referencia al documento donde quedó decidido (PRD para producto, TRD para técnica).
> **Cuándo está bien:** un lector que no estuvo en el aula del 20/10 entiende el producto
> completo leyendo solo este archivo, y puede rastrear cada decisión hasta su origen.

## 1. Identidad del producto

- **Nombre propio:** **Roadmap de Cursos** (la comunidad que arma, en conjunto, su mapa de aprendizaje gratuito)
- **Una línea:** para estudiantes y autodidactas · catálogo comunitario y validado de cursos gratuitos de cualquier plataforma + roadmap personal para planificar y seguir el aprendizaje · porque lo gratuito existe de sobra, pero está disperso, sin criterio común y sin orden.

### Glosario mínimo

| Término | Significado en este producto |
|---------|------------------------------|
| **Curso** | Recurso de aprendizaje gratuito alojado en una plataforma o proveedor externo; el producto guarda sus metadatos y su enlace, no su contenido. |
| **Aporte** | Un curso en su ciclo de contribución: desde que un usuario lo carga hasta que es publicado o rechazado. Técnicamente es el mismo registro `curso` con un `estado`. |
| **Catálogo comunitario** | Conjunto de cursos en estado `publicado`; es público y paginado. |
| **Validador** | Usuario con rol `validador`, designado para revisar aportes. |
| **Roadmap personal** | Lista privada y ordenable de cursos del catálogo que un usuario eligió, con su progreso. Es sinónimo de "mi catálogo" de la SPEC de clase. |
| **Declaración de toma** | Dato obligatorio del aporte: si quien lo carga tomó (cursó) el curso, sí o no. |

## 2. Problema

Quien quiere aprender hoy con cursos gratuitos se enfrenta a una oferta enorme y desordenada:
Coursera, edX, YouTube, freeCodeCamp, plataformas universitarias, fundaciones y empresas
publican contenido gratuito, cada una con su propio buscador y sin un criterio común. Las preguntas
que más importan antes de empezar —¿da certificado?, ¿tiene examen?, ¿lo avala una organización?,
¿de qué año es y sigue vigente?, ¿alguien que lo cursó lo recomienda?— están enterradas en cada sitio
o directamente no se responden.

Lo que existe hoy no resuelve el problema. Los catálogos de cada plataforma solo muestran *sus*
cursos y tienen un interés comercial en retener al usuario. Los buscadores y las redes premian
el posicionamiento, no la calidad ni la vigencia. Las listas que circulan por grupos de chat
o planillas compartidas se pierden, se desactualizan y no se pueden filtrar. Y para planificar
el aprendizaje cada persona termina usando notas sueltas o marcadores del navegador, sin orden
ni seguimiento de progreso.

Una comunidad cambia la ecuación del catálogo: ninguna persona puede relevar cientos de plataformas,
pero muchas personas pueden aportar cada una los cursos que conocen, y unas pocas pueden revisarlos
con un criterio común antes de publicarlos. La declaración de "lo tomé / no lo tomé" agrega una
señal de confianza que ningún catálogo comercial ofrece, y la validación evita que el catálogo
se llene de enlaces rotos, cursos pagos disfrazados o duplicados. Sobre ese catálogo confiable,
cada persona arma su propio roadmap y avanza a su ritmo.

## 3. Visión

En 12 meses, Roadmap de Cursos es la referencia de una comunidad de estudio para encontrar
cursos gratuitos confiables: un catálogo con miles de cursos validados de decenas de plataformas,
un grupo estable de validadores voluntarios con tiempos de revisión de pocas horas, y roadmaps
personales que los usuarios consultan semana a semana para decidir qué estudiar a continuación.
La confianza surge de la combinación de metadatos claros (certificado, examen, aval, versión, año),
validación humana y la experiencia declarada de quienes ya tomaron cada curso.

## 4. Alcance

### Dentro

- **Identidad:** registro, login, logout, recuperación de contraseña (ciclo completo: solicitud → enlace con token → nueva contraseña), rate limiting en login (y en recuperación y registro), contraseñas con hash robusto, dos roles (`usuario`, `validador`).
- **Catálogo comunitario público:** listado paginado, búsqueda por texto, filtro por categoría, filtros por atributos (certificado, examen, cuestionarios, aval), detalle de curso con enlace externo.
- **Aporte de cursos:** formulario con los metadatos exigidos por la SPEC de clase más plataforma e idioma; declaración de toma; detección de enlaces duplicados; seguimiento del estado de cada aporte; borrador y reenvío tras rechazo.
- **Validación comunitaria:** cola de revisión para validadores; aprobar o rechazar (con motivo) con registro de cada decisión.
- **Roadmap personal:** agregar cursos publicados, marcar progreso (pendiente / en curso / completado), ordenar y quitar; privado.
- **Interfaz:** mobile-first con mejora progresiva, menú sándwich en mobile, todo listado paginado, estética inspirada en Google/Material, accesibilidad AA.
- **Entorno de desarrollo reproducible** con Docker Compose (incluye una bandeja de correo local, Mailpit, para el flujo de recuperación de contraseña).

### Fuera (out of scope explícito)

- Pagos, cursos de pago o cualquier forma de monetización.
- Alojar contenido de cursos o emitir certificados propios: el producto solo enlaza a cursos externos.
- App móvil nativa, PWA/offline y modo oscuro.
- Inicio de sesión social (Google, GitHub, etc.), autenticación de dos factores y verificación de email.
- Panel de administración: la gestión de categorías y de roles se hace fuera de la UI (seed y script).
- Edición o despublicación de cursos ya publicados.
- Reseñas, puntajes, comentarios, foros y cualquier interacción social entre usuarios.
- Roadmaps compartidos o públicos; más de un roadmap por usuario.
- Verificación automática de enlaces (scraping, chequeos HTTP) y reporte de enlaces rotos.
- Notificaciones (email o push) de aprobación/rechazo: el estado se consulta dentro de la app.
- Recomendaciones automáticas o IA, importación masiva de cursos, internacionalización (solo español).

## 5. Reglas de producto clave

| # | Regla | Origen |
|---|-------|--------|
| BR-001 | Un curso aportado entra al sistema `en_revision` y solo llega al catálogo comunitario tras ser **validado** por un validador. | SPEC clase ("cursos cargados y **validados** pasan al catálogo") |
| BR-002 | Quien aporta un curso declara obligatoriamente si lo tomó o no, y esa declaración es pública en el detalle. | SPEC clase |
| BR-004 | Un mismo enlace no puede estar dos veces en el sistema entre cursos activos (`en_revision` o `publicado`): el catálogo no tiene duplicados. | decisión propia (§8 #6) |
| BR-005 | El roadmap es **personal y privado**: cada usuario ve y edita solo el suyo, y solo puede incluir cursos publicados. | SPEC clase + decisión propia |
| BR-007 | Existen dos roles, `usuario` y `validador`; un validador **no puede validar sus propios aportes**. | decisión propia (§8 #1, #2) |

> El detalle completo de reglas vive en el [PRD §7](PRD.md#7-reglas-de-negocio). Acá van las 5 que definen el carácter del producto.

## 6. Stack registrado (versiones exactas con las que se va a desarrollar)

| Capa | Tecnología | Versión exacta | Cómo se verifica / registra |
|------|------------|----------------|-----------------------------|
| Frontend | React + Vite + pnpm | React **19.x** (última stable de la serie 19 al instalar; queda congelada en `pnpm-lock.yaml`) · Vite y pnpm: última stable al instalar | `pnpm -v`, `pnpm ls react vite` |
| Backend | FastAPI + uv | FastAPI **0.158.2** (referencia de la SPEC oficial al 21/10/2026) · Python 3.13 gestionado por uv · uv: última stable | `uv --version`, `uv pip show fastapi` |
| Base de datos | PostgreSQL | **18.6** | `SELECT version();` |
| Infra (dev) | Docker + Docker Compose | última stable al instalar | `docker --version`, `docker compose version` |
| Runtime del frontend en contenedor | Node.js | **24 LTS** (Node 20 ya no recibe soporte desde abril de 2026) | `node -v` |
| Correo (dev) | Mailpit | última stable, tag fijado en `docker-compose.yml` | imagen `axllent/mailpit:<tag>` |

> **Nota de registro:** las versiones con "última stable al instalar" se escriben acá, con número exacto,
> en la tarea 0.1 del [Implementation Plan](IMPLEMENTATION_PLAN.md) (durante la Instancia B), y se respaldan con
> los lockfiles (`pnpm-lock.yaml`, `uv.lock`). Este documento se actualiza con lo que **realmente** se instaló.
> Mailpit no altera el stack fijado por la SPEC: es una herramienta de desarrollo para poder recibir
> localmente el correo de recuperación de contraseña.

## 7. Restricciones técnicas heredadas de la SPEC de clase

| # | Restricción | Cómo la vamos a cumplir (1-2 líneas) |
|---|-------------|--------------------------------------|
| 1 | Mobile-first con mejora progresiva: base sin media queries; `@media (min-width: …)` solo para agregar/mejorar | El CSS base se escribe para 360 px sin ninguna media query; solo hay dos capas `min-width` (768 px y 1024 px) que **agregan** (grid de 2/3 columnas, nav horizontal, tabla real). Ver UX-UI §3. |
| 2 | Paginación de todas las consultas de listado y de sus tablas | Paginación **offset + total** (`page`, `page_size`; defecto 12, máximo 50) en catálogo, roadmap, mis aportes y cola de validación; el front siempre muestra paginador. Ver TRD §2 y PRD RNF-001. |
| 3 | Menú sándwich en mobile | Componente de header con botón hamburguesa visible por debajo de 768 px (panel lateral accesible: `aria-expanded`, foco atrapado, cierre con ESC); desde 768 px pasa a navegación horizontal. Ver UX-UI §4.5. |
| 4 | Screaming Architecture | Las carpetas nombran el dominio, no el framework: backend `identidad/`, `categorias/`, `catalogo/`, `aportes/`, `roadmap/`; frontend `features/identidad`, `catalogo`, `aportes`, `validacion`, `roadmap`. Ver TRD §3.2. |
| 5 | Apariencia y experiencia inspiradas en Google/Material | UX-UI con valores concretos: azul primario `#1a73e8`, texto `#202124`/`#5f6368`, Roboto, radios 8/12/18 px, sombras `rgba(60,64,67,…)`, iconos Material Symbols, contraste AA verificado. Ver UX-UI §2. |

## 8. Vacíos de la SPEC de clase y decisiones tomadas

> La SPEC de clase fue escrita a propósito incompleta. Esta tabla es la prueba de que
> los huecos los **resolví yo**, no que los esquivé.

| # | Vacío detectado en la SPEC | Opciones consideradas | Decisión | Dónde se desarrolla |
|---|----------------------------|-----------------------|----------|---------------------|
| 1 | ¿Quién valida los cursos aportados? | Auto-moderación · validación por docente · puntuación comunitaria · validadores designados | **Validadores designados** (rol `validador`): revisión manual con checklist de 4 verificaciones (enlace activo, curso realmente gratuito, datos coinciden con el curso, categoría correcta). Sin auto-publicación ni votación: la calidad del catálogo es la propuesta de valor. | PRD BR-001, BR-007, BR-008 · RF-020, RF-021 |
| 2 | ¿Hay roles? | Sin roles · usuario + admin · usuario + validador | **Dos roles:** `usuario` y `validador`. No hay admin con interfaz propia: el alcance se mantiene acotado. | PRD BR-007 · RF-008 |
| 3 | ¿Cómo alguien llega a ser validador? | Auto-solicitud · UI de administración · script/seed | **Script de línea de comandos** y seed inicial por variable de entorno; no hay UI de gestión de roles (fuera de alcance). | PRD RF-008 · TRD §4 · Plan M1 |
| 4 | ¿Qué es exactamente "incluir en mi catálogo"? | Copiar el curso al usuario · referenciarlo con estado | **Referencia** al curso publicado mediante tabla intermedia con `progreso` y `orden`. "Mi catálogo" y "mi roadmap" son lo mismo. Un curso no se duplica ni se copia. | PRD BR-005, BR-006 · RF-023 a RF-027 · BackendSchema §4 |
| 5 | ¿La búsqueda es por texto, filtro o ambos? | Solo filtro · solo texto · ambos | **Ambos, combinables:** texto (título, tema, docentes; sin distinguir mayúsculas ni tildes) + categoría (P0); filtros por atributos del curso (P1). Todo se refleja en la URL. | PRD RF-010, RF-013 |
| 6 | ¿Cómo se evitan duplicados? | Sin control · por usuario · global por URL | **Global por URL normalizada** (minúsculas en el host, sin fragmento, sin parámetros `utm_*`, sin barra final) entre cursos activos (`en_revision`/`publicado`). | PRD BR-004 · RF-016 |
| 7 | ¿Qué significa "curso gratuito"? | Sin crear cuenta · cuenta gratuita permitida · incluir certificado gratis | **Acceso al contenido sin pago** (puede pedir una cuenta gratuita). No se modela el costo del certificado: "extiende certificado" es solo sí/no. El aportante lo confirma y el validador lo verifica. | PRD BR-003 · RF-015 |
| 8 | La SPEC dice "y demás datos necesarios": ¿cuáles? | Solo los mínimos · agregar extras | **Obligatorios extra:** plataforma/proveedor e idioma (es/en/pt/otro). **Opcionales:** duración estimada en horas y descripción breve (≤ 500 caracteres). | PRD BR-011 · RF-014 |
| 9 | ¿Qué implica la "declaración de toma"? | Privada · pública · con reseña obligatoria | **Pública**, booleana, obligatoria. Funciona como señal de confianza. Declarar "no lo tomé" es perfectamente válido. No hay reseña. | PRD BR-002 |
| 10 | ¿Qué pasa con un aporte rechazado? | Estado final · se puede corregir y reenviar | **Se puede corregir y reenviar:** `rechazado → en_revision`. El rechazo exige un motivo visible para el autor, y toda decisión queda auditada. | PRD BR-008, BR-009, BR-010, BR-014 · RF-019, RF-022 |
| 11 | ¿Existen borradores? | Sin borrador · borrador completo · borrador parcial | **Borrador parcial** (solo el título es obligatorio); la validación completa se aplica al enviar. Es P1. | PRD BR-009 · RF-019 · US-012 |
| 12 | ¿Quién ve cursos no publicados? | Todos · solo el autor · autor + validadores | **Autor y validadores** (el `borrador`, solo su autor). Para el resto (incluidos visitantes) un curso no publicado "no existe" (404). | PRD BR-016 |
| 13 | Recuperación de contraseña: canal y seguridad | Email con token · preguntas secretas · código SMS | **Email con enlace y token aleatorio de un solo uso, vigencia 30 min, guardado hasheado;** respuesta idéntica exista o no la cuenta; al restablecer se invalidan las sesiones. En dev el correo llega a Mailpit. | PRD BR-012 · RF-005, RF-006 · TRD §2, §4 |
| 14 | ¿Qué alcance tiene el rate limiting? | Solo login · login + recuperación + registro | **Login:** 5 intentos fallidos por email+IP y 20 por IP, ambos en ventana de 15 min → 429 con `Retry-After`. **Recuperación:** 3/hora por email y 10/hora por IP. **Registro:** 10/hora por IP. | PRD BR-012 · RF-003 |
| 15 | Algoritmo de hash de contraseñas | bcrypt (mínimo SPEC) · argon2id | **argon2id** (más fuerte que bcrypt, recomendado por OWASP). La SPEC permite superar a bcrypt si se justifica en el TRD, donde queda la justificación y los parámetros. | PRD RF-007 · TRD §2 |
| 16 | Estrategia de sesión | JWT stateless · sesión server-side con cookie | **Sesión server-side** con identificador opaco en cookie `HttpOnly`, `SameSite=Lax`, vencimiento por inactividad. Permite logout e invalidación real. | PRD RF-004 · TRD §2 |
| 17 | Estrategia de paginación | Offset + total · cursor | **Offset + total**, `page_size` 12 por defecto y 50 máximo: la UI necesita paginador numerado y el volumen (miles de filas) lo permite. | PRD RNF-001, BR-015 · TRD §2 |
| 18 | ¿Se pueden editar o despublicar cursos publicados? | Sí (validador/autor) · no | **No en esta versión.** Un publicado es inmutable; queda como pregunta abierta. | PRD §8, §10 |
| 19 | ¿Se verifica el email al registrarse? | Sí · no | **No en esta versión.** Se asume el riesgo; el rate limiting de registro lo mitiga parcialmente. | PRD §8, §10 |
| 20 | Idioma de la interfaz | Multi-idioma · solo español | **Solo español (es-AR).** Los cursos sí pueden estar en es/en/pt/otro. | PRD RNF-010 |
| 21 | Versión de FastAPI: el borrador de clase dice `0.143.3` y la SPEC oficial `0.158.2` | Respetar el borrador · la SPEC oficial | **0.158.2** (la SPEC oficial prevalece sobre el borrador del aula). | §6 · TRD §1 |
| 22 | ¿Desde qué ancho deja de verse el menú sándwich? | < 768 px · < 1024 px | **< 768 px** (mobile). Desde 768 px la navegación es horizontal. | UX-UI §3, §4.5 |

## 9. Historia de la SPEC (autoregistro de cambios)

| Fecha | Cambio | Por qué |
|-------|--------|---------|
| 20/10/2026 | SPEC de clase recibida en el aula (borrador con errores de tipeo, preservado en `SPEC-borrador-clase-2026-10-20.md`) | — |
| 21/10/2026 | Primer commit: SPEC de clase tal cual; se recibe la SPEC oficial limpia (FastAPI ref. `0.158.2`) | regla de la consigna |
| 23/10/2026 | Se crea `docs/SPEC.md` con identidad, problema, visión, alcance y glosario (§1–§4) | la SPEC de clase no definía producto ni límites |
| 23/10/2026 | Se agrega §8 con 22 vacíos resueltos (validación, roles, roadmap, búsqueda, duplicados, seguridad de cuenta, paginación y otros) | la SPEC los dejaba abiertos a propósito |
| 23/10/2026 | Se adopta FastAPI `0.158.2` (no `0.143.3`) y Node 24 LTS; se incorpora Mailpit como herramienta de dev | la SPEC oficial prevalece; Node 20 está fuera de soporte; el flujo de recuperación necesita un buzón local |
| 23/10/2026 | Se fija argon2id en lugar de bcrypt como algoritmo de hash | supera el mínimo exigido; justificación en TRD §2 |
