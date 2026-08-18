export const ROLE_NAMES = {
  admin: 'Administrador Master',
  buyer: 'Comprador',
  seller: 'Vendedor',
} as const

export type SystemRoleName =
  (typeof ROLE_NAMES)[keyof typeof ROLE_NAMES]

export interface AuthUser {
  id: number
  full_name: string
  username: string
  email: string
  role_id: number
  is_active: boolean
  last_login_at: string | null
  created_at: string
  updated_at: string
}

export interface AuthenticatedSession {
  user: AuthUser
  role_name: string
}

export interface LoginCredentials {
  login: string
  password: string
}

export interface LoginResponse
  extends AuthenticatedSession {
  access_token: string
  token_type: string
}