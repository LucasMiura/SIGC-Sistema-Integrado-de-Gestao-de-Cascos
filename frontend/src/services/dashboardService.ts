import { httpClient } from './httpClient'
import type {
  DashboardSummary,
} from '../types/dashboard'

export interface DashboardFilters {
  supplierId?: number
  partId?: number
  originType?: 'PURCHASE' | 'TRANSFER'
  deadlineStatus?:
    | 'NORMAL'
    | 'ATTENTION'
    | 'URGENT'
    | 'OVERDUE'
  dateFrom?: string
  dateTo?: string
}

function buildDashboardQuery(
  filters: DashboardFilters,
): string {
  const params =
    new URLSearchParams()

  if (filters.supplierId) {
    params.set(
      'supplier_id',
      String(filters.supplierId),
    )
  }

  if (filters.partId) {
    params.set(
      'part_id',
      String(filters.partId),
    )
  }

  if (filters.originType) {
    params.set(
      'origin_type',
      filters.originType,
    )
  }

  if (filters.deadlineStatus) {
    params.set(
      'deadline_status',
      filters.deadlineStatus,
    )
  }

  if (filters.dateFrom) {
    params.set(
      'date_from',
      filters.dateFrom,
    )
  }

  if (filters.dateTo) {
    params.set(
      'date_to',
      filters.dateTo,
    )
  }

  const query =
    params.toString()

  return query
    ? `/dashboard?${query}`
    : '/dashboard'
}

export const dashboardService = {
  getSummary(
    filters: DashboardFilters = {},
  ): Promise<DashboardSummary> {
    return httpClient.get<
      DashboardSummary
    >(
      buildDashboardQuery(
        filters,
      ),
    )
  },
}