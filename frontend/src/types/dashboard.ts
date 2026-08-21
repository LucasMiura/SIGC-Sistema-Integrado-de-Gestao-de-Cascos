export interface DashboardDeadlineIndicators {
  normal_quantity: number
  attention_quantity: number
  urgent_quantity: number
  overdue_quantity: number
}

export interface DashboardCustomerReturnIndicators {
  outbound_quantity: number
  returned_quantity: number
  pending_quantity: number

  pending_origin_count: number
  partial_origin_count: number
  completed_origin_count: number
}

export interface DashboardSupplierReturnIndicators {
  available_quantity: number
  returned_quantity: number
  pending_quantity: number
}

export interface DashboardTransferReturnIndicators {
  available_quantity: number
  returned_quantity: number
  pending_quantity: number
}

export interface DashboardStockPositionItem {
  part_id: number
  part_code: string
  part_name: string

  stock_quantity: number

  workshop_pending_quantity: number
  customer_pending_quantity: number

  workshop_returned_quantity: number
  customer_returned_quantity: number

  available_core_quantity: number
}

export interface DashboardSummary {
  total_origin_count: number
  total_available_quantity: number

  deadline: DashboardDeadlineIndicators

  customer_returns:
    DashboardCustomerReturnIndicators

  supplier_returns:
    DashboardSupplierReturnIndicators

  transfer_returns:
    DashboardTransferReturnIndicators
}