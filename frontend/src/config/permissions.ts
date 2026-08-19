import {
  ROLE_NAMES,
  type SystemRoleName,
} from '../types/auth'

export type PermissionKey =
  | 'dashboard'
  | 'purchases'
  | 'outbounds'
  | 'customerReturns'
  | 'supplierReturns'
  | 'transfers'
  | 'parts'
  | 'suppliers'
  | 'users'
  | 'purchaseTracking'
  | 'audit'

const ALL_OPERATIONAL_ROLES:
  readonly SystemRoleName[] = [
    ROLE_NAMES.admin,
    ROLE_NAMES.buyer,
    ROLE_NAMES.seller,
  ]

const ADMIN_AND_BUYER:
  readonly SystemRoleName[] = [
    ROLE_NAMES.admin,
    ROLE_NAMES.buyer,
  ]

const ADMIN_AND_SELLER:
  readonly SystemRoleName[] = [
    ROLE_NAMES.admin,
    ROLE_NAMES.seller,
  ]

const ADMIN_ONLY:
  readonly SystemRoleName[] = [
    ROLE_NAMES.admin,
  ]

export const PERMISSIONS: Record<
  PermissionKey,
  readonly SystemRoleName[]
> = {
  dashboard:
    ALL_OPERATIONAL_ROLES,

  purchases:
    ADMIN_AND_BUYER,

  outbounds:
    ADMIN_AND_SELLER,

  customerReturns:
    ALL_OPERATIONAL_ROLES,

  supplierReturns:
    ADMIN_AND_BUYER,

  transfers:
    ADMIN_AND_BUYER,

  parts:
    ADMIN_AND_BUYER,

  suppliers:
    ADMIN_AND_BUYER,

  users:
    ADMIN_ONLY,

  purchaseTracking:
    ADMIN_AND_BUYER,

  audit:
    ADMIN_ONLY,
}

const SYSTEM_ROLE_NAMES =
  Object.values(
    ROLE_NAMES,
  ) as SystemRoleName[]

export function isSystemRoleName(
  roleName: string,
): roleName is SystemRoleName {
  return SYSTEM_ROLE_NAMES.includes(
    roleName as SystemRoleName,
  )
}

export function hasPermission(
  roleName: string | null | undefined,
  permission: PermissionKey,
): boolean {
  if (
    !roleName ||
    !isSystemRoleName(roleName)
  ) {
    return false
  }

  return PERMISSIONS[
    permission
  ].includes(roleName)
}