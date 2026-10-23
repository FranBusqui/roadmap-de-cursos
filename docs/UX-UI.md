# UX-UI — Guía visual de estilos — Roadmap de Cursos

> **Qué es:** la gramática visual de la interfaz: tokens, componentes, estados, accesibilidad.
> No es un prototipo navegable (eso lo cubre el [APPFlow](APPFlow.md)); es el conjunto de reglas con las que
> se construye cada pantalla **antes** de escribir CSS.
> **Inspiración fijada por la SPEC:** la apariencia y experiencia son similares a **Google**
> (estética Material: limpieza, espacio en blanco, azul primario, sombras sutiles, radios amplios).
> **Cuándo está bien:** dos personas que sigan esta guía construyen la misma pantalla y queda
> igual; todos los estados de cada componente (focus, error, empty, loading) están definidos
> de antemano; la estrategia mobile-first con mejora progresiva es explícita.
> **Sobre los contrastes:** los ratios de este documento se calcularon con la fórmula de luminancia
> relativa de WCAG 2.x y se redondearon a dos decimales; **antes de cerrar la Instancia B hay que
> reverificarlos** en https://webaim.org/resources/contrastchecker/.

## 1. Principios

1. **Limpieza sobre adorno.** Si un elemento no comunica información ni habilita una acción, sobra. Sin ilustraciones decorativas ni degradados.
2. **Mobile primero, de verdad.** El layout base se diseña para 360 px y se **mejora** hacia arriba; nunca se repara una pantalla grande para que entre en el celular.
3. **Una acción primaria por pantalla.** El azul relleno marca *lo principal que se puede hacer*; todo lo demás es secundario (contorno) o terciario (texto).
4. **Los estados son parte del diseño.** `loading`, `empty`, `error` y los estados de foco de cada componente se definen antes de construir, no después.
5. **Accesible por construcción.** Los pares de color ya están calculados, el foco es siempre visible y todo se puede operar con teclado y con el pulgar (targets ≥ 44 px).

## 2. Design tokens

### 2.1 Paleta de colores

| Token | Valor | Uso | Contraste (AA) |
|-------|-------|-----|----------------|
| `--color-primary` | `#1a73e8` | fondo de botones primarios, anillo de foco, bordes activos, iconos de acento | blanco sobre primary: **4.51:1** ✓ · anillo de foco sobre `#ffffff`: 4.51:1 ✓ (≥ 3:1). **Prohibido como color de texto sobre `--color-background`** (4.27:1 ✗) |
| `--color-primary-dark` | `#185abc` | hover/active del primario; texto de chips y badges sobre `--color-primary-container` | blanco sobre `#185abc`: **6.51:1** ✓ · sobre `#e8f0fe`: 5.68:1 ✓ |
| `--color-link` | `#185abc` | **texto** de enlaces y de botones secundarios/terciarios | sobre `#ffffff`: 6.51:1 ✓ · sobre `#f8f9fa`: 6.17:1 ✓ |
| `--color-primary-container` | `#e8f0fe` | chips seleccionados, ítem activo del menú, hover de botones secundarios | — (fondo; ver pares arriba) |
| `--color-on-primary` | `#ffffff` | texto e iconos sobre `--color-primary` | 4.51:1 ✓ (14 px/500; mantener sin reducir brillo ni opacidad) |
| `--color-surface` | `#ffffff` | cards, header, drawer, formularios | — |
| `--color-background` | `#f8f9fa` | fondo de página | — |
| `--color-text` | `#202124` | texto principal | sobre `#ffffff`: **16.10:1** ✓ · sobre `#f8f9fa`: 15.27:1 ✓ |
| `--color-text-muted` | `#5f6368` | metadatos, ayudas, placeholders | sobre `#ffffff`: **6.05:1** ✓ · sobre `#f8f9fa`: 5.74:1 ✓ · sobre `#f1f3f4`: 5.44:1 ✓ |
| `--color-border` | `#dadce0` | divisores, borde de cards (decorativo) | 1.37:1 — **solo decorativo**: nunca identifica un control |
| `--color-border-strong` | `#80868b` | borde de inputs, selects, checkboxes y radios | sobre `#ffffff`: **3.68:1** ✓ · sobre `#f8f9fa`: 3.50:1 ✓ (≥ 3:1, WCAG 1.4.11) |
| `--color-hover-grey` | `#f1f3f4` | hover de filas, fondo de skeleton, campos deshabilitados, badge neutro | — |
| `--color-success` | `#188038` | iconos de éxito | sobre `#ffffff`: 5.02:1 ✓ |
| `--color-success-text` | `#137333` | texto de badges de éxito (`publicado`, `completado`) | sobre `#e6f4ea`: 5.24:1 ✓ |
| `--color-success-container` | `#e6f4ea` | fondo de badges y alertas de éxito | — |
| `--color-warning` | `#f9ab00` | fondo de badge `en revisión` y alertas de aviso | texto `--color-on-warning` sobre `#f9ab00`: 8.32:1 ✓ |
| `--color-on-warning` | `#202124` | texto sobre `--color-warning` (**nunca texto blanco**: 1.93:1 ✗) | — |
| `--color-error` | `#d93025` | borde y fondo del botón peligroso; iconos de error | blanco sobre `#d93025`: 4.77:1 ✓ · sobre `#f8f9fa`: 4.53:1 ✓ |
| `--color-error-text` | `#c5221f` | texto de mensajes de error y de badge `rechazado` | sobre `#ffffff`: 5.80:1 ✓ · sobre `#fce8e6`: 4.92:1 ✓ |
| `--color-error-container` | `#fce8e6` | fondo de badge `rechazado` y alertas de error | — |
| `--color-snackbar` | `#323232` | fondo del toast | blanco sobre `#323232`: 12.82:1 ✓ |
| `--color-overlay` | `rgba(32, 33, 36, 0.6)` | fondo detrás del drawer y los modales | — |

> **Dos decisiones que se apartan del ejemplo de la plantilla, y por qué:**
> (1) `#1a73e8` apenas supera el AA sobre blanco (4.51:1) y *no* lo cumple sobre el gris de fondo (4.27:1),
> por eso el **texto** azul usa `--color-link` (`#185abc`) y el primario queda para rellenos y foco.
> (2) `#dadce0` (1.37:1) no alcanza los 3:1 que WCAG 1.4.11 pide para identificar un control, por eso los
> controles de formulario usan `--color-border-strong` (3.68:1) y `--color-border` queda para divisores decorativos.

### 2.2 Tipografía

| Token | Familia | Tamaño / line-height | Peso | Uso |
|-------|---------|----------------------|------|-----|
| `--font-family-base` | Roboto, `system-ui`, `-apple-system`, `"Segoe UI"`, sans-serif | — | — | toda la interfaz |
| `--text-xs` | | 12px / 16px | 500 | badges y chips |
| `--text-sm` | | 14px / 20px | 400 · 500 en botones y labels | metadatos, tabla, ayudas, botones |
| `--text-base` | | 16px / 24px | 400 | cuerpo, **texto dentro de inputs (mínimo 16 px: evita el zoom automático de iOS)** |
| `--text-lg` | | 18px / 24px | 500 | título de card, título de sección |
| `--text-xl` | | 22px / 28px | 400 | título de pantalla (`h1`) |
| `--text-2xl` | | 28px / 36px | 400 | título del hero de Home (solo `h1` de Home) |

> Roboto se self-hostea con `@fontsource/roboto` (pesos 400, 500 y 700, subset *latin* y *latin-ext* por los
> acentos) con `font-display: swap`. Jerarquía: un solo `h1` por pantalla; `h2` para secciones; `h3` para cards.
> En ≥ 768 px `--text-xl` pasa a 24px/32px (mejora progresiva, §3).

### 2.3 Espaciado, radios, sombras, z-index, movimiento y medidas

| Token | Valor | Uso |
|-------|-------|-----|
| `--space-1` … `--space-8` | 4, 8, 12, 16, 24, 32, 40, 48 px | ritmo de 4 px en todo margen, padding y gap |
| `--radius-input` | 8px | inputs, selects, textareas |
| `--radius-card` | 12px | cards de curso, formularios, alertas |
| `--radius-button` | 999px (pill) | botones y chips de filtro |
| `--radius-badge` | 8px | badges de estado |
| `--radius-modal` | 28px | modales (Material 3) |
| `--radius-drawer` | 0 16px 16px 0 | panel del menú sándwich |
| `--shadow-1` | `0 1px 2px rgba(60,64,67,.1), 0 1px 3px 1px rgba(60,64,67,.15)` | reposo de cards, header con scroll |
| `--shadow-2` | `0 1px 2px rgba(60,64,67,.1), 0 2px 6px 2px rgba(60,64,67,.15)` | hover de card, drawer, modal, snackbar |
| `--z-header` / `--z-drawer` / `--z-modal` / `--z-toast` | 100 / 200 / 300 / 400 | orden de capas |
| `--motion-fast` / `--motion-base` | 120ms / 200ms | hover y foco / apertura de drawer y modal |
| `--motion-easing` | `cubic-bezier(0.2, 0, 0, 1)` | todas las transiciones |
| `--target-min` | 44px | tamaño mínimo de cualquier elemento tocable |
| `--header-height` | 64px | alto del header sticky |
| `--drawer-width` | 280px | ancho del menú sándwich |
| `--container-max` | 1140px | ancho máximo del contenido |

> Los breakpoints **no** son variables (las custom properties no funcionan dentro de `@media`): son dos
> constantes documentadas, `768px` y `1024px`.

### 2.4 Bloque de variables listo para copiar (`src/styles/tokens.css`)

```css
:root {
  color-scheme: light;

  /* Color */
  --color-primary: #1a73e8;
  --color-primary-dark: #185abc;
  --color-link: #185abc;
  --color-primary-container: #e8f0fe;
  --color-on-primary: #ffffff;
  --color-surface: #ffffff;
  --color-background: #f8f9fa;
  --color-text: #202124;
  --color-text-muted: #5f6368;
  --color-border: #dadce0;
  --color-border-strong: #80868b;
  --color-hover-grey: #f1f3f4;
  --color-success: #188038;
  --color-success-text: #137333;
  --color-success-container: #e6f4ea;
  --color-warning: #f9ab00;
  --color-on-warning: #202124;
  --color-error: #d93025;
  --color-error-text: #c5221f;
  --color-error-container: #fce8e6;
  --color-snackbar: #323232;
  --color-overlay: rgba(32, 33, 36, 0.6);

  /* Tipografía */
  --font-family-base: "Roboto", system-ui, -apple-system, "Segoe UI", sans-serif;
  --text-xs: 0.75rem;   /* 12 / 16 */
  --text-sm: 0.875rem;  /* 14 / 20 */
  --text-base: 1rem;    /* 16 / 24 */
  --text-lg: 1.125rem;  /* 18 / 24 */
  --text-xl: 1.375rem;  /* 22 / 28 */
  --text-2xl: 1.75rem;  /* 28 / 36 */

  /* Espaciado */
  --space-1: 4px;  --space-2: 8px;  --space-3: 12px; --space-4: 16px;
  --space-5: 24px; --space-6: 32px; --space-7: 40px; --space-8: 48px;

  /* Radios */
  --radius-input: 8px;
  --radius-card: 12px;
  --radius-button: 999px;
  --radius-badge: 8px;
  --radius-modal: 28px;
  --radius-drawer: 0 16px 16px 0;

  /* Sombras */
  --shadow-1: 0 1px 2px rgba(60, 64, 67, .1), 0 1px 3px 1px rgba(60, 64, 67, .15);
  --shadow-2: 0 1px 2px rgba(60, 64, 67, .1), 0 2px 6px 2px rgba(60, 64, 67, .15);

  /* Capas */
  --z-header: 100; --z-drawer: 200; --z-modal: 300; --z-toast: 400;

  /* Movimiento y medidas */
  --motion-fast: 120ms;
  --motion-base: 200ms;
  --motion-easing: cubic-bezier(0.2, 0, 0, 1);
  --target-min: 44px;
  --header-height: 64px;
  --drawer-width: 280px;
  --container-max: 1140px;
}
```

## 3. Estrategia mobile-first con mejora progresiva

> Obligatorio según la SPEC. **Prohibido** usar media queries para "arreglar" el layout base:
> solo para agregar o mejorar a medida que la pantalla crece.

| Capa | Dónde aplica | Qué define |
|------|--------------|------------|
| **Base (sin media queries)** | todos los viewports, pensada para 360 px | layout de 1 columna; header con logo + botón hamburguesa; menú en panel lateral; grid de cards apiladas; **tablas reestilizadas como cards apiladas** (sin scroll horizontal); paginador compacto "‹ Página 2 de 7 ›"; barra de filtros colapsada tras un botón "Filtros"; botones de formulario a ancho completo; tipografía mobile; todos los targets ≥ 44 px |
| `@media (min-width: 768px)` | tablet | grid de **2 columnas** de cards; **nav horizontal** en el header (se oculta la hamburguesa y el panel); tablas reales con `<thead>`; paginador numerado "‹ 1 2 3 … ›"; barra de filtros visible en línea; botones de formulario con ancho automático alineados a la derecha; modales de 480 px; toasts abajo a la izquierda; `--text-xl` 24/32; padding lateral de página 24 px |
| `@media (min-width: 1024px)` | desktop | grid de **3 columnas**; contenedor centrado con `max-width: var(--container-max)`; filtros del catálogo en columna lateral de 240 px; formularios en dos columnas para los campos cortos |

**Patrón de CSS** (ejemplo del grid de cards):

```css
/* Base: sin media queries */
.grid { display: grid; grid-template-columns: 1fr; gap: var(--space-4); }

/* Mejora progresiva: solo AGREGA columnas */
@media (min-width: 768px)  { .grid { grid-template-columns: repeat(2, 1fr); } }
@media (min-width: 1024px) { .grid { grid-template-columns: repeat(3, 1fr); } }
```

**Reglas auditables:**

1. Prohibido `max-width` y `min-height`/`max-height` en media queries. Las únicas permitidas: `(min-width: 768px)`, `(min-width: 1024px)` y, como excepción de accesibilidad que no depende del tamaño de pantalla, `(prefers-reduced-motion: reduce)`.
2. Verificación: `grep -rn "@media" frontend/src | grep -v "min-width" | grep -v "prefers-reduced-motion"` debe devolver **vacío**.
3. Lo que existe en la base **no se ocluye** para "reparar": lo único que una capa superior puede ocultar es la hamburguesa y el panel, porque su función pasa a cumplirla la navegación horizontal que se **agrega**.
4. Probar siempre a 360 px, 768 px y 1280 px, sin scroll horizontal (WCAG 1.4.10, reflow a 320 px).

## 4. Componentes (anatomía + estados)

> Por cada componente: anatomía breve, tokens usados y **todos** sus estados.
> Foco visible común a todo interactivo: `outline: 2px solid var(--color-primary); outline-offset: 2px`.

### 4.1 Botón (primario / secundario / terciario / peligro)

- **Anatomía común:** alto mínimo `--target-min` (44 px), padding `0 24px`, `--radius-button`, Roboto 500 `--text-sm`, icono opcional de 20 px a la izquierda con gap `--space-2`. En la base los botones de formulario ocupan el 100 % del ancho.
- **Primario (filled):** fondo `--color-primary`, texto `--color-on-primary`. Una sola vez por pantalla.
- **Secundario (outlined):** fondo transparente, borde 1 px `--color-border-strong`, texto `--color-link`.
- **Terciario (text):** sin borde ni fondo, texto `--color-link`, padding `0 12px`.
- **Peligro:** outlined con texto `--color-error-text` y borde `--color-error`; en el paso de confirmación, filled con fondo `--color-error` y texto blanco.
- **Estados** (todos): `default` · `hover` (primario: fondo `--color-primary-dark` + `--shadow-1`; secundario y terciario: fondo `--color-primary-container`; peligro outlined: fondo `--color-error-container`) · `focus-visible` (anillo común) · `active` (primario: `--color-primary-dark` sin sombra; otros: fondo un tono más marcado que el hover) · `disabled` (opacidad .38, sin hover, `cursor: not-allowed`; se usa `aria-disabled` cuando el motivo debe poder leerse) · `loading` (spinner de 20 px reemplaza el icono, texto se mantiene, `aria-busy="true"`, no clickeable).

### 4.2 Campo de formulario (input / select / textarea)

- **Anatomía:** `label` **siempre visible** arriba (`--text-sm`, 500, `--color-text`) · campo de 48 px de alto, texto `--text-base`, padding `0 16px`, borde 1 px `--color-border-strong`, `--radius-input`, fondo `--color-surface` · texto de ayuda opcional abajo (`--text-sm`, `--color-text-muted`) · mensaje de error abajo con icono.
- Los campos obligatorios llevan "(obligatorio)" en el label; los opcionales, "(opcional)". No se usa solo el asterisco.
- **Estados:** `default` · `hover` (borde `--color-text`) · `focus` (borde 2 px `--color-primary`, sin cambio de tamaño: se logra con `box-shadow: inset 0 0 0 1px`) · `filled` · `error` (borde 2 px `--color-error`, icono y mensaje en `--color-error-text` asociados con `aria-describedby`, `aria-invalid="true"`) · `disabled` (fondo `--color-hover-grey`, texto muted).
- **Select:** `<select>` nativo con flecha propia (mejor accesibilidad y teclado móvil).
- **Radios sí/no** (cuestionarios, examen, certificado, aval, declaración de toma): grupo `role="radiogroup"` con `<legend>`; cada opción es un radio de 24 px con área tocable de 44 px; **sin opción preseleccionada** (BR-011).
- **Docentes:** lista dinámica de inputs de texto; botón terciario "Agregar docente" (máx. 10) y botón-icono "Quitar" (`aria-label="Quitar docente 2"`).
- Al enviar un formulario con errores, el foco va al **primer campo inválido** y se muestra un resumen arriba ("Revisá 3 campos").

### 4.3 Card de curso

- **Anatomía:** superficie `--color-surface`, `--radius-card`, `--shadow-1`, padding `--space-4`, gap vertical `--space-3`. De arriba a abajo: chip de categoría → **título** (`h3`, `--text-lg`, `--color-text`; es el enlace al detalle y estira su área a toda la card con `::after`) → plataforma · año · versión (`--text-sm`, muted) → docentes (`--text-sm`, muted, máx. 2 líneas) → fila de **atributos** (hasta 4 chips con icono + texto: "Certificado", "Examen", "Cuestionarios", "Aval") → pie: "Aportado por *Nombre* · **Lo tomó** / **No lo tomó**" (`--text-sm`) y botón secundario "Agregar a mi roadmap".
- Los atributos se muestran solo cuando son verdaderos, **siempre con texto** (nunca solo icono).
- **Estados:** `default` · `hover` (`--shadow-2`, `cursor: pointer`) · `focus-visible` (anillo sobre el enlace, visible sobre toda la card) · `seleccionada / en mi roadmap` (borde 2 px `--color-primary`, el botón pasa a "En tu roadmap ✓" deshabilitado con `aria-disabled`) · `loading` (skeleton de la misma altura).

### 4.4 Lista / tabla paginada

- **Base (< 768 px):** cada fila se reestiliza como una **card apilada** (`display: block`; cada celda muestra su cabecera con `data-label` como texto muted). El marcado es una `<table>` real con roles ARIA explícitos (`table`, `row`, `cell`, `columnheader`) para no perder semántica.
- **≥ 768 px:** tabla real: encabezado `--text-sm` 500 muted, filas con divisor `--color-border`, hover `--color-hover-grey`, celdas con padding `--space-3` `--space-4`. `<caption>` visualmente oculto.
- **Paginador** (`<nav aria-label="Paginación">`): botones circulares de 44 px. Base: "‹ Página 2 de 7 ›". ≥ 768 px: "‹ 1 2 3 … 7 ›" con la página actual como **ventana** (actual ± 1, primera y última, puntos suspensivos); la actual con fondo `--color-primary-container`, texto `--color-primary-dark` y `aria-current="page"`; anterior/siguiente deshabilitados en los extremos. Arriba o abajo, texto "Mostrando 13–24 de 47".
- **Estados de la lista:** `loading` (skeleton de 3 a 6 filas/cards) · `ok` · `empty` (§4.8) · `error` (§4.8, con "Reintentar"). Al cambiar de página, la lista anterior permanece (con opacidad .6) hasta que llega la nueva, sin saltos.

### 4.5 Menú sándwich

- **Anatomía:** botón hamburguesa de 44 px (icono `menu` de 24 px) en el extremo izquierdo del header, visible en la base (< 768 px). Al activarlo se abre un **panel lateral** `--color-surface`, `--radius-drawer`, `--shadow-2`, ancho `--drawer-width`, deslizando desde la izquierda en `--motion-base`, con **overlay** `--color-overlay` detrás.
- **Contenido del panel:** logo + botón X (arriba) · ítems de navegación (según rol, ver APPFlow §2) de 48 px de alto con icono + texto; el ítem de la ruta actual con fondo `--color-primary-container`, texto `--color-primary-dark` y `aria-current="page"` · al final, "Ingresar / Registrarse" o "Cerrar sesión".
- **Estados:** `cerrado` · `abierto` · `item hover` (`--color-hover-grey`) · `item focus-visible` (anillo interior) · `item activo`.
- **Cierre:** toque en un enlace, botón X, tecla `ESC`, clic en el overlay. Al abrir, `aria-expanded="true"` en el botón, foco al primer ítem, foco atrapado dentro del panel, el `body` no hace scroll; al cerrar, el foco **vuelve al botón**.
- **ARIA:** botón con `aria-label="Abrir menú"`, `aria-expanded` y `aria-controls="nav-panel"`; el panel es un `<nav id="nav-panel" aria-label="Principal">`.
- **≥ 768 px:** el botón y el panel dejan de mostrarse y aparece la **nav horizontal** del header con los mismos ítems.

### 4.6 Modal

- **Anatomía:** `role="dialog" aria-modal="true" aria-labelledby` · superficie `--color-surface`, `--radius-modal`, `--shadow-2`, padding `--space-5`, ancho `calc(100vw - 32px)` en la base (máx. 480 px desde 768 px) · overlay `--color-overlay` · título `--text-lg` · cuerpo · acciones a la derecha: terciario "Cancelar" + primario (o peligro).
- Se usa para: confirmar "Quitar del roadmap" y pedir el **motivo del rechazo** (textarea obligatoria, mín. 10 caracteres con contador).
- **Estados:** `cerrado` · `abierto` (foco al primer control, **focus trap**, scroll del fondo bloqueado) · `enviando` (acción en `loading`, no se puede cerrar con ESC mientras se envía). Cierre con `ESC`, X o clic en el overlay; el foco vuelve al elemento que lo abrió.

### 4.7 Toast (snackbar)

- **Anatomía:** fondo `--color-snackbar`, texto blanco `--text-sm`, `--radius-input` (8 px), `--shadow-2`, padding `12px 16px`, icono a la izquierda (✓ verde, ! rojo, i azul), acción opcional en texto `--color-primary-container`, botón "Cerrar" de 44 px.
- **Posición:** inferior centrado ocupando el ancho menos 16 px en la base; **desde 768 px** inferior izquierda con ancho mínimo 344 px.
- **Tipos y comportamiento:** éxito e info — 4 s, `role="status"` (`aria-live="polite"`); error — 6 s o hasta cerrarlo, `role="alert"`. Se pausa con hover/foco. Se muestra de a uno (los demás hacen cola).

### 4.8 Skeleton, Empty state y Error state

- **Skeleton:** bloques `--color-hover-grey` con la forma del contenido (card de curso, fila de tabla) y *shimmer* suave; `aria-busy="true"` en el contenedor.
- **Empty state:** icono de 64 px en `--color-text-muted` + título `--text-lg` + bajada `--text-base` muted + CTA primario cuando hay acción. Textos definidos:

| Pantalla | Título | CTA |
|----------|--------|-----|
| Catálogo sin cursos | "Todavía no hay cursos publicados" | "Aportá el primero" |
| Búsqueda sin resultados | "No encontramos cursos con esos filtros" | "Limpiar filtros" |
| Roadmap vacío | "Tu roadmap está vacío" | "Explorar el catálogo" |
| Mis aportes vacío | "Todavía no aportaste cursos" | "Aportar mi primer curso" |
| Cola de validación vacía | "No hay aportes pendientes. ¡Buen trabajo!" | — |

- **Error state:** icono `error` + "No pudimos cargar esto" + causa breve + botón secundario **"Reintentar"** (vuelve a pedir; no recarga la página).

### 4.9 Badge y chip

- **Badge de estado** (`--text-xs`, 500, `--radius-badge`, padding `4px 8px`, siempre con **texto**, nunca solo color):

| Valor | Fondo | Texto |
|-------|-------|-------|
| `borrador` | `--color-hover-grey` | `--color-text-muted` (5.44:1 ✓) |
| `en_revision` ("En revisión") | `--color-warning` | `--color-on-warning` (8.32:1 ✓) |
| `publicado` ("Publicado") | `--color-success-container` | `--color-success-text` (5.24:1 ✓) |
| `rechazado` ("Rechazado") | `--color-error-container` | `--color-error-text` (4.92:1 ✓) |
| progreso `pendiente` | `--color-hover-grey` | `--color-text-muted` |
| progreso `en_curso` ("En curso") | `--color-primary-container` | `--color-primary-dark` (5.68:1 ✓) |
| progreso `completado` ("Completado") | `--color-success-container` | `--color-success-text` |

- **Chip** (categoría y atributos): pill `--text-sm`, fondo `--color-primary-container`, texto `--color-primary-dark`; los **chips de filtro** son botones con estados `default` / `hover` / `focus-visible` / `seleccionado` (borde 1 px primary + check).

### 4.10 Buscador y filtros

- **Buscador:** `<form role="search">` con input de tipo `search` de 48 px, icono `search` a la izquierda y botón "Limpiar" (X) cuando hay texto. Busca al presionar Enter o tras 300 ms sin escribir (*debounce*); el estado va a la URL.
- **Filtros — base:** botón secundario "Filtros" con contador de filtros activos y `aria-expanded`; despliega un panel debajo con el select de categoría y, si aplica (P1), los atributos: "Da certificado", "Con cuestionarios", "Requiere examen: sí/no", "Con aval" (checkboxes) e idioma (select). Botones "Aplicar" y "Limpiar".
- **Filtros — ≥ 768 px:** el panel se **agrega** abierto en línea; **≥ 1024 px:** columna lateral de 240 px. Los filtros activos se muestran como chips removibles sobre el listado.

### 4.11 Checklist del validador y selector de progreso

- **Checklist:** 4 checkboxes de 24 px (área 44 px) con borde `--color-border-strong`: "El enlace está activo", "El curso es realmente gratuito", "Los datos coinciden con el curso", "La categoría es correcta". El botón **Aprobar** usa `aria-disabled="true"` y un texto de ayuda ("Completá las 4 verificaciones") hasta que estén todos tildados.
- **Selector de progreso** (roadmap): `<select>` nativo con las tres opciones y el mismo estilo de campo; el cambio se guarda al instante (toast "Progreso actualizado"; si falla, se revierte y se muestra el error).

### 4.12 Alerta / banner

- Bloque `--radius-card`, padding `--space-4`, icono + texto, botón de acción opcional. Tipos: `info` (`--color-primary-container`), `success` (`--color-success-container`), `warning` (`--color-warning` con texto `--color-on-warning`), `error` (`--color-error-container`, texto `--color-error-text`). `role="alert"` para error, `role="status"` para el resto. Se usa para el rate limiting (429), la sesión expirada y la red caída.

## 5. Layout y navegación

- **Header:** sticky (`--z-header`), fondo `--color-surface`, alto `--header-height`. **Base:** hamburguesa + logo a la izquierda, a la derecha avatar con menú (sesión iniciada) o botón terciario "Ingresar". **≥ 768 px:** logo + nav horizontal (Catálogo · Mi roadmap · Aportar · Mis aportes · Validar*) + acciones de sesión. La sombra `--shadow-1` aparece al hacer scroll. (*) "Validar" solo con rol `validador`.
- **Elementos globales:** enlace "Saltar al contenido" como primer elemento focuseable; `<main id="contenido">` con foco programático en el `h1` al cambiar de ruta.
- **Contenedores:** `max-width: var(--container-max)`, centrado; padding lateral `--space-4` (base) y `--space-5` (≥ 768 px); separación vertical entre secciones `--space-5`.
- **Pantallas** (el detalle de navegación, rutas y APIs vive en el [APPFlow](APPFlow.md)):

| Pantalla | Composición |
|----------|-------------|
| Home | hero (`h1` `--text-2xl`, bajada, CTA primario "Explorar el catálogo" y secundario "Aportar un curso") · 3 pasos ("Aportá", "Validamos", "Armá tu roadmap") · "Últimos cursos agregados" (6 cards con enlace "Ver todo el catálogo") |
| Catálogo | `h1` · buscador · filtros · total de resultados · grid de cards (1/2/3 columnas) · paginador |
| Detalle de curso | breadcrumb "Catálogo › Título" · `h1` · chips de categoría/idioma · bloque de metadatos (lista de definición) · atributos · bloque "Aportado por" con "Lo tomó/No lo tomó" · acciones: "Ir al curso" (primario, abre pestaña nueva) y "Agregar a mi roadmap" (secundario) |
| Login / Registro / Recuperar / Restablecer | card centrada de máx. 440 px sobre `--color-background`, un campo por fila, botón primario a ancho completo, enlaces terciarios para alternar entre pantallas |
| Aportar / Editar aporte | formulario en 3 cards: "1. Enlace y datos básicos" · "2. Características del curso" · "3. Tu experiencia y confirmación"; botones al final: "Guardar borrador" (secundario, P1) y "Enviar a revisión" (primario) |
| Mis aportes | `h1` + botón primario "Aportar curso" · lista/tabla paginada con título, fecha, badge de estado y acción · detalle con motivo de rechazo |
| Cola de validación y Revisión | tabla paginada (título, aportante, fecha de envío) · en la revisión: datos completos + enlace externo + checklist + botones "Aprobar" (primario) y "Rechazar" (peligro, abre modal de motivo) |
| Roadmap | `h1` · lista/tabla paginada con curso, selector de progreso, botones subir/bajar (P1) y quitar |
| 404 / Sin permiso | icono + mensaje + CTA "Volver al catálogo" |

## 6. Accesibilidad mínima (no negociable)

**Garantizado por los tokens** (valores calculados en §2.1):

- [x] Texto principal y muted ≥ 4.5:1 sobre blanco y gris de fondo (`#202124` 16.10 · `#5f6368` 6.05 / 5.74)
- [x] Texto de enlaces y botones secundarios (`#185abc`) ≥ 4.5:1 (6.51 sobre blanco, 6.17 sobre fondo)
- [x] Botón primario: blanco sobre `#1a73e8` = 4.51:1 (cumple AA con margen mínimo; no usar variantes más claras ni opacidad)
- [x] Bordes de controles ≥ 3:1 (`#80868b` = 3.68:1) y anillo de foco ≥ 3:1 (4.51:1)
- [x] Badges y mensajes de error con pares ≥ 4.5:1 (§4.9)

**A verificar durante la implementación** (cada ítem es criterio de aceptación de M5 del plan):

- [ ] `:focus-visible` visible en **todo** elemento interactivo; nada con `outline: none` sin reemplazo
- [ ] Todo el sitio se opera solo con teclado; el orden de tabulación sigue el orden visual
- [ ] Menú sándwich con `aria-expanded` / `aria-controls`, foco atrapado y restaurado al cerrar; cierre con `ESC`
- [ ] Modales con `role="dialog"`, `aria-modal`, focus trap y retorno del foco
- [ ] Targets táctiles ≥ 44 × 44 px (botones, hamburguesa, paginador, checkboxes, radios)
- [ ] `prefers-reduced-motion: reduce` desactiva shimmer, deslizamiento del drawer y transiciones de elevación
- [ ] Imágenes e iconos con `alt`/`aria-label` si comunican; iconos decorativos con `aria-hidden="true"`
- [ ] Errores de formulario asociados al campo (`aria-describedby` + `aria-invalid`), con foco al primer error
- [ ] Estados comunicados con texto, no solo color (badges, "En tu roadmap ✓")
- [ ] `lang="es-AR"` en `<html>`, `<title>` único por ruta, un solo `h1`, jerarquía de títulos sin saltos y landmarks (`header`, `nav`, `main`)
- [ ] Reflow sin scroll horizontal a 320 px y zoom de texto al 200 %
- [ ] Toasts y alertas anunciados (`role="status"` / `role="alert"`)
- [ ] Lighthouse (móvil) en `/catalogo`: Accesibilidad ≥ 95 · Performance ≥ 85

## 7. Iconografía y assets

- **Set elegido:** **Material Symbols** (outlined, peso 400), el set de Google — https://fonts.google.com/icons
- **Cómo se incorporan:** solo los ~25 iconos usados, como **SVG inline** en `src/shared/icons/` (componentes React). No se carga la fuente de iconos completa (varios MB) y se evita el parpadeo de texto antes de que cargue la fuente.
- **Iconos previstos:** `menu`, `close`, `search`, `filter_list`, `chevron_left`, `chevron_right`, `expand_more`, `check`, `check_circle`, `error`, `warning`, `info`, `add`, `delete`, `arrow_upward`, `arrow_downward`, `open_in_new`, `workspace_premium` (certificado), `quiz` (examen), `checklist` (cuestionarios), `verified` (aval), `school` (lo tomó), `bookmark_add` / `bookmark_added` (roadmap), `logout`, `login`, `person`.
- **Tamaño y color por defecto:** 20 px en botones, 24 px en listas y menú, 64 px en estados vacíos; color `currentColor` (hereda del texto; los de estado vacío en `--color-text-muted`).
- **Imágenes:** sin fotos de stock ni imágenes decorativas; los estados vacíos usan un icono grande en `--color-text-muted`. El logo es texto (wordmark "Roadmap de Cursos") con un icono de ruta en `--color-primary`.

---

**Referencias:**
- NN/g — Front-End Style-Guides (definición y checklist): https://www.nngroup.com/articles/front-end-style-guides/
- NN/g — Design Systems 101: https://www.nngroup.com/articles/design-systems-101/
- Material Design 3: https://m3.material.io/
- WCAG 2.2 — Contraste de componentes no textuales (1.4.11) y reflow (1.4.10): https://www.w3.org/TR/WCAG22/
- WebAIM Contrast Checker: https://webaim.org/resources/contrastchecker/
