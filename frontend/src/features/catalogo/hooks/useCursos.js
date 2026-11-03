import { useEffect, useState } from 'react'
import { listarCursos } from '../api.js'

export function useCursos() {
  const [cursos, setCursos] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    let vigente = true // no actualiza el estado si el componente ya se desmontó
    listarCursos()
      .then((pagina) => vigente && setCursos(pagina.items))
      .catch((e) => vigente && setError(e))
      .finally(() => vigente && setLoading(false))
    return () => {
      vigente = false
    }
  }, [])

  return { cursos, loading, error }
}
