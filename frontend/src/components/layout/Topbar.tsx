import {
  ChevronDown,
  LogOut,
  Search,
} from 'lucide-react'

import { useAuth } from '../../hooks/useAuth'
import {
  IconButton,
} from '../ui/IconButton'

export function Topbar() {
  const {
    session,
    logout,
  } = useAuth()

  const fullName =
    session?.user.full_name
    ?? 'Usuário'

  const initial =
    fullName
      .trim()
      .charAt(0)
      .toUpperCase()
      || 'U'

  return (
    <header className="app-topbar">
      <div className="app-topbar__search">
        <Search
          size={18}
          aria-hidden="true"
        />

        <span>
          Busca global será habilitada
          futuramente
        </span>

        <kbd>
          Ctrl K
        </kbd>
      </div>

      <div className="app-topbar__account">
        <div
          className="app-topbar__avatar"
          aria-hidden="true"
        >
          {initial}
        </div>

        <div className="app-topbar__user">
          <strong>
            {fullName}
          </strong>

          <span>
            {session?.role_name}
          </span>
        </div>

        <ChevronDown
          className="app-topbar__chevron"
          size={16}
          aria-hidden="true"
        />

        <div className="app-topbar__divider" />

        <IconButton
          label="Sair do SIGC"
          onClick={logout}
        >
          <LogOut size={18} />
        </IconButton>
      </div>
    </header>
  )
}