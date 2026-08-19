import {
  ArrowLeft,
  ShieldAlert,
} from 'lucide-react'
import {
  useNavigate,
} from 'react-router'

import {
  Button,
} from '../components/ui/Button'
import {
  Card,
} from '../components/ui/Card'

export function AccessDeniedPage() {
  const navigate =
    useNavigate()

  return (
    <div className="access-denied-page">
      <Card
        className="access-denied-card"
        padding="lg"
      >
        <div className="access-denied-card__icon">
          <ShieldAlert
            size={30}
            strokeWidth={1.7}
          />
        </div>

        <div className="access-denied-card__content">
          <span className="access-denied-card__eyebrow">
            Acesso restrito
          </span>

          <h1>
            Você não possui acesso
            a este módulo.
          </h1>

          <p>
            Seu perfil atual não possui
            permissão para visualizar esta
            área do SIGC.
          </p>

          <Button
            variant="secondary"
            onClick={() => {
              navigate(
                '/',
                {
                  replace: true,
                },
              )
            }}
          >
            <ArrowLeft
              size={16}
              strokeWidth={1.8}
            />

            Voltar ao Dashboard
          </Button>
        </div>
      </Card>
    </div>
  )
}