import type {
  ReactNode,
} from 'react'

interface PageHeaderProps {
  title: string
  description?: string
  eyebrow?: string
  actions?: ReactNode
}

export function PageHeader({
  title,
  description,
  eyebrow,
  actions,
}: PageHeaderProps) {
  return (
    <header className="ui-page-header">
      <div className="ui-page-header__content">
        {eyebrow && (
          <span className="ui-page-header__eyebrow">
            {eyebrow}
          </span>
        )}

        <h1 className="ui-page-header__title">
          {title}
        </h1>

        {description && (
          <p className="ui-page-header__description">
            {description}
          </p>
        )}
      </div>

      {actions && (
        <div className="ui-page-header__actions">
          {actions}
        </div>
      )}
    </header>
  )
}