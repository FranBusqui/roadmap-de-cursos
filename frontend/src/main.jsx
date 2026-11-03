import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import CatalogoPage from './features/catalogo/CatalogoPage.jsx'

// shortcut: renderiza el catálogo directo; el router y el shell llegan en la tarea 0.4
createRoot(document.getElementById('root')).render(
  <StrictMode>
    <CatalogoPage />
  </StrictMode>,
)
