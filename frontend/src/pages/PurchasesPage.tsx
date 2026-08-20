import {
  AlertCircle,
  Plus,
  ReceiptText,
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
  PurchaseForm,
} from '../components/purchases/PurchaseForm'
import {
  PurchaseItemsPanel,
} from '../components/purchases/PurchaseItemsPanel'
import {
  PurchaseTable,
} from '../components/purchases/PurchaseTable'
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
  Toast,
} from '../components/ui/Toast'

import {
  ApiError,
} from '../services/httpClient'
import {
  partService,
} from '../services/partService'
import {
  purchaseService,
} from '../services/purchaseService'
import {
  supplierService,
} from '../services/supplierService'

import type {
  Part,
} from '../types/part'
import type {
  Purchase,
  PurchaseCreatePayload,
  PurchaseFormValues,
  PurchaseStatus,
  PurchaseUpdatePayload,
} from '../types/purchase'
import type {
  Supplier,
} from '../types/supplier'

type PurchaseFilter =
  | 'all'
  | PurchaseStatus

type PurchaseModalMode =
  | 'create'
  | 'edit'
  | 'cancel'
  | null

function getPurchaseErrorMessage(
  error: unknown,
): string {
  if (error instanceof ApiError) {
    return error.message
  }

  return (
    'Não foi possível concluir a operação com compras.'
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

export function PurchasesPage() {
  const [
    purchases,
    setPurchases,
  ] = useState<Purchase[]>([])

  const [
    suppliers,
    setSuppliers,
  ] = useState<Supplier[]>([])

  const [
    parts,
    setParts,
  ] = useState<Part[]>([])

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
    searchValue,
    setSearchValue,
  ] = useState('')

  const [
    statusFilter,
    setStatusFilter,
  ] = useState<PurchaseFilter>(
    'all',
  )

  const [
    supplierFilter,
    setSupplierFilter,
  ] = useState('all')

  const [
    modalMode,
    setModalMode,
  ] = useState<PurchaseModalMode>(
    null,
  )

  const [
    selectedPurchase,
    setSelectedPurchase,
  ] = useState<
    Purchase | null
  >(null)

  const [
    itemsPurchase,
    setItemsPurchase,
  ] = useState<
    Purchase | null
  >(null)

  const [
    isSubmitting,
    setIsSubmitting,
  ] = useState(false)

  const [
    modalError,
    setModalError,
  ] = useState<string | null>(
    null,
  )

  const [
    cancelJustification,
    setCancelJustification,
  ] = useState('')

  const [
    toastMessage,
    setToastMessage,
  ] = useState<string | null>(
    null,
  )

  function replacePurchase(
    updatedPurchase: Purchase,
  ) {
    setPurchases(
      (currentPurchases) =>
        currentPurchases.map(
          (purchase) =>
            purchase.id ===
            updatedPurchase.id
              ? updatedPurchase
              : purchase,
        ),
    )
  }

  async function reloadData() {
    setIsLoading(true)
    setPageError(null)

    try {
      const [
        purchasesData,
        suppliersData,
        partsData,
      ] = await Promise.all([
        purchaseService.list(),
        supplierService.list(),
        partService.list(),
      ])

      setPurchases(
        purchasesData,
      )
      setSuppliers(
        suppliersData,
      )
      setParts(partsData)
    } catch (error) {
      setPageError(
        getPurchaseErrorMessage(
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

      Promise.all([
        purchaseService.list(),
        supplierService.list(),
        partService.list(),
      ])
        .then(
          ([
            purchasesData,
            suppliersData,
            partsData,
          ]) => {
            if (ignore) {
              return
            }

            setPurchases(
              purchasesData,
            )

            setSuppliers(
              suppliersData,
            )

            setParts(
              partsData,
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
              getPurchaseErrorMessage(
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

  const supplierNameById =
    useMemo(
      () =>
        new Map(
          suppliers.map(
            (supplier) => [
              supplier.id,
              supplier.name,
            ],
          ),
        ),
      [
        suppliers,
      ],
    )

  const filteredPurchases =
    useMemo(
      () => {
        const search =
          normalizeSearchValue(
            searchValue,
          )

        return purchases
          .filter(
            (purchase) => {
              if (
                statusFilter !==
                  'all' &&
                purchase.status !==
                  statusFilter
              ) {
                return false
              }

              if (
                supplierFilter !==
                  'all' &&
                purchase.supplier_id !==
                  Number(
                    supplierFilter,
                  )
              ) {
                return false
              }

              if (!search) {
                return true
              }

              const supplierName =
                supplierNameById.get(
                  purchase.supplier_id,
                ) ?? ''

              const searchableValue =
                [
                  purchase.invoice_number,
                  purchase.invoice_series ??
                    '',
                  supplierName,
                  purchase.notes ?? '',
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
          .sort(
            (left, right) =>
              new Date(
                right.created_at,
              ).getTime() -
              new Date(
                left.created_at,
              ).getTime(),
          )
      },
      [
        purchases,
        searchValue,
        statusFilter,
        supplierFilter,
        supplierNameById,
      ],
    )

  const pendingCount =
    purchases.filter(
      (purchase) =>
        purchase.status ===
        'PENDING',
    ).length

  const receivedCount =
    purchases.filter(
      (purchase) =>
        purchase.status ===
        'RECEIVED',
    ).length

  const activeSuppliers =
    suppliers.filter(
      (supplier) =>
        supplier.is_active,
    )

  function closeModal() {
    if (isSubmitting) {
      return
    }

    setModalMode(null)
    setSelectedPurchase(null)
    setModalError(null)
    setCancelJustification('')
  }

  function openCreateModal() {
    setSelectedPurchase(null)
    setModalError(null)
    setModalMode('create')
  }

  function openEditModal(
    purchase: Purchase,
  ) {
    setSelectedPurchase(
      purchase,
    )
    setModalError(null)
    setModalMode('edit')
  }

  function openCancelModal(
    purchase: Purchase,
  ) {
    setSelectedPurchase(
      purchase,
    )

    setCancelJustification(
      '',
    )

    setModalError(null)
    setModalMode('cancel')
  }

  async function handleSubmit(
    values:
      PurchaseFormValues,
  ) {
    setIsSubmitting(true)
    setModalError(null)

    try {
      if (
        modalMode === 'edit' &&
        selectedPurchase
      ) {
        const payload:
          PurchaseUpdatePayload = {}

        if (
          values.supplier_id !==
          selectedPurchase.supplier_id
        ) {
          payload.supplier_id =
            values.supplier_id
        }

        if (
          values.invoice_number !==
          selectedPurchase.invoice_number
        ) {
          payload.invoice_number =
            values.invoice_number
        }

        if (
          values.invoice_series !==
          selectedPurchase.invoice_series
        ) {
          payload.invoice_series =
            values.invoice_series
        }

        if (
          values.issue_date !==
          selectedPurchase.issue_date
        ) {
          payload.issue_date =
            values.issue_date
        }

        if (
          values.notes !==
          selectedPurchase.notes
        ) {
          payload.notes =
            values.notes
        }

        const updated =
          await purchaseService
            .update(
              selectedPurchase.id,
              payload,
            )

        replacePurchase(
          updated,
        )

        setToastMessage(
          'Compra atualizada com sucesso.',
        )

        setModalMode(null)
        setSelectedPurchase(null)
      } else {
        const payload:
          PurchaseCreatePayload = {
            supplier_id:
              values.supplier_id,

            invoice_number:
              values.invoice_number,

            invoice_series:
              values.invoice_series,

            issue_date:
              values.issue_date,

            status: 'PENDING',

            notes:
              values.notes,
          }

        const created =
          await purchaseService
            .create(payload)

        setPurchases(
          (currentPurchases) => [
            created,
            ...currentPurchases,
          ],
        )

        setModalMode(null)
        setSelectedPurchase(null)

        setItemsPurchase(
          created,
        )
      }
    } catch (error) {
      setModalError(
        getPurchaseErrorMessage(
          error,
        ),
      )
    } finally {
      setIsSubmitting(false)
    }
  }

  async function handleReceive(
    purchase: Purchase,
  ) {
    setPageError(null)

    try {
      const updated =
        await purchaseService
          .update(
            purchase.id,
            {
              status:
                'RECEIVED',
            },
          )

      replacePurchase(
        updated,
      )

      setToastMessage(
        'Compra marcada como recebida.',
      )

    } catch (error) {
      setPageError(
        getPurchaseErrorMessage(
          error,
        ),
      )
    }
  }

  async function handleCancelSubmit(
    event:
      FormEvent<HTMLFormElement>,
  ) {
    event.preventDefault()

    if (
      !selectedPurchase ||
      isSubmitting
    ) {
      return
    }

    const justification =
      cancelJustification.trim()

    if (!justification) {
      setModalError(
        'Informe a justificativa para cancelar a compra.',
      )

      return
    }

    setIsSubmitting(true)
    setModalError(null)

    try {
      const updated =
        await purchaseService
          .cancel(
            selectedPurchase.id,
            {
              justification,
            },
          )

      replacePurchase(
        updated,
      )

      setToastMessage(
        'Compra cancelada com sucesso.',
      )

      setModalMode(null)
      setSelectedPurchase(null)
      setCancelJustification('')
    } catch (error) {
      setModalError(
        getPurchaseErrorMessage(
          error,
        ),
      )
    } finally {
      setIsSubmitting(false)
    }
  }

  const selectedSupplier =
    itemsPurchase
      ? suppliers.find(
          (supplier) =>
            supplier.id ===
            itemsPurchase.supplier_id,
        ) ?? null
      : null

  return (
    <div className="page-stack">
      <PageHeader
        eyebrow="Operações"
        title="Compras"
        description="Gerencie as Notas Fiscais de compra e as peças com obrigação de devolução de casco."
        actions={
          <Button
            type="button"
            disabled={
              activeSuppliers.length ===
              0
            }
            onClick={
              openCreateModal
            }
          >
            <Plus
              size={17}
            />

            Nova compra
          </Button>
        }
      />

      <section
        className="purchase-summary"
        aria-label="Resumo das compras"
      >
        <Card
          className="purchase-summary__card"
          padding="md"
        >
          <span>
            Registradas
          </span>

          <strong>
            {purchases.length}
          </strong>
        </Card>

        <Card
          className="purchase-summary__card"
          padding="md"
        >
          <span>
            Pendentes
          </span>

          <strong>
            {pendingCount}
          </strong>

          <StatusBadge tone="attention">
            Aguardando
          </StatusBadge>
        </Card>

        <Card
          className="purchase-summary__card"
          padding="md"
        >
          <span>
            Recebidas
          </span>

          <strong>
            {receivedCount}
          </strong>

          <StatusBadge tone="success">
            Concluídas
          </StatusBadge>
        </Card>
      </section>

      <Card
        className="purchase-management"
        padding="none"
      >
        <div className="purchase-toolbar">
          <div className="purchase-search">
            <Search
              size={18}
              strokeWidth={1.8}
            />

            <input
              type="search"
              value={searchValue}
              placeholder="Buscar por NF, série ou fornecedor"
              aria-label="Buscar compras"
              onChange={(event) => {
                setSearchValue(
                  event.target.value,
                )
              }}
            />

            {searchValue && (
              <button
                type="button"
                className="purchase-search__clear"
                aria-label="Limpar busca"
                onClick={() => {
                  setSearchValue('')
                }}
              >
                <X
                  size={15}
                />
              </button>
            )}
          </div>

          <div className="purchase-toolbar__filters">
            <label className="purchase-supplier-filter">
              <span className="sr-only">
                Filtrar por fornecedor
              </span>

              <select
                value={supplierFilter}
                onChange={(event) => {
                  setSupplierFilter(
                    event.target.value,
                  )
                }}
              >
                <option value="all">
                  Todos os fornecedores
                </option>

                {suppliers.map(
                  (supplier) => (
                    <option
                      key={supplier.id}
                      value={supplier.id}
                    >
                      {supplier.name}
                    </option>
                  ),
                )}
              </select>
            </label>

            <div className="purchase-status-filter">
              {[
                [
                  'all',
                  'Todas',
                ],
                [
                  'PENDING',
                  'Pendentes',
                ],
                [
                  'RECEIVED',
                  'Recebidas',
                ],
                [
                  'CANCELLED',
                  'Canceladas',
                ],
              ].map(
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
                        ? 'purchase-status-filter__button purchase-status-filter__button--active'
                        : 'purchase-status-filter__button'
                    }
                    onClick={() => {
                      setStatusFilter(
                        value as
                          PurchaseFilter,
                      )
                    }}
                  >
                    {label}
                  </button>
                ),
              )}
            </div>
          </div>
        </div>

        {pageError && (
          <div
            className="purchase-page-error"
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
                void reloadData()
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
          <div className="purchase-loading">
            <div className="dashboard-state__spinner" />

            <div>
              <strong>
                Carregando compras
              </strong>

              <p>
                Consultando as operações
                registradas.
              </p>
            </div>
          </div>
        ) : (
          <>
            <div className="purchase-table-summary">
              <span>
                {filteredPurchases.length}
                {' '}
                {filteredPurchases.length ===
                  1
                  ? 'compra exibida'
                  : 'compras exibidas'}
              </span>
            </div>

            <PurchaseTable
              purchases={
                filteredPurchases
              }
              suppliers={
                suppliers
              }
              onItems={
                setItemsPurchase
              }
              onEdit={
                openEditModal
              }
              onReceive={
                (purchase) => {
                  void handleReceive(
                    purchase,
                  )
                }
              }
              onCancel={
                openCancelModal
              }
            />
          </>
        )}
      </Card>

      {(modalMode === 'create' ||
        modalMode === 'edit') && (
        <div
          className="purchase-modal-backdrop"
          role="presentation"
        >
          <div
            className="purchase-modal"
            role="dialog"
            aria-modal="true"
          >
            <PurchaseForm
              key={
                selectedPurchase
                  ? `purchase-${selectedPurchase.id}`
                  : 'new-purchase'
              }
              purchase={
                selectedPurchase
              }
              suppliers={
                suppliers
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
          </div>
        </div>
      )}

      {modalMode ===
        'cancel' &&
        selectedPurchase && (
          <div
            className="purchase-modal-backdrop"
            role="presentation"
          >
            <div
              className="purchase-modal purchase-modal--compact"
              role="dialog"
              aria-modal="true"
              aria-labelledby="purchase-cancel-title"
            >
              <form
                className="purchase-cancel"
                onSubmit={
                  handleCancelSubmit
                }
              >
                <header className="purchase-cancel__header">
                  <div>
                    <span className="purchase-form__eyebrow">
                      Cancelamento
                    </span>

                    <h2
                      id="purchase-cancel-title"
                    >
                      Cancelar compra
                    </h2>

                    <p>
                      A compra permanecerá
                      preservada no histórico
                      e na auditoria do SIGC.
                    </p>
                  </div>

                  <button
                    type="button"
                    className="purchase-form__close"
                    aria-label="Fechar cancelamento"
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

                <div className="purchase-cancel__body">
                  <div className="purchase-cancel__purchase">
                    <div className="purchase-cancel__icon">
                      <ReceiptText
                        size={22}
                        strokeWidth={1.7}
                      />
                    </div>

                    <div>
                      <strong>
                        NF {
                          selectedPurchase
                            .invoice_number
                        }
                      </strong>

                      <span>
                        {supplierNameById.get(
                          selectedPurchase
                            .supplier_id,
                        ) ??
                          `Fornecedor #${selectedPurchase.supplier_id}`}
                      </span>
                    </div>
                  </div>

                  <label className="purchase-field">
                    <span className="purchase-field__label">
                      Justificativa
                    </span>

                    <textarea
                      className="purchase-field__textarea"
                      rows={4}
                      maxLength={1000}
                      required
                      autoFocus
                      disabled={
                        isSubmitting
                      }
                      value={
                        cancelJustification
                      }
                      onChange={(event) => {
                        setCancelJustification(
                          event.target.value,
                        )
                      }}
                    />

                    <span className="purchase-field__counter">
                      {cancelJustification.length}
                      /1000
                    </span>
                  </label>

                  {modalError && (
                    <div
                      className="purchase-form__error"
                      role="alert"
                    >
                      {modalError}
                    </div>
                  )}
                </div>

                <footer className="purchase-form__actions">
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
                    Cancelar
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
                      : 'Cancelar compra'}
                  </Button>
                </footer>
              </form>
            </div>
          </div>
        )}

      {itemsPurchase && (
        <PurchaseItemsPanel
          purchase={
            itemsPurchase
          }
          supplier={
            selectedSupplier
          }
          parts={parts}
          onClose={() => {
            setItemsPurchase(
              null,
            )
          }}
          onComplete={() => {
            setItemsPurchase(
              null,
            )

            setToastMessage(
              'Compra e itens registrados com sucesso.',
            )
          }}
        />
      )}

      {toastMessage && (
        <Toast
          message={toastMessage}
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