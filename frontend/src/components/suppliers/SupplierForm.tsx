import {
  X,
} from 'lucide-react'
import {
  useState,
  type FormEvent,
} from 'react'

import type {
  Supplier,
  SupplierCreatePayload,
} from '../../types/supplier'
import {
  Button,
} from '../ui/Button'
import {
  TextField,
} from '../ui/TextField'
import {
  FeedbackMessage,
} from '../ui/FeedbackMessage'

interface SupplierFormProps {
  supplier?: Supplier | null
  isSubmitting: boolean
  errorMessage?: string | null

  onCancel(): void

  onSubmit(
    payload: SupplierCreatePayload,
  ): Promise<void>
}

function normalizeOptionalValue(
  value: string,
): string | null {
  const normalized =
    value.trim()

  return normalized || null
}

export function SupplierForm({
  supplier = null,
  isSubmitting,
  errorMessage = null,
  onCancel,
  onSubmit,
}: SupplierFormProps) {
  const [
    name,
    setName,
  ] = useState(
    supplier?.name ?? '',
  )

  const [
    document,
    setDocument,
  ] = useState(
    supplier?.document ?? '',
  )

  const [
    address,
    setAddress,
  ] = useState(
    supplier?.address ?? '',
  )

  const [
    notes,
    setNotes,
  ] = useState(
    supplier?.notes ?? '',
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

      document:
        normalizeOptionalValue(
          document,
        ),

      address:
        normalizeOptionalValue(
          address,
        ),

      notes:
        normalizeOptionalValue(
          notes,
        ),
    })
  }

  const title =
    supplier
      ? 'Editar fornecedor'
      : 'Novo fornecedor'

  const description =
    supplier
      ? 'Atualize os dados cadastrais do fornecedor.'
      : 'Informe os dados principais para adicionar um fornecedor ao SIGC.'

  return (
    <form
      className="supplier-form"
      onSubmit={handleSubmit}
    >
      <header className="supplier-form__header">
        <div>
          <span className="supplier-form__eyebrow">
            Cadastro
          </span>

          <h2>
            {title}
          </h2>

          <p>
            {description}
          </p>
        </div>

        <button
          type="button"
          className="supplier-form__close"
          aria-label={
            supplier
              ? 'Cancelar edição'
              : 'Cancelar cadastro'
          }
          disabled={isSubmitting}
          onClick={onCancel}
        >
          <X
            size={20}
            strokeWidth={1.8}
          />
        </button>
      </header>

      {errorMessage && (
        <div className="supplier-form__feedback">
          <FeedbackMessage
            message={errorMessage}
            tone="error"
          />
        </div>
      )}

      <div className="supplier-form__body">
        <div className="supplier-form__fields">
          <TextField
            label="Nome ou razão social"
            name="supplier-name"
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
            label="CPF, CNPJ ou documento"
            name="supplier-document"
            value={document}
            maxLength={50}
            disabled={isSubmitting}
            placeholder="Opcional"
            onChange={(event) => {
              setDocument(
                event.target.value,
              )
            }}
          />

          <label className="supplier-field">
            <span className="supplier-field__label">
              Endereço
            </span>

            <textarea
              className="supplier-field__textarea"
              name="supplier-address"
              rows={3}
              value={address}
              disabled={isSubmitting}
              placeholder="Endereço completo do fornecedor"
              onChange={(event) => {
                setAddress(
                  event.target.value,
                )
              }}
            />
          </label>

          <label className="supplier-field">
            <span className="supplier-field__label">
              Observações
            </span>

            <textarea
              className="supplier-field__textarea"
              name="supplier-notes"
              rows={4}
              value={notes}
              disabled={isSubmitting}
              placeholder="Informações adicionais relevantes"
              onChange={(event) => {
                setNotes(
                  event.target.value,
                )
              }}
            />
          </label>
        </div>
      </div>

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
            : supplier
              ? 'Salvar alterações'
              : 'Cadastrar fornecedor'}
        </Button>
      </footer>
    </form>
  )
}