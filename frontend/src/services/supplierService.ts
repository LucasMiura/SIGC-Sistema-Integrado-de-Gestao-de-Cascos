import { httpClient } from './httpClient'
import type {
  Supplier,
  SupplierCreatePayload,
  SupplierDeactivatePayload,
  SupplierUpdatePayload,
} from '../types/supplier'

export const supplierService = {
  list(): Promise<Supplier[]> {
    return httpClient.get<
      Supplier[]
    >(
      '/suppliers',
    )
  },

  getById(
    supplierId: number,
  ): Promise<Supplier> {
    return httpClient.get<
      Supplier
    >(
      `/suppliers/${supplierId}`,
    )
  },

  create(
    payload: SupplierCreatePayload,
  ): Promise<Supplier> {
    return httpClient.post<
      Supplier
    >(
      '/suppliers',
      payload,
    )
  },

  update(
    supplierId: number,
    payload: SupplierUpdatePayload,
  ): Promise<Supplier> {
    return httpClient.patch<
      Supplier
    >(
      `/suppliers/${supplierId}`,
      payload,
    )
  },

  activate(
    supplierId: number,
  ): Promise<Supplier> {
    return httpClient.patch<
      Supplier
    >(
      `/suppliers/${supplierId}/activate`,
    )
  },

  deactivate(
    supplierId: number,
    payload: SupplierDeactivatePayload,
  ): Promise<Supplier> {
    return httpClient.patch<
      Supplier
    >(
      `/suppliers/${supplierId}/deactivate`,
      payload,
    )
  },
}