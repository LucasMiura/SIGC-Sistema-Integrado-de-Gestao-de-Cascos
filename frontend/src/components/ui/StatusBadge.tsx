import type {
  ReactNode,
} from 'react'

export type StatusBadgeTone =
  | 'neutral'
  | 'success'
  | 'info'
  | 'attention'
  | 'urgent'
  | 'overdue'

interface StatusBadgeProps {
  children: ReactNode
  tone?: StatusBadgeTone
}

export function StatusBadge({
  children,
  tone = 'neutral',
}: StatusBadgeProps) {
  return (
    <span
      className={[
        'ui-status-badge',
        `ui-status-badge--${tone}`,
      ].join(' ')}
    >
      <span
        className="ui-status-badge__dot"
        aria-hidden="true"
      />

      {children}
    </span>
  )
}