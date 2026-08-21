import {
  Boxes,
  Plus,
  X,
} from 'lucide-react'

import {
  useEffect,
  useMemo,
  useState,
  type FormEvent,
} from 'react'

import type {
  Part,
} from '../../types/part'

import type {
  Outbound,
  OutboundItem,
} from '../../types/outbound'

import {
  ApiError,
} from '../../services/httpClient'

import {
  outboundService,
} from '../../services/outboundService'

import {
  Button,
} from '../ui/Button'

import {
  FeedbackMessage,
} from '../ui/FeedbackMessage'

interface OutboundItemsPanelProps {
  outbound: Outbound
  parts: Part[]

  onClose(): void
  onComplete(): void
}

function getErrorMessage(
  error: unknown,
): string {
  if (
    error instanceof ApiError
  ) {
    return error.message
  }

  return (
    'Não foi possível concluir a operação com os itens da saída.'
  )
}

function getPart(
  partId: number,
  parts: Part[],
): Part | undefined {
  return parts.find(
    (part) =>
      part.id === partId,
  )
}

function getReference(
  outbound: Outbound,
): string {
  if (
    outbound.destination_type ===
    'WORK_ORDER'
  ) {
    return (
      outbound.work_order_number ??
      `Saída #${outbound.id}`
    )
  }

  return (
    outbound.sales_invoice_number ??
    `Saída #${outbound.id}`
  )
}

export function OutboundItemsPanel({
  outbound,
  parts,
  onClose,
  onComplete,
}: OutboundItemsPanelProps) {
  const [
    items,
    setItems,
  ] = useState<OutboundItem[]>(
    [],
  )

  const [
    isLoading,
    setIsLoading,
  ] = useState(true)

  const [
    errorMessage,
    setErrorMessage,
  ] = useState<string | null>(
    null,
  )

  const [
    isAdding,
    setIsAdding,
  ] = useState(false)

  const [
    isSubmitting,
    setIsSubmitting,
  ] = useState(false)

  const [
    partId,
    setPartId,
  ] = useState('')

  const [
    quantity,
    setQuantity,
  ] = useState('')

  useEffect(
    () => {
      let ignore = false

      outboundService
        .listItems(
          outbound.id,
        )
        .then((data) => {
          if (ignore) {
            return
          }

          setItems(data)
          setErrorMessage(null)
        })
        .catch(
          (error: unknown) => {
            if (ignore) {
              return
            }

            setErrorMessage(
              getErrorMessage(
                error,
              ),
            )
          },
        )
        .finally(() => {
          if (ignore) {
            return
          }

          setIsLoading(false)
        })

      return () => {
        ignore = true
      }
    },
    [
      outbound.id,
    ],
  )

  const availableParts =
    useMemo(
      () => {
        const usedPartIds =
          new Set(
            items.map(
              (item) =>
                item.part_id,
            ),
          )

        return parts
          .filter(
            (part) =>
              part.is_active &&
              !usedPartIds.has(
                part.id,
              ),
          )
          .sort(
            (left, right) =>
              left.name.localeCompare(
                right.name,
                'pt-BR',
              ),
          )
      },
      [
        items,
        parts,
      ],
    )

  async function handleAddItem(
    event:
      FormEvent<HTMLFormElement>,
  ) {
    event.preventDefault()

    if (isSubmitting) {
      return
    }

    const parsedPartId =
      Number(partId)

    const parsedQuantity =
      Number(quantity)

    if (
      !Number.isInteger(
        parsedPartId,
      ) ||
      parsedPartId <= 0 ||
      !Number.isInteger(
        parsedQuantity,
      ) ||
      parsedQuantity <= 0
    ) {
      return
    }

    setIsSubmitting(true)
    setErrorMessage(null)

    try {
      const created =
        await outboundService
          .addItem(
            outbound.id,
            {
              part_id:
                parsedPartId,

              quantity:
                parsedQuantity,
            },
          )

      setItems(
        (currentItems) => [
          ...currentItems,
          created,
        ],
      )

      setPartId('')
      setQuantity('')
      setIsAdding(false)
    } catch (error) {
      setErrorMessage(
        getErrorMessage(
          error,
        ),
      )
    } finally {
      setIsSubmitting(false)
    }
  }

  const totalQuantity =
    items.reduce(
      (total, item) =>
        total + item.quantity,
      0,
    )

  return (
    <div
      className="outbound-modal-backdrop"
      role="presentation"
    >
      <section
        className="outbound-items-panel"
        role="dialog"
        aria-modal="true"
        aria-labelledby="outbound-items-title"
      >
        <header className="outbound-items-panel__header">
          <div>
            <span>
              Saída
            </span>

            <h2
              id="outbound-items-title"
            >
              {getReference(
                outbound,
              )}
            </h2>

            <p>
              {outbound.customer_name}
              {' · '}
              {outbound.destination_type ===
              'WORK_ORDER'
                ? 'Oficina'
                : 'Balcão'}
            </p>
          </div>

          <button
            type="button"
            className="outbound-items-panel__close"
            aria-label="Fechar itens da saída"
            onClick={onClose}
          >
            <X
              size={20}
              strokeWidth={1.8}
            />
          </button>
        </header>

        <div className="outbound-items-panel__toolbar">
          <div className="outbound-items-panel__metrics">
            <div>
              <span>
                Peças
              </span>

              <strong>
                {items.length}
              </strong>
            </div>

            <div>
              <span>
                Quantidade total
              </span>

              <strong>
                {totalQuantity}
              </strong>
            </div>
          </div>

          {outbound.status ===
            'ACTIVE' && (
            <Button
              type="button"
              size="sm"
              disabled={
                availableParts.length ===
                0
              }
              onClick={() => {
                setIsAdding(
                  (current) =>
                    !current,
                )
              }}
            >
              <Plus
                size={16}
              />

              Adicionar peça
            </Button>
          )}
        </div>

        {errorMessage && (
          <div className="outbound-items-panel__feedback">
            <FeedbackMessage
              message={errorMessage}
              tone="error"
            />
          </div>
        )}

        <div className="outbound-items-panel__body">
          {isAdding && (
            <form
              className="outbound-item-form"
              onSubmit={
                handleAddItem
              }
            >
              <div>
                <label className="outbound-field">
                  <span className="outbound-field__label">
                    Peça
                  </span>

                  <select
                    className="outbound-field__select"
                    value={partId}
                    required
                    autoFocus
                    disabled={
                      isSubmitting
                    }
                    onChange={(event) => {
                      setPartId(
                        event.target.value,
                      )
                    }}
                  >
                    <option value="">
                      Selecione uma peça
                    </option>

                    {availableParts.map(
                      (part) => (
                        <option
                          key={part.id}
                          value={part.id}
                        >
                          {part.part_code}
                          {' — '}
                          {part.name}
                        </option>
                      ),
                    )}
                  </select>
                </label>

                <label className="outbound-field">
                  <span className="outbound-field__label">
                    Quantidade
                  </span>

                  <input
                    className="outbound-field__input"
                    type="number"
                    min={1}
                    step={1}
                    required
                    value={quantity}
                    disabled={
                      isSubmitting
                    }
                    onChange={(event) => {
                      setQuantity(
                        event.target.value,
                      )
                    }}
                  />
                </label>
              </div>

              <div className="outbound-item-form__info">
                O SIGC selecionará
                automaticamente a origem
                do estoque disponível.
              </div>

              <footer>
                <Button
                  type="button"
                  variant="secondary"
                  size="sm"
                  disabled={
                    isSubmitting
                  }
                  onClick={() => {
                    setIsAdding(false)
                    setPartId('')
                    setQuantity('')
                  }}
                >
                  Cancelar
                </Button>

                <Button
                  type="submit"
                  size="sm"
                  disabled={
                    isSubmitting ||
                    !partId ||
                    !quantity
                  }
                >
                  {isSubmitting
                    ? 'Adicionando...'
                    : 'Adicionar'}
                </Button>
              </footer>
            </form>
          )}

          {isLoading ? (
            <div className="outbound-item-state">
              <div className="dashboard-state__spinner" />

              <span>
                Carregando itens...
              </span>
            </div>
          ) : items.length === 0 ? (
            <div className="outbound-item-state">
              <div className="outbound-empty__icon">
                <Boxes
                  size={22}
                />
              </div>

              <strong>
                Nenhuma peça adicionada
              </strong>

              <p>
                Adicione as peças
                relacionadas a esta saída.
              </p>
            </div>
          ) : (
            <div className="outbound-items-list">
              {items.map(
                (item) => {
                  const part =
                    getPart(
                      item.part_id,
                      parts,
                    )

                  return (
                    <article
                      className="outbound-item-card"
                      key={item.id}
                    >
                      <div className="outbound-item-card__identity">
                        <div className="outbound-item-card__icon">
                          <Boxes
                            size={19}
                          />
                        </div>

                        <div>
                          <strong>
                            {part?.name ??
                              `Peça #${item.part_id}`}
                          </strong>

                          <span>
                            {part?.part_code ??
                              `ID ${item.part_id}`}
                          </span>
                        </div>
                      </div>

                      <div className="outbound-item-card__quantity">
                        <span>
                          Quantidade
                        </span>

                        <strong>
                          {item.quantity}
                        </strong>
                      </div>
                    </article>
                  )
                },
              )}
            </div>
          )}
        </div>

        <footer className="outbound-items-panel__footer">
          <div className="outbound-items-panel__footer-info">
            <strong>
              A saída já está salva.
            </strong>

            <span>
              Concluir finaliza esta
              etapa de lançamento.
            </span>
          </div>

          <div className="outbound-items-panel__footer-actions">
            <Button
              type="button"
              variant="secondary"
              onClick={onClose}
            >
              Fechar por agora
            </Button>

            <Button
              type="button"
              disabled={
                items.length === 0 ||
                isSubmitting
              }
              onClick={onComplete}
            >
              Concluir lançamento
            </Button>
          </div>
        </footer>
      </section>
    </div>
  )
}