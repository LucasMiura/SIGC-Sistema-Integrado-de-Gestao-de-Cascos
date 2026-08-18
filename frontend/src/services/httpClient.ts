import { env } from '../config/env'
import { tokenStorage } from '../storage/tokenStorage'
import type {
  ApiErrorDetail,
  ApiErrorResponse,
  ApiRequestOptions,
} from '../types/api'

export class ApiError extends Error {
  readonly status: number
  readonly data: ApiErrorResponse | null

  constructor(
    message: string,
    status: number,
    data: ApiErrorResponse | null = null,
  ) {
    super(message)

    this.name = 'ApiError'
    this.status = status
    this.data = data
  }
}

function buildUrl(path: string): string {
  const normalizedPath = path.startsWith('/')
    ? path
    : `/${path}`

  return `${env.apiBaseUrl}${normalizedPath}`
}

function buildHeaders(
  headers: HeadersInit | undefined,
  hasBody: boolean,
  includeAuth: boolean,
): Headers {
  const result = new Headers(headers)

  result.set(
    'Accept',
    'application/json',
  )

  if (
    hasBody &&
    !result.has('Content-Type')
  ) {
    result.set(
      'Content-Type',
      'application/json',
    )
  }

  if (
    includeAuth &&
    !result.has('Authorization')
  ) {
    const token = tokenStorage.get()

    if (token) {
      result.set(
        'Authorization',
        `Bearer ${token}`,
      )
    }
  }

  return result
}

async function parseResponseBody(
  response: Response,
): Promise<unknown> {
  if (response.status === 204) {
    return null
  }

  const contentType =
    response.headers.get(
      'content-type',
    )

  if (
    contentType?.includes(
      'application/json',
    )
  ) {
    return response.json()
  }

  const text = await response.text()

  return text || null
}

function getDetailMessage(
  detail: ApiErrorDetail,
): string | null {
  if (typeof detail === 'string') {
    return detail
  }

  if (
    typeof detail.msg === 'string' &&
    detail.msg.trim()
  ) {
    return detail.msg
  }

  return null
}

function getErrorMessage(
  status: number,
  data: unknown,
): string {
  if (
    typeof data === 'object' &&
    data !== null &&
    'detail' in data
  ) {
    const detail = (
      data as ApiErrorResponse
    ).detail

    if (Array.isArray(detail)) {
      for (const item of detail) {
        const message =
          getDetailMessage(item)

        if (message) {
          return message
        }
      }

      return (
        `A API retornou o status ${status}.`
      )
    }

    if (detail !== undefined) {
      const message =
        getDetailMessage(detail)

      if (message) {
        return message
      }
    }
  }

  return (
    `A API retornou o status ${status}.`
  )
}

export async function apiRequest<T>(
  path: string,
  options: ApiRequestOptions = {},
): Promise<T> {
  const {
    body,
    headers,
    auth = true,
    ...requestOptions
  } = options

  const hasBody =
    body !== undefined

  const response = await fetch(
    buildUrl(path),
    {
      ...requestOptions,

      headers: buildHeaders(
        headers,
        hasBody,
        auth,
      ),

      body: hasBody
        ? JSON.stringify(body)
        : undefined,
    },
  )

  const data = await parseResponseBody(
    response,
  )

  if (!response.ok) {
    throw new ApiError(
      getErrorMessage(
        response.status,
        data,
      ),
      response.status,
      (
        typeof data === 'object' &&
        data !== null
          ? data as ApiErrorResponse
          : null
      ),
    )
  }

  return data as T
}

export const httpClient = {
  get<T>(
    path: string,
    options: ApiRequestOptions = {},
  ): Promise<T> {
    return apiRequest<T>(
      path,
      {
        ...options,
        method: 'GET',
      },
    )
  },

  post<T>(
    path: string,
    body?: unknown,
    options: ApiRequestOptions = {},
  ): Promise<T> {
    return apiRequest<T>(
      path,
      {
        ...options,
        method: 'POST',
        body,
      },
    )
  },

  patch<T>(
    path: string,
    body?: unknown,
    options: ApiRequestOptions = {},
  ): Promise<T> {
    return apiRequest<T>(
      path,
      {
        ...options,
        method: 'PATCH',
        body,
      },
    )
  },

  delete<T>(
    path: string,
    options: ApiRequestOptions = {},
  ): Promise<T> {
    return apiRequest<T>(
      path,
      {
        ...options,
        method: 'DELETE',
      },
    )
  },
}