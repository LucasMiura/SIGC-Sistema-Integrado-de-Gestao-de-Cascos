export type ApiErrorDetail =
  | string
  | {
      loc?: Array<string | number>
      msg?: string
      type?: string
      [key: string]: unknown
    }

export interface ApiErrorResponse {
  detail?: ApiErrorDetail | ApiErrorDetail[]
}

export interface ApiRequestOptions
  extends Omit<RequestInit, 'body'> {
  body?: unknown

  /**
   * Define se o Bearer token deve ser
   * incluído automaticamente.
   *
   * O padrão é true.
   */
  auth?: boolean
}