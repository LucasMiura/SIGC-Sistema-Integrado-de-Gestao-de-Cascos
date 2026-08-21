import {
  ShoppingBag,
  Wrench,
  X,
} from 'lucide-react'

import {
  useState,
  type FormEvent,
} from 'react'

import type {
  Outbound,
  OutboundDestinationType,
  OutboundFormValues,
} from '../../types/outbound'

import {
  Button,
} from '../ui/Button'

import {
  FeedbackMessage,
} from '../ui/FeedbackMessage'

import {
  TextField,
} from '../ui/TextField'

interface OutboundFormProps {
  outbound?: Outbound | null

  isSubmitting: boolean

  errorMessage?:
    string | null

  onCancel(): void

  onSubmit(
    values:
      OutboundFormValues,
  ): Promise<void>
}

function getInitialReference(
  outbound?: Outbound | null,
): string {
  if (!outbound) {
    return ''
  }

  if (
    outbound.destination_type ===
    'WORK_ORDER'
  ) {
    return (
      outbound.work_order_number ??
      ''
    )
  }

  return (
    outbound.sales_invoice_number ??
    ''
  )
}

export function OutboundForm({
  outbound = null,
  isSubmitting,
  errorMessage = null,
  onCancel,
  onSubmit,
}: OutboundFormProps) {
  const [
    destinationType,
    setDestinationType,
  ] = useState<
    OutboundDestinationType
  >(
    outbound?.destination_type ??
      'WORK_ORDER',
  )

  const [
    referenceNumber,
    setReferenceNumber,
  ] = useState(
    getInitialReference(
      outbound,
    ),
  )

  const [
    customerName,
    setCustomerName,
  ] = useState(
    outbound?.customer_name ?? '',
  )

  async function handleSubmit(
    event:
      FormEvent<HTMLFormElement>,
  ) {
    event.preventDefault()

    if (isSubmitting) {
      return
    }

    const normalizedReference =
      referenceNumber.trim()

    const normalizedCustomer =
      customerName.trim()

    if (
      !normalizedReference ||
      !normalizedCustomer
    ) {
      return
    }

    await onSubmit({
      destination_type:
        destinationType,

      reference_number:
        normalizedReference,

      customer_name:
        normalizedCustomer,
    })
  }

  return (
    <form
      className="outbound-form"
      onSubmit={handleSubmit}
    >
      <header className="outbound-form__header">
        <div>
          <span className="outbound-form__eyebrow">
            Movimentação
          </span>

          <h2>
            {outbound
              ? 'Editar saída'
              : 'Nova saída'}
          </h2>

          <p>
            {outbound
              ? 'Atualize os dados da movimentação registrada.'
              : 'Registre o destino e a identificação da saída. As peças serão adicionadas na próxima etapa.'}
          </p>
        </div>

        <button
          type="button"
          className="outbound-form__close"
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
        <div className="outbound-form__feedback">
          <FeedbackMessage
            message={errorMessage}
            tone="error"
          />
        </div>
      )}

      <div className="outbound-form__body">
        <div className="outbound-form__fields">
          <fieldset className="outbound-destination">
            <legend>
              Destino da saída
            </legend>

            <div className="outbound-destination__options">
              <button
                type="button"
                className={
                  destinationType ===
                  'WORK_ORDER'
                    ? 'outbound-destination__option outbound-destination__option--active'
                    : 'outbound-destination__option'
                }
                disabled={isSubmitting}
                onClick={() => {
                  setDestinationType(
                    'WORK_ORDER',
                  )

                  setReferenceNumber('')
                }}
              >
                <Wrench
                  size={20}
                  strokeWidth={1.8}
                />

                <span>
                  <strong>
                    Oficina
                  </strong>

                  <small>
                    Ordem de Serviço
                  </small>
                </span>
              </button>

              <button
                type="button"
                className={
                  destinationType ===
                  'SALE'
                    ? 'outbound-destination__option outbound-destination__option--active'
                    : 'outbound-destination__option'
                }
                disabled={isSubmitting}
                onClick={() => {
                  setDestinationType(
                    'SALE',
                  )

                  setReferenceNumber('')
                }}
              >
                <ShoppingBag
                  size={20}
                  strokeWidth={1.8}
                />

                <span>
                  <strong>
                    Balcão
                  </strong>

                  <small>
                    Nota Fiscal de venda
                  </small>
                </span>
              </button>
            </div>
          </fieldset>

          <TextField
            label={
              destinationType ===
              'WORK_ORDER'
                ? 'Número da Ordem de Serviço'
                : 'Número da Nota Fiscal'
            }
            name="outbound-reference"
            value={referenceNumber}
            maxLength={100}
            required
            autoFocus
            disabled={isSubmitting}
            placeholder={
              destinationType ===
              'WORK_ORDER'
                ? 'Ex.: OS-12345'
                : 'Ex.: NFV-12345'
            }
            onChange={(event) => {
              setReferenceNumber(
                event.target.value,
              )
            }}
          />

          <TextField
            label="Cliente"
            name="outbound-customer"
            value={customerName}
            maxLength={200}
            required
            disabled={isSubmitting}
            placeholder="Nome simplificado para identificação"
            hint="Não é necessário cadastrar todos os dados do cliente."
            onChange={(event) => {
              setCustomerName(
                event.target.value,
              )
            }}
          />

          {!outbound && (
            <div className="outbound-form__note">
              <strong>
                Próxima etapa
              </strong>

              <p>
                Após registrar a saída,
                o SIGC abrirá a seleção
                das peças e quantidades.
                A origem do estoque será
                determinada automaticamente.
              </p>
            </div>
          )}
        </div>
      </div>

      <footer className="outbound-form__actions">
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
            !referenceNumber.trim() ||
            !customerName.trim()
          }
        >
          {isSubmitting
            ? 'Salvando...'
            : outbound
              ? 'Salvar alterações'
              : 'Registrar saída'}
        </Button>
      </footer>
    </form>
  )
}