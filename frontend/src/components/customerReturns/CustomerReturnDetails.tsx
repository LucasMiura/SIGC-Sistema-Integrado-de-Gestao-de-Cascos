import {
  AlertCircle,
  X,
} from 'lucide-react'

import {
  useEffect,
  useState,
} from 'react'

import {
  Button,
} from '../ui/Button'

import {
  StatusBadge,
} from '../ui/StatusBadge'

import {
  ApiError,
  httpClient,
} from '../../services/httpClient'

import {
  customerReturnService,
} from '../../services/customerReturnService'

import type {
  Part,
} from '../../types/part'

import type {
  CustomerReturn,
  CustomerReturnItem,
} from '../../types/customerReturn'

interface CustomerReturnDetailsProps {
  customerReturn:
    CustomerReturn

  onClose: () => void
}

function getErrorMessage(
  error: unknown,
): string {
  if (error instanceof ApiError) {
    return error.message
  }

  return (
    'Não foi possível carregar os itens da devolução.'
  )
}

export function CustomerReturnDetails({
  customerReturn,
  onClose,
}: CustomerReturnDetailsProps) {
  const [
    items,
    setItems,
  ] = useState<
    CustomerReturnItem[]
  >([])

  const [
    parts,
    setParts,
  ] = useState<Part[]>([])

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

  useEffect(
    () => {
      let ignore = false

      Promise.all([
        customerReturnService
          .listItems(
            customerReturn.id,
          ),

        httpClient.get<Part[]>(
          '/parts',
        ),
      ])
        .then(
          ([
            itemData,
            partData,
          ]) => {
            if (ignore) {
              return
            }

            setItems(
              itemData,
            )

            setParts(
              partData,
            )

            setErrorMessage(
              null,
            )
          },
        )
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
          if (!ignore) {
            setIsLoading(false)
          }
        })

      return () => {
        ignore = true
      }
    },
    [
      customerReturn.id,
    ],
  )

  const totalQuantity =
    items.reduce(
      (
        total,
        item,
      ) =>
        total +
        item.quantity,
      0,
    )

  function getPart(
    partId: number,
  ): Part | undefined {
    return parts.find(
      (part) =>
        part.id === partId,
    )
  }


  return (
    <div
      className="customer-return-modal-backdrop"
      role="presentation"
    >
      <div
        className="customer-return-modal customer-return-modal--wide"
        role="dialog"
        aria-modal="true"
        aria-label="Detalhes da devolução"
      >
        <div className="customer-return-modal__header">
          <div>
            <span>
              Devolução #
              {customerReturn.id}
            </span>

            <h2>
              {
                customerReturn
                  .reference_number
              }
            </h2>

            <p>
              {
                customerReturn
                  .customer_name
              }
            </p>
          </div>

          <button
            type="button"
            className="customer-return-modal__close"
            aria-label="Fechar"
            onClick={onClose}
          >
            <X size={20} />
          </button>
        </div>

        <div className="customer-return-details-summary">
          <div>
            <span>
              Origem
            </span>

            <strong>
              {customerReturn
                .return_type ===
              'WORK_ORDER'
                ? 'Oficina'
                : 'Balcão'}
            </strong>
          </div>

          <div>
            <span>
              Status
            </span>

            {customerReturn
              .status ===
            'ACTIVE' ? (
              <StatusBadge tone="success">
                Ativa
              </StatusBadge>
            ) : (
              <StatusBadge tone="neutral">
                Cancelada
              </StatusBadge>
            )}
          </div>

          <div>
            <span>
              Quantidade recebida
            </span>

            <strong>
              {totalQuantity}
            </strong>
          </div>
        </div>

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

        {isLoading ? (
          <div className="customer-return-loading">
            <div className="dashboard-state__spinner" />

            <span>
              Carregando itens...
            </span>
          </div>
        ) : (
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
                    Quantidade recebida
                  </th>
                </tr>
              </thead>

              <tbody>
                {items.map(
                  (item) => {
                    const part =
                      getPart(
                        item.part_id,
                      )

                    return (
                      <tr
                        key={
                          item.id
                        }
                      >
                        <td>
                          <strong>
                            {part?.name ??
                              `Peça #${item.part_id}`}
                          </strong>
                        </td>

                        <td>
                          <span className="customer-return-code">
                            {part?.part_code ??
                              `ID ${item.part_id}`}
                          </span>
                        </td>

                        <td>
                          <strong>
                            {
                              item.quantity
                            }
                          </strong>
                        </td>
                      </tr>
                    )
                  },
                )}
              </tbody>
            </table>
          </div>
        )}

        {customerReturn.notes && (
          <div className="customer-return-details-notes">
            <span>
              Observações
            </span>

            <p>
              {
                customerReturn.notes
              }
            </p>
          </div>
        )}

        <div className="customer-return-modal__footer">
          <Button
            type="button"
            variant="secondary"
            onClick={onClose}
          >
            Fechar
          </Button>
        </div>
      </div>
    </div>
  )
}