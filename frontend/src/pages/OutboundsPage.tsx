import {
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
  OutboundForm,
} from '../components/outbounds/OutboundForm'

import {
  OutboundItemsPanel,
} from '../components/outbounds/OutboundItemsPanel'

import {
  OutboundTable,
} from '../components/outbounds/OutboundTable'

import {
  Button,
} from '../components/ui/Button'

import {
  Card,
} from '../components/ui/Card'

import {
  FeedbackMessage,
} from '../components/ui/FeedbackMessage'

import {
  PageHeader,
} from '../components/ui/PageHeader'

import {
  StatusBadge,
} from '../components/ui/StatusBadge'

import {
  Toast,
} from '../components/ui/Toast'

import {
  ApiError,
  httpClient,
} from '../services/httpClient'

import {
  outboundService,
} from '../services/outboundService'

import type {
  Outbound,
  OutboundDestinationType,
  OutboundFormValues,
  OutboundStatus,
} from '../types/outbound'

import type {
  Part,
} from '../types/part'

type StatusFilter =
  | 'ALL'
  | OutboundStatus

type DestinationFilter =
  | 'ALL'
  | OutboundDestinationType

type ModalMode =
  | 'create'
  | 'edit'
  | 'cancel'
  | null

function getErrorMessage(
  error: unknown,
): string {
  if (
    error instanceof ApiError
  ) {
    return error.message
  }

  return (
    'Não foi possível concluir a operação com as saídas.'
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
      ''
    )
  }

  return (
    outbound.sales_invoice_number ??
    ''
  )
}

export function OutboundsPage() {
  const [
    outbounds,
    setOutbounds,
  ] = useState<Outbound[]>(
    [],
  )

  const [
    parts,
    setParts,
  ] = useState<Part[]>(
    [],
  )

  const [
    isLoading,
    setIsLoading,
  ] = useState(true)

  const [
    isRefreshing,
    setIsRefreshing,
  ] = useState(false)

  const [
    pageError,
    setPageError,
  ] = useState<string | null>(
    null,
  )

  const [
    modalError,
    setModalError,
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
    modalMode,
    setModalMode,
  ] = useState<ModalMode>(
    null,
  )

  const [
    selectedOutbound,
    setSelectedOutbound,
  ] = useState<Outbound | null>(
    null,
  )

  const [
    itemsOutbound,
    setItemsOutbound,
  ] = useState<Outbound | null>(
    null,
  )

  const [
    isSubmitting,
    setIsSubmitting,
  ] = useState(false)

  const [
    searchValue,
    setSearchValue,
  ] = useState('')

  const [
    statusFilter,
    setStatusFilter,
  ] = useState<StatusFilter>(
    'ALL',
  )

  const [
    destinationFilter,
    setDestinationFilter,
  ] = useState<DestinationFilter>(
    'ALL',
  )

  const [
    cancelJustification,
    setCancelJustification,
  ] = useState('')

  useEffect(
    () => {
      let ignore = false

      Promise.all([
        outboundService.list(),
        httpClient.get<Part[]>(
          '/parts',
        ),
      ])
        .then(
          ([
            outboundData,
            partData,
          ]) => {
            if (ignore) {
              return
            }

            setOutbounds(
              outboundData,
            )

            setParts(
              partData,
            )

            setPageError(null)
          },
        )
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
          if (ignore) {
            return
          }

          setIsLoading(false)
        })

      return () => {
        ignore = true
      }
    },
    [],
  )

  async function handleRefresh() {
    if (isRefreshing) {
      return
    }

    setIsRefreshing(true)
    setPageError(null)

    try {
      const [
        outboundData,
        partData,
      ] = await Promise.all([
        outboundService.list(),
        httpClient.get<Part[]>(
          '/parts',
        ),
      ])

      setOutbounds(
        outboundData,
      )

      setParts(
        partData,
      )
    } catch (error) {
      setPageError(
        getErrorMessage(
          error,
        ),
      )
    } finally {
      setIsRefreshing(false)
    }
  }

  function openCreateModal() {
    setSelectedOutbound(null)
    setModalError(null)
    setModalMode('create')
  }

  function openEditModal(
    outbound: Outbound,
  ) {
    setSelectedOutbound(
      outbound,
    )

    setModalError(null)
    setModalMode('edit')
  }

  function openCancelModal(
    outbound: Outbound,
  ) {
    setSelectedOutbound(
      outbound,
    )

    setCancelJustification('')
    setModalError(null)
    setModalMode('cancel')
  }

  function closeModal() {
    if (isSubmitting) {
      return
    }

    setModalMode(null)
    setSelectedOutbound(null)
    setCancelJustification('')
    setModalError(null)
  }

  function replaceOutbound(
    updated: Outbound,
  ) {
    setOutbounds(
      (currentOutbounds) =>
        currentOutbounds.map(
          (outbound) =>
            outbound.id ===
            updated.id
              ? updated
              : outbound,
        ),
    )
  }

  async function handleSubmit(
    values:
      OutboundFormValues,
  ) {
    if (isSubmitting) {
      return
    }

    setIsSubmitting(true)
    setModalError(null)

    try {
      if (
        modalMode === 'edit' &&
        selectedOutbound
      ) {
        const updated =
          await outboundService
            .update(
              selectedOutbound.id,
              {
                destination_type:
                  values.destination_type,

                work_order_number:
                  values.destination_type ===
                  'WORK_ORDER'
                    ? values.reference_number
                    : null,

                sales_invoice_number:
                  values.destination_type ===
                  'SALE'
                    ? values.reference_number
                    : null,

                customer_name:
                  values.customer_name,
              },
            )

        replaceOutbound(
          updated,
        )

        setToastMessage(
          'Saída atualizada com sucesso.',
        )

        setModalMode(null)
        setSelectedOutbound(null)

        return
      }

      const created =
        await outboundService
          .create({
            destination_type:
              values.destination_type,

            work_order_number:
              values.destination_type ===
              'WORK_ORDER'
                ? values.reference_number
                : null,

            sales_invoice_number:
              values.destination_type ===
              'SALE'
                ? values.reference_number
                : null,

            customer_name:
              values.customer_name,

            status:
              'ACTIVE',
          })

      setOutbounds(
        (currentOutbounds) => [
          created,
          ...currentOutbounds,
        ],
      )

      setModalMode(null)
      setSelectedOutbound(null)

      setItemsOutbound(
        created,
      )
    } catch (error) {
      setModalError(
        getErrorMessage(
          error,
        ),
      )
    } finally {
      setIsSubmitting(false)
    }
  }

  async function handleCancelSubmit(
    event:
      FormEvent<HTMLFormElement>,
  ) {
    event.preventDefault()

    if (
      !selectedOutbound ||
      isSubmitting
    ) {
      return
    }

    const justification =
      cancelJustification.trim()

    if (!justification) {
      return
    }

    setIsSubmitting(true)
    setModalError(null)

    try {
      const updated =
        await outboundService
          .cancel(
            selectedOutbound.id,
            {
              justification,
            },
          )

      replaceOutbound(
        updated,
      )

      setToastMessage(
        'Saída cancelada com sucesso.',
      )

      setModalMode(null)
      setSelectedOutbound(null)
      setCancelJustification('')
    } catch (error) {
      setModalError(
        getErrorMessage(
          error,
        ),
      )
    } finally {
      setIsSubmitting(false)
    }
  }

  const sortedOutbounds =
    useMemo(
      () =>
        [...outbounds].sort(
          (left, right) =>
            new Date(
              right.created_at,
            ).getTime() -
            new Date(
              left.created_at,
            ).getTime(),
        ),
      [
        outbounds,
      ],
    )

  const filteredOutbounds =
    useMemo(
      () => {
        const normalizedSearch =
          searchValue
            .trim()
            .toLocaleLowerCase(
              'pt-BR',
            )

        return sortedOutbounds.filter(
          (outbound) => {
            if (
              statusFilter !==
                'ALL' &&
              outbound.status !==
                statusFilter
            ) {
              return false
            }

            if (
              destinationFilter !==
                'ALL' &&
              outbound.destination_type !==
                destinationFilter
            ) {
              return false
            }

            if (
              !normalizedSearch
            ) {
              return true
            }

            const searchable =
              [
                outbound.id,
                outbound.customer_name,
                outbound
                  .work_order_number,
                outbound
                  .sales_invoice_number,
              ]
                .filter(
                  (value) =>
                    value !== null &&
                    value !== undefined,
                )
                .join(' ')
                .toLocaleLowerCase(
                  'pt-BR',
                )

            return searchable.includes(
              normalizedSearch,
            )
          },
        )
      },
      [
        destinationFilter,
        searchValue,
        sortedOutbounds,
        statusFilter,
      ],
    )

  const activeCount =
    outbounds.filter(
      (outbound) =>
        outbound.status ===
        'ACTIVE',
    ).length

  const cancelledCount =
    outbounds.filter(
      (outbound) =>
        outbound.status ===
        'CANCELLED',
    ).length

  const workshopCount =
    outbounds.filter(
      (outbound) =>
        outbound.status ===
          'ACTIVE' &&
        outbound.destination_type ===
          'WORK_ORDER',
    ).length

  const saleCount =
    outbounds.filter(
      (outbound) =>
        outbound.status ===
          'ACTIVE' &&
        outbound.destination_type ===
          'SALE',
    ).length

  return (
    <div className="page-stack">
      <PageHeader
        eyebrow="Movimentações"
        title="Saídas"
        description="Registre peças destinadas à oficina ou ao balcão, mantendo a rastreabilidade do estoque e dos cascos."
        actions={
          <Button
            type="button"
            onClick={
              openCreateModal
            }
          >
            <Plus
              size={17}
            />

            Nova saída
          </Button>
        }
      />

      <section
        className="outbound-summary"
        aria-label="Resumo das saídas"
      >
        <Card
          className="outbound-summary__card"
          padding="md"
        >
          <span>
            Registradas
          </span>

          <strong>
            {outbounds.length}
          </strong>
        </Card>

        <Card
          className="outbound-summary__card"
          padding="md"
        >
          <span>
            Ativas
          </span>

          <strong>
            {activeCount}
          </strong>

          <StatusBadge tone="success">
            Em andamento
          </StatusBadge>
        </Card>

        <Card
          className="outbound-summary__card"
          padding="md"
        >
          <span>
            Oficina
          </span>

          <strong>
            {workshopCount}
          </strong>

          <StatusBadge tone="info">
            OS
          </StatusBadge>
        </Card>

        <Card
          className="outbound-summary__card"
          padding="md"
        >
          <span>
            Balcão
          </span>

          <strong>
            {saleCount}
          </strong>

          <StatusBadge tone="info">
            NF
          </StatusBadge>
        </Card>

        <Card
          className="outbound-summary__card"
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

      {pageError && (
        <FeedbackMessage
          message={pageError}
          tone="error"
        />
      )}

      <Card
        className="outbound-management"
        padding="none"
      >
        <div className="outbound-toolbar">
          <div className="outbound-search">
            <Search
              size={18}
              strokeWidth={1.8}
              aria-hidden="true"
            />

            <input
              type="search"
              value={searchValue}
              placeholder="Buscar por cliente, OS, NF ou ID"
              aria-label="Buscar saídas"
              onChange={(event) => {
                setSearchValue(
                  event.target.value,
                )
              }}
            />
          </div>

          <div className="outbound-toolbar__right">
            <label className="outbound-destination-filter">
              <span>
                Destino
              </span>

              <select
                value={
                  destinationFilter
                }
                onChange={(event) => {
                  setDestinationFilter(
                    event.target
                      .value as DestinationFilter,
                  )
                }}
              >
                <option value="ALL">
                  Todos
                </option>

                <option value="WORK_ORDER">
                  Oficina
                </option>

                <option value="SALE">
                  Balcão
                </option>
              </select>
            </label>

            <Button
              type="button"
              variant="ghost"
              size="sm"
              disabled={
                isRefreshing
              }
              onClick={
                handleRefresh
              }
            >
              <RefreshCcw
                size={16}
                className={
                  isRefreshing
                    ? 'outbound-refresh-icon outbound-refresh-icon--spinning'
                    : 'outbound-refresh-icon'
                }
              />

              {isRefreshing
                ? 'Atualizando...'
                : 'Atualizar'}
            </Button>
          </div>
        </div>

        <div className="outbound-status-filter">
          <button
            type="button"
            className={
              statusFilter ===
              'ALL'
                ? 'outbound-status-filter__button outbound-status-filter__button--active'
                : 'outbound-status-filter__button'
            }
            onClick={() => {
              setStatusFilter(
                'ALL',
              )
            }}
          >
            Todas

            <span>
              {outbounds.length}
            </span>
          </button>

          <button
            type="button"
            className={
              statusFilter ===
              'ACTIVE'
                ? 'outbound-status-filter__button outbound-status-filter__button--active'
                : 'outbound-status-filter__button'
            }
            onClick={() => {
              setStatusFilter(
                'ACTIVE',
              )
            }}
          >
            Ativas

            <span>
              {activeCount}
            </span>
          </button>

          <button
            type="button"
            className={
              statusFilter ===
              'CANCELLED'
                ? 'outbound-status-filter__button outbound-status-filter__button--active'
                : 'outbound-status-filter__button'
            }
            onClick={() => {
              setStatusFilter(
                'CANCELLED',
              )
            }}
          >
            Canceladas

            <span>
              {cancelledCount}
            </span>
          </button>
        </div>

        <div className="outbound-table-summary">
          <span>
            {filteredOutbounds.length}
            {' '}
            {filteredOutbounds.length ===
            1
              ? 'registro encontrado'
              : 'registros encontrados'}
          </span>
        </div>

        {isLoading ? (
          <div className="outbound-loading">
            <div className="dashboard-state__spinner" />

            <span>
              Carregando saídas...
            </span>
          </div>
        ) : (
          <OutboundTable
            outbounds={
              filteredOutbounds
            }
            onItems={(outbound) => {
              setItemsOutbound(
                outbound,
              )
            }}
            onEdit={
              openEditModal
            }
            onCancel={
              openCancelModal
            }
          />
        )}
      </Card>

      {(modalMode ===
        'create' ||
        modalMode ===
          'edit') && (
        <div
          className="outbound-modal-backdrop"
          role="presentation"
        >
          <section
            className="outbound-modal"
            role="dialog"
            aria-modal="true"
          >
            <OutboundForm
              outbound={
                modalMode ===
                'edit'
                  ? selectedOutbound
                  : null
              }
              isSubmitting={
                isSubmitting
              }
              errorMessage={
                modalError
              }
              onCancel={
                closeModal
              }
              onSubmit={
                handleSubmit
              }
            />
          </section>
        </div>
      )}

      {modalMode ===
        'cancel' &&
        selectedOutbound && (
        <div
          className="outbound-modal-backdrop"
          role="presentation"
        >
          <section
            className="outbound-modal outbound-modal--compact"
            role="dialog"
            aria-modal="true"
            aria-labelledby="outbound-cancel-title"
          >
            <form
              className="outbound-cancel"
              onSubmit={
                handleCancelSubmit
              }
            >
              <header className="outbound-cancel__header">
                <div>
                  <span>
                    Operação sensível
                  </span>

                  <h2
                    id="outbound-cancel-title"
                  >
                    Cancelar saída
                  </h2>

                  <p>
                    {getReference(
                      selectedOutbound,
                    )}
                    {' · '}
                    {
                      selectedOutbound
                        .customer_name
                    }
                  </p>
                </div>

                <button
                  type="button"
                  className="outbound-form__close"
                  aria-label="Fechar"
                  disabled={
                    isSubmitting
                  }
                  onClick={
                    closeModal
                  }
                >
                  <X
                    size={20}
                    strokeWidth={1.8}
                  />
                </button>
              </header>

              {modalError && (
                <div className="outbound-cancel__feedback">
                  <FeedbackMessage
                    message={
                      modalError
                    }
                    tone="error"
                  />
                </div>
              )}

              <div className="outbound-cancel__body">
                <div className="outbound-cancel__warning">
                  <strong>
                    O estoque consumido por esta saída será restaurado.
                  </strong>

                  <p>
                    O cancelamento ficará registrado na auditoria e exige uma justificativa.
                  </p>
                </div>

                <label className="outbound-field">
                  <span className="outbound-field__label">
                    Justificativa
                  </span>

                  <textarea
                    className="outbound-field__textarea"
                    value={
                      cancelJustification
                    }
                    required
                    autoFocus
                    disabled={
                      isSubmitting
                    }
                    placeholder="Informe o motivo do cancelamento"
                    onChange={(event) => {
                      setCancelJustification(
                        event.target.value,
                      )
                    }}
                  />
                </label>
              </div>

              <footer className="outbound-cancel__actions">
                <Button
                  type="button"
                  variant="secondary"
                  disabled={
                    isSubmitting
                  }
                  onClick={
                    closeModal
                  }
                >
                  Voltar
                </Button>

                <Button
                  type="submit"
                  variant="danger"
                  disabled={
                    isSubmitting ||
                    !cancelJustification
                      .trim()
                  }
                >
                  {isSubmitting
                    ? 'Cancelando...'
                    : 'Cancelar saída'}
                </Button>
              </footer>
            </form>
          </section>
        </div>
      )}

      {itemsOutbound && (
        <OutboundItemsPanel
          outbound={
            itemsOutbound
          }
          parts={parts}
          onClose={() => {
            setItemsOutbound(
              null,
            )
          }}
          onComplete={() => {
            setItemsOutbound(
              null,
            )

            setToastMessage(
              'Saída e itens registrados com sucesso.',
            )
          }}
        />
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