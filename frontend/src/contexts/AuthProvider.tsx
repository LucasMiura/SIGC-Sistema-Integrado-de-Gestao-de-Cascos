import {
  useCallback,
  useEffect,
  useMemo,
  useRef,
  useState,
} from 'react'

import {
  AuthContext,
  type AuthContextValue,
} from './authContext'
import { authService } from '../services/authService'
import { tokenStorage } from '../storage/tokenStorage'
import type {
  AuthenticatedSession,
  LoginCredentials,
} from '../types/auth'

interface AuthProviderProps {
  children: React.ReactNode
}

export function AuthProvider({
  children,
}: AuthProviderProps) {
  const [
    session,
    setSession,
  ] = useState<
    AuthenticatedSession | null
  >(null)

  const [
    isLoading,
    setIsLoading,
  ] = useState(true)

  const restoreStarted =
    useRef(false)

  useEffect(
    () => {
      if (restoreStarted.current) {
        return
      }

      restoreStarted.current = true

      async function restoreSession() {
        const token =
          tokenStorage.get()

        if (!token) {
          setIsLoading(false)
          return
        }

        try {
          const currentSession =
            await authService
              .getCurrentSession()

          setSession(
            currentSession,
          )

        } catch {
          tokenStorage.clear()
          setSession(null)

        } finally {
          setIsLoading(false)
        }
      }

      void restoreSession()
    },
    [],
  )

  const login = useCallback(
    async (
      credentials: LoginCredentials,
    ) => {
      const response =
        await authService.login(
          credentials,
        )

      tokenStorage.set(
        response.access_token,
      )

      setSession({
        user: response.user,
        role_name:
          response.role_name,
      })
    },
    [],
  )

  const logout = useCallback(
    () => {
      tokenStorage.clear()
      setSession(null)
    },
    [],
  )

  const value =
    useMemo<AuthContextValue>(
      () => ({
        session,
        isAuthenticated:
          session !== null,
        isLoading,
        login,
        logout,
      }),
      [
        session,
        isLoading,
        login,
        logout,
      ],
    )

  return (
    <AuthContext.Provider
      value={value}
    >
      {children}
    </AuthContext.Provider>
  )
}