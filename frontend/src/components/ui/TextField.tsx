import type {
  InputHTMLAttributes,
} from 'react'

interface TextFieldProps
  extends InputHTMLAttributes<HTMLInputElement> {
  label: string
  error?: string | null
  hint?: string
}

export function TextField({
  label,
  error,
  hint,
  id,
  className = '',
  ...props
}: TextFieldProps) {
  const inputId =
    id ?? props.name

  const descriptionId =
    error
      ? `${inputId}-error`
      : hint
        ? `${inputId}-hint`
        : undefined

  return (
    <label
      className={[
        'ui-field',
        className,
      ]
        .filter(Boolean)
        .join(' ')}
      htmlFor={inputId}
    >
      <span className="ui-field__label">
        {label}
      </span>

      <input
        {...props}
        id={inputId}
        className={[
          'ui-field__input',
          error
            ? 'ui-field__input--error'
            : '',
        ]
          .filter(Boolean)
          .join(' ')}
        aria-invalid={
          error
            ? true
            : undefined
        }
        aria-describedby={
          descriptionId
        }
      />

      {error ? (
        <span
          id={descriptionId}
          className="ui-field__error"
        >
          {error}
        </span>
      ) : hint ? (
        <span
          id={descriptionId}
          className="ui-field__hint"
        >
          {hint}
        </span>
      ) : null}
    </label>
  )
}