import {
  Outlet,
} from 'react-router'

import { useAuth } from '../hooks/useAuth'

export function AppLayout() {
  const {
    session,
    logout,
  } = useAuth()

  return (
    <div className="app-shell">
      <header className="temporary-header">
        <div>
          <strong>
            SIGC
          </strong>

          {session && (
            <span className="session-summary">
              {session.user.full_name}
              {' — '}
              {session.role_name}
            </span>
          )}
        </div>

        <button
          type="button"
          onClick={logout}
        >
          Sair
        </button>
      </header>

      <main className="app-content">
        <Outlet />
      </main>
    </div>
  )
}