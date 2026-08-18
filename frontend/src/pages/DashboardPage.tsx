import { env } from '../config/env'
import { useAuth } from '../hooks/useAuth'

export function DashboardPage() {
  const {
    session,
  } = useAuth()

  return (
    <section>
      <h1>
        Dashboard
      </h1>

      <p>
        Autenticação do frontend
        configurada com sucesso.
      </p>

      {session && (
        <dl className="technical-info">
          <div>
            <dt>
              Usuário
            </dt>

            <dd>
              {session.user.full_name}
            </dd>
          </div>

          <div>
            <dt>
              Perfil
            </dt>

            <dd>
              {session.role_name}
            </dd>
          </div>

          <div>
            <dt>
              API
            </dt>

            <dd>
              {env.apiBaseUrl}
            </dd>
          </div>
        </dl>
      )}

      <p className="temporary-notice">
        Este ainda não é o Dashboard
        definitivo do SIGC.
      </p>
    </section>
  )
}