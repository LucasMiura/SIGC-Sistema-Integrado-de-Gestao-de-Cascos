import {
  Ban,
  Boxes,
  Pencil,
  ReceiptText,
  ShoppingBag,
  Wrench,
} from 'lucide-react'

import type {
  Outbound,
} from '../../types/outbound'

import {
  Button,
} from '../ui/Button'

import {
  StatusBadge,
} from '../ui/StatusBadge'

interface OutboundTableProps {
  outbounds: Outbound[]

  onItems(
    outbound: Outbound,
  ): void

  onEdit(
    outbound: Outbound,
  ): void

  onCancel(
    outbound: Outbound,
  ): void
}

function formatDateTime(
  value: string,
): string {
  const date =
    new Date(value)

  if (
    Number.isNaN(
      date.getTime(),
    )
  ) {
    return value
  }

  return new Intl.DateTimeFormat(
    'pt-BR',
    {
      dateStyle: 'short',
      timeStyle: 'short',
    },
  ).format(date)
}

function getReference(
  outbound: Outbound,
): string {
  return (
    outbound.destination_type ===
    'WORK_ORDER'
      ? outbound.work_order_number ??
        'Sem OS'
      : outbound.sales_invoice_number ??
        'Sem NF'
  )
}

export function OutboundTable({
  outbounds,
  onItems,
  onEdit,
  onCancel,
}: OutboundTableProps) {
  if (outbounds.length === 0) {
    return (
      <div className="outbound-empty">
        <div className="outbound-empty__icon">
          <ReceiptText
            size={24}
            strokeWidth={1.7}
          />
        </div>

        <strong>
          Nenhuma saída encontrada
        </strong>

        <p>
          Ajuste os filtros ou registre
          uma nova movimentação.
        </p>
      </div>
    )
  }

  return (
    <div className="outbound-table-wrapper">
      <table className="outbound-table">
        <thead>
          <tr>
            <th>
              Referência
            </th>

            <th>
              Cliente
            </th>

            <th>
              Destino
            </th>

            <th>
              Registro
            </th>

            <th>
              Situação
            </th>

            <th className="outbound-table__actions-heading">
              Ações
            </th>
          </tr>
        </thead>

        <tbody>
          {outbounds.map(
            (outbound) => (
              <tr key={outbound.id}>
                <td>
                  <div className="outbound-table__reference">
                    <strong>
                      {getReference(
                        outbound,
                      )}
                    </strong>

                    <span>
                      Saída #{outbound.id}
                    </span>
                  </div>
                </td>

                <td>
                  <span className="outbound-table__customer">
                    {outbound.customer_name}
                  </span>
                </td>

                <td>
                  <div className="outbound-table__destination">
                    {outbound.destination_type ===
                    'WORK_ORDER' ? (
                      <Wrench
                        size={16}
                      />
                    ) : (
                      <ShoppingBag
                        size={16}
                      />
                    )}

                    <span>
                      {outbound.destination_type ===
                      'WORK_ORDER'
                        ? 'Oficina'
                        : 'Balcão'}
                    </span>
                  </div>
                </td>

                <td>
                  <span className="outbound-table__date">
                    {formatDateTime(
                      outbound.created_at,
                    )}
                  </span>
                </td>

                <td>
                  <StatusBadge
                    tone={
                      outbound.status ===
                      'ACTIVE'
                        ? 'success'
                        : 'neutral'
                    }
                  >
                    {outbound.status ===
                    'ACTIVE'
                      ? 'Ativa'
                      : 'Cancelada'}
                  </StatusBadge>
                </td>

                <td>
                  <div className="outbound-table__actions">
                    <Button
                      type="button"
                      variant="ghost"
                      size="sm"
                      onClick={() => {
                        onItems(
                          outbound,
                        )
                      }}
                    >
                      <Boxes
                        size={15}
                      />

                      Itens
                    </Button>

                    {outbound.status ===
                      'ACTIVE' && (
                      <>
                        <Button
                          type="button"
                          variant="ghost"
                          size="sm"
                          onClick={() => {
                            onEdit(
                              outbound,
                            )
                          }}
                        >
                          <Pencil
                            size={15}
                          />

                          Editar
                        </Button>

                        <Button
                          type="button"
                          variant="ghost"
                          size="sm"
                          onClick={() => {
                            onCancel(
                              outbound,
                            )
                          }}
                        >
                          <Ban
                            size={15}
                          />

                          Cancelar
                        </Button>
                      </>
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