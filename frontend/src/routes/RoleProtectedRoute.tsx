import type {
  ReactNode,
} from 'react'
import {
  Navigate,
  useLocation,
} from 'react-router'

import {
  hasPermission,
  type PermissionKey,
} from '../config/permissions'
import { useAuth } from '../hooks/useAuth'

interface RoleProtectedRouteProps {
  permission: PermissionKey
  children: ReactNode
}

export function RoleProtectedRoute({
  permission,
  children,
}: RoleProtectedRouteProps) {
  const {
    session,
  } = useAuth()

  const location =
    useLocation()

  const allowed =
    hasPermission(
      session?.role_name,
      permission,
    )

  if (!allowed) {
    return (
      <Navigate
        to="/acesso-negado"
        replace
        state={{
          from:
            location.pathname,
        }}
      />
    )
  }

  return children
}