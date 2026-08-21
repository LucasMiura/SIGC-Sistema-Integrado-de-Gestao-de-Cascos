export type OutboundStatus =
  | 'ACTIVE'
  | 'CANCELLED'

export type OutboundDestinationType =
  | 'WORK_ORDER'
  | 'SALE'

export interface Outbound {
  id: number

  destination_type:
    OutboundDestinationType

  work_order_number:
    string | null

  sales_invoice_number:
    string | null

  customer_name: string

  created_by: number

  created_at: string
  updated_at: string

  status: OutboundStatus
}

export interface OutboundItem {
  id: number
  outbound_id: number
  part_id: number
  quantity: number
  created_at: string
}

export interface OutboundCreatePayload {
  destination_type:
    OutboundDestinationType

  work_order_number?:
    string | null

  sales_invoice_number?:
    string | null

  customer_name: string

  status?: OutboundStatus
}

export interface OutboundUpdatePayload {
  destination_type?:
    OutboundDestinationType

  work_order_number?:
    string | null

  sales_invoice_number?:
    string | null

  customer_name?: string

  status?: OutboundStatus
}

export interface OutboundCancelPayload {
  justification: string
}

export interface OutboundItemCreatePayload {
  part_id: number
  quantity: number
}

export interface OutboundFormValues {
  destination_type:
    OutboundDestinationType

  reference_number: string
  customer_name: string
}