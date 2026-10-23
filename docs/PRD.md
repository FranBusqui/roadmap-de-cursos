# PRD — Product Requirements Document — Roadmap de Cursos

> **Qué es:** el QUÉ y el POR QUÉ. Para quién construimos, qué problema resuelve, qué hace
> y — con el mismo peso — qué **no** hace. No habla de tecnología ni de carpetas (eso es el [TRD](TRD.md)).
> **Cuándo está bien:** alguien del equipo puede construir la feature correcta sin preguntarme
> nada de producto; el "no" (out of scope) está tan claro como el "sí"; cada historia tiene
> criterios de aceptación verificables.
> **Contexto y decisiones de origen:** [SPEC.md](SPEC.md) (§8 lista los vacíos resueltos).

## 1. Resumen ejecutivo

Roadmap de Cursos es una webapp donde una comunidad de estudiantes construye en conjunto un
catálogo de cursos **gratuitos** de cualquier plataforma y gestiona su aprendizaje con **roadmaps
personales**. Cualquier usuario registrado aporta un curso con sus metadatos (categoría, versión,
año, docentes, cuestionarios, examen, certificado, aval) y declara si lo tomó; un validador lo
revisa y, si lo aprueba, pasa al catálogo público. Desde el catálogo cada persona arma su roadmap
privado, lo ordena y marca su progreso. El producto resuelve la dispersión y la falta de criterio
común de la oferta gratuita: un solo lugar, con datos comparables y revisados por humanos.

## 2. Objetivos y métricas de éxito

> Las metas se miden sobre un piloto de las primeras **4 semanas** con una comunidad de referencia
> de ~100 estudiantes y un mínimo de 2 validadores.

| Objetivo | Cómo sabemos que lo logramos |
|----------|------------------------------|
| **O1.** Que el catálogo comunitario tenga cursos validados de múltiples plataformas y categorías | ≥ 60 cursos publicados · ≥ 5 plataformas distintas · ≥ 6 de las 10 categorías con ≥ 5 cursos |
| **O2.** Que la validación mantenga la calidad sin volverse un cuello de botella | ≥ 70 % de los aportes terminan publicados · mediana de tiempo en `en_revision` ≤ 48 h · 100 % de los rechazos con motivo |
| **O3.** Que el roadmap sea usado para planificar | ≥ 60 % de los usuarios registrados agregan ≥ 1 curso a su roadmap en sus primeros 7 días · ≥ 30 % marcan ≥ 1 curso como `completado` dentro de los 30 días |
| **O4.** Que la comunidad contribuya, no solo consuma | ≥ 20 % de los usuarios registrados envían ≥ 1 aporte en el primer mes |
| **O5.** Que la cuenta sea segura y recuperable sin soporte humano | 0 contraseñas en claro en BD o logs · el ciclo de recuperación se completa en ≤ 3 pasos · los intentos de fuerza bruta sobre login reciben 429 |
| **O6.** Que la experiencia sea usable desde el celular y accesible | Lighthouse móvil en catálogo: Accesibilidad ≥ 95 y Performance ≥ 85 · sin scroll horizontal a 360 px · contraste AA en todo el texto |
| **O7 (MVP técnico).** Que el MVP sea verificable | En una máquina limpia, `docker compose up` y las 12 historias P0 recorren end-to-end sin errores en consola |

## 3. Personas

### Persona 1 — Lucía, estudiante autodidacta (23 años, Ingeniería en Sistemas)

- **Contexto:** estudia en la universidad y complementa con cursos gratuitos de programación e inglés.
  Entra desde el celular, en los viajes y en ratos libres.
- **Motivaciones:** armar un camino ordenado (por ejemplo "Python → datos → IA"), conseguir certificados
  que sumen a su CV y no perder tiempo en cursos desactualizados.
- **Frustraciones hoy:** guarda enlaces en notas y marcadores que no recuerda; no sabe si un curso da
  certificado o tiene examen hasta que ya empezó; encuentra cursos de 2019 con contenido vencido.
- **Historias tipo:**
  - "Quiero ver todos los cursos de datos que dan certificado, sin tener que abrir diez sitios."
  - "Quiero ordenar los cursos que voy a hacer y marcar cuáles ya terminé."
  - "Cuando encuentro un buen curso, quiero compartirlo con la comunidad."

### Persona 2 — Martín, profesional en reconversión (34 años, administrativo → analista de datos)

- **Contexto:** trabaja a tiempo completo y estudia de noche. Tiene poco tiempo y no puede darse el
  lujo de equivocarse de curso. Usa la notebook y el celular.
- **Motivaciones:** curso con aval de una organización conocida y con examen final, para poder
  demostrar lo aprendido; saber si alguien ya lo hizo y lo recomienda.
- **Frustraciones hoy:** no confía en los rankings de las plataformas; no distingue cursos
  realmente gratuitos de pruebas gratis que terminan en un cobro; no tiene un plan de estudio visible.
- **Historias tipo:**
  - "Quiero filtrar por 'con aval' y 'con examen' y ver si quien lo aportó lo cursó."
  - "Quiero un plan con orden y progreso para no abandonar a mitad de camino."
  - "Quiero entrar sin registrarme primero para ver si esto me sirve."

### Persona 3 — Carolina, validadora voluntaria (29 años, ayudante de cátedra)

- **Contexto:** conoce bien varias áreas y le interesa que la comunidad tenga material confiable.
  Revisa aportes en bloques cortos, desde la notebook.
- **Motivaciones:** mantener la calidad del catálogo con un proceso claro y rápido; dar
  devoluciones útiles a quien aporta cuando rechaza algo.
- **Frustraciones hoy:** las listas de recursos compartidas están llenas de enlaces rotos, cursos pagos
  y duplicados, y nadie las cura.
- **Historias tipo:**
  - "Quiero ver los aportes pendientes, del más antiguo al más nuevo, y resolverlos rápido."
  - "Quiero un checklist para no olvidarme de verificar algo."
  - "Si rechazo un aporte, quiero explicar por qué para que el autor pueda corregirlo."

## 4. User stories

> 15 historias: **12 P0** (el producto no funciona sin ellas el día del MVP) y 3 P1.
> Los criterios de aceptación son verificables en la UI o contra la API.
> Los listados usan `page_size` = 12 por defecto (BR-015).

| ID | Prioridad | Historia | Criterios de aceptación |
|----|-----------|----------|-------------------------|
| US-001 | P0 | Como visitante, quiero ver el catálogo comunitario paginado, para descubrir cursos gratuitos sin registrarme | - [ ] Dado que visito `/catalogo`, veo la primera página con hasta 12 cursos publicados, los más recientes primero<br>- [ ] Dado que hay más de 12 cursos, aparece el paginador con el total de resultados y cambio de página sin recargar<br>- [ ] Dado que no hay cursos publicados, veo un empty state con CTA "Aportá el primero"<br>- [ ] Dado que la lista está cargando veo un skeleton; si falla la red, veo un mensaje de error con botón "Reintentar"<br>- [ ] Dado un curso en `borrador`, `en_revision` o `rechazado`, nunca aparece en el listado |
| US-002 | P0 | Como visitante o usuario, quiero buscar por texto y filtrar por categoría, para encontrar rápido lo que me interesa | - [ ] Dado que escribo en el buscador, la lista se filtra por coincidencia parcial en título, tema o docentes, sin distinguir mayúsculas ni tildes<br>- [ ] Dado que elijo una categoría, solo veo cursos de esa categoría, y la búsqueda de texto y la categoría se combinan<br>- [ ] Dado que cambio un filtro, vuelvo a la página 1 y el estado de búsqueda queda reflejado en la URL (se puede compartir el enlace)<br>- [ ] Dado que no hay coincidencias, veo "Sin resultados" con la acción "Limpiar filtros" |
| US-003 | P0 | Como visitante o usuario, quiero ver el detalle de un curso, para decidir si me conviene antes de ir al sitio externo | - [ ] Dado `/catalogo/:id` de un curso publicado, veo título, categoría, tema, plataforma, versión, año, docentes, idioma, cuestionarios, examen, certificado, aval (con organización), nombre del aportante y si lo tomó o no<br>- [ ] Dado el botón "Ir al curso", se abre el enlace externo en una pestaña nueva con `rel="noopener noreferrer"`<br>- [ ] Dado un ID inexistente o de un curso no publicado, veo la página 404 (no se revela que existe)<br>- [ ] Dado que estoy logueado, veo "Agregar a mi roadmap" o, si ya lo tengo, "En tu roadmap ✓" |
| US-004 | P0 | Como persona nueva, quiero registrarme con email y contraseña, para aportar cursos y armar mi roadmap | - [ ] Dado `/registro`, completo nombre (2–60), email y contraseña (10–128); con datos válidos se crea mi cuenta con rol `usuario` y quedo con la sesión iniciada<br>- [ ] Dado un email ya registrado (sin distinguir mayúsculas), veo el error "Ese email ya está registrado" junto al campo<br>- [ ] Dado una contraseña de menos de 10 caracteres, veo el error junto al campo y no se envía<br>- [ ] Dado el alta exitosa, la contraseña no aparece en ninguna respuesta ni log y se guarda solo su hash<br>- [ ] Dado más de 10 registros por hora desde una misma IP, recibo 429 |
| US-005 | P0 | Como usuario, quiero iniciar y cerrar sesión de forma segura, para acceder a mis datos y proteger mi cuenta | - [ ] Dado credenciales válidas, inicio sesión y vuelvo a la ruta que quería visitar (o a `/catalogo`)<br>- [ ] Dado credenciales inválidas, veo "Email o contraseña incorrectos" sin revelar cuál falló<br>- [ ] Dado 5 intentos fallidos en 15 min con el mismo email e IP (o 20 desde la misma IP), recibo 429 con `Retry-After` y la UI muestra "Demasiados intentos. Probá de nuevo en N minutos"<br>- [ ] Dado que cierro sesión, la sesión queda invalidada en el servidor y las rutas protegidas me redirigen a `/login`<br>- [ ] Dado que entro a una ruta protegida sin sesión, voy a `/login` y vuelvo a ella tras autenticarme |
| US-006 | P0 | Como usuario que olvidó su contraseña, quiero recuperarla por email, para volver a entrar sin ayuda | - [ ] Dado `/recuperar`, ingreso mi email y veo el mismo mensaje exista o no la cuenta<br>- [ ] Dado que la cuenta existe, recibo un email (en desarrollo, visible en Mailpit) con un enlace con token válido 30 min y de un solo uso<br>- [ ] Dado el enlace válido, ingreso una nueva contraseña (≥ 10 caracteres) y puedo iniciar sesión con ella; la anterior deja de funcionar<br>- [ ] Dado un token inválido, vencido o ya usado, veo un mensaje claro y la opción de pedir uno nuevo<br>- [ ] Dado que restablezco la contraseña, todas mis sesiones previas quedan invalidadas<br>- [ ] Dado más de 3 solicitudes por hora para el mismo email, recibo 429 |
| US-007 | P0 | Como usuario, quiero aportar un curso gratuito con sus metadatos, para enriquecer el catálogo de la comunidad | - [ ] Dado `/aportar` con sesión, el formulario pide todos los campos obligatorios de RF-014, incluida la categoría (lista cerrada), la declaración "lo tomé / no lo tomé" y la confirmación de que el curso es gratuito<br>- [ ] Dado datos inválidos (campo vacío, URL que no es http/https, año fuera de rango, aval sin organización), veo errores inline y no pierdo lo ya escrito<br>- [ ] Dado una URL ya presente en un curso activo, veo el error de duplicado con un enlace al curso existente (si está publicado) o el aviso "ya está en revisión"<br>- [ ] Dado un envío válido, el curso queda en estado `en_revision`, veo un toast de confirmación y paso a "Mis aportes"<br>- [ ] Dado el aporte recién enviado, no aparece en el catálogo público hasta que sea validado (BR-001) |
| US-008 | P0 | Como aportante, quiero ver el estado de mis aportes, para saber si fueron publicados o rechazados y por qué | - [ ] Dado "Mis aportes", veo una lista paginada con título, fecha y estado (`borrador`, `en_revision`, `publicado`, `rechazado`) de mis aportes<br>- [ ] Dado un aporte `rechazado`, veo el motivo indicado por el validador<br>- [ ] Dado un aporte `publicado`, puedo ir a su detalle público<br>- [ ] Dado que intento ver el aporte de otro usuario, no obtengo sus datos (403/404)<br>- [ ] Dado que no aporté nada, veo un empty state con CTA "Aportar mi primer curso" |
| US-009 | P0 | Como validador, quiero revisar la cola de aportes y aprobarlos o rechazarlos, para que el catálogo sea confiable | - [ ] Dado que soy validador, accedo a `/validar` y veo los aportes `en_revision` paginados, del más antiguo al más nuevo; un usuario sin rol no puede acceder (403 / redirección)<br>- [ ] Dado un aporte abierto, veo todos sus datos y el enlace externo, más un checklist de 4 verificaciones (enlace activo, curso realmente gratuito, datos coinciden, categoría correcta)<br>- [ ] Dado el checklist completo, "Aprobar" cambia el estado a `publicado` y el curso aparece en el catálogo<br>- [ ] Dado "Rechazar", se exige un motivo de al menos 10 caracteres y el estado pasa a `rechazado`<br>- [ ] Dado un aporte propio, no puedo aprobarlo ni rechazarlo (acciones deshabilitadas y 403 en la API)<br>- [ ] Dado que otro validador ya resolvió ese aporte, recibo un aviso de conflicto (409) y la cola se refresca<br>- [ ] Dada cada decisión, queda registrada con validador, fecha, resultado y motivo |
| US-010 | P0 | Como usuario, quiero agregar un curso del catálogo a mi roadmap, para planificar mi aprendizaje | - [ ] Dado un curso publicado (en la card o en el detalle), "Agregar a mi roadmap" lo suma al final con progreso `pendiente` y muestra un toast<br>- [ ] Dado un curso que ya tengo, el botón se muestra como "En tu roadmap ✓" y no se puede duplicar (409 en la API)<br>- [ ] Dado un curso no publicado, la API rechaza la acción (404)<br>- [ ] Dado que soy visitante, el botón me lleva a `/login` y vuelvo al curso al autenticarme |
| US-011 | P0 | Como usuario, quiero ver y gestionar mi roadmap, para seguir mi progreso | - [ ] Dado `/roadmap` con sesión, veo mis cursos paginados con los datos del curso y su progreso<br>- [ ] Dado un curso de mi roadmap, puedo cambiar su progreso entre `pendiente`, `en_curso` y `completado`, y el cambio persiste al recargar<br>- [ ] Dado "Quitar", tras confirmar, el curso sale de mi roadmap pero sigue en el catálogo<br>- [ ] Dado el roadmap de otra persona, no puedo verlo ni modificarlo<br>- [ ] Dado un roadmap vacío, veo un empty state con CTA "Explorar el catálogo" |
| US-012 | P1 | Como aportante, quiero guardar borradores y corregir aportes rechazados, para no perder trabajo y volver a enviarlos | - [ ] Dado el formulario, puedo "Guardar borrador" con solo el título completo; el aporte queda en `borrador` y solo lo veo yo<br>- [ ] Dado un `borrador` o un `rechazado`, puedo editarlo y "Enviar a revisión": se aplica la validación completa y pasa a `en_revision`<br>- [ ] Dado un aporte `en_revision` o `publicado`, no puedo editarlo<br>- [ ] Dado un reenvío, el historial conserva los motivos de rechazos anteriores |
| US-013 | P1 | Como usuario, quiero reordenar los cursos de mi roadmap, para reflejar en qué orden voy a estudiarlos | - [ ] Dado un curso de mi roadmap, los botones "Subir" y "Bajar" cambian su posición, y son operables con teclado<br>- [ ] Dado el cambio, el orden persiste y es global (no solo dentro de la página visible)<br>- [ ] Dado el primer o último curso, el botón correspondiente aparece deshabilitado |
| US-014 | P1 | Como visitante o usuario, quiero filtrar por atributos del curso, para encontrar cursos con certificado, sin examen o con aval | - [ ] Dado los filtros "Da certificado", "Con cuestionarios", "Requiere examen" (sí / no), "Con aval" e idioma, puedo combinarlos entre sí y con la búsqueda y la categoría<br>- [ ] Dado que activo un filtro, el paginador y el total se actualizan, y el estado queda en la URL<br>- [ ] Dado que no hay resultados, veo el empty state con "Limpiar filtros" |
| US-015 | P0 | Como persona que usa el celular, quiero un menú sándwich, para navegar con una mano sin perder espacio de pantalla | - [ ] Dado un viewport menor a 768 px, el header muestra logo y botón hamburguesa; al tocarlo se abre un panel con la navegación<br>- [ ] Dado el panel abierto, se cierra con un toque en un enlace, el botón X, la tecla `ESC` o un clic fuera; el foco vuelve al botón<br>- [ ] Dado un viewport de 768 px o más, se ve la navegación horizontal y no el botón hamburguesa<br>- [ ] Dado el botón, expone `aria-expanded` y `aria-controls` y su área táctil es de al menos 44 px |

## 5. Requisitos funcionales

| ID | Requisito | Historia relacionada |
|----|-----------|----------------------|
| RF-001 | El sistema permite registrar usuarios con nombre, email (único, sin distinguir mayúsculas) y contraseña; el nuevo usuario tiene rol `usuario` y queda con sesión iniciada | US-004 |
| RF-002 | El sistema autentica con email y contraseña y responde con un mensaje genérico ante credenciales inválidas | US-005 |
| RF-003 | El sistema aplica rate limiting: login (5 fallidos por email+IP y 20 por IP en 15 min), recuperación (3/h por email y 10/h por IP) y registro (10/h por IP); al excederlo responde 429 con `Retry-After` | US-004, US-005, US-006 |
| RF-004 | El sistema permite cerrar sesión (invalidación en el servidor) y vence las sesiones por inactividad | US-005 |
| RF-005 | El sistema recibe una solicitud de recuperación y responde de forma idéntica exista o no la cuenta; si existe, envía por email un enlace con token aleatorio de un solo uso y 30 min de vigencia | US-006 |
| RF-006 | El sistema restablece la contraseña con un token válido, lo invalida y cierra todas las sesiones previas del usuario | US-006 |
| RF-007 | Las contraseñas se almacenan solo como hash con un algoritmo robusto (argon2id, ver TRD); nunca se guardan, devuelven ni loguean en claro | US-004, US-006 |
| RF-008 | El sistema maneja los roles `usuario` y `validador`; protege rutas y endpoints según sesión y rol; el rol `validador` se asigna con un script de línea de comandos y un seed inicial, no desde la interfaz | US-005, US-009 |
| RF-009 | El sistema expone un listado público, paginado y ordenado del más reciente al más antiguo de los cursos `publicado` | US-001 |
| RF-010 | El sistema permite buscar por texto (título, tema, docentes; sin distinguir mayúsculas ni tildes) y filtrar por categoría, de forma combinable | US-002 |
| RF-011 | El sistema expone el detalle público de un curso publicado con todos sus metadatos, el aportante y su declaración de toma; los no publicados responden 404 | US-003 |
| RF-012 | El sistema ofrece una lista cerrada de 10 categorías (ver Anexo A), cargada por seed y consultable | US-002, US-007 |
| RF-013 | El sistema permite filtrar el catálogo por atributos: certificado, cuestionarios, examen (sí/no), aval e idioma | US-014 |
| RF-014 | El formulario de aporte exige: URL activa, categoría, tema, título, versión, año de edición, docentes (1 a 10), plataforma, idioma, ¿cuestionarios?, ¿examen?, ¿certificado?, ¿aval? (con organización si es sí), declaración de toma y confirmación de gratuidad; admite además duración en horas y descripción breve (opcionales) | US-007 |
| RF-015 | El sistema valida el aporte en cliente y servidor según los límites de BR-011 y exige la confirmación de gratuidad (BR-003) | US-007 |
| RF-016 | El sistema normaliza la URL y rechaza el envío si ya existe un curso activo con la misma URL normalizada (BR-004) | US-007 |
| RF-017 | Al enviarse, el aporte queda en estado `en_revision` y fuera del catálogo público | US-007 |
| RF-018 | El sistema muestra al autor una lista paginada de sus aportes con estado y motivo de rechazo | US-008 |
| RF-019 | El sistema permite guardar borradores parciales, editar `borrador`/`rechazado` y reenviarlos a revisión (con validación completa) | US-012 |
| RF-020 | El sistema muestra a los validadores una cola paginada de aportes `en_revision`, del más antiguo al más nuevo | US-009 |
| RF-021 | El validador aprueba (con el checklist de 4 verificaciones completo) o rechaza (con motivo ≥ 10 caracteres); nunca sobre un aporte propio; ante resolución concurrente responde 409 | US-009 |
| RF-022 | El sistema registra cada decisión de validación: aporte, validador, resultado, motivo y fecha | US-009, US-012 |
| RF-023 | El usuario agrega un curso publicado a su roadmap; el sistema impide duplicados y cursos no publicados | US-010 |
| RF-024 | El usuario ve su roadmap paginado, ordenado por posición, con datos del curso y progreso | US-011 |
| RF-025 | El usuario cambia el progreso de un curso de su roadmap: `pendiente`, `en_curso`, `completado` | US-011 |
| RF-026 | El usuario quita un curso de su roadmap sin afectar el catálogo | US-011 |
| RF-027 | El usuario reordena los cursos de su roadmap (subir/bajar) y el orden persiste | US-013 |
| RF-028 | La interfaz ofrece menú sándwich accesible por debajo de 768 px y navegación horizontal desde 768 px | US-015 |

## 6. Requisitos no funcionales

| ID | Requisito | Notas |
|----|-----------|-------|
| RNF-001 | Todos los listados y sus tablas están paginados (catálogo, roadmap, mis aportes, cola de validación); `page_size` 12 por defecto, máximo 50 | heredado de SPEC clase |
| RNF-002 | Mobile-first con mejora progresiva: base sin media queries; `@media (min-width: …)` solo para agregar | heredado de SPEC clase |
| RNF-003 | El listado del catálogo responde en < 500 ms (p95) con 1.000 cursos publicados, y la pantalla alcanza LCP < 2,5 s en conexión 4G simulada | decisión propia |
| RNF-004 | Menú sándwich en mobile, accesible por teclado y lector de pantalla | heredado de SPEC clase |
| RNF-005 | Accesibilidad WCAG 2.2 nivel AA: contraste ≥ 4.5:1 en texto, foco visible, navegación completa por teclado, `prefers-reduced-motion` respetado | decisión propia |
| RNF-006 | Seguridad: hash robusto de contraseñas, rate limiting, tokens de recuperación almacenados hasheados, sin enumeración de cuentas en login ni recuperación, validación de entrada en servidor, CORS restringido, cookies `HttpOnly` | decisión propia |
| RNF-007 | Screaming Architecture: la estructura de carpetas expresa el dominio (identidad, categorías, catálogo, aportes, roadmap) | heredado de SPEC clase |
| RNF-008 | Entorno reproducible: `docker compose up` levanta base de datos, backend, frontend y bandeja de correo en una máquina limpia | heredado de SPEC clase (infra) |
| RNF-009 | Todo listado y detalle define sus cuatro estados de UI: `loading`, `ok`, `empty`, `error` (con reintento) | decisión propia |
| RNF-010 | Interfaz solo en español (es-AR); fechas y horas se guardan en UTC y se muestran en hora local del navegador | decisión propia |
| RNF-011 | Cobertura de tests ≥ 85 % en la capa de servicios (reglas de negocio); se implementa en la clase del 27/10 | decisión propia (ver Plan §5) |
| RNF-012 | Logging estructurado sin datos personales sensibles ni secretos (contraseñas, tokens, cookies) | decisión propia |
| RNF-013 | Apariencia y experiencia inspiradas en Google/Material, con tokens concretos documentados en UX-UI | heredado de SPEC clase |

## 7. Reglas de negocio

| ID | Regla | Fuente |
|----|-------|--------|
| BR-001 | Un curso aportado no aparece en el catálogo comunitario hasta ser validado (`publicado`). | SPEC clase |
| BR-002 | Quien aporta un curso declara obligatoriamente si lo tomó o no. La declaración es pública en el detalle y no puede dejarse sin responder. | SPEC clase |
| BR-003 | Solo se aportan cursos **gratuitos**: el contenido es accesible sin pago (puede exigir una cuenta gratuita). El aportante lo confirma al enviar y el validador lo verifica. No se modela el costo del certificado. | SPEC clase + decisión propia |
| BR-004 | No puede haber dos cursos activos (`en_revision` o `publicado`) con la misma URL normalizada (host en minúsculas, sin fragmento, sin parámetros `utm_*`, sin barra final), sin importar quién los aporte. Un `rechazado` o un `borrador` no bloquean la URL. | decisión propia |
| BR-005 | El roadmap es **personal, privado y único** por usuario (equivale a "mi catálogo" de la SPEC de clase) y solo puede incluir cursos publicados. Ningún otro usuario, ni siquiera un validador, ve el roadmap ajeno. | SPEC clase + decisión propia |
| BR-006 | Un curso no puede aparecer dos veces en el mismo roadmap. Cada ítem tiene un progreso (`pendiente`, `en_curso`, `completado`; inicial `pendiente`) y una posición. | decisión propia |
| BR-007 | Roles: `usuario` y `validador`. El rol `validador` se asigna fuera de la UI. Un validador **no puede aprobar ni rechazar sus propios aportes** (separación de funciones). | decisión propia |
| BR-008 | Rechazar un aporte exige un motivo de al menos 10 caracteres, visible para el autor. Aprobar exige completar el checklist de 4 verificaciones. | decisión propia |
| BR-009 | Ciclo de vida del curso: `borrador → en_revision` (el autor envía) · `en_revision → publicado` (aprobación) · `en_revision → rechazado` (rechazo con motivo) · `rechazado → en_revision` (el autor corrige y reenvía). `publicado` es un estado final e inmutable en esta versión. Un aporte creado con "Enviar" nace directamente en `en_revision`. | decisión propia |
| BR-010 | Solo el autor puede editar un aporte, y solo mientras esté en `borrador` o `rechazado`. | decisión propia |
| BR-011 | Límites del aporte: URL http/https ≤ 2048 · título 5–200 · tema 3–120 · versión 1–50 (texto libre, ej. "2025", "v3") · año de edición entre 2000 y el año en curso · docentes 1 a 10, cada uno de 2 a 120 caracteres · plataforma 2–80 · idioma `es`/`en`/`pt`/`otro` · cuestionarios, examen y certificado: sí/no explícito (sin valor por defecto) · aval: sí/no, con organización de 2–120 caracteres si es sí · duración opcional 1–2000 h · descripción opcional ≤ 500. | decisión propia |
| BR-012 | Seguridad de cuenta: contraseña de 10 a 128 caracteres; login con rate limiting (5 fallidos por email+IP y 20 por IP cada 15 min); recuperación limitada a 3/h por email y 10/h por IP; registro limitado a 10/h por IP; token de recuperación de un solo uso con 30 min de vigencia; restablecer la contraseña cierra todas las sesiones. | SPEC clase (rate limit, bcrypt como mínimo, recuperación) + decisión propia |
| BR-013 | En el catálogo se muestra públicamente el nombre del aportante (el nombre de pantalla, nunca su email). | decisión propia |
| BR-014 | Toda decisión de validación queda registrada (quién, cuándo, resultado, motivo) y no se borra. | decisión propia |
| BR-015 | Paginación: `page` desde 1, `page_size` 12 por defecto y 50 como máximo; toda respuesta de listado incluye el total. | SPEC clase + decisión propia |
| BR-016 | Visibilidad: `en_revision` y `rechazado` solo los ven el autor y los validadores; `borrador` solo su autor; para cualquier otra persona, esos cursos no existen (404). | decisión propia |

## 8. Fuera de alcance (out of scope)

- **Dinero:** pagos, cursos de pago, suscripciones y cualquier monetización.
- **Contenido propio:** alojar videos o materiales de cursos; emitir certificados desde la plataforma (solo se enlaza a cursos externos).
- **Plataformas:** app móvil nativa, PWA/offline, modo oscuro, internacionalización (solo es-AR).
- **Cuenta:** inicio de sesión social (OAuth), autenticación de dos factores, verificación de email, edición de perfil y eliminación de cuenta.
- **Administración:** panel de administración, alta/baja de categorías o roles desde la interfaz, moderación de usuarios (bloqueos o suspensiones).
- **Curaduría posterior:** edición o despublicación de cursos ya publicados, reporte de enlaces rotos, verificación automática de enlaces (scraping o chequeos HTTP).
- **Social:** reseñas, puntajes, comentarios, foros, seguir a otros usuarios, roadmaps compartidos o públicos.
- **Roadmap avanzado:** más de un roadmap por usuario, fechas objetivo, recordatorios, estadísticas de estudio, arrastrar y soltar (se reordena con botones).
- **Notificaciones:** emails o push de aprobación/rechazo de aportes (el estado se consulta en "Mis aportes"; el único email del sistema es el de recuperación de contraseña).
- **Inteligencia:** recomendaciones automáticas, IA, importación masiva, analítica de producto.

## 9. Supuestos y decisiones sobre la SPEC de clase

**Decisiones:** los 22 vacíos de la SPEC de clase y su resolución están en [`docs/SPEC.md` §8](SPEC.md#8-vacíos-de-la-spec-de-clase-y-decisiones-tomadas). Las más determinantes para el producto: validación por **validadores designados** (BR-001, BR-007, BR-008), **dos roles** sin panel de administración (BR-007) y el **roadmap como referencia privada** a cursos publicados (BR-005, BR-006).

**Supuestos** (si alguno falla, hay que revisar el PRD):

1. La comunidad piloto es chica (≤ 500 usuarios, ≤ 5.000 cursos), por lo que offset + total es suficiente para paginar.
2. Existen al menos 2 validadores voluntarios desde el primer día (si no, un aporte propio de un validador no puede ser revisado por nadie más).
3. Los usuarios acceden mayormente desde el celular, de ahí el enfoque mobile-first.
4. Todos los usuarios tienen un email al que acceden, lo que permite la recuperación de contraseña sin verificación previa.
5. Las plataformas externas mantienen sus enlaces razonablemente estables; no se verifica su vigencia más allá de la revisión humana.
6. El idioma de trabajo de la comunidad es el español rioplatense.

## 10. Preguntas abiertas

| Pregunta | Impacto | Estado |
|----------|---------|--------|
| ¿Los aportes `en_revision` expiran si nadie los valida? | medio | decidida para el MVP: **no expiran**; se revisa si la mediana de tiempo en revisión supera 48 h (O2) |
| ¿Se pueden editar o despublicar cursos ya publicados (por ejemplo, un enlace que deja de funcionar)? | alto | abierta — fuera de alcance de esta versión (§8) |
| ¿Cómo se detectan y reportan enlaces rotos con el tiempo? | alto | abierta — sin verificación automática en esta versión |
| ¿Cómo crece el equipo de validadores (criterio de selección, relevo)? | medio | abierta — por ahora se asigna con script |
| ¿Hay que verificar el email al registrarse para frenar cuentas falsas? | medio | abierta — mitigado parcialmente por rate limiting de registro |
| ¿Se debe modelar si el certificado es gratuito o con costo? | bajo | abierta — hoy solo se registra "extiende certificado: sí/no" (BR-003) |
| ¿El roadmap podría compartirse con otras personas? | bajo | abierta — privado por decisión (BR-005) |
| ¿Se notifica por email la aprobación o el rechazo de un aporte? | medio | decidida para el MVP: **no**; se consulta en "Mis aportes" (§8) |

---

## Anexo A — Categorías (lista cerrada, cargada por seed)

1. Programación y desarrollo
2. Datos e inteligencia artificial
3. Ciberseguridad y redes
4. Diseño y creatividad
5. Negocios y emprendimiento
6. Idiomas
7. Matemática y ciencias
8. Salud y bienestar
9. Humanidades y sociedad
10. Otros

## Anexo B — Matriz de trazabilidad (historias → requisitos → reglas → módulo del plan)

> Los módulos son los que desarrolla el [Implementation Plan](IMPLEMENTATION_PLAN.md):
> **M0** Scaffold e infraestructura · **M1** Identidad y autenticación · **M2** Catálogo comunitario ·
> **M3** Aportes y validación · **M4** Roadmap personal · **M5** Cierre: accesibilidad, QA y docs.

| Historia | Prioridad | Requisitos funcionales | Reglas de negocio | Módulo |
|----------|-----------|------------------------|-------------------|--------|
| US-001 | P0 | RF-009 | BR-001, BR-015, BR-016 | M2 |
| US-002 | P0 | RF-010, RF-012 | BR-015 | M2 |
| US-003 | P0 | RF-011 | BR-002, BR-013, BR-016 | M2 |
| US-004 | P0 | RF-001, RF-003, RF-007 | BR-012 | M1 |
| US-005 | P0 | RF-002, RF-003, RF-004, RF-008 | BR-012 | M1 |
| US-006 | P0 | RF-003, RF-005, RF-006, RF-007 | BR-012 | M1 |
| US-007 | P0 | RF-012, RF-014, RF-015, RF-016, RF-017 | BR-001, BR-002, BR-003, BR-004, BR-011 | M3 |
| US-008 | P0 | RF-018 | BR-008, BR-016 | M3 |
| US-009 | P0 | RF-008, RF-020, RF-021, RF-022 | BR-007, BR-008, BR-009, BR-014 | M3 |
| US-010 | P0 | RF-023 | BR-005, BR-006 | M4 |
| US-011 | P0 | RF-024, RF-025, RF-026 | BR-005, BR-006 | M4 |
| US-012 | P1 | RF-019, RF-022 | BR-009, BR-010, BR-014 | M3 |
| US-013 | P1 | RF-027 | BR-006 | M4 |
| US-014 | P1 | RF-013 | BR-015 | M2 |
| US-015 | P0 | RF-028 | — | M0 |

> Los RNF son transversales: RNF-001, 002, 005, 009 y 013 se verifican en M5 y se respetan en cada módulo;
> RNF-008 se cumple en M0; RNF-011 se planifica en el Plan §5 y se implementa el 27/10.
