import react from '@vitejs/plugin-react'
import { defineConfig } from 'vite'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      // En Docker VITE_PROXY_TARGET apunta a http://backend:8000 (.env.example)
      '/api': process.env.VITE_PROXY_TARGET ?? 'http://localhost:8000',
    },
  },
})
