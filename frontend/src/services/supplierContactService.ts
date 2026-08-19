import { httpClient } from './httpClient'
import type {
  SupplierContact,
  SupplierContactCreatePayload,
  SupplierContactDeactivatePayload,
  SupplierContactUpdatePayload,
} from '../types/supplierContact'

function getBasePath(
  supplierId: number,
): string {
  return (
    `/suppliers/${supplierId}/contacts`
  )
}

export const supplierContactService = {
  list(
    supplierId: number,
  ): Promise<SupplierContact[]> {
    return httpClient.get<
      SupplierContact[]
    >(
      getBasePath(
        supplierId,
      ),
    )
  },

  create(
    supplierId: number,
    payload:
      SupplierContactCreatePayload,
  ): Promise<SupplierContact> {
    return httpClient.post<
      SupplierContact
    >(
      getBasePath(
        supplierId,
      ),
      payload,
    )
  },

  update(
    supplierId: number,
    contactId: number,
    payload:
      SupplierContactUpdatePayload,
  ): Promise<SupplierContact> {
    return httpClient.patch<
      SupplierContact
    >(
      `${getBasePath(
        supplierId,
      )}/${contactId}`,
      payload,
    )
  },

  activate(
    supplierId: number,
    contactId: number,
  ): Promise<SupplierContact> {
    return httpClient.patch<
      SupplierContact
    >(
      `${getBasePath(
        supplierId,
      )}/${contactId}/activate`,
    )
  },

  deactivate(
    supplierId: number,
    contactId: number,
    payload:
      SupplierContactDeactivatePayload,
  ): Promise<SupplierContact> {
    return httpClient.patch<
      SupplierContact
    >(
      `${getBasePath(
        supplierId,
      )}/${contactId}/deactivate`,
      payload,
    )
  },
}