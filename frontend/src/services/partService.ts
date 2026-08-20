import { httpClient } from './httpClient'

import type {
  Part,
  PartCreatePayload,
  PartDeactivatePayload,
  PartUpdatePayload,
} from '../types/part'

function buildListPath(
  supplierId?: number,
): string {
  if (!supplierId) {
    return '/parts'
  }

  const params =
    new URLSearchParams()

  params.set(
    'supplier_id',
    String(supplierId),
  )

  return (
    `/parts?${params.toString()}`
  )
}

export const partService = {
  list(
    supplierId?: number,
  ): Promise<Part[]> {
    return httpClient.get<
      Part[]
    >(
      buildListPath(
        supplierId,
      ),
    )
  },

  getById(
    partId: number,
  ): Promise<Part> {
    return httpClient.get<
      Part
    >(
      `/parts/${partId}`,
    )
  },

  create(
    payload: PartCreatePayload,
  ): Promise<Part> {
    return httpClient.post<
      Part
    >(
      '/parts',
      payload,
    )
  },

  update(
    partId: number,
    payload: PartUpdatePayload,
  ): Promise<Part> {
    return httpClient.patch<
      Part
    >(
      `/parts/${partId}`,
      payload,
    )
  },

  activate(
    partId: number,
  ): Promise<Part> {
    return httpClient.patch<
      Part
    >(
      `/parts/${partId}/activate`,
    )
  },

  deactivate(
    partId: number,
    payload: PartDeactivatePayload,
  ): Promise<Part> {
    return httpClient.patch<
      Part
    >(
      `/parts/${partId}/deactivate`,
      payload,
    )
  },
}