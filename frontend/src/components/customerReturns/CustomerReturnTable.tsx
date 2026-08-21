import {
  Ban,
  Eye,
} from 'lucide-react'

import {
  Button,
} from '../ui/Button'

import {
  StatusBadge,
} from '../ui/StatusBadge'

import type {
  CustomerReturn,
} from '../../types/customerReturn'

interface CustomerReturnTableProps {
  customerReturns:
    CustomerReturn[]

  onDetails:
    (
      customerReturn:
        CustomerReturn,
    ) => void

  onCancel:
    (
      customerReturn:
        CustomerReturn,
    ) => void
}

function formatDate(
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

export function CustomerReturnTable({
  customerReturns,
  onDetails,
  onCancel,
}: CustomerReturnTableProps) {
  if (
    customerReturns.length === 0
  ) {
    return (
      <div className="customer-return-empty">
        <strong>
          Nenhuma devolução encontrada
        </strong>

        <p>
          Não existem devoluções
          correspondentes aos filtros
          selecionados.
        </p>
      </div>
    )
  }

  return (
    <div className="customer-return-table-wrapper">
      <table className="customer-return-table">
        <thead>
          <tr>
            <th>
              Referência
            </th>

            <th>
              Cliente
            </th>

            <th>
              Origem
            </th>

            <th>
              Data
            </th>

            <th>
              Status
            </th>

            <th>
              Ações
            </th>
          </tr>
        </thead>

        <tbody>
          {customerReturns.map(
            (customerReturn) => (
              <tr
                key={
                  customerReturn.id
                }
              >
                <td>
                  <strong>
                    {
                      customerReturn
                        .reference_number
                    }
                  </strong>
                </td>

                <td>
                  {
                    customerReturn
                      .customer_name
                  }
                </td>

                <td>
                  {customerReturn
                    .return_type ===
                  'WORK_ORDER'
                    ? 'Oficina'
                    : 'Balcão'}
                </td>

                <td>
                  {formatDate(
                    customerReturn
                      .created_at,
                  )}
                </td>

                <td>
                  {customerReturn
                    .status ===
                  'ACTIVE' ? (
                    <StatusBadge tone="success">
                      Ativa
                    </StatusBadge>
                  ) : (
                    <StatusBadge tone="neutral">
                      Cancelada
                    </StatusBadge>
                  )}
                </td>

                <td>
                  <div className="customer-return-actions">
                    <Button
                      type="button"
                      variant="ghost"
                      size="sm"
                      onClick={() => {
                        onDetails(
                          customerReturn,
                        )
                      }}
                    >
                      <Eye
                        size={15}
                      />

                      Detalhes
                    </Button>

                    {customerReturn
                      .status ===
                      'ACTIVE' && (
                      <Button
                        type="button"
                        variant="ghost"
                        size="sm"
                        onClick={() => {
                          onCancel(
                            customerReturn,
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
            ),
          )}
        </tbody>
      </table>
    </div>
  )
}