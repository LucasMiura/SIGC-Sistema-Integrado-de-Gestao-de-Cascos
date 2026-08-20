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

import type {
  Part,
  PartFormValues,
} from '../../types/part'
import type {
  Supplier,
} from '../../types/supplier'

interface PartFormProps {
  part?: Part | null
  suppliers: Supplier[]

  isSubmitting: boolean
  errorMessage?: string | null

  onCancel(): void

  onSubmit(
    values: PartFormValues,
  ): Promise<void>
}

function normalizeOptionalText(
  value: string,
): string | null {
  const normalized =
    value.trim()

  return normalized || null
}

export function PartForm({
  part = null,
  suppliers,
  isSubmitting,
  errorMessage = null,
  onCancel,
  onSubmit,
}: PartFormProps) {
  const [
    supplierId,
    setSupplierId,
  ] = useState(
    part
      ? String(
          part.supplier_id,
        )
      : '',
  )

  const [
    partCode,
    setPartCode,
  ] = useState(
    part?.part_code ?? '',
  )

  const [
    name,
    setName,
  ] = useState(
    part?.name ?? '',
  )

  const [
    returnDeadlineDays,
    setReturnDeadlineDays,
  ] = useState(
    part
      ? String(
          part.return_deadline_days,
        )
      : '',
  )

  const [
    description,
    setDescription,
  ] = useState(
    part?.description ?? '',
  )

  const availableSuppliers =
    suppliers.filter(
      (supplier) =>
        supplier.is_active ||
        supplier.id ===
          part?.supplier_id,
    )

  async function handleSubmit(
    event:
      FormEvent<HTMLFormElement>,
  ) {
    event.preventDefault()

    if (isSubmitting) {
      return
    }

    const normalizedCode =
      partCode.trim()

    const normalizedName =
      name.trim()

    const parsedSupplierId =
      Number(supplierId)

    const parsedDeadline =
      Number(
        returnDeadlineDays,
      )

    if (
      !normalizedCode ||
      !normalizedName ||
      !Number.isInteger(
        parsedSupplierId,
      ) ||
      parsedSupplierId <= 0 ||
      !Number.isInteger(
        parsedDeadline,
      ) ||
      parsedDeadline <= 0 ||
      parsedDeadline > 3650
    ) {
      return
    }

    await onSubmit({
      supplier_id:
        parsedSupplierId,

      part_code:
        normalizedCode,

      name:
        normalizedName,

      description:
        normalizeOptionalText(
          description,
        ),

      return_deadline_days:
        parsedDeadline,
    })
  }

  return (
    <form
      className="part-form"
      onSubmit={handleSubmit}
    >
      <header className="part-form__header">
        <div>
          <span className="part-form__eyebrow">
            Cadastro
          </span>

          <h2>
            {part
              ? 'Editar peça'
              : 'Nova peça'}
          </h2>

          <p>
            {part
              ? 'Atualize os dados utilizados no controle deste casco.'
              : 'Informe os dados da peça sujeita à devolução de casco.'}
          </p>
        </div>

        <button
          type="button"
          className="part-form__close"
          aria-label={
            part
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

      <div className="part-form__body">
        <div className="part-form__fields">
          <label className="part-field">
            <span className="part-field__label">
              Fornecedor
            </span>

            <select
              className="part-field__select"
              value={supplierId}
              disabled={isSubmitting}
              required
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
                    key={
                      supplier.id
                    }
                    value={
                      supplier.id
                    }
                  >
                    {supplier.name}
                    {!supplier.is_active
                      ? ' — Inativo'
                      : ''}
                  </option>
                ),
              )}
            </select>

            {part &&
              suppliers.find(
                (supplier) =>
                  supplier.id ===
                  part.supplier_id,
              )?.is_active === false && (
                <span className="part-field__hint">
                  Este fornecedor está inativo.
                  Você pode manter o vínculo atual,
                  mas não poderá utilizá-lo para uma
                  nova associação.
                </span>
              )}
          </label>

          <div className="part-form__row">
            <TextField
              label="Código original"
              name="part-code"
              value={partCode}
              maxLength={100}
              required
              autoFocus
              disabled={isSubmitting}
              placeholder="Ex.: 07C911023H"
              onChange={(event) => {
                setPartCode(
                  event.target.value,
                )
              }}
            />

            <TextField
              label="Prazo de devolução"
              name="return-deadline"
              type="number"
              min={1}
              max={3650}
              step={1}
              value={
                returnDeadlineDays
              }
              required
              disabled={isSubmitting}
              placeholder="Ex.: 90"
              onChange={(event) => {
                setReturnDeadlineDays(
                  event.target.value,
                )
              }}
            />
          </div>

          <TextField
            label="Nome da peça"
            name="part-name"
            value={name}
            maxLength={200}
            required
            disabled={isSubmitting}
            placeholder="Ex.: Bico injetor"
            onChange={(event) => {
              setName(
                event.target.value,
              )
            }}
          />

          <label className="part-field">
            <span className="part-field__label">
              Descrição
            </span>

            <textarea
              className="part-field__textarea"
              name="part-description"
              rows={4}
              maxLength={1000}
              value={description}
              disabled={isSubmitting}
              placeholder="Informações complementares sobre a peça"
              onChange={(event) => {
                setDescription(
                  event.target.value,
                )
              }}
            />

            <span className="part-field__counter">
              {description.length}
              /1000
            </span>
          </label>

          <div className="part-form__deadline-note">
            <strong>
              Prazo padrão
            </strong>

            <p>
              O prazo informado será utilizado
              como referência nas novas compras.
              Alterações futuras não modificam
              os prazos históricos já aplicados.
            </p>
          </div>
        </div>

        {errorMessage && (
          <div
            className="part-form__error"
            role="alert"
          >
            {errorMessage}
          </div>
        )}
      </div>

      <footer className="part-form__actions">
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
            !partCode.trim() ||
            !name.trim() ||
            !returnDeadlineDays
          }
        >
          {isSubmitting
            ? 'Salvando...'
            : part
              ? 'Salvar alterações'
              : 'Cadastrar peça'}
        </Button>
      </footer>
    </form>
  )
}