import { useCursos } from './hooks/useCursos.js'

export default function CatalogoPage() {
  const { cursos, loading, error } = useCursos()

  return (
    <main>
      <h1>Catálogo de cursos</h1>
      {loading && <p role="status">Cargando cursos…</p>}
      {error && <p role="alert">No pudimos cargar los cursos ({error.message}).</p>}
      {!loading && !error && cursos.length === 0 && (
        <p>Todavía no hay cursos en el catálogo. ¡Aportá el primero!</p>
      )}
      {cursos.length > 0 && (
        <ul>
          {cursos.map((curso) => (
            <li key={curso.id}>{curso.titulo}</li>
          ))}
        </ul>
      )}
    </main>
  )
}
