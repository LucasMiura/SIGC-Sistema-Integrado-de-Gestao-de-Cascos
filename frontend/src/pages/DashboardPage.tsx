import {
  ArrowRight,
  CheckCircle2,
  Clock3,
  ShieldCheck,
  Sparkles,
} from 'lucide-react'

import {
  Button,
} from '../components/ui/Button'
import {
  Card,
} from '../components/ui/Card'
import {
  PageHeader,
} from '../components/ui/PageHeader'
import {
  StatusBadge,
} from '../components/ui/StatusBadge'
import { useAuth } from '../hooks/useAuth'

export function DashboardPage() {
  const {
    session,
  } = useAuth()

  const firstName =
    session?.user.full_name
      .trim()
      .split(' ')[0]
    ?? 'Usuário'

  return (
    <div className="page-stack">
      <PageHeader
        eyebrow="Visão geral"
        title={`Olá, ${firstName}.`}
        description={
          'A base visual do SIGC está pronta para receber os indicadores operacionais reais.'
        }
        actions={
          <Button
            variant="secondary"
          >
            Ver acompanhamento
            <ArrowRight size={16} />
          </Button>
        }
      />

      <section
        className="dashboard-welcome"
        aria-label="Apresentação do novo ambiente"
      >
        <div className="dashboard-welcome__content">
          <span className="dashboard-welcome__eyebrow">
            <Sparkles size={15} />
            Nova experiência SIGC
          </span>

          <h2>
            Operação clara.
            Informação no lugar certo.
          </h2>

          <p>
            O frontend agora utiliza uma base
            visual própria, preparada para
            transformar os fluxos de cascos em
            uma experiência rápida, organizada
            e previsível.
          </p>
        </div>

        <div
          className="dashboard-welcome__visual"
          aria-hidden="true"
        >
          <div className="dashboard-welcome__orb dashboard-welcome__orb--one" />
          <div className="dashboard-welcome__orb dashboard-welcome__orb--two" />

          <div className="dashboard-welcome__symbol">
            SIGC
          </div>
        </div>
      </section>

      <section className="dashboard-preview-grid">
        <Card padding="md">
          <div className="preview-card">
            <div className="preview-card__icon">
              <CheckCircle2 size={20} />
            </div>

            <div>
              <span className="preview-card__label">
                Sessão
              </span>

              <strong>
                Autenticada
              </strong>

              <StatusBadge tone="success">
                Ativa
              </StatusBadge>
            </div>
          </div>
        </Card>

        <Card padding="md">
          <div className="preview-card">
            <div className="preview-card__icon">
              <ShieldCheck size={20} />
            </div>

            <div>
              <span className="preview-card__label">
                Perfil atual
              </span>

              <strong>
                {session?.role_name}
              </strong>

              <StatusBadge tone="info">
                Autorização ativa
              </StatusBadge>
            </div>
          </div>
        </Card>

        <Card padding="md">
          <div className="preview-card">
            <div className="preview-card__icon">
              <Clock3 size={20} />
            </div>

            <div>
              <span className="preview-card__label">
                Prazos
              </span>

              <strong>
                Design preparado
              </strong>

              <StatusBadge tone="attention">
                Atenção
              </StatusBadge>
            </div>
          </div>
        </Card>
      </section>

      <section>
        <div className="section-heading">
          <div>
            <span>
              Linguagem de status
            </span>

            <h2>
              Alertas claros sem depender
              apenas de cor
            </h2>
          </div>
        </div>

        <Card padding="lg">
          <div className="status-preview">
            <StatusBadge tone="success">
              Normal
            </StatusBadge>

            <StatusBadge tone="attention">
              Atenção
            </StatusBadge>

            <StatusBadge tone="urgent">
              Urgente
            </StatusBadge>

            <StatusBadge tone="overdue">
              Atrasado
            </StatusBadge>
          </div>
        </Card>
      </section>
    </div>
  )
}