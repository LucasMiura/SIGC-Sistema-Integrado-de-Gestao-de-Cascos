import {
  AlertCircle,
  Building2,
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
  SupplierForm,
} from '../components/suppliers/SupplierForm'
import {
  SupplierTable,
} from '../components/suppliers/SupplierTable'
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
  SupplierContactsPanel,
} from '../components/suppliers/SupplierContactsPanel'
import {
  ApiError,
} from '../services/httpClient'
import {
  supplierService,
} from '../services/supplierService'
import type {
  Supplier,
  SupplierCreatePayload,
} from '../types/supplier'

type SupplierStatusFilter =
  | 'all'
  | 'active'
  | 'inactive'

type SupplierModalMode =
  | 'create'
  | 'edit'
  | 'deactivate'
  | null

function getSupplierErrorMessage(
  error: unknown,
): string {
  if (
    error instanceof ApiError
  ) {
    return error.message
  }

  return (
    'Não foi possível concluir a operação com fornecedores.'
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

export function SuppliersPage() {
  const [
    suppliers,
    setSuppliers,
  ] = useState<Supplier[]>([])

  const [
    contactsSupplier,
    setContactsSupplier,
  ] = useState<
    Supplier | null
  >(null)

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
  ] =
    useState<SupplierStatusFilter>(
      'all',
    )

  const [
    modalMode,
    setModalMode,
  ] =
    useState<SupplierModalMode>(
      null,
    )

  const [
    selectedSupplier,
    setSelectedSupplier,
  ] = useState<
    Supplier | null
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

  function replaceSupplier(
    updatedSupplier: Supplier,
  ) {
    setSuppliers(
      (currentSuppliers) =>
        currentSuppliers.map(
          (supplier) =>
            supplier.id ===
            updatedSupplier.id
              ? updatedSupplier
              : supplier,
        ),
    )
  }

  async function reloadSuppliers() {
    setIsLoading(true)
    setPageError(null)

    try {
      const data =
        await supplierService.list()

      setSuppliers(data)
    } catch (error) {
      setPageError(
        getSupplierErrorMessage(
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

      supplierService
        .list()
        .then((data) => {
          if (ignore) {
            return
          }

          setSuppliers(data)
          setPageError(null)
        })
        .catch(
          (error: unknown) => {
            if (ignore) {
              return
            }

            setPageError(
              getSupplierErrorMessage(
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

  const filteredSuppliers =
    useMemo(
      () => {
        const search =
          normalizeSearchValue(
            searchValue,
          )

        return suppliers.filter(
          (supplier) => {
            const matchesStatus =
              statusFilter ===
                'all' ||
              (
                statusFilter ===
                  'active' &&
                supplier.is_active
              ) ||
              (
                statusFilter ===
                  'inactive' &&
                !supplier.is_active
              )

            if (!matchesStatus) {
              return false
            }

            if (!search) {
              return true
            }

            const searchableValue =
              [
                supplier.name,
                supplier.document ?? '',
                supplier.address ?? '',
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
        suppliers,
        searchValue,
        statusFilter,
      ],
    )

  const activeCount =
    suppliers.filter(
      (supplier) =>
        supplier.is_active,
    ).length

  const inactiveCount =
    suppliers.length -
    activeCount

  function closeModal() {
    if (isSubmitting) {
      return
    }

    setModalMode(null)
    setSelectedSupplier(null)
    setModalError(null)
    setDeactivateJustification('')
  }

  function openCreateModal() {
    setSelectedSupplier(null)
    setModalError(null)
    setModalMode('create')
  }

  function openEditModal(
    supplier: Supplier,
  ) {
    setSelectedSupplier(
      supplier,
    )
    setModalError(null)
    setModalMode('edit')
  }

  function openDeactivateModal(
    supplier: Supplier,
  ) {
    setSelectedSupplier(
      supplier,
    )
    setModalError(null)
    setDeactivateJustification('')
    setModalMode(
      'deactivate',
    )
  }

  async function handleSupplierSubmit(
    payload: SupplierCreatePayload,
  ) {
    setIsSubmitting(true)
    setModalError(null)

    try {
      if (
        modalMode === 'edit' &&
        selectedSupplier
      ) {
        const updatedSupplier =
          await supplierService
            .update(
              selectedSupplier.id,
              payload,
            )

        replaceSupplier(
          updatedSupplier,
        )
      } else {
        const createdSupplier =
          await supplierService
            .create(payload)

        setSuppliers(
          (currentSuppliers) => [
            ...currentSuppliers,
            createdSupplier,
          ],
        )
      }

      setModalMode(null)
      setSelectedSupplier(null)
    } catch (error) {
      setModalError(
        getSupplierErrorMessage(
          error,
        ),
      )
    } finally {
      setIsSubmitting(false)
    }
  }

  async function handleActivate(
    supplier: Supplier,
  ) {
    try {
      const updatedSupplier =
        await supplierService
          .activate(
            supplier.id,
          )

      replaceSupplier(
        updatedSupplier,
      )
    } catch (error) {
      setPageError(
        getSupplierErrorMessage(
          error,
        ),
      )
    }
  }

  async function handleDeactivateSubmit(
    event: FormEvent<HTMLFormElement>,
  ) {
    event.preventDefault()

    if (
      !selectedSupplier ||
      isSubmitting
    ) {
      return
    }

    const justification =
      deactivateJustification
        .trim()

    if (!justification) {
      setModalError(
        'Informe a justificativa para desativar o fornecedor.',
      )

      return
    }

    setIsSubmitting(true)
    setModalError(null)

    try {
      const updatedSupplier =
        await supplierService
          .deactivate(
            selectedSupplier.id,
            {
              justification,
            },
          )

      replaceSupplier(
        updatedSupplier,
      )

      setModalMode(null)
      setSelectedSupplier(null)
      setDeactivateJustification('')
    } catch (error) {
      setModalError(
        getSupplierErrorMessage(
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
        title="Fornecedores"
        description="Gerencie os fornecedores vinculados às peças e aos fluxos de devolução de cascos."
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

            Novo fornecedor
          </Button>
        }
      />

      <section
        className="supplier-summary"
        aria-label="Resumo dos fornecedores"
      >
        <Card
          className="supplier-summary__card"
          padding="md"
        >
          <span>
            Cadastrados
          </span>

          <strong>
            {suppliers.length}
          </strong>
        </Card>

        <Card
          className="supplier-summary__card"
          padding="md"
        >
          <span>
            Ativos
          </span>

          <strong>
            {activeCount}
          </strong>

          <StatusBadge tone="success">
            Em uso
          </StatusBadge>
        </Card>

        <Card
          className="supplier-summary__card"
          padding="md"
        >
          <span>
            Inativos
          </span>

          <strong>
            {inactiveCount}
          </strong>

          <StatusBadge tone="neutral">
            Arquivados
          </StatusBadge>
        </Card>
      </section>

      <Card
        className="supplier-management"
        padding="none"
      >
        <div className="supplier-toolbar">
          <div className="supplier-search">
            <Search
              size={18}
              strokeWidth={1.8}
              aria-hidden="true"
            />

            <input
              type="search"
              value={searchValue}
              placeholder="Buscar por nome, documento ou endereço"
              aria-label="Buscar fornecedores"
              onChange={(event) => {
                setSearchValue(
                  event.target.value,
                )
              }}
            />

            {searchValue && (
              <button
                type="button"
                className="supplier-search__clear"
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

          <div
            className="supplier-status-filter"
            aria-label="Filtrar fornecedores por status"
          >
            <button
              type="button"
              className={
                statusFilter === 'all'
                  ? 'supplier-status-filter__button supplier-status-filter__button--active'
                  : 'supplier-status-filter__button'
              }
              onClick={() => {
                setStatusFilter(
                  'all',
                )
              }}
            >
              Todos
            </button>

            <button
              type="button"
              className={
                statusFilter === 'active'
                  ? 'supplier-status-filter__button supplier-status-filter__button--active'
                  : 'supplier-status-filter__button'
              }
              onClick={() => {
                setStatusFilter(
                  'active',
                )
              }}
            >
              Ativos
            </button>

            <button
              type="button"
              className={
                statusFilter === 'inactive'
                  ? 'supplier-status-filter__button supplier-status-filter__button--active'
                  : 'supplier-status-filter__button'
              }
              onClick={() => {
                setStatusFilter(
                  'inactive',
                )
              }}
            >
              Inativos
            </button>
          </div>
        </div>

        {pageError && (
          <div
            className="supplier-page-error"
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
                void reloadSuppliers()
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
          <div className="supplier-loading">
            <div className="dashboard-state__spinner" />

            <div>
              <strong>
                Carregando fornecedores
              </strong>

              <p>
                Consultando os cadastros disponíveis.
              </p>
            </div>
          </div>
        ) : (
          <>
            <div className="supplier-table-summary">
              <span>
                {filteredSuppliers.length}
                {' '}
                {filteredSuppliers.length === 1
                  ? 'fornecedor exibido'
                  : 'fornecedores exibidos'}
              </span>
            </div>

            <SupplierTable
              suppliers={
                filteredSuppliers
              }
              onContacts={
                setContactsSupplier
              }
              onEdit={
                openEditModal
              }
              onActivate={
                (supplier) => {
                  void handleActivate(
                    supplier,
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
          className="supplier-modal-backdrop"
          role="presentation"
        >
          <div
            className="supplier-modal"
            role="dialog"
            aria-modal="true"
            aria-label={
              modalMode === 'edit'
                ? 'Editar fornecedor'
                : 'Cadastrar fornecedor'
            }
          >
            <SupplierForm
              key={
                selectedSupplier
                  ? `edit-${selectedSupplier.id}`
                  : 'create'
              }
              supplier={
                selectedSupplier
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
                handleSupplierSubmit
              }
            />
          </div>
        </div>
      )}

      {modalMode ===
        'deactivate' &&
        selectedSupplier && (
          <div
            className="supplier-modal-backdrop"
            role="presentation"
          >
            <div
              className="supplier-modal supplier-modal--compact"
              role="dialog"
              aria-modal="true"
              aria-labelledby="supplier-deactivate-title"
            >
              <form
                className="supplier-deactivate"
                onSubmit={
                  handleDeactivateSubmit
                }
              >
                <div className="supplier-deactivate__icon">
                  <Building2
                    size={24}
                    strokeWidth={1.7}
                  />
                </div>

                <header>
                  <span>
                    Desativação
                  </span>

                  <h2
                    id="supplier-deactivate-title"
                  >
                    Desativar fornecedor
                  </h2>

                  <p>
                    O fornecedor continuará
                    preservado no histórico,
                    mas deixará de ficar ativo
                    para novas operações.
                  </p>
                </header>

                <div className="supplier-deactivate__supplier">
                  <span>
                    Fornecedor
                  </span>

                  <strong>
                    {selectedSupplier.name}
                  </strong>
                </div>

                <label className="supplier-field">
                  <span className="supplier-field__label">
                    Justificativa
                  </span>

                  <textarea
                    className="supplier-field__textarea"
                    rows={4}
                    maxLength={1000}
                    required
                    autoFocus
                    disabled={
                      isSubmitting
                    }
                    value={
                      deactivateJustification
                    }
                    placeholder="Informe o motivo da desativação"
                    onChange={(event) => {
                      setDeactivateJustification(
                        event.target.value,
                      )
                    }}
                  />

                  <span className="supplier-field__counter">
                    {
                      deactivateJustification
                        .length
                    }
                    /1000
                  </span>
                </label>

                {modalError && (
                  <div
                    className="supplier-form__error"
                    role="alert"
                  >
                    {modalError}
                  </div>
                )}

                <footer className="supplier-form__actions">
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
                      !deactivateJustification
                        .trim()
                    }
                  >
                    {isSubmitting
                      ? 'Desativando...'
                      : 'Desativar fornecedor'}
                  </Button>
                </footer>
              </form>
            </div>
          </div>
        )}
        {contactsSupplier && (
            <SupplierContactsPanel
                supplier={
                contactsSupplier
                }
                onClose={() => {
                setContactsSupplier(
                    null,
                )
                }}
            />
        )}
    </div>
  )
}