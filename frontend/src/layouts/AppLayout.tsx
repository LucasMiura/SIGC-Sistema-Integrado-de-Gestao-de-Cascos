import {
  useState,
} from 'react'
import {
  Outlet,
} from 'react-router'

import {
  Sidebar,
} from '../components/layout/Sidebar'
import {
  Topbar,
} from '../components/layout/Topbar'

export function AppLayout() {
  const [
    sidebarCollapsed,
    setSidebarCollapsed,
  ] = useState(false)

  return (
    <div
      className={[
        'app-shell',
        sidebarCollapsed
          ? 'app-shell--sidebar-collapsed'
          : '',
      ]
        .filter(Boolean)
        .join(' ')}
    >
      <Sidebar
        collapsed={sidebarCollapsed}
        onToggle={() => {
          setSidebarCollapsed(
            (current) => !current,
          )
        }}
      />

      <div className="app-shell__workspace">
        <Topbar />

        <main className="app-main">
          <div className="app-main__container">
            <Outlet />
          </div>
        </main>
      </div>
    </div>
  )
}