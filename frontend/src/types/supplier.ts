export interface Supplier {
  id: number

  name: string
  document: string | null
  address: string | null
  notes: string | null

  is_active: boolean

  created_at: string
  updated_at: string
}

export interface SupplierCreatePayload {
  name: string
  document?: string | null
  address?: string | null
  notes?: string | null
}

export interface SupplierUpdatePayload {
  name?: string
  document?: string | null
  address?: string | null
  notes?: string | null
}

export interface SupplierDeactivatePayload {
  justification: string
}