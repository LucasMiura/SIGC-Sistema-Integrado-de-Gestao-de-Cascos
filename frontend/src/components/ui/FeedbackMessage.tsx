import {
  AlertCircle,
  CheckCircle2,
  Info,
  TriangleAlert,
} from 'lucide-react'

interface FeedbackMessageProps {
  message: string

  tone?:
    | 'error'
    | 'success'
    | 'warning'
    | 'info'
}

export function FeedbackMessage({
  message,
  tone = 'error',
}: FeedbackMessageProps) {
  const Icon =
    tone === 'success'
      ? CheckCircle2
      : tone === 'warning'
        ? TriangleAlert
        : tone === 'info'
          ? Info
          : AlertCircle

  return (
    <div
      className={[
        'ui-feedback',
        `ui-feedback--${tone}`,
      ].join(' ')}
      role={
        tone === 'error'
          ? 'alert'
          : 'status'
      }
    >
      <div className="ui-feedback__icon">
        <Icon
          size={19}
          strokeWidth={2}
        />
      </div>

      <div className="ui-feedback__content">
        <strong>
          {tone === 'error'
            ? 'Não foi possível concluir'
            : tone === 'warning'
              ? 'Atenção'
              : tone === 'success'
                ? 'Operação concluída'
                : 'Informação'}
        </strong>

        <span>
          {message}
        </span>
      </div>
    </div>
  )
}