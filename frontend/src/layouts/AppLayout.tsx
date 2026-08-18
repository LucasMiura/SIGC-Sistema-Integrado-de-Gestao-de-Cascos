import {
  Link,
  Outlet,
} from 'react-router'

export function AppLayout() {
  return (
    <div className="app-shell">
      <header className="temporary-header">
        <strong>SIGC</strong>

        <nav
          className="temporary-navigation"
          aria-label="Navegação provisória"
        >
          <Link to="/">
            Dashboard
          </Link>

          <Link to="/login">
            Login
          </Link>
        </nav>
      </header>

      <main className="app-content">
        <Outlet />
      </main>
    </div>
  )
}