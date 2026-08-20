export interface Part {
  id: number

  supplier_id: number
  part_code: string
  name: string
  description: string | null
  return_deadline_days: number

  is_active: boolean

  created_at: string
  updated_at: string
}

export interface PartCreatePayload {
  supplier_id: number
  part_code: string
  name: string
  description?: string | null
  return_deadline_days: number
}

export interface PartUpdatePayload {
  supplier_id?: number
  part_code?: string
  name?: string
  description?: string | null
  return_deadline_days?: number
}

export interface PartDeactivatePayload {
  justification: string
}

export interface PartFormValues {
  supplier_id: number
  part_code: string
  name: string
  description: string | null
  return_deadline_days: number
}