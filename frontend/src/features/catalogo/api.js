export async function listarCursos() {
  const respuesta = await fetch('/api/v1/cursos')
  if (!respuesta.ok) throw new Error(`El servidor respondió ${respuesta.status}`)
  return respuesta.json()
}
