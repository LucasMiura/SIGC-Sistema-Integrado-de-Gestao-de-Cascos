const DEFAULT_API_BASE_URL = 'http://127.0.0.1:8000'

function normalizeBaseUrl(value: string): string {
  return value.trim().replace(/\/+$/, '')
}

function getApiBaseUrl(): string {
  const configuredUrl = import.meta.env.VITE_API_BASE_URL

  if (!configuredUrl) {
    return DEFAULT_API_BASE_URL
  }

  const normalizedUrl = normalizeBaseUrl(configuredUrl)

  if (!normalizedUrl) {
    return DEFAULT_API_BASE_URL
  }

  return normalizedUrl
}

export const env = {
  apiBaseUrl: getApiBaseUrl(),
} as const