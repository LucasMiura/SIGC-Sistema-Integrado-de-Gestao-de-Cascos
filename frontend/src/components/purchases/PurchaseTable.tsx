import {
  Ban,
  Boxes,
  CheckCircle2,
  Pencil,
  ReceiptText,
} from 'lucide-react'

import {
  Button,
} from '../ui/Button'
import {
  StatusBadge,
  type StatusBadgeTone,
} from '../ui/StatusBadge'

import type {
  Purchase,
} from '../../types/purchase'
import type {
  Supplier,
} from '../../types/supplier'

interface PurchaseTableProps {
  purchases: Purchase[]
  suppliers: Supplier[]

  onItems(
    purchase: Purchase,
  ): void

  onEdit(
    purchase: Purchase,
  ): void

  onReceive(
    purchase: Purchase,
  ): void

  onCancel(
    purchase: Purchase,
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

function getStatusData(
  status: Purchase['status'],
): {
  label: string
  tone: StatusBadgeTone
} {
  switch (status) {
    case 'PENDING':
      return {
        label: 'Pendente',
        tone: 'attention',
      }

    case 'RECEIVED':
      return {
        label: 'Recebida',
        tone: 'success',
      }

    case 'CANCELLED':
      return {
        label: 'Cancelada',
        tone: 'neutral',
      }
  }
}

function formatDate(
  value: string,
): string {
  const [
    year,
    month,
    day,
  ] = value.split('-')

  if (
    !year ||
    !month ||
    !day
  ) {
    return value
  }

  return `${day}/${month}/${year}`
}

export function PurchaseTable({
  purchases,
  suppliers,
  onItems,
  onEdit,
  onReceive,
  onCancel,
}: PurchaseTableProps) {
  if (purchases.length === 0) {
    return (
      <div className="purchase-empty">
        <div className="purchase-empty__icon">
          <ReceiptText
            size={24}
            strokeWidth={1.7}
          />
        </div>

        <strong>
          Nenhuma compra encontrada
        </strong>

        <p>
          Ajuste os filtros ou registre
          uma nova Nota Fiscal de compra.
        </p>
      </div>
    )
  }

  return (
    <div className="purchase-table-wrapper">
      <table className="purchase-table">
        <thead>
          <tr>
            <th>
              Nota Fiscal
            </th>

            <th>
              Fornecedor
            </th>

            <th>
              Emissão
            </th>

            <th>
              Situação
            </th>

            <th className="purchase-table__actions-heading">
              Ações
            </th>
          </tr>
        </thead>

        <tbody>
          {purchases.map(
            (purchase) => {
              const statusData =
                getStatusData(
                  purchase.status,
                )

              return (
                <tr
                  key={purchase.id}
                >
                  <td>
                    <div className="purchase-table__invoice">
                      <strong>
                        NF {purchase.invoice_number}
                      </strong>

                      <span>
                        {purchase.invoice_series
                          ? `Série ${purchase.invoice_series}`
                          : `ID ${purchase.id}`}
                      </span>
                    </div>
                  </td>

                  <td>
                    <span className="purchase-table__supplier">
                      {getSupplierName(
                        purchase.supplier_id,
                        suppliers,
                      )}
                    </span>
                  </td>

                  <td>
                    <span className="purchase-table__date">
                      {formatDate(
                        purchase.issue_date,
                      )}
                    </span>
                  </td>

                  <td>
                    <StatusBadge
                      tone={
                        statusData.tone
                      }
                    >
                      {statusData.label}
                    </StatusBadge>
                  </td>

                  <td>
                    <div className="purchase-table__actions">
                      <Button
                        type="button"
                        variant="ghost"
                        size="sm"
                        onClick={() => {
                          onItems(
                            purchase,
                          )
                        }}
                      >
                        <Boxes
                          size={15}
                        />

                        Itens
                      </Button>

                      {purchase.status !==
                        'CANCELLED' && (
                        <Button
                          type="button"
                          variant="ghost"
                          size="sm"
                          onClick={() => {
                            onEdit(
                              purchase,
                            )
                          }}
                        >
                          <Pencil
                            size={15}
                          />

                          Editar
                        </Button>
                      )}

                      {purchase.status ===
                        'PENDING' && (
                        <Button
                          type="button"
                          variant="ghost"
                          size="sm"
                          onClick={() => {
                            onReceive(
                              purchase,
                            )
                          }}
                        >
                          <CheckCircle2
                            size={15}
                          />

                          Receber
                        </Button>
                      )}

                      {purchase.status !==
                        'CANCELLED' && (
                        <Button
                          type="button"
                          variant="ghost"
                          size="sm"
                          onClick={() => {
                            onCancel(
                              purchase,
                            )
                          }}
                        >
                          <Ban
                            size={15}
                          />

                          Cancelar
                        </Button>
                      )}
                    </div>
                  </td>
                </tr>
              )
            },
          )}
        </tbody>
      </table>
    </div>
  )
}