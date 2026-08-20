export type PurchaseStatus =
  | 'PENDING'
  | 'RECEIVED'
  | 'CANCELLED'

export interface Purchase {
  id: number
  supplier_id: number

  invoice_number: string
  invoice_series: string | null

  issue_date: string
  received_at: string | null

  notes: string | null

  created_by: number
  created_at: string
  updated_at: string

  status: PurchaseStatus
}

export interface PurchaseItem {
  id: number
  purchase_id: number
  part_id: number

  quantity_purchased: number
  quantity_available: number

  created_at: string
}

export interface PurchaseCreatePayload {
  supplier_id: number
  invoice_number: string
  invoice_series?: string | null
  issue_date: string
  status?: PurchaseStatus
  notes?: string | null
}

export interface PurchaseUpdatePayload {
  supplier_id?: number
  invoice_number?: string
  invoice_series?: string | null
  issue_date?: string
  status?: PurchaseStatus
  notes?: string | null
}

export interface PurchaseCancelPayload {
  justification: string
}

export interface PurchaseItemCreatePayload {
  part_id: number
  quantity_purchased: number
}

export interface PurchaseFormValues {
  supplier_id: number
  invoice_number: string
  invoice_series: string | null
  issue_date: string
  notes: string | null
}