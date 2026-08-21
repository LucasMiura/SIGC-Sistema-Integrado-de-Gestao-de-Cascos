import {
  AlertCircle,
  ArrowLeft,
  CheckCircle2,
  Search,
} from 'lucide-react'

import {
  useState,
  type FormEvent,
} from 'react'

import {
  Button,
} from '../ui/Button'

import {
  Card,
} from '../ui/Card'

import {
  ApiError,
} from '../../services/httpClient'

import {
  customerReturnService,
} from '../../services/customerReturnService'

import type {
  CustomerReturnOrigin,
  CustomerReturnType,
} from '../../types/customerReturn'

interface CustomerReturnFormProps {
  onCancel: () => void
  onCreated: () => void
}

interface QuantityMap {
  [partId: number]: number
}

function getErrorMessage(
  error: unknown,
): string {
  if (error instanceof ApiError) {
    return error.message
  }

  return (
    'Não foi possível concluir a devolução.'
  )
}

export function CustomerReturnForm({
  onCancel,
  onCreated,
}: CustomerReturnFormProps) {
  const [
    returnType,
    setReturnType,
  ] = useState<CustomerReturnType>(
    'WORK_ORDER',
  )

  const [
    referenceNumber,
    setReferenceNumber,
  ] = useState('')

  const [
    origin,
    setOrigin,
  ] = useState<
    CustomerReturnOrigin | null
  >(null)

  const [
    quantities,
    setQuantities,
  ] = useState<QuantityMap>({})

  const [
    notes,
    setNotes,
  ] = useState('')

  const [
    isSearching,
    setIsSearching,
  ] = useState(false)

  const [
    isSubmitting,
    setIsSubmitting,
  ] = useState(false)

  const [
    errorMessage,
    setErrorMessage,
  ] = useState<string | null>(
    null,
  )

  function resetOrigin() {
    setOrigin(null)
    setQuantities({})
    setErrorMessage(null)
  }

  async function handleSearch(
    event: FormEvent<HTMLFormElement>,
  ) {
    event.preventDefault()

    const reference =
      referenceNumber.trim()

    if (!reference) {
      setErrorMessage(
        returnType === 'WORK_ORDER'
          ? 'Informe o número da Ordem de Serviço.'
          : 'Informe o número da Nota Fiscal.',
      )

      return
    }

    setIsSearching(true)
    setErrorMessage(null)

    try {
      const data =
        await customerReturnService
          .getOrigin(
            returnType,
            reference,
          )

      setOrigin(data)

      setQuantities({})

    } catch (error) {
      setOrigin(null)
      setQuantities({})

      setErrorMessage(
        getErrorMessage(error),
      )
    } finally {
      setIsSearching(false)
    }
  }

  function updateQuantity(
    partId: number,
    quantity: number,
  ) {
    setQuantities(
      (current) => ({
        ...current,
        [partId]: quantity,
      }),
    )
  }

  async function handleSubmit() {
    if (
      !origin ||
      isSubmitting
    ) {
      return
    }

    const selectedItems =
      origin.items
        .map((item) => ({
          item,
          quantity:
            quantities[
              item.part_id
            ] ?? 0,
        }))
        .filter(
          ({ quantity }) =>
            quantity > 0,
        )

    if (
      selectedItems.length === 0
    ) {
      setErrorMessage(
        'Informe a quantidade de pelo menos uma peça devolvida.',
      )

      return
    }

    const invalidItem =
      selectedItems.find(
        ({ item, quantity }) =>
          quantity >
          item.pending_quantity,
      )

    if (invalidItem) {
      setErrorMessage(
        `A quantidade informada para ${invalidItem.item.part_name} é superior ao saldo pendente.`,
      )

      return
    }

    setIsSubmitting(true)
    setErrorMessage(null)

    let createdReturnId:
      number | null = null

    try {
      const createdReturn =
        await customerReturnService
          .create({
            return_type:
              origin.return_type,

            reference_number:
              origin.reference_number,

            customer_name:
              origin.customer_name,

            status: 'ACTIVE',

            notes:
              notes.trim() || null,
          })

      createdReturnId =
        createdReturn.id

      for (
        const {
          item,
          quantity,
        } of selectedItems
      ) {
        await customerReturnService
          .addItem(
            createdReturn.id,
            {
              part_id:
                item.part_id,
              quantity,
            },
          )
      }

      onCreated()
    } catch (error) {
      if (createdReturnId) {
        setErrorMessage(
          'A devolução foi iniciada, mas nem todos os itens puderam ser registrados. Atualize a listagem antes de tentar novamente.',
        )
      } else {
        setErrorMessage(
          getErrorMessage(error),
        )
      }
    } finally {
      setIsSubmitting(false)
    }
  }

  return (
    <div className="customer-return-form">
      <div className="customer-return-form__header">
        <Button
          type="button"
          variant="ghost"
          size="sm"
          disabled={isSubmitting}
          onClick={onCancel}
        >
          <ArrowLeft size={16} />

          Voltar
        </Button>

        <div>
          <h2>
            Nova devolução
          </h2>

          <p>
            Localize a saída original e
            informe as peças devolvidas
            pelo cliente.
          </p>
        </div>
      </div>

      {!origin ? (
        <Card
          className="customer-return-origin-search"
          padding="lg"
        >
          <form
            onSubmit={
              handleSearch
            }
          >
            <div className="customer-return-type">
              <span className="customer-return-field-label">
                Origem da devolução
              </span>

              <div className="customer-return-type__options">
                <button
                  type="button"
                  className={
                    returnType ===
                    'WORK_ORDER'
                      ? 'customer-return-type__button customer-return-type__button--active'
                      : 'customer-return-type__button'
                  }
                  onClick={() => {
                    setReturnType(
                      'WORK_ORDER',
                    )

                    setErrorMessage(
                      null,
                    )
                  }}
                >
                  Oficina
                  <small>
                    Ordem de Serviço
                  </small>
                </button>

                <button
                  type="button"
                  className={
                    returnType ===
                    'SALE'
                      ? 'customer-return-type__button customer-return-type__button--active'
                      : 'customer-return-type__button'
                  }
                  onClick={() => {
                    setReturnType(
                      'SALE',
                    )

                    setErrorMessage(
                      null,
                    )
                  }}
                >
                  Balcão
                  <small>
                    Nota Fiscal
                  </small>
                </button>
              </div>
            </div>

            <label className="customer-return-reference">
              <span className="customer-return-field-label">
                {returnType ===
                'WORK_ORDER'
                  ? 'Número da Ordem de Serviço'
                  : 'Número da Nota Fiscal'}
              </span>

              <div className="customer-return-reference__input">
                <input
                  type="text"
                  value={
                    referenceNumber
                  }
                  autoFocus
                  placeholder={
                    returnType ===
                    'WORK_ORDER'
                      ? 'Ex.: OS-12345'
                      : 'Ex.: NFV-12345'
                  }
                  onChange={(
                    event,
                  ) => {
                    setReferenceNumber(
                      event.target.value,
                    )
                  }}
                />

                <Button
                  type="submit"
                  disabled={
                    isSearching
                  }
                >
                  <Search
                    size={17}
                  />

                  {isSearching
                    ? 'Buscando...'
                    : 'Buscar saída'}
                </Button>
              </div>
            </label>

            {errorMessage && (
              <div
                className="customer-return-error"
                role="alert"
              >
                <AlertCircle
                  size={18}
                />

                {errorMessage}
              </div>
            )}
          </form>
        </Card>
      ) : (
        <>
          <Card
            className="customer-return-origin"
            padding="lg"
          >
            <div className="customer-return-origin__header">
              <div>
                <span>
                  Saída localizada
                </span>

                <strong>
                  {
                    origin.reference_number
                  }
                </strong>
              </div>

              <Button
                type="button"
                variant="secondary"
                size="sm"
                disabled={
                  isSubmitting
                }
                onClick={
                  resetOrigin
                }
              >
                Buscar outra
              </Button>
            </div>

            <div className="customer-return-origin__info">
              <div>
                <span>
                  Cliente
                </span>

                <strong>
                  {
                    origin.customer_name
                  }
                </strong>
              </div>

              <div>
                <span>
                  Tipo
                </span>

                <strong>
                  {origin.return_type ===
                  'WORK_ORDER'
                    ? 'Oficina'
                    : 'Balcão'}
                </strong>
              </div>

              <div>
                <span>
                  Quantidade saída
                </span>

                <strong>
                  {
                    origin.total_outbound_quantity
                  }
                </strong>
              </div>

              <div>
                <span>
                  Já devolvida
                </span>

                <strong>
                  {
                    origin.total_returned_quantity
                  }
                </strong>
              </div>

              <div>
                <span>
                  Pendente
                </span>

                <strong>
                  {
                    origin.total_pending_quantity
                  }
                </strong>
              </div>
            </div>
          </Card>

          <Card
            className="customer-return-items"
            padding="none"
          >
            <div className="customer-return-items__header">
              <div>
                <h3>
                  Peças da saída
                </h3>

                <p>
                  Informe somente as
                  quantidades recebidas
                  nesta devolução.
                </p>
              </div>
            </div>

            <div className="customer-return-table-wrapper">
              <table className="customer-return-table">
                <thead>
                  <tr>
                    <th>
                      Peça
                    </th>

                    <th>
                      Código
                    </th>

                    <th>
                      Saída
                    </th>

                    <th>
                      Devolvido
                    </th>

                    <th>
                      Pendente
                    </th>

                    <th className="customer-return-table__quantity-header">
                      Recebido agora
                      <span>
                        Preencha abaixo
                      </span>
                    </th>
                  </tr>
                </thead>

                <tbody>
                  {origin.items.map(
                    (item) => {
                      const unavailable =
                        item.pending_quantity ===
                        0

                      return (
                        <tr
                          key={
                            item.part_id
                          }
                        >
                          <td>
                            <strong>
                              {
                                item.part_name
                              }
                            </strong>
                          </td>

                          <td>
                            <span className="customer-return-code">
                              {
                                item.part_code
                              }
                            </span>
                          </td>

                          <td>
                            {
                              item.outbound_quantity
                            }
                          </td>

                          <td>
                            {
                              item.returned_quantity
                            }
                          </td>

                          <td>
                            <strong>
                              {
                                item.pending_quantity
                              }
                            </strong>
                          </td>

                          <td>
                            {unavailable ? (
                              <span className="customer-return-completed">
                                <CheckCircle2
                                  size={
                                    15
                                  }
                                />

                                Completo
                              </span>
                            ) : (
                              <input
                                className="customer-return-quantity"
                                type="number"
                                min={0}
                                max={
                                  item.pending_quantity
                                }
                                placeholder="Qtd."
                                aria-label={`Quantidade recebida de ${item.part_name}`}
                                value={
                                  quantities[
                                    item.part_id
                                  ] ?? ''
                                }
                                disabled={
                                  isSubmitting
                                }
                                onChange={(
                                  event,
                                ) => {
                                  const value =
                                    Number(
                                      event
                                        .target
                                        .value,
                                    )

                                  updateQuantity(
                                    item.part_id,
                                    Number
                                      .isFinite(
                                        value,
                                      )
                                      ? value
                                      : 0,
                                  )
                                }}
                              />
                            )}
                          </td>
                        </tr>
                      )
                    },
                  )}
                </tbody>
              </table>
            </div>
          </Card>

          <Card
            className="customer-return-notes"
            padding="lg"
          >
            <label>
              <span className="customer-return-field-label">
                Observações
              </span>

              <textarea
                value={notes}
                maxLength={1000}
                disabled={
                  isSubmitting
                }
                placeholder="Observações opcionais sobre a devolução..."
                onChange={(
                  event,
                ) => {
                  setNotes(
                    event.target.value,
                  )
                }}
              />
            </label>
          </Card>

          {errorMessage && (
            <div
              className="customer-return-error"
              role="alert"
            >
              <AlertCircle
                size={18}
              />

              {errorMessage}
            </div>
          )}

          <div className="customer-return-form__actions">
            <Button
              type="button"
              variant="secondary"
              disabled={
                isSubmitting
              }
              onClick={onCancel}
            >
              Cancelar
            </Button>

            <Button
              type="button"
              disabled={
                isSubmitting ||
                origin
                  .total_pending_quantity ===
                  0
              }
              onClick={() => {
                void handleSubmit()
              }}
            >
              {isSubmitting
                ? 'Registrando...'
                : 'Registrar devolução'}
            </Button>
          </div>
        </>
      )}
    </div>
  )
}