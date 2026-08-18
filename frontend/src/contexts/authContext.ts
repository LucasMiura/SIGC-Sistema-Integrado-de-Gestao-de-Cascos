import { createContext } from 'react'

import type {
  AuthenticatedSession,
  LoginCredentials,
} from '../types/auth'

export interface AuthContextValue {
  session: AuthenticatedSession | null
  isAuthenticated: boolean
  isLoading: boolean

  login(
    credentials: LoginCredentials,
  ): Promise<void>

  logout(): void
}

export const AuthContext =
  createContext<AuthContextValue | null>(
    null,
  )