import { env } from '../config/env'

export function DashboardPage() {
  return (
    <section>
      <h1>SIGC</h1>

      <p>
        Fundação técnica do frontend
        configurada com sucesso.
      </p>

      <dl className="technical-info">
        <div>
          <dt>Frontend</dt>
          <dd>
            React + TypeScript + Vite
          </dd>
        </div>

        <div>
          <dt>API configurada</dt>
          <dd>
            {env.apiBaseUrl}
          </dd>
        </div>
      </dl>

      <p className="temporary-notice">
        Esta não é a interface definitiva
        do Dashboard.
      </p>
    </section>
  )
}