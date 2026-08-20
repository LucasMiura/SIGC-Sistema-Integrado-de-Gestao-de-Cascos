import {
  AlertCircle,
  Boxes,
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
  PartForm,
} from '../components/parts/PartForm'
import {
  PartTable,
} from '../components/parts/PartTable'
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
  partService,
} from '../services/partService'
import {
  supplierService,
} from '../services/supplierService'

import type {
  Part,
  PartCreatePayload,
  PartFormValues,
  PartUpdatePayload,
} from '../types/part'
import type {
  Supplier,
} from '../types/supplier'

type PartStatusFilter =
  | 'active'
  | 'inactive'

type PartModalMode =
  | 'create'
  | 'edit'
  | 'deactivate'
  | null

function getPartErrorMessage(
  error: unknown,
): string {
  if (error instanceof ApiError) {
    return error.message
  }

  return (
    'Não foi possível concluir a operação com peças.'
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

export function PartsPage() {
  const [
    parts,
    setParts,
  ] = useState<Part[]>([])

  const [
    suppliers,
    setSuppliers,
  ] = useState<Supplier[]>([])

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
  ] = useState<
    PartStatusFilter
  >('active')

  const [
    supplierFilter,
    setSupplierFilter,
  ] = useState('all')

  const [
    modalMode,
    setModalMode,
  ] = useState<
    PartModalMode
  >(null)

  const [
    selectedPart,
    setSelectedPart,
  ] = useState<
    Part | null
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
    deactivateJustification,
    setDeactivateJustification,
  ] = useState('')

  function replacePart(
    updatedPart: Part,
  ) {
    setParts(
      (currentParts) =>
        currentParts.map(
          (part) =>
            part.id ===
            updatedPart.id
              ? updatedPart
              : part,
        ),
    )
  }

  async function reloadData() {
    setIsLoading(true)
    setPageError(null)

    try {
      const [
        partsData,
        suppliersData,
      ] = await Promise.all([
        partService.list(),
        supplierService.list(),
      ])

      setParts(partsData)
      setSuppliers(
        suppliersData,
      )
    } catch (error) {
      setPageError(
        getPartErrorMessage(
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
        partService.list(),
        supplierService.list(),
      ])
        .then(
          ([
            partsData,
            suppliersData,
          ]) => {
            if (ignore) {
              return
            }

            setParts(partsData)
            setSuppliers(
              suppliersData,
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
              getPartErrorMessage(
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

  const filteredParts =
    useMemo(
        () => {
        const search =
            normalizeSearchValue(
            searchValue,
            )

        return parts
            .filter(
            (part) => {
                const matchesStatus =
                statusFilter ===
                    'active'
                    ? part.is_active
                    : !part.is_active

                if (!matchesStatus) {
                return false
                }

                const matchesSupplier =
                supplierFilter ===
                    'all' ||
                part.supplier_id ===
                    Number(
                    supplierFilter,
                    )

                if (!matchesSupplier) {
                return false
                }

                if (!search) {
                return true
                }

                const supplierName =
                supplierNameById.get(
                    part.supplier_id,
                ) ?? ''

                const searchableValue =
                [
                    part.part_code,
                    part.name,
                    part.description ?? '',
                    supplierName,
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
        parts,
        searchValue,
        statusFilter,
        supplierFilter,
        supplierNameById,
        ],
    )

  const activeCount =
    parts.filter(
      (part) =>
        part.is_active,
    ).length

  const inactiveCount =
    parts.length -
    activeCount

  const activeSuppliersCount =
    suppliers.filter(
      (supplier) =>
        supplier.is_active,
    ).length

  function closeModal() {
    if (isSubmitting) {
      return
    }

    setModalMode(null)
    setSelectedPart(null)
    setModalError(null)
    setDeactivateJustification('')
  }

  function openCreateModal() {
    setSelectedPart(null)
    setModalError(null)
    setModalMode('create')
  }

  function openEditModal(
    part: Part,
  ) {
    setSelectedPart(part)
    setModalError(null)
    setModalMode('edit')
  }

  function openDeactivateModal(
    part: Part,
  ) {
    setSelectedPart(part)
    setModalError(null)

    setDeactivateJustification(
      '',
    )

    setModalMode(
      'deactivate',
    )
  }

  async function handlePartSubmit(
    values: PartFormValues,
  ) {
    setIsSubmitting(true)
    setModalError(null)

    try {
      if (
        modalMode === 'edit' &&
        selectedPart
      ) {
        const payload:
          PartUpdatePayload = {}

        if (
          values.supplier_id !==
          selectedPart.supplier_id
        ) {
          payload.supplier_id =
            values.supplier_id
        }

        if (
          values.part_code !==
          selectedPart.part_code
        ) {
          payload.part_code =
            values.part_code
        }

        if (
          values.name !==
          selectedPart.name
        ) {
          payload.name =
            values.name
        }

        if (
          values.description !==
          selectedPart.description
        ) {
          payload.description =
            values.description
        }

        if (
          values.return_deadline_days !==
          selectedPart.return_deadline_days
        ) {
          payload.return_deadline_days =
            values.return_deadline_days
        }

        const updatedPart =
          await partService.update(
            selectedPart.id,
            payload,
          )

        replacePart(
          updatedPart,
        )
      } else {
        const payload:
          PartCreatePayload = {
            supplier_id:
              values.supplier_id,

            part_code:
              values.part_code,

            name:
              values.name,

            description:
              values.description,

            return_deadline_days:
              values.return_deadline_days,
          }

        const createdPart =
          await partService.create(
            payload,
          )

        setParts(
          (currentParts) => [
            ...currentParts,
            createdPart,
          ],
        )
      }

      setModalMode(null)
      setSelectedPart(null)
    } catch (error) {
      setModalError(
        getPartErrorMessage(
          error,
        ),
      )
    } finally {
      setIsSubmitting(false)
    }
  }

  async function handleActivate(
    part: Part,
  ) {
    setPageError(null)

    try {
      const updatedPart =
        await partService.activate(
          part.id,
        )

      replacePart(
        updatedPart,
      )
    } catch (error) {
      setPageError(
        getPartErrorMessage(
          error,
        ),
      )
    }
  }

  async function handleDeactivateSubmit(
    event:
      FormEvent<HTMLFormElement>,
  ) {
    event.preventDefault()

    if (
      !selectedPart ||
      isSubmitting
    ) {
      return
    }

    const justification =
      deactivateJustification
        .trim()

    if (!justification) {
      setModalError(
        'Informe a justificativa para desativar a peça.',
      )

      return
    }

    setIsSubmitting(true)
    setModalError(null)

    try {
      const updatedPart =
        await partService.deactivate(
          selectedPart.id,
          {
            justification,
          },
        )

      replacePart(
        updatedPart,
      )

      setModalMode(null)
      setSelectedPart(null)

      setDeactivateJustification(
        '',
      )
    } catch (error) {
      setModalError(
        getPartErrorMessage(
          error,
        ),
      )
    } finally {
      setIsSubmitting(false)
    }
  }

  return (
    <div className="page-stack">
      <PageHeader
        eyebrow="Cadastros"
        title="Peças"
        description="Gerencie as peças sujeitas à devolução de casco e seus prazos padrão."
        actions={
          <Button
            type="button"
            disabled={
              activeSuppliersCount === 0
            }
            onClick={
              openCreateModal
            }
          >
            <Plus
              size={17}
            />

            Nova peça
          </Button>
        }
      />

      <section
        className="part-summary"
        aria-label="Resumo das peças"
      >
        <Card
          className="part-summary__card"
          padding="md"
        >
          <span>
            Cadastradas
          </span>

          <strong>
            {parts.length}
          </strong>
        </Card>

        <Card
          className="part-summary__card"
          padding="md"
        >
          <span>
            Ativas
          </span>

          <strong>
            {activeCount}
          </strong>

          <StatusBadge tone="success">
            Em uso
          </StatusBadge>
        </Card>

        <Card
          className="part-summary__card"
          padding="md"
        >
          <span>
            Inativas
          </span>

          <strong>
            {inactiveCount}
          </strong>

          <StatusBadge tone="neutral">
            Arquivadas
          </StatusBadge>
        </Card>
      </section>

      <Card
        className="part-management"
        padding="none"
      >
        <div className="part-toolbar">
          <div className="part-search">
            <Search
              size={18}
              strokeWidth={1.8}
              aria-hidden="true"
            />

            <input
              type="search"
              value={searchValue}
              placeholder="Buscar por código, peça ou fornecedor"
              aria-label="Buscar peças"
              onChange={(event) => {
                setSearchValue(
                  event.target.value,
                )
              }}
            />

            {searchValue && (
              <button
                type="button"
                className="part-search__clear"
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

          <div className="part-toolbar__filters">
            <label className="part-supplier-filter">
              <span className="sr-only">
                Filtrar por fornecedor
              </span>

              <select
                value={
                  supplierFilter
                }
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
                      key={
                        supplier.id
                      }
                      value={
                        supplier.id
                      }
                    >
                      {supplier.name}
                    </option>
                  ),
                )}
              </select>
            </label>

            <div
              className="part-status-filter"
              aria-label="Filtrar peças por status"
            >
              <button
                type="button"
                className={
                  statusFilter ===
                    'active'
                    ? 'part-status-filter__button part-status-filter__button--active'
                    : 'part-status-filter__button'
                }
                onClick={() => {
                  setStatusFilter(
                    'active',
                  )
                }}
              >
                Ativas
              </button>

              <button
                type="button"
                className={
                  statusFilter ===
                    'inactive'
                    ? 'part-status-filter__button part-status-filter__button--active'
                    : 'part-status-filter__button'
                }
                onClick={() => {
                  setStatusFilter(
                    'inactive',
                  )
                }}
              >
                Inativas
              </button>
            </div>
          </div>
        </div>

        {pageError && (
          <div
            className="part-page-error"
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
          <div className="part-loading">
            <div className="dashboard-state__spinner" />

            <div>
              <strong>
                Carregando peças
              </strong>

              <p>
                Consultando os cadastros
                disponíveis.
              </p>
            </div>
          </div>
        ) : (
          <>
            <div className="part-table-summary">
              <span>
                {filteredParts.length}
                {' '}
                {filteredParts.length === 1
                  ? 'peça exibida'
                  : 'peças exibidas'}
              </span>
            </div>

            <PartTable
              parts={
                filteredParts
              }
              suppliers={
                suppliers
              }
              onEdit={
                openEditModal
              }
              onActivate={
                (part) => {
                  void handleActivate(
                    part,
                  )
                }
              }
              onDeactivate={
                openDeactivateModal
              }
            />
          </>
        )}
      </Card>

      {(modalMode === 'create' ||
        modalMode === 'edit') && (
        <div
          className="part-modal-backdrop"
          role="presentation"
        >
          <div
            className="part-modal"
            role="dialog"
            aria-modal="true"
            aria-label={
              modalMode === 'edit'
                ? 'Editar peça'
                : 'Cadastrar peça'
            }
          >
            <PartForm
              key={
                selectedPart
                  ? `edit-${selectedPart.id}`
                  : 'create'
              }
              part={
                selectedPart
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
                handlePartSubmit
              }
            />
          </div>
        </div>
      )}

      {modalMode ===
        'deactivate' &&
        selectedPart && (
          <div
            className="part-modal-backdrop"
            role="presentation"
          >
            <div
              className="part-modal part-modal--compact"
              role="dialog"
              aria-modal="true"
              aria-labelledby="part-deactivate-title"
            >
              <form
                className="part-deactivate"
                onSubmit={handleDeactivateSubmit}
              >
                <header className="part-deactivate__header">
                  <div>
                    <span className="part-form__eyebrow">
                      Desativação
                    </span>

                    <h2 id="part-deactivate-title">
                      Desativar peça
                    </h2>

                    <p>
                      A peça permanecerá no histórico do SIGC
                      e poderá ser reativada futuramente.
                    </p>
                  </div>

                  <button
                    type="button"
                    className="part-form__close"
                    aria-label="Fechar desativação"
                    disabled={isSubmitting}
                    onClick={closeModal}
                  >
                    <X
                      size={20}
                      strokeWidth={1.8}
                    />
                  </button>
                </header>

                <div className="part-deactivate__body">
                  <div className="part-deactivate__part">
                    <div className="part-deactivate__icon">
                      <Boxes
                        size={22}
                        strokeWidth={1.7}
                      />
                    </div>

                    <div className="part-deactivate__identity">
                      <strong>
                        {selectedPart.name}
                      </strong>

                      <span>
                        {selectedPart.part_code}
                      </span>
                    </div>
                  </div>

                  <label className="part-field">
                    <span className="part-field__label">
                      Justificativa
                    </span>

                    <textarea
                      className="part-field__textarea"
                      rows={4}
                      maxLength={1000}
                      autoFocus
                      required
                      value={deactivateJustification}
                      disabled={isSubmitting}
                      onChange={(event) => {
                        setDeactivateJustification(
                          event.target.value,
                        )
                      }}
                    />

                    <span className="part-field__counter">
                      {deactivateJustification.length}/1000
                    </span>
                  </label>

                  {modalError && (
                    <div
                      className="part-form__error"
                      role="alert"
                    >
                      {modalError}
                    </div>
                  )}
                </div>

                <footer className="part-form__actions">
                  <Button
                    type="button"
                    variant="secondary"
                    disabled={isSubmitting}
                    onClick={closeModal}
                  >
                    Cancelar
                  </Button>

                  <Button
                    type="submit"
                    variant="danger"
                    disabled={
                      isSubmitting ||
                      !deactivateJustification.trim()
                    }
                  >
                    {isSubmitting
                      ? 'Desativando...'
                      : 'Desativar peça'}
                  </Button>
                </footer>
              </form>
            </div>
          </div>
        )}
    </div>
  )
}