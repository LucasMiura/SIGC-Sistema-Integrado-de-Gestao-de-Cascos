import {
  ContactRound,
  MoreHorizontal,
  Pencil,
  Power,
  PowerOff,
} from 'lucide-react'

import {
  Button,
} from '../ui/Button'
import {
  StatusBadge,
} from '../ui/StatusBadge'
import type {
  Supplier,
} from '../../types/supplier'

interface SupplierTableProps {
  suppliers: Supplier[]

  onContacts(
    supplier: Supplier,
  ): void

  onEdit(
    supplier: Supplier,
  ): void

  onActivate(
    supplier: Supplier,
  ): void

  onDeactivate(
    supplier: Supplier,
  ): void
}

function formatDocument(
  document: string | null,
): string {
  return (
    document ??
    'Não informado'
  )
}

export function SupplierTable({
  suppliers,
  onContacts,
  onEdit,
  onActivate,
  onDeactivate,
}: SupplierTableProps) {
  if (
    suppliers.length === 0
  ) {
    return (
      <div className="supplier-empty">
        <div className="supplier-empty__icon">
          <MoreHorizontal
            size={24}
            strokeWidth={1.7}
          />
        </div>

        <strong>
          Nenhum fornecedor encontrado
        </strong>

        <p>
          Ajuste os filtros ou cadastre
          um novo fornecedor.
        </p>
      </div>
    )
  }

  return (
    <div className="supplier-table-wrapper">
      <table className="supplier-table">
        <thead>
          <tr>
            <th>
              Fornecedor
            </th>

            <th>
              Documento
            </th>

            <th>
              Endereço
            </th>

            <th>
              Status
            </th>

            <th className="supplier-table__actions-heading">
              Ações
            </th>
          </tr>
        </thead>

        <tbody>
          {suppliers.map(
            (supplier) => (
              <tr
                key={supplier.id}
              >
                <td>
                  <div className="supplier-table__identity">
                    <strong>
                      {supplier.name}
                    </strong>

                    <span>
                      ID {supplier.id}
                    </span>
                  </div>
                </td>

                <td>
                  <span className="supplier-table__secondary">
                    {formatDocument(
                      supplier.document,
                    )}
                  </span>
                </td>

                <td>
                  <span className="supplier-table__address">
                    {supplier.address ??
                      'Não informado'}
                  </span>
                </td>

                <td>
                  <StatusBadge
                    tone={
                      supplier.is_active
                        ? 'success'
                        : 'neutral'
                    }
                  >
                    {supplier.is_active
                      ? 'Ativo'
                      : 'Inativo'}
                  </StatusBadge>
                </td>

                <td>
                  <div className="supplier-table__actions">
                    <Button
                      type="button"
                      variant="ghost"
                      size="sm"
                      onClick={() => {
                        onContacts(
                          supplier,
                        )
                      }}
                    >
                      <ContactRound
                        size={15}
                      />

                      Contatos
                    </Button>

                    <Button
                      type="button"
                      variant="ghost"
                      size="sm"
                      onClick={() => {
                        onEdit(
                          supplier,
                        )
                      }}
                    >
                      <Pencil
                        size={15}
                      />

                      Editar
                    </Button>

                    {supplier.is_active ? (
                      <Button
                        type="button"
                        variant="ghost"
                        size="sm"
                        onClick={() => {
                          onDeactivate(
                            supplier,
                          )
                        }}
                      >
                        <PowerOff
                          size={15}
                        />

                        Desativar
                      </Button>
                    ) : (
                      <Button
                        type="button"
                        variant="ghost"
                        size="sm"
                        onClick={() => {
                          onActivate(
                            supplier,
                          )
                        }}
                      >
                        <Power
                          size={15}
                        />

                        Ativar
                      </Button>
                    )}
                  </div>
                </td>
              </tr>
            ),
          )}
        </tbody>
      </table>
    </div>
  )
}