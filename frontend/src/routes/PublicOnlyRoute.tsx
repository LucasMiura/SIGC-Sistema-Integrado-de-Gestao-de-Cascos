import {
  Navigate,
} from 'react-router'

import { useAuth } from '../hooks/useAuth'

interface PublicOnlyRouteProps {
  children: React.ReactNode
}

export function PublicOnlyRoute({
  children,
}: PublicOnlyRouteProps) {
  const {
    isAuthenticated,
    isLoading,
  } = useAuth()

  if (isLoading) {
    return (
      <main className="session-loading">
        <p>
          Validando sessão...
        </p>
      </main>
    )
  }

  if (isAuthenticated) {
    return (
      <Navigate
        to="/"
        replace
      />
    )
  }

  return children
}