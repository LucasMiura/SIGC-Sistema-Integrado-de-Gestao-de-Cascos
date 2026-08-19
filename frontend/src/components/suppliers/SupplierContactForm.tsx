import {
  useState,
  type FormEvent,
} from 'react'

import {
  Button,
} from '../ui/Button'
import {
  TextField,
} from '../ui/TextField'
import type {
  SupplierContact,
  SupplierContactCreatePayload,
} from '../../types/supplierContact'

interface SupplierContactFormProps {
  contact?: SupplierContact | null
  isSubmitting: boolean
  errorMessage?: string | null

  onCancel(): void

  onSubmit(
    payload:
      SupplierContactCreatePayload,
  ): Promise<void>
}

function normalizeOptionalValue(
  value: string,
): string | null {
  const normalized =
    value.trim()

  return normalized || null
}

export function SupplierContactForm({
  contact = null,
  isSubmitting,
  errorMessage = null,
  onCancel,
  onSubmit,
}: SupplierContactFormProps) {
  const [
    name,
    setName,
  ] = useState(
    contact?.name ?? '',
  )

  const [
    email,
    setEmail,
  ] = useState(
    contact?.email ?? '',
  )

  const [
    phone,
    setPhone,
  ] = useState(
    contact?.phone ?? '',
  )

  const [
    position,
    setPosition,
  ] = useState(
    contact?.position ?? '',
  )

  const [
    isPrimary,
    setIsPrimary,
  ] = useState(
    contact?.is_primary ?? false,
  )

  async function handleSubmit(
    event: FormEvent<HTMLFormElement>,
  ) {
    event.preventDefault()

    if (isSubmitting) {
      return
    }

    const normalizedName =
      name.trim()

    if (!normalizedName) {
      return
    }

    await onSubmit({
      name: normalizedName,

      email:
        normalizeOptionalValue(
          email,
        ),

      phone:
        normalizeOptionalValue(
          phone,
        ),

      position:
        normalizeOptionalValue(
          position,
        ),

      is_primary:
        isPrimary,
    })
  }

  return (
    <form
      className="supplier-contact-form"
      onSubmit={handleSubmit}
    >
      <header className="supplier-contact-form__header">
        <span>
          Contato
        </span>

        <h3>
          {contact
            ? 'Editar contato'
            : 'Novo contato'}
        </h3>

        <p>
          {contact
            ? 'Atualize as informações deste contato.'
            : 'Adicione uma pessoa de referência para este fornecedor.'}
        </p>
      </header>

      <div className="supplier-contact-form__fields">
        <TextField
          label="Nome"
          name="contact-name"
          value={name}
          maxLength={200}
          required
          autoFocus
          disabled={isSubmitting}
          onChange={(event) => {
            setName(
              event.target.value,
            )
          }}
        />

        <TextField
          label="Cargo ou área"
          name="contact-position"
          value={position}
          maxLength={100}
          placeholder="Ex.: Garantia, Financeiro"
          disabled={isSubmitting}
          onChange={(event) => {
            setPosition(
              event.target.value,
            )
          }}
        />

        <div className="supplier-contact-form__row">
          <TextField
            label="E-mail"
            type="email"
            name="contact-email"
            value={email}
            maxLength={255}
            placeholder="Opcional"
            disabled={isSubmitting}
            onChange={(event) => {
              setEmail(
                event.target.value,
              )
            }}
          />

          <TextField
            label="Telefone"
            type="tel"
            name="contact-phone"
            value={phone}
            maxLength={50}
            placeholder="Opcional"
            disabled={isSubmitting}
            onChange={(event) => {
              setPhone(
                event.target.value,
              )
            }}
          />
        </div>

        <label className="supplier-contact-primary">
          <input
            type="checkbox"
            checked={isPrimary}
            disabled={isSubmitting}
            onChange={(event) => {
              setIsPrimary(
                event.target.checked,
              )
            }}
          />

          <span>
            <strong>
              Contato principal
            </strong>

            <small>
              Utilize para indicar a
              principal pessoa de referência
              deste fornecedor.
            </small>
          </span>
        </label>
      </div>

      {errorMessage && (
        <div
          className="supplier-form__error"
          role="alert"
        >
          {errorMessage}
        </div>
      )}

      <footer className="supplier-form__actions">
        <Button
          type="button"
          variant="secondary"
          disabled={isSubmitting}
          onClick={onCancel}
        >
          Cancelar
        </Button>

        <Button
          type="submit"
          disabled={
            isSubmitting ||
            !name.trim()
          }
        >
          {isSubmitting
            ? 'Salvando...'
            : contact
              ? 'Salvar contato'
              : 'Adicionar contato'}
        </Button>
      </footer>
    </form>
  )
}