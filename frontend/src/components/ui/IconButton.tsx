import type {
  ButtonHTMLAttributes,
  ReactNode,
} from 'react'

interface IconButtonProps
  extends ButtonHTMLAttributes<HTMLButtonElement> {
  children: ReactNode
  label: string
}

export function IconButton({
  children,
  label,
  className = '',
  type = 'button',
  ...props
}: IconButtonProps) {
  return (
    <button
      type={type}
      className={[
        'ui-icon-button',
        className,
      ]
        .filter(Boolean)
        .join(' ')}
      aria-label={label}
      title={label}
      {...props}
    >
      {children}
    </button>
  )
}