export interface SupplierContact {
  id: number
  supplier_id: number

  name: string
  email: string | null
  phone: string | null
  position: string | null

  is_primary: boolean
  is_active: boolean

  created_at: string
}

export interface SupplierContactCreatePayload {
  name: string
  email?: string | null
  phone?: string | null
  position?: string | null
  is_primary: boolean
}

export interface SupplierContactUpdatePayload {
  name?: string
  email?: string | null
  phone?: string | null
  position?: string | null
  is_primary?: boolean
}

export interface SupplierContactDeactivatePayload {
  justification: string
}