import {
  X,
} from 'lucide-react'
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
import {
  FeedbackMessage,
} from '../ui/FeedbackMessage'

import type {
  Purchase,
  PurchaseFormValues,
} from '../../types/purchase'
import type {
  Supplier,
} from '../../types/supplier'

interface PurchaseFormProps {
  purchase?: Purchase | null
  suppliers: Supplier[]

  isSubmitting: boolean
  errorMessage?: string | null

  onCancel(): void

  onSubmit(
    values: PurchaseFormValues,
  ): Promise<void>
}

function normalizeOptionalText(
  value: string,
): string | null {
  const normalized =
    value.trim()

  return normalized || null
}

export function PurchaseForm({
  purchase = null,
  suppliers,
  isSubmitting,
  errorMessage = null,
  onCancel,
  onSubmit,
}: PurchaseFormProps) {
  const [
    supplierId,
    setSupplierId,
  ] = useState(
    purchase
      ? String(
          purchase.supplier_id,
        )
      : '',
  )

  const [
    invoiceNumber,
    setInvoiceNumber,
  ] = useState(
    purchase?.invoice_number ?? '',
  )

  const [
    invoiceSeries,
    setInvoiceSeries,
  ] = useState(
    purchase?.invoice_series ?? '',
  )

  const [
    issueDate,
    setIssueDate,
  ] = useState(
    purchase?.issue_date ?? '',
  )

  const [
    notes,
    setNotes,
  ] = useState(
    purchase?.notes ?? '',
  )

  const availableSuppliers =
    suppliers.filter(
      (supplier) =>
        supplier.is_active ||
        supplier.id ===
          purchase?.supplier_id,
    )

  async function handleSubmit(
    event:
      FormEvent<HTMLFormElement>,
  ) {
    event.preventDefault()

    if (isSubmitting) {
      return
    }

    const parsedSupplierId =
      Number(supplierId)

    const normalizedInvoice =
      invoiceNumber.trim()

    if (
      !Number.isInteger(
        parsedSupplierId,
      ) ||
      parsedSupplierId <= 0 ||
      !normalizedInvoice ||
      !issueDate
    ) {
      return
    }

    await onSubmit({
      supplier_id:
        parsedSupplierId,

      invoice_number:
        normalizedInvoice,

      invoice_series:
        normalizeOptionalText(
          invoiceSeries,
        ),

      issue_date:
        issueDate,

      notes:
        normalizeOptionalText(
          notes,
        ),
    })
  }

  return (
    <form
      className="purchase-form"
      onSubmit={handleSubmit}
    >
      <header className="purchase-form__header">
        <div>
          <span className="purchase-form__eyebrow">
            Operação
          </span>

          <h2>
            {purchase
              ? 'Editar compra'
              : 'Nova compra'}
          </h2>

          <p>
            {purchase
              ? 'Atualize os dados da Nota Fiscal de compra.'
              : 'Registre primeiro os dados da Nota Fiscal. Os itens serão adicionados na etapa seguinte.'}
          </p>
        </div>

        <button
          type="button"
          className="purchase-form__close"
          aria-label="Fechar"
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
        <div className="purchase-form__feedback">
          <FeedbackMessage
            message={errorMessage}
            tone="error"
          />
        </div>
      )}

      <div className="purchase-form__body">
        <div className="purchase-form__fields">
          <label className="purchase-field">
            <span className="purchase-field__label">
              Fornecedor
            </span>

            <select
              className="purchase-field__select"
              value={supplierId}
              required
              disabled={isSubmitting}
              onChange={(event) => {
                setSupplierId(
                  event.target.value,
                )
              }}
            >
              <option value="">
                Selecione um fornecedor
              </option>

              {availableSuppliers.map(
                (supplier) => (
                  <option
                    key={supplier.id}
                    value={supplier.id}
                  >
                    {supplier.name}
                    {!supplier.is_active
                      ? ' — Inativo'
                      : ''}
                  </option>
                ),
              )}
            </select>
          </label>

          <div className="purchase-form__row">
            <TextField
              label="Número da Nota Fiscal"
              name="purchase-invoice"
              value={invoiceNumber}
              maxLength={100}
              required
              autoFocus
              disabled={isSubmitting}
              placeholder="Ex.: 158742"
              onChange={(event) => {
                setInvoiceNumber(
                  event.target.value,
                )
              }}
            />

            <TextField
              label="Série"
              name="purchase-series"
              value={invoiceSeries}
              maxLength={50}
              disabled={isSubmitting}
              placeholder="Opcional"
              onChange={(event) => {
                setInvoiceSeries(
                  event.target.value,
                )
              }}
            />
          </div>

          <TextField
            label="Data de emissão"
            type="date"
            name="purchase-issue-date"
            value={issueDate}
            required
            disabled={isSubmitting}
            onChange={(event) => {
              setIssueDate(
                event.target.value,
              )
            }}
          />

          <label className="purchase-field">
            <span className="purchase-field__label">
              Observações
            </span>

            <textarea
              className="purchase-field__textarea"
              rows={4}
              maxLength={1000}
              value={notes}
              disabled={isSubmitting}
              placeholder="Informações complementares da compra"
              onChange={(event) => {
                setNotes(
                  event.target.value,
                )
              }}
            />

            <span className="purchase-field__counter">
              {notes.length}/1000
            </span>
          </label>

          {!purchase && (
            <div className="purchase-form__note">
              <strong>
                Próxima etapa
              </strong>

              <p>
                Após registrar a Nota Fiscal,
                o SIGC abrirá automaticamente
                a gestão dos itens dessa compra.
              </p>
            </div>
          )}
        </div>
      </div>

      <footer className="purchase-form__actions">
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
            !supplierId ||
            !invoiceNumber.trim() ||
            !issueDate
          }
        >
          {isSubmitting
            ? 'Salvando...'
            : purchase
              ? 'Salvar alterações'
              : 'Registrar compra'}
        </Button>
      </footer>
    </form>
  )
}