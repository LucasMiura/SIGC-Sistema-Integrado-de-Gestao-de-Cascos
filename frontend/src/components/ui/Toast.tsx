import {
  CheckCircle2,
  Info,
  X,
} from 'lucide-react'
import {
  useEffect,
} from 'react'

interface ToastProps {
  message: string

  tone?:
    | 'success'
    | 'info'

  duration?: number

  onClose(): void
}

export function Toast({
  message,
  tone = 'success',
  duration = 4000,
  onClose,
}: ToastProps) {
  useEffect(
    () => {
      const timeoutId =
        window.setTimeout(
          onClose,
          duration,
        )

      return () => {
        window.clearTimeout(
          timeoutId,
        )
      }
    },
    [
      duration,
      onClose,
    ],
  )

  const Icon =
    tone === 'success'
      ? CheckCircle2
      : Info

  return (
    <div
      className={[
        'ui-toast',
        `ui-toast--${tone}`,
      ].join(' ')}
      role="status"
      aria-live="polite"
    >
      <div className="ui-toast__icon">
        <Icon
          size={20}
          strokeWidth={2}
        />
      </div>

      <span>
        {message}
      </span>

      <button
        type="button"
        className="ui-toast__close"
        aria-label="Fechar notificação"
        onClick={onClose}
      >
        <X
          size={17}
        />
      </button>
    </div>
  )
}