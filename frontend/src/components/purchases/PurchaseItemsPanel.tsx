import {
  AlertCircle,
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

import {
  purchaseService,
} from '../../services/purchaseService'
import {
  ApiError,
} from '../../services/httpClient'

import type {
  Part,
} from '../../types/part'
import type {
  Purchase,
  PurchaseItem,
} from '../../types/purchase'
import type {
  Supplier,
} from '../../types/supplier'

import {
  Button,
} from '../ui/Button'
import {
  StatusBadge,
} from '../ui/StatusBadge'

interface PurchaseItemsPanelProps {
  purchase: Purchase
  supplier: Supplier | null
  parts: Part[]

  onClose(): void
  onComplete(): void
}

function getErrorMessage(
  error: unknown,
): string {
  if (error instanceof ApiError) {
    return error.message
  }

  return (
    'Não foi possível concluir a operação com os itens da compra.'
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

export function PurchaseItemsPanel({
  purchase,
  supplier,
  parts,
  onClose,
  onComplete,
}: PurchaseItemsPanelProps) {
  const [
    items,
    setItems,
  ] = useState<PurchaseItem[]>(
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

      purchaseService
        .listItems(
          purchase.id,
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
      purchase.id,
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
              part.supplier_id ===
                purchase.supplier_id &&
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
        purchase.supplier_id,
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
        await purchaseService
          .addItem(
            purchase.id,
            {
              part_id:
                parsedPartId,

              quantity_purchased:
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

  const totalPurchased =
    items.reduce(
      (total, item) =>
        total +
        item.quantity_purchased,
      0,
    )

  const totalAvailable =
    items.reduce(
      (total, item) =>
        total +
        item.quantity_available,
      0,
    )

  return (
    <div
      className="purchase-modal-backdrop"
      role="presentation"
    >
      <section
        className="purchase-items-panel"
        role="dialog"
        aria-modal="true"
        aria-labelledby="purchase-items-title"
      >
        <header className="purchase-items-panel__header">
          <div>
            <span>
              Compra
            </span>

            <h2
              id="purchase-items-title"
            >
              NF {purchase.invoice_number}
            </h2>

            <p>
              {supplier?.name ??
                `Fornecedor #${purchase.supplier_id}`}
            </p>
          </div>

          <button
            type="button"
            className="purchase-items-panel__close"
            aria-label="Fechar itens da compra"
            onClick={onClose}
          >
            <X
              size={20}
              strokeWidth={1.8}
            />
          </button>
        </header>

        <div className="purchase-items-panel__toolbar">
          <div className="purchase-items-panel__metrics">
            <div>
              <span>
                Itens
              </span>

              <strong>
                {items.length}
              </strong>
            </div>

            <div>
              <span>
                Compradas
              </span>

              <strong>
                {totalPurchased}
              </strong>
            </div>

            <div>
              <span>
                Disponíveis
              </span>

              <strong>
                {totalAvailable}
              </strong>
            </div>
          </div>

          {purchase.status !==
            'CANCELLED' && (
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
          <div
            className="purchase-page-error"
            role="alert"
          >
            <AlertCircle
              size={18}
            />

            <span>
              {errorMessage}
            </span>
          </div>
        )}

        <div className="purchase-items-panel__body">
          {isAdding && (
            <form
              className="purchase-item-form"
              onSubmit={
                handleAddItem
              }
            >
              <div>
                <label className="purchase-field">
                  <span className="purchase-field__label">
                    Peça
                  </span>

                  <select
                    className="purchase-field__select"
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

                <label className="purchase-field">
                  <span className="purchase-field__label">
                    Quantidade
                  </span>

                  <input
                    className="purchase-field__input"
                    type="number"
                    min={1}
                    step={1}
                    value={quantity}
                    required
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
            <div className="purchase-item-state">
              <div className="dashboard-state__spinner" />

              <span>
                Carregando itens...
              </span>
            </div>
          ) : items.length === 0 ? (
            <div className="purchase-item-state">
              <div className="purchase-empty__icon">
                <Boxes
                  size={22}
                />
              </div>

              <strong>
                Nenhuma peça adicionada
              </strong>

              <p>
                Adicione as peças que fazem
                parte desta Nota Fiscal.
              </p>
            </div>
          ) : (
            <div className="purchase-items-list">
              {items.map(
                (item) => {
                  const part =
                    getPart(
                      item.part_id,
                      parts,
                    )

                  return (
                    <article
                      className="purchase-item-card"
                      key={item.id}
                    >
                      <div className="purchase-item-card__identity">
                        <div className="purchase-item-card__icon">
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

                      <div className="purchase-item-card__quantities">
                        <div>
                          <span>
                            Comprada
                          </span>

                          <strong>
                            {item.quantity_purchased}
                          </strong>
                        </div>

                        <div>
                          <span>
                            Disponível
                          </span>

                          <strong>
                            {item.quantity_available}
                          </strong>
                        </div>
                      </div>

                      {item.quantity_available <
                        item.quantity_purchased && (
                        <StatusBadge tone="info">
                          Com movimentação
                        </StatusBadge>
                      )}
                    </article>
                  )
                },
              )}
            </div>
          )}
        </div>

        <footer className="purchase-items-panel__footer">
          <div className="purchase-items-panel__footer-info">
            <strong>
              A compra já está salva.
            </strong>

            <span>
              Concluir finaliza esta etapa de
              lançamento dos itens.
            </span>
          </div>

          <div className="purchase-items-panel__footer-actions">
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