import {
  Boxes,
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
  Part,
} from '../../types/part'
import type {
  Supplier,
} from '../../types/supplier'

interface PartTableProps {
  parts: Part[]
  suppliers: Supplier[]

  onEdit(
    part: Part,
  ): void

  onActivate(
    part: Part,
  ): void

  onDeactivate(
    part: Part,
  ): void
}

function getSupplierName(
  supplierId: number,
  suppliers: Supplier[],
): string {
  return (
    suppliers.find(
      (supplier) =>
        supplier.id ===
        supplierId,
    )?.name ??
    `Fornecedor #${supplierId}`
  )
}

export function PartTable({
  parts,
  suppliers,
  onEdit,
  onActivate,
  onDeactivate,
}: PartTableProps) {
  if (parts.length === 0) {
    return (
      <div className="part-empty">
        <div className="part-empty__icon">
          <Boxes
            size={24}
            strokeWidth={1.7}
          />
        </div>

        <strong>
          Nenhuma peça encontrada
        </strong>

        <p>
          Ajuste os filtros ou cadastre
          uma nova peça controlada pelo
          SIGC.
        </p>
      </div>
    )
  }

  return (
    <div className="part-table-wrapper">
      <table className="part-table">
        <thead>
          <tr>
            <th>
              Código original
            </th>

            <th>
              Peça
            </th>

            <th>
              Fornecedor
            </th>

            <th>
              Prazo
            </th>

            <th>
              Status
            </th>

            <th className="part-table__actions-heading">
              Ações
            </th>
          </tr>
        </thead>

        <tbody>
          {parts.map(
            (part) => (
              <tr
                key={part.id}
              >
                <td>
                  <span className="part-table__code">
                    {part.part_code}
                  </span>
                </td>

                <td>
                  <div className="part-table__identity">
                    <strong>
                      {part.name}
                    </strong>

                    <span>
                      {part.description ??
                        `ID ${part.id}`}
                    </span>
                  </div>
                </td>

                <td>
                  <span className="part-table__supplier">
                    {getSupplierName(
                      part.supplier_id,
                      suppliers,
                    )}
                  </span>
                </td>

                <td>
                  <div className="part-table__deadline">
                    <strong>
                      {
                        part.return_deadline_days
                      }
                    </strong>

                    <span>
                      dias
                    </span>
                  </div>
                </td>

                <td>
                  <StatusBadge
                    tone={
                      part.is_active
                        ? 'success'
                        : 'neutral'
                    }
                  >
                    {part.is_active
                      ? 'Ativa'
                      : 'Inativa'}
                  </StatusBadge>
                </td>

                <td>
                  <div className="part-table__actions">
                    <Button
                      type="button"
                      variant="ghost"
                      size="sm"
                      onClick={() => {
                        onEdit(part)
                      }}
                    >
                      <Pencil
                        size={15}
                      />

                      Editar
                    </Button>

                    {part.is_active ? (
                      <Button
                        type="button"
                        variant="ghost"
                        size="sm"
                        onClick={() => {
                          onDeactivate(
                            part,
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
                            part,
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