import {
  AlertCircle,
  Crown,
  Mail,
  Pencil,
  Phone,
  Plus,
  Power,
  PowerOff,
  UserRound,
  X,
} from 'lucide-react'
import {
  useEffect,
  useState,
  type FormEvent,
} from 'react'

import {
  supplierContactService,
} from '../../services/supplierContactService'
import {
  ApiError,
} from '../../services/httpClient'
import type {
  Supplier,
} from '../../types/supplier'
import type {
  SupplierContact,
  SupplierContactCreatePayload,
} from '../../types/supplierContact'
import {
  Button,
} from '../ui/Button'
import {
  StatusBadge,
} from '../ui/StatusBadge'
import {
  Toast,
} from '../ui/Toast'

import {
  SupplierContactForm,
} from './SupplierContactForm'

interface SupplierContactsPanelProps {
  supplier: Supplier
  onClose(): void
}

type ContactFormMode =
  | 'create'
  | 'edit'
  | null

function getContactErrorMessage(
  error: unknown,
): string {
  if (
    error instanceof ApiError
  ) {
    return error.message
  }

  return (
    'Não foi possível concluir a operação com o contato.'
  )
}

export function SupplierContactsPanel({
  supplier,
  onClose,
}: SupplierContactsPanelProps) {
  const [
    contacts,
    setContacts,
  ] = useState<
    SupplierContact[]
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
    formMode,
    setFormMode,
  ] = useState<
    ContactFormMode
  >(null)

  const [
    selectedContact,
    setSelectedContact,
  ] = useState<
    SupplierContact | null
  >(null)

  const [
    isSubmitting,
    setIsSubmitting,
  ] = useState(false)

  const [
    formError,
    setFormError,
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
    contactToDeactivate,
    setContactToDeactivate,
  ] = useState<
    SupplierContact | null
  >(null)

  const [
    justification,
    setJustification,
  ] = useState('')

  useEffect(
    () => {
      let ignore = false

      supplierContactService
        .list(
          supplier.id,
        )
        .then((data) => {
          if (ignore) {
            return
          }

          setContacts(data)
          setPageError(null)
        })
        .catch(
          (error: unknown) => {
            if (ignore) {
              return
            }

            setPageError(
              getContactErrorMessage(
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
      supplier.id,
    ],
  )

  function replaceContact(
    updatedContact:
      SupplierContact,
  ) {
    setContacts(
      (currentContacts) =>
        currentContacts.map(
          (contact) => {
            if (
              contact.id ===
              updatedContact.id
            ) {
              return updatedContact
            }

            if (
              updatedContact.is_primary &&
              contact.id !==
                updatedContact.id
            ) {
              return {
                ...contact,
                is_primary: false,
              }
            }

            return contact
          },
        ),
    )
  }

  async function handleSubmit(
    payload:
      SupplierContactCreatePayload,
  ) {
    setIsSubmitting(true)
    setFormError(null)

    try {
      if (
        formMode === 'edit' &&
        selectedContact
      ) {
        const updated =
          await supplierContactService
            .update(
              supplier.id,
              selectedContact.id,
              payload,
            )

        replaceContact(updated)

        setToastMessage(
          'Contato atualizado com sucesso.',
        )
      } else {
        const created =
          await supplierContactService
            .create(
              supplier.id,
              payload,
            )

        setContacts(
          (currentContacts) => {
            const normalized =
              created.is_primary
                ? currentContacts.map(
                    (contact) => ({
                      ...contact,
                      is_primary: false,
                    }),
                  )
                : currentContacts

            return [
              ...normalized,
              created,
            ]
          },
        )

        setToastMessage(
          'Contato cadastrado com sucesso.',
        )
      }

      setFormMode(null)
      setSelectedContact(null)
    } catch (error) {
      setFormError(
        getContactErrorMessage(
          error,
        ),
      )
    } finally {
      setIsSubmitting(false)
    }
  }

  async function handleActivate(
    contact: SupplierContact,
  ) {
    setPageError(null)

    try {
      const updated =
        await supplierContactService
          .activate(
            supplier.id,
            contact.id,
          )

      replaceContact(updated)

      setToastMessage(
        'Contato reativado com sucesso.',
      )

    } catch (error) {
      setPageError(
        getContactErrorMessage(
          error,
        ),
      )
    }
  }

  async function handleDeactivate(
    event:
      FormEvent<HTMLFormElement>,
  ) {
    event.preventDefault()

    if (
      !contactToDeactivate ||
      isSubmitting
    ) {
      return
    }

    const normalized =
      justification.trim()

    if (!normalized) {
      setFormError(
        'Informe a justificativa para desativar o contato.',
      )

      return
    }

    setIsSubmitting(true)
    setFormError(null)

    try {
      const updated =
        await supplierContactService
          .deactivate(
            supplier.id,
            contactToDeactivate.id,
            {
              justification:
                normalized,
            },
          )

      replaceContact(updated)

      setToastMessage(
        'Contato desativado com sucesso.',
      )

      setContactToDeactivate(
        null,
      )

      setJustification('')
    } catch (error) {
      setFormError(
        getContactErrorMessage(
          error,
        ),
      )
    } finally {
      setIsSubmitting(false)
    }
  }

  const sortedContacts =
    [...contacts].sort(
      (left, right) => {
        if (
          left.is_primary !==
          right.is_primary
        ) {
          return left.is_primary
            ? -1
            : 1
        }

        if (
          left.is_active !==
          right.is_active
        ) {
          return left.is_active
            ? -1
            : 1
        }

        return (
          new Date(
            right.created_at,
          ).getTime() -
          new Date(
            left.created_at,
          ).getTime()
        )
      },
    )

  return (
    <div
      className="supplier-modal-backdrop"
      role="presentation"
    >
      <section
        className="supplier-contacts-panel"
        role="dialog"
        aria-modal="true"
        aria-labelledby="supplier-contacts-title"
      >
        <header className="supplier-contacts-panel__header">
          <div>
            <span>
              Fornecedor
            </span>

            <h2
              id="supplier-contacts-title"
            >
              {supplier.name}
            </h2>

            <p>
              Gerencie as pessoas de
              contato vinculadas a este
              fornecedor.
            </p>
          </div>

          <button
            type="button"
            className="supplier-contacts-panel__close"
            aria-label="Fechar contatos"
            onClick={onClose}
          >
            <X
              size={20}
            />
          </button>
        </header>

        <div className="supplier-contacts-panel__toolbar">
          <div>
            <strong>
              Contatos
            </strong>

            <span>
              {contacts.length}
              {' '}
              {contacts.length === 1
                ? 'registro'
                : 'registros'}
            </span>
          </div>

          <Button
            type="button"
            size="sm"
            onClick={() => {
              setSelectedContact(
                null,
              )
              setContactToDeactivate(
                null,
              )
              setFormError(null)
              setFormMode(
                'create',
              )
            }}
          >
            <Plus
              size={16}
            />

            Novo contato
          </Button>
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
          </div>
        )}

        <div className="supplier-contacts-panel__body">
          <div className="supplier-contacts-list">
            {isLoading ? (
              <div className="supplier-contact-state">
                <div className="dashboard-state__spinner" />

                <span>
                  Carregando contatos...
                </span>
              </div>
            ) : sortedContacts.length === 0 ? (
              <div className="supplier-contact-state">
                <div className="supplier-empty__icon">
                  <UserRound
                    size={22}
                  />
                </div>

                <strong>
                  Nenhum contato cadastrado
                </strong>

                <p>
                  Adicione a primeira pessoa
                  de referência deste
                  fornecedor.
                </p>
              </div>
            ) : (
              sortedContacts.map(
                (contact) => (
                  <article
                    className={[
                      'supplier-contact-card',
                      !contact.is_active
                        ? 'supplier-contact-card--inactive'
                        : '',
                    ]
                      .filter(Boolean)
                      .join(' ')}
                    key={contact.id}
                  >
                    <div className="supplier-contact-card__top">
                      <div className="supplier-contact-card__identity">
                        <div className="supplier-contact-card__avatar">
                          <UserRound
                            size={19}
                          />
                        </div>

                        <div>
                          <div className="supplier-contact-card__name">
                            <strong>
                              {contact.name}
                            </strong>

                            {contact.is_primary && (
                              <span className="supplier-contact-card__primary">
                                <Crown
                                  size={12}
                                />
                                Principal
                              </span>
                            )}
                          </div>

                          <span>
                            {contact.position ??
                              'Cargo não informado'}
                          </span>
                        </div>
                      </div>

                      <StatusBadge
                        tone={
                          contact.is_active
                            ? 'success'
                            : 'neutral'
                        }
                      >
                        {contact.is_active
                          ? 'Ativo'
                          : 'Inativo'}
                      </StatusBadge>
                    </div>

                    <div className="supplier-contact-card__details">
                      <div>
                        <Mail
                          size={15}
                        />

                        <span>
                          {contact.email ??
                            'E-mail não informado'}
                        </span>
                      </div>

                      <div>
                        <Phone
                          size={15}
                        />

                        <span>
                          {contact.phone ??
                            'Telefone não informado'}
                        </span>
                      </div>
                    </div>

                    <footer className="supplier-contact-card__actions">
                      <Button
                        type="button"
                        variant="ghost"
                        size="sm"
                        onClick={() => {
                          setSelectedContact(
                            contact,
                          )
                          setContactToDeactivate(
                            null,
                          )
                          setFormError(null)
                          setFormMode(
                            'edit',
                          )
                        }}
                      >
                        <Pencil
                          size={14}
                        />

                        Editar
                      </Button>

                      {contact.is_active ? (
                        <Button
                          type="button"
                          variant="ghost"
                          size="sm"
                          onClick={() => {
                            setFormMode(null)
                            setSelectedContact(
                              null,
                            )
                            setFormError(null)
                            setJustification('')
                            setContactToDeactivate(
                              contact,
                            )
                          }}
                        >
                          <PowerOff
                            size={14}
                          />

                          Desativar
                        </Button>
                      ) : (
                        <Button
                          type="button"
                          variant="ghost"
                          size="sm"
                          onClick={() => {
                            void handleActivate(
                              contact,
                            )
                          }}
                        >
                          <Power
                            size={14}
                          />

                          Ativar
                        </Button>
                      )}
                    </footer>
                  </article>
                ),
              )
            )}
          </div>

          {(formMode === 'create' ||
            formMode === 'edit') && (
            <aside className="supplier-contacts-panel__editor">
              <SupplierContactForm
                key={
                  selectedContact
                    ? `contact-${selectedContact.id}`
                    : 'new-contact'
                }
                contact={
                  selectedContact
                }
                isSubmitting={
                  isSubmitting
                }
                errorMessage={
                  formError
                }
                onCancel={() => {
                  setFormMode(null)
                  setSelectedContact(
                    null,
                  )
                  setFormError(null)
                }}
                onSubmit={
                  handleSubmit
                }
              />
            </aside>
          )}

          {contactToDeactivate && (
            <aside className="supplier-contacts-panel__editor">
              <form
                className="supplier-contact-deactivate"
                onSubmit={
                  handleDeactivate
                }
              >
                <header>
                  <span>
                    Desativação
                  </span>

                  <h3>
                    Desativar contato
                  </h3>

                  <p>
                    O contato permanecerá
                    no histórico do
                    fornecedor.
                  </p>
                </header>

                <div className="supplier-contact-deactivate__identity">
                  <strong>
                    {
                      contactToDeactivate
                        .name
                    }
                  </strong>

                  <span>
                    {
                      contactToDeactivate
                        .position ??
                      'Cargo não informado'
                    }
                  </span>
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
                      justification
                    }
                    onChange={(event) => {
                      setJustification(
                        event.target.value,
                      )
                    }}
                  />

                  <span className="supplier-field__counter">
                    {
                      justification.length
                    }
                    /1000
                  </span>
                </label>

                {formError && (
                  <div
                    className="supplier-form__error"
                    role="alert"
                  >
                    {formError}
                  </div>
                )}

                <footer className="supplier-form__actions">
                  <Button
                    type="button"
                    variant="secondary"
                    disabled={
                      isSubmitting
                    }
                    onClick={() => {
                      setContactToDeactivate(
                        null,
                      )
                      setFormError(null)
                      setJustification('')
                    }}
                  >
                    Cancelar
                  </Button>

                  <Button
                    type="submit"
                    variant="danger"
                    disabled={
                      isSubmitting ||
                      !justification.trim()
                    }
                  >
                    {isSubmitting
                      ? 'Desativando...'
                      : 'Desativar contato'}
                  </Button>
                </footer>
              </form>
            </aside>
          )}
        </div>
      </section>

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