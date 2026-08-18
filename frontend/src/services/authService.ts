import { httpClient } from './httpClient'
import type {
  AuthenticatedSession,
  LoginCredentials,
  LoginResponse,
} from '../types/auth'

export const authService = {
  login(
    credentials: LoginCredentials,
  ): Promise<LoginResponse> {
    return httpClient.post<LoginResponse>(
      '/auth/login',
      credentials,
      {
        auth: false,
      },
    )
  },

  getCurrentSession():
    Promise<AuthenticatedSession> {
    return httpClient.get<
      AuthenticatedSession
    >(
      '/auth/me',
    )
  },
}