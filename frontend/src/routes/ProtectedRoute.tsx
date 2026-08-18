import {
  Navigate,
  Outlet,
  useLocation,
} from 'react-router'

import { useAuth } from '../hooks/useAuth'

export function ProtectedRoute() {
  const {
    isAuthenticated,
    isLoading,
  } = useAuth()

  const location = useLocation()

  if (isLoading) {
    return (
      <main className="session-loading">
        <p>
          Validando sessão...
        </p>
      </main>
    )
  }

  if (!isAuthenticated) {
    return (
      <Navigate
        to="/login"
        replace
        state={{
          from: location.pathname,
        }}
      />
    )
  }

  return <Outlet />
}