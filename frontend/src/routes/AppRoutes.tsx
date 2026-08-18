import {
  Route,
  Routes,
} from 'react-router'

import { AppLayout } from '../layouts/AppLayout'
import { DashboardPage } from '../pages/DashboardPage'
import { LoginPage } from '../pages/LoginPage'
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
              <DashboardPage />
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