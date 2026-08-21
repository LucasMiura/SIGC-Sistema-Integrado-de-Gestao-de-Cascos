import {
  Route,
  Routes,
} from 'react-router'

import { AppLayout } from '../layouts/AppLayout'
import {
  AccessDeniedPage,
} from '../pages/AccessDeniedPage'
import { DashboardPage } from '../pages/DashboardPage'
import { LoginPage } from '../pages/LoginPage'
import {
  SuppliersPage,
} from '../pages/SuppliersPage'
import {
  PartsPage,
} from '../pages/PartsPage'
import {
  PurchasesPage,
} from '../pages/PurchasesPage'
import {
  ModulePlaceholderPage,
} from '../pages/ModulePlaceholderPage'
import { NotFoundPage } from '../pages/NotFoundPage'
import {
  OutboundsPage,
} from '../pages/OutboundsPage'
import { ProtectedRoute } from './ProtectedRoute'
import { PublicOnlyRoute } from './PublicOnlyRoute'
import {
  RoleProtectedRoute,
} from './RoleProtectedRoute'

export function AppRoutes() {
  return (
    <Routes>
      <Route
        path="/login"
        element={
          <PublicOnlyRoute>
            <LoginPage />
          </PublicOnlyRoute>
        }
      />

      <Route
        element={
          <ProtectedRoute />
        }
      >
        <Route
          element={
            <AppLayout />
          }
        >
          <Route
            index
            element={
              <RoleProtectedRoute
                permission="dashboard"
              >
                <DashboardPage />
              </RoleProtectedRoute>
            }
          />

          <Route
            path="acesso-negado"
            element={
              <AccessDeniedPage />
            }
          />

          <Route
            path="compras"
            element={
              <RoleProtectedRoute
                permission="purchases"
              >
                <PurchasesPage />
              </RoleProtectedRoute>
            }
          />

          <Route
            path="saidas"
            element={
              <RoleProtectedRoute
                permission="outbounds"
              >
                <OutboundsPage />
              </RoleProtectedRoute>
            }
          />

          <Route
            path="devolucoes-clientes"
            element={
              <RoleProtectedRoute
                permission="customerReturns"
              >
                <ModulePlaceholderPage
                  title="Devoluções de clientes"
                  description="Acompanhe devoluções totais e parciais vinculadas às saídas realizadas."
                />
              </RoleProtectedRoute>
            }
          />

          <Route
            path="devolucoes-fornecedores"
            element={
              <RoleProtectedRoute
                permission="supplierReturns"
              >
                <ModulePlaceholderPage
                  title="Remessas ao fornecedor"
                  description="Controle as devoluções de cascos aos fornecedores e seus respectivos saldos."
                />
              </RoleProtectedRoute>
            }
          />

          <Route
            path="transferencias"
            element={
              <RoleProtectedRoute
                permission="transfers"
              >
                <ModulePlaceholderPage
                  title="Transferências"
                  description="Gerencie movimentações entre filiais preservando a responsabilidade pela origem."
                />
              </RoleProtectedRoute>
            }
          />

          <Route
            path="pecas"
            element={
              <RoleProtectedRoute
                permission="parts"
              >
                <PartsPage />
              </RoleProtectedRoute>
            }
          />

          <Route
            path="fornecedores"
            element={
              <RoleProtectedRoute
                permission="suppliers"
              >
                <SuppliersPage />
              </RoleProtectedRoute>
            }
          />

          <Route
            path="usuarios"
            element={
              <RoleProtectedRoute
                permission="users"
              >
                <ModulePlaceholderPage
                  title="Usuários"
                  description="Gerencie acessos, perfis e status dos usuários do SIGC."
                />
              </RoleProtectedRoute>
            }
          />

          <Route
            path="acompanhamento"
            element={
              <RoleProtectedRoute
                permission="purchaseTracking"
              >
                <ModulePlaceholderPage
                  title="Acompanhamento"
                  description="Consulte o ciclo completo das compras e os saldos relacionados às devoluções."
                />
              </RoleProtectedRoute>
            }
          />

          <Route
            path="auditoria"
            element={
              <RoleProtectedRoute
                permission="audit"
              >
                <ModulePlaceholderPage
                  title="Auditoria"
                  description="Consulte o histórico permanente das operações relevantes realizadas no sistema."
                />
              </RoleProtectedRoute>
            }
          />

          <Route
            path="*"
            element={
              <NotFoundPage />
            }
          />
        </Route>
      </Route>
    </Routes>
  )
}