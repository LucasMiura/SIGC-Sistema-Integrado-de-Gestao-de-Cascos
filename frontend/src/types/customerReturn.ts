export type CustomerReturnType =
  | 'WORK_ORDER'
  | 'SALE'

export type CustomerReturnStatus =
  | 'ACTIVE'
  | 'CANCELLED'

export interface CustomerReturn {
  id: number

  return_type: CustomerReturnType
  reference_number: string
  customer_name: string

  created_by: number
  created_at: string
  updated_at: string

  status: CustomerReturnStatus

  notes: string | null
}

export interface CustomerReturnItem {
  id: number
  customer_return_id: number
  part_id: number
  quantity: number
  created_at: string
}

export interface CustomerReturnOriginItem {
  part_id: number
  part_code: string
  part_name: string

  outbound_quantity: number
  returned_quantity: number
  pending_quantity: number
}

export interface CustomerReturnOrigin {
  outbound_id: number

  return_type: CustomerReturnType
  reference_number: string
  customer_name: string

  items: CustomerReturnOriginItem[]

  total_outbound_quantity: number
  total_returned_quantity: number
  total_pending_quantity: number
}

export interface CustomerReturnCreatePayload {
  return_type: CustomerReturnType
  reference_number: string
  customer_name: string
  status?: CustomerReturnStatus
  notes?: string | null
}

export interface CustomerReturnItemCreatePayload {
  part_id: number
  quantity: number
}

export interface CustomerReturnCancelPayload {
  justification: string
}