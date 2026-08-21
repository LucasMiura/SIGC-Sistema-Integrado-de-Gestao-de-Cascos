import { httpClient } from './httpClient'

import type {
  CustomerReturn,
  CustomerReturnCancelPayload,
  CustomerReturnCreatePayload,
  CustomerReturnItem,
  CustomerReturnItemCreatePayload,
  CustomerReturnOrigin,
  CustomerReturnType,
} from '../types/customerReturn'

export const customerReturnService = {
  list(): Promise<CustomerReturn[]> {
    return httpClient.get<
      CustomerReturn[]
    >(
      '/customer-returns',
    )
  },

  getById(
    customerReturnId: number,
  ): Promise<CustomerReturn> {
    return httpClient.get<
      CustomerReturn
    >(
      `/customer-returns/${customerReturnId}`,
    )
  },

  getOrigin(
    returnType: CustomerReturnType,
    referenceNumber: string,
  ): Promise<CustomerReturnOrigin> {
    const params =
      new URLSearchParams({
        return_type: returnType,
        reference_number:
          referenceNumber,
      })

    return httpClient.get<
      CustomerReturnOrigin
    >(
      `/customer-returns/origin?${params.toString()}`,
    )
  },

  create(
    payload: CustomerReturnCreatePayload,
  ): Promise<CustomerReturn> {
    return httpClient.post<
      CustomerReturn
    >(
      '/customer-returns',
      payload,
    )
  },

  addItem(
    customerReturnId: number,
    payload:
      CustomerReturnItemCreatePayload,
  ): Promise<CustomerReturnItem> {
    return httpClient.post<
      CustomerReturnItem
    >(
      `/customer-returns/${customerReturnId}/items`,
      payload,
    )
  },

  listItems(
    customerReturnId: number,
  ): Promise<CustomerReturnItem[]> {
    return httpClient.get<
      CustomerReturnItem[]
    >(
      `/customer-returns/${customerReturnId}/items`,
    )
  },

  cancel(
    customerReturnId: number,
    payload: CustomerReturnCancelPayload,
  ): Promise<CustomerReturn> {
    return httpClient.patch<
      CustomerReturn
    >(
      `/customer-returns/${customerReturnId}/cancel`,
      payload,
    )
  },
}