import {
  Route,
  Routes,
} from 'react-router'

import { AppLayout } from '../layouts/AppLayout'
import { DashboardPage } from '../pages/DashboardPage'
import { LoginPage } from '../pages/LoginPage'
import {
  ModulePlaceholderPage,
} from '../pages/ModulePlaceholderPage'
import { NotFoundPage } from '../pages/NotFoundPage'
import { ProtectedRoute } from './ProtectedRoute'
import { PublicOnlyRoute } from './PublicOnlyRoute'

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
        element={<ProtectedRoute />}
      >
        <Route
          element={<AppLayout />}
        >
          <Route
            index
            element={<DashboardPage />}
          />

          <Route
            path="compras"
            element={
              <ModulePlaceholderPage
                title="Compras"
                description="Gerencie as Notas Fiscais de compra e os itens com obrigação de devolução de casco."
              />
            }
          />

          <Route
            path="saidas"
            element={
              <ModulePlaceholderPage
                title="Saídas"
                description="Registre movimentações para oficina e balcão mantendo a rastreabilidade de origem."
              />
            }
          />

          <Route
            path="devolucoes-clientes"
            element={
              <ModulePlaceholderPage
                title="Devoluções de clientes"
                description="Acompanhe devoluções totais e parciais vinculadas às saídas realizadas."
              />
            }
          />

          <Route
            path="devolucoes-fornecedores"
            element={
              <ModulePlaceholderPage
                title="Remessas ao fornecedor"
                description="Controle as devoluções de cascos aos fornecedores e seus respectivos saldos."
              />
            }
          />

          <Route
            path="transferencias"
            element={
              <ModulePlaceholderPage
                title="Transferências"
                description="Gerencie movimentações entre filiais preservando a responsabilidade pela origem."
              />
            }
          />

          <Route
            path="pecas"
            element={
              <ModulePlaceholderPage
                title="Peças"
                description="Mantenha o cadastro das peças sujeitas ao controle de casco."
              />
            }
          />

          <Route
            path="fornecedores"
            element={
              <ModulePlaceholderPage
                title="Fornecedores"
                description="Gerencie fornecedores e seus respectivos contatos."
              />
            }
          />

          <Route
            path="usuarios"
            element={
              <ModulePlaceholderPage
                title="Usuários"
                description="Gerencie acessos, perfis e status dos usuários do SIGC."
              />
            }
          />

          <Route
            path="acompanhamento"
            element={
              <ModulePlaceholderPage
                title="Acompanhamento"
                description="Consulte o ciclo completo das compras e os saldos relacionados às devoluções."
              />
            }
          />

          <Route
            path="auditoria"
            element={
              <ModulePlaceholderPage
                title="Auditoria"
                description="Consulte o histórico permanente das operações relevantes realizadas no sistema."
              />
            }
          />

          <Route
            path="*"
            element={<NotFoundPage />}
          />
        </Route>
      </Route>
    </Routes>
  )
}