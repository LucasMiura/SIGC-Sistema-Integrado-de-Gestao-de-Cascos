import { httpClient } from './httpClient'

import type {
  Purchase,
  PurchaseCancelPayload,
  PurchaseCreatePayload,
  PurchaseItem,
  PurchaseItemCreatePayload,
  PurchaseUpdatePayload,
} from '../types/purchase'

function buildListPath(
  supplierId?: number,
): string {
  if (!supplierId) {
    return '/purchases'
  }

  const params =
    new URLSearchParams()

  params.set(
    'supplier_id',
    String(supplierId),
  )

  return (
    `/purchases?${params.toString()}`
  )
}

export const purchaseService = {
  list(
    supplierId?: number,
  ): Promise<Purchase[]> {
    return httpClient.get<
      Purchase[]
    >(
      buildListPath(
        supplierId,
      ),
    )
  },

  getById(
    purchaseId: number,
  ): Promise<Purchase> {
    return httpClient.get<
      Purchase
    >(
      `/purchases/${purchaseId}`,
    )
  },

  create(
    payload: PurchaseCreatePayload,
  ): Promise<Purchase> {
    return httpClient.post<
      Purchase
    >(
      '/purchases',
      payload,
    )
  },

  update(
    purchaseId: number,
    payload: PurchaseUpdatePayload,
  ): Promise<Purchase> {
    return httpClient.patch<
      Purchase
    >(
      `/purchases/${purchaseId}`,
      payload,
    )
  },

  cancel(
    purchaseId: number,
    payload: PurchaseCancelPayload,
  ): Promise<Purchase> {
    return httpClient.patch<
      Purchase
    >(
      `/purchases/${purchaseId}/cancel`,
      payload,
    )
  },

  listItems(
    purchaseId: number,
  ): Promise<PurchaseItem[]> {
    return httpClient.get<
      PurchaseItem[]
    >(
      `/purchases/${purchaseId}/items`,
    )
  },

  addItem(
    purchaseId: number,
    payload:
      PurchaseItemCreatePayload,
  ): Promise<PurchaseItem> {
    return httpClient.post<
      PurchaseItem
    >(
      `/purchases/${purchaseId}/items`,
      payload,
    )
  },
}