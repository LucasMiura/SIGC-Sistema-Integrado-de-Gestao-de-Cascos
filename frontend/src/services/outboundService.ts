import {
  httpClient,
} from './httpClient'

import type {
  Outbound,
  OutboundCancelPayload,
  OutboundCreatePayload,
  OutboundItem,
  OutboundItemCreatePayload,
  OutboundUpdatePayload,
} from '../types/outbound'

export const outboundService = {
  list(): Promise<Outbound[]> {
    return httpClient.get<
      Outbound[]
    >(
      '/outbounds',
    )
  },

  getById(
    outboundId: number,
  ): Promise<Outbound> {
    return httpClient.get<
      Outbound
    >(
      `/outbounds/${outboundId}`,
    )
  },

  create(
    payload:
      OutboundCreatePayload,
  ): Promise<Outbound> {
    return httpClient.post<
      Outbound
    >(
      '/outbounds',
      payload,
    )
  },

  update(
    outboundId: number,
    payload:
      OutboundUpdatePayload,
  ): Promise<Outbound> {
    return httpClient.patch<
      Outbound
    >(
      `/outbounds/${outboundId}`,
      payload,
    )
  },

  cancel(
    outboundId: number,
    payload:
      OutboundCancelPayload,
  ): Promise<Outbound> {
    return httpClient.patch<
      Outbound
    >(
      `/outbounds/${outboundId}/cancel`,
      payload,
    )
  },

  listItems(
    outboundId: number,
  ): Promise<OutboundItem[]> {
    return httpClient.get<
      OutboundItem[]
    >(
      `/outbounds/${outboundId}/items`,
    )
  },

  addItem(
    outboundId: number,
    payload:
      OutboundItemCreatePayload,
  ): Promise<OutboundItem> {
    return httpClient.post<
      OutboundItem
    >(
      `/outbounds/${outboundId}/items`,
      payload,
    )
  },
}