import {
  AlertCircle,
  Plus,
  RefreshCcw,
  Search,
  X,
} from 'lucide-react'

import {
  useEffect,
  useMemo,
  useState,
  type FormEvent,
} from 'react'

import {
  CustomerReturnDetails,
} from '../components/customerReturns/CustomerReturnDetails'

import {
  CustomerReturnForm,
} from '../components/customerReturns/CustomerReturnForm'

import {
  CustomerReturnTable,
} from '../components/customerReturns/CustomerReturnTable'

import {
  Button,
} from '../components/ui/Button'

import {
  Card,
} from '../components/ui/Card'

import {
  PageHeader,
} from '../components/ui/PageHeader'

import {
  StatusBadge,
} from '../components/ui/StatusBadge'

import {
  ApiError,
} from '../services/httpClient'

import {
  customerReturnService,
} from '../services/customerReturnService'

import type {
  CustomerReturn,
} from '../types/customerReturn'

import {
  Toast,
} from '../components/ui/Toast'

type StatusFilter =
  | 'all'
  | 'active'
  | 'cancelled'

type ViewMode =
  | 'list'
  | 'create'

function getErrorMessage(
  error: unknown,
): string {
  if (error instanceof ApiError) {
    return error.message
  }

  return (
    'Não foi possível concluir a operação com devoluções.'
  )
}

function normalizeSearchValue(
  value: string,
): string {
  return value
    .trim()
    .toLocaleLowerCase(
      'pt-BR',
    )
}

export function CustomerReturnsPage() {
  const [
    customerReturns,
    setCustomerReturns,
  ] = useState<
    CustomerReturn[]
  >([])

  const [
    isLoading,
    setIsLoading,
  ] = useState(true)

  const [
    pageError,
    setPageError,
  ] = useState<string | null>(
    null,
  )

  const [
    toastMessage,
    setToastMessage,
  ] = useState<string | null>(
    null,
  )

  const [
    searchValue,
    setSearchValue,
  ] = useState('')

  const [
    statusFilter,
    setStatusFilter,
  ] = useState<StatusFilter>(
    'all',
  )

  const [
    viewMode,
    setViewMode,
  ] = useState<ViewMode>(
    'list',
  )

  const [
    detailsReturn,
    setDetailsReturn,
  ] = useState<
    CustomerReturn | null
  >(null)

  const [
    cancelReturn,
    setCancelReturn,
  ] = useState<
    CustomerReturn | null
  >(null)

  const [
    cancelJustification,
    setCancelJustification,
  ] = useState('')

  const [
    cancelError,
    setCancelError,
  ] = useState<string | null>(
    null,
  )

  const [
    isCancelling,
    setIsCancelling,
  ] = useState(false)

  async function reload() {
    setIsLoading(true)
    setPageError(null)

    try {
      const data =
        await customerReturnService
          .list()

      setCustomerReturns(
        data,
      )
    } catch (error) {
      setPageError(
        getErrorMessage(
          error,
        ),
      )
    } finally {
      setIsLoading(false)
    }
  }

  useEffect(
    () => {
      let ignore = false

      customerReturnService
        .list()
        .then((data) => {
          if (ignore) {
            return
          }

          setCustomerReturns(
            data,
          )

          setPageError(null)
        })
        .catch(
          (error: unknown) => {
            if (ignore) {
              return
            }

            setPageError(
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
    [],
  )

  const filteredReturns =
    useMemo(
      () => {
        const search =
          normalizeSearchValue(
            searchValue,
          )

        return customerReturns.filter(
          (customerReturn) => {
            const matchesStatus =
              statusFilter ===
                'all' ||
              (
                statusFilter ===
                  'active' &&
                customerReturn
                  .status ===
                  'ACTIVE'
              ) ||
              (
                statusFilter ===
                  'cancelled' &&
                customerReturn
                  .status ===
                  'CANCELLED'
              )

            if (!matchesStatus) {
              return false
            }

            if (!search) {
              return true
            }

            const searchableValue =
              [
                customerReturn
                  .reference_number,
                customerReturn
                  .customer_name,
                customerReturn
                  .return_type,
              ]
                .join(' ')
                .toLocaleLowerCase(
                  'pt-BR',
                )

            return (
              searchableValue
                .includes(search)
            )
          },
        )
      },
      [
        customerReturns,
        searchValue,
        statusFilter,
      ],
    )

  const activeCount =
    customerReturns.filter(
      (customerReturn) =>
        customerReturn.status ===
        'ACTIVE',
    ).length

  const cancelledCount =
    customerReturns.length -
    activeCount

  async function handleCreated() {
    setViewMode('list')

    await reload()

    setToastMessage(
      'Devolução registrada com sucesso.',
    )
  }

  function openCancel(
    customerReturn:
      CustomerReturn,
  ) {
    setCancelReturn(
      customerReturn,
    )

    setCancelJustification('')
    setCancelError(null)
  }

  function closeCancel() {
    if (isCancelling) {
      return
    }

    setCancelReturn(null)
    setCancelJustification('')
    setCancelError(null)
  }

  async function handleCancel(
    event:
      FormEvent<HTMLFormElement>,
  ) {
    event.preventDefault()

    if (
      !cancelReturn ||
      isCancelling
    ) {
      return
    }

    const justification =
      cancelJustification.trim()

    if (!justification) {
      setCancelError(
        'Informe a justificativa para cancelar a devolução.',
      )

      return
    }

    setIsCancelling(true)
    setCancelError(null)

    try {
      const updated =
        await customerReturnService
          .cancel(
            cancelReturn.id,
            {
              justification,
            },
          )

      setCustomerReturns(
        (current) =>
          current.map(
            (item) =>
              item.id ===
              updated.id
                ? updated
                : item,
          ),
      )

      setCancelReturn(null)
      setCancelJustification('')

      setToastMessage(
        'Devolução cancelada com sucesso.',
      )

    } catch (error) {
      setCancelError(
        getErrorMessage(
          error,
        ),
      )
    } finally {
      setIsCancelling(false)
    }
  }

  if (
    viewMode === 'create'
  ) {
    return (
      <CustomerReturnForm
        onCancel={() => {
          setViewMode('list')
        }}
        onCreated={() => {
          void handleCreated()
        }}
      />
    )
  }

  return (
    <div className="page-stack">
      <PageHeader
        eyebrow="Movimentações"
        title="Devoluções de clientes"
        description="Registre e acompanhe os cascos devolvidos pelos clientes vinculados às saídas de oficina e balcão."
        actions={
          <Button
            type="button"
            onClick={() => {
              setViewMode(
                'create',
              )
            }}
          >
            <Plus size={17} />

            Nova devolução
          </Button>
        }
      />

      <section className="customer-return-summary">
        <Card
          className="customer-return-summary__card"
          padding="md"
        >
          <span>
            Registradas
          </span>

          <strong>
            {
              customerReturns.length
            }
          </strong>
        </Card>

        <Card
          className="customer-return-summary__card"
          padding="md"
        >
          <span>
            Ativas
          </span>

          <strong>
            {activeCount}
          </strong>

          <StatusBadge tone="success">
            Válidas
          </StatusBadge>
        </Card>

        <Card
          className="customer-return-summary__card"
          padding="md"
        >
          <span>
            Canceladas
          </span>

          <strong>
            {cancelledCount}
          </strong>

          <StatusBadge tone="neutral">
            Histórico
          </StatusBadge>
        </Card>
      </section>

      <Card
        className="customer-return-management"
        padding="none"
      >
        <div className="customer-return-toolbar">
          <div className="customer-return-search">
            <Search
              size={18}
              strokeWidth={1.8}
            />

            <input
              type="search"
              value={searchValue}
              placeholder="Buscar por OS, NF ou cliente"
              aria-label="Buscar devoluções"
              onChange={(event) => {
                setSearchValue(
                  event.target.value,
                )
              }}
            />

            {searchValue && (
              <button
                type="button"
                className="customer-return-search__clear"
                aria-label="Limpar busca"
                onClick={() => {
                  setSearchValue('')
                }}
              >
                <X size={15} />
              </button>
            )}
          </div>

          <div className="customer-return-status-filter">
            {(
              [
                [
                  'all',
                  'Todas',
                ],
                [
                  'active',
                  'Ativas',
                ],
                [
                  'cancelled',
                  'Canceladas',
                ],
              ] as const
            ).map(
              ([
                value,
                label,
              ]) => (
                <button
                  key={value}
                  type="button"
                  className={
                    statusFilter ===
                    value
                      ? 'customer-return-status-filter__button customer-return-status-filter__button--active'
                      : 'customer-return-status-filter__button'
                  }
                  onClick={() => {
                    setStatusFilter(
                      value,
                    )
                  }}
                >
                  {label}
                </button>
              ),
            )}
          </div>
        </div>

        {pageError && (
          <div
            className="customer-return-page-error"
            role="alert"
          >
            <AlertCircle
              size={18}
            />

            <span>
              {pageError}
            </span>

            <Button
              type="button"
              variant="ghost"
              size="sm"
              onClick={() => {
                void reload()
              }}
            >
              <RefreshCcw
                size={15}
              />

              Tentar novamente
            </Button>
          </div>
        )}

        {isLoading ? (
          <div className="customer-return-loading">
            <div className="dashboard-state__spinner" />

            <div>
              <strong>
                Carregando devoluções
              </strong>

              <p>
                Consultando os registros disponíveis.
              </p>
            </div>
          </div>
        ) : (
          <>
            <div className="customer-return-table-summary">
              <span>
                {
                  filteredReturns.length
                }
                {' '}
                {filteredReturns.length ===
                1
                  ? 'devolução exibida'
                  : 'devoluções exibidas'}
              </span>
            </div>

            <CustomerReturnTable
              customerReturns={
                filteredReturns
              }
              onDetails={
                setDetailsReturn
              }
              onCancel={
                openCancel
              }
            />
          </>
        )}
      </Card>

      {detailsReturn && (
        <CustomerReturnDetails
          customerReturn={
            detailsReturn
          }
          onClose={() => {
            setDetailsReturn(
              null,
            )
          }}
        />
      )}

      {cancelReturn && (
        <div
          className="customer-return-modal-backdrop"
          role="presentation"
        >
          <div
            className="customer-return-modal"
            role="dialog"
            aria-modal="true"
            aria-label="Cancelar devolução"
          >
            <form
              onSubmit={
                handleCancel
              }
            >
              <div className="customer-return-modal__header">
                <div>
                  <span>
                    Cancelamento
                  </span>

                  <h2>
                    Cancelar devolução
                  </h2>

                  <p>
                    {
                      cancelReturn
                        .reference_number
                    }
                    {' — '}
                    {
                      cancelReturn
                        .customer_name
                    }
                  </p>
                </div>
              </div>

              <div className="customer-return-modal__body">
                <p>
                  O registro será mantido
                  no histórico e os saldos
                  serão recalculados.
                </p>

                <label>
                  <span className="customer-return-field-label">
                    Justificativa
                  </span>

                  <textarea
                    autoFocus
                    value={
                      cancelJustification
                    }
                    maxLength={1000}
                    disabled={
                      isCancelling
                    }
                    placeholder="Informe o motivo do cancelamento..."
                    onChange={(
                      event,
                    ) => {
                      setCancelJustification(
                        event
                          .target
                          .value,
                      )
                    }}
                  />
                </label>

                {cancelError && (
                  <div
                    className="customer-return-error"
                    role="alert"
                  >
                    <AlertCircle
                      size={18}
                    />

                    {
                      cancelError
                    }
                  </div>
                )}
              </div>

              <div className="customer-return-modal__footer">
                <Button
                  type="button"
                  variant="secondary"
                  disabled={
                    isCancelling
                  }
                  onClick={
                    closeCancel
                  }
                >
                  Voltar
                </Button>

                <Button
                  type="submit"
                  variant="danger"
                  disabled={
                    isCancelling
                  }
                >
                  {isCancelling
                    ? 'Cancelando...'
                    : 'Confirmar cancelamento'}
                </Button>
              </div>
            </form>
          </div>
        </div>
      )}

      {toastMessage && (
        <Toast
          message={
            toastMessage
          }
          onClose={() => {
            setToastMessage(
              null,
            )
          }}
        />
      )}
      
    </div>
  )
}