import {
  Boxes,
  FileClock,
  Gauge,
  PackageCheck,
  PanelLeftClose,
  PanelLeftOpen,
  RefreshCcw,
  Repeat2,
  ShieldCheck,
  ShoppingCart,
  Truck,
  Users,
  Warehouse,
  type LucideIcon,
} from 'lucide-react'
import {
  NavLink,
} from 'react-router'

import sigcMark from '../../assets/brand/sigc-mark-inverse.png'
import {
  hasPermission,
  type PermissionKey,
} from '../../config/permissions'
import { useAuth } from '../../hooks/useAuth'
import {
  IconButton,
} from '../ui/IconButton'

interface SidebarProps {
  collapsed: boolean
  onToggle(): void
}

interface NavigationItem {
  label: string
  path: string
  icon: LucideIcon
  permission: PermissionKey
}

interface NavigationGroup {
  label: string
  items: NavigationItem[]
}

const navigationGroups:
  NavigationGroup[] = [
    {
      label: 'Visão geral',
      items: [
        {
          label: 'Dashboard',
          path: '/',
          icon: Gauge,
          permission:
            'dashboard',
        },
      ],
    },
    {
      label: 'Operações',
      items: [
        {
          label: 'Compras',
          path: '/compras',
          icon: ShoppingCart,
          permission:
            'purchases',
        },
        {
          label: 'Saídas',
          path: '/saidas',
          icon: PackageCheck,
          permission:
            'outbounds',
        },
        {
          label:
            'Devoluções de clientes',
          path:
            '/devolucoes-clientes',
          icon: RefreshCcw,
          permission:
            'customerReturns',
        },
        {
          label:
            'Remessas ao fornecedor',
          path:
            '/devolucoes-fornecedores',
          icon: Truck,
          permission:
            'supplierReturns',
        },
        {
          label: 'Transferências',
          path: '/transferencias',
          icon: Repeat2,
          permission:
            'transfers',
        },
      ],
    },
    {
      label: 'Cadastros',
      items: [
        {
          label: 'Peças',
          path: '/pecas',
          icon: Boxes,
          permission:
            'parts',
        },
        {
          label: 'Fornecedores',
          path: '/fornecedores',
          icon: Warehouse,
          permission:
            'suppliers',
        },
        {
          label: 'Usuários',
          path: '/usuarios',
          icon: Users,
          permission:
            'users',
        },
      ],
    },
    {
      label: 'Controle',
      items: [
        {
          label: 'Acompanhamento',
          path: '/acompanhamento',
          icon: FileClock,
          permission:
            'purchaseTracking',
        },
        {
          label: 'Auditoria',
          path: '/auditoria',
          icon: ShieldCheck,
          permission:
            'audit',
        },
      ],
    },
  ]

export function Sidebar({
  collapsed,
  onToggle,
}: SidebarProps) {
  const {
    session,
  } = useAuth()

  const roleName =
    session?.role_name

  const visibleGroups =
    navigationGroups
      .map((group) => ({
        ...group,

        items:
          group.items.filter(
            (item) =>
              hasPermission(
                roleName,
                item.permission,
              ),
          ),
      }))
      .filter(
        (group) =>
          group.items.length > 0,
      )

  return (
    <aside
      className={[
        'app-sidebar',
        collapsed
          ? 'app-sidebar--collapsed'
          : '',
      ]
        .filter(Boolean)
        .join(' ')}
    >
      <div className="app-sidebar__brand">
        <div
          className="app-sidebar__brand-mark"
          aria-hidden="true"
        >
          <img
            src={sigcMark}
            alt=""
          />
        </div>

        {!collapsed && (
          <div className="app-sidebar__brand-copy">
            <strong>
              SIGC
            </strong>

            <span>
              Gestão de Cascos
            </span>
          </div>
        )}

        <IconButton
          className="app-sidebar__toggle"
          label={
            collapsed
              ? 'Expandir menu'
              : 'Recolher menu'
          }
          onClick={onToggle}
        >
          {collapsed ? (
            <PanelLeftOpen
              size={18}
            />
          ) : (
            <PanelLeftClose
              size={18}
            />
          )}
        </IconButton>
      </div>

      <nav
        className="app-sidebar__navigation"
        aria-label="Navegação principal"
      >
        {visibleGroups.map(
          (group) => (
            <div
              className="app-sidebar__group"
              key={group.label}
            >
              {!collapsed && (
                <span className="app-sidebar__group-label">
                  {group.label}
                </span>
              )}

              <div className="app-sidebar__items">
                {group.items.map(
                  (item) => {
                    const Icon =
                      item.icon

                    return (
                      <NavLink
                        key={item.path}
                        to={item.path}
                        end={
                          item.path === '/'
                        }
                        title={
                          collapsed
                            ? item.label
                            : undefined
                        }
                        className={({
                          isActive,
                        }) => [
                          'app-sidebar__link',
                          isActive
                            ? 'app-sidebar__link--active'
                            : '',
                        ]
                          .filter(Boolean)
                          .join(' ')
                        }
                      >
                        <Icon
                          size={19}
                          strokeWidth={1.8}
                        />

                        {!collapsed && (
                          <span>
                            {item.label}
                          </span>
                        )}
                      </NavLink>
                    )
                  },
                )}
              </div>
            </div>
          ),
        )}
      </nav>

      <div className="app-sidebar__footer">
        {!collapsed && (
          <>
            <span>
              Sistema interno
            </span>

            <small>
              Ambiente de desenvolvimento
            </small>
          </>
        )}
      </div>
    </aside>
  )
}