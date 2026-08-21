import {
  AlertCircle,
  ArrowRight,
  Boxes,
  CheckCircle2,
  Clock3,
  PackageCheck,
  RefreshCcw,
  RotateCcw,
  Search,
  Truck,
  Warehouse,
} from 'lucide-react'
import {
  useEffect,
  useMemo,
  useState,
} from 'react'
import {
  useNavigate,
} from 'react-router'

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
  type StatusBadgeTone,
} from '../components/ui/StatusBadge'
import {
  hasPermission,
} from '../config/permissions'
import { useAuth } from '../hooks/useAuth'
import {
  dashboardService,
} from '../services/dashboardService'
import {
  ApiError,
} from '../services/httpClient'
import type {
  DashboardStockPositionItem,
  DashboardSummary,
} from '../types/dashboard'

const numberFormatter =
  new Intl.NumberFormat(
    'pt-BR',
  )

interface DeadlineItem {
  label: string
  description: string
  quantity: number
  tone: StatusBadgeTone
}

function formatQuantity(
  value: number,
): string {
  return numberFormatter.format(
    value,
  )
}

function getDashboardErrorMessage(
  error: unknown,
): string {
  if (error instanceof ApiError) {
    return error.message
  }

  return (
    'Não foi possível carregar os indicadores do Dashboard.'
  )
}

export function DashboardPage() {
  const {
    session,
  } = useAuth()

  const navigate =
    useNavigate()

  const [
    summary,
    setSummary,
  ] = useState<
    DashboardSummary | null
  >(null)

  const [
    stockPosition,
    setStockPosition,
  ] = useState<
    DashboardStockPositionItem[]
  >([])

  const [
    stockSearch,
    setStockSearch,
  ] = useState('')

  const [
    isLoading,
    setIsLoading,
  ] = useState(true)

  const [
    errorMessage,
    setErrorMessage,
  ] = useState<string | null>(
    null,
  )

  const firstName =
    session?.user.full_name
      .trim()
      .split(' ')[0]
    ?? 'Usuário'

  const canViewTracking =
    hasPermission(
      session?.role_name,
      'purchaseTracking',
    )

  async function reloadDashboard() {
    setIsLoading(true)
    setErrorMessage(null)

    try {
      const [
        summaryData,
        stockPositionData,
      ] = await Promise.all([
        dashboardService
          .getSummary(),

        dashboardService
          .getStockPosition(),
      ])

      setSummary(
        summaryData,
      )

      setStockPosition(
        stockPositionData,
      )
    } catch (error) {
      setSummary(null)
      setStockPosition([])

      setErrorMessage(
        getDashboardErrorMessage(
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
        dashboardService
          .getSummary(),

        dashboardService
          .getStockPosition(),
      ])
        .then(
          ([
            summaryData,
            stockPositionData,
          ]) => {
            if (ignore) {
              return
            }

            setSummary(
              summaryData,
            )

            setStockPosition(
              stockPositionData,
            )

            setErrorMessage(null)
          },
        )
        .catch(
          (error: unknown) => {
            if (ignore) {
              return
            }

            setSummary(null)
            setStockPosition([])

            setErrorMessage(
              getDashboardErrorMessage(
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

  const filteredStockPosition =
    useMemo(
      () => {
        const normalizedSearch =
          stockSearch
            .trim()
            .toLocaleLowerCase(
              'pt-BR',
            )

        const sorted =
          [...stockPosition].sort(
            (left, right) =>
              left.part_name.localeCompare(
                right.part_name,
                'pt-BR',
                {
                  sensitivity: 'base',
                },
              ),
          )

        if (!normalizedSearch) {
          return sorted
        }

        return sorted.filter(
          (item) => {
            const searchable =
              [
                item.part_name,
                item.part_code,
              ]
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
        stockPosition,
        stockSearch,
      ],
    )

  if (isLoading) {
    return (
      <div className="page-stack">
        <PageHeader
          eyebrow="Visão geral"
          title={`Olá, ${firstName}.`}
          description="Carregando a situação operacional atual do SIGC."
        />

        <section
          className="dashboard-state"
          aria-live="polite"
        >
          <div className="dashboard-state__spinner" />

          <div>
            <strong>
              Atualizando indicadores
            </strong>

            <p>
              Consultando as informações
              operacionais mais recentes.
            </p>
          </div>
        </section>
      </div>
    )
  }

  if (
    errorMessage ||
    !summary
  ) {
    return (
      <div className="page-stack">
        <PageHeader
          eyebrow="Visão geral"
          title={`Olá, ${firstName}.`}
          description="Não foi possível apresentar os indicadores operacionais neste momento."
        />

        <Card
          className="dashboard-error"
          padding="lg"
        >
          <div className="dashboard-error__icon">
            <AlertCircle
              size={26}
              strokeWidth={1.8}
            />
          </div>

          <div className="dashboard-error__content">
            <span>
              Falha ao carregar
            </span>

            <h2>
              Os indicadores não puderam
              ser atualizados.
            </h2>

            <p>
              {errorMessage ??
                'Ocorreu um erro inesperado ao consultar o Dashboard.'}
            </p>

            <Button
              variant="secondary"
              type="button"
              onClick={() => {
                void reloadDashboard()
              }}
            >
              <RotateCcw
                size={16}
              />

              Tentar novamente
            </Button>
          </div>
        </Card>
      </div>
    )
  }

  const deadlineItems:
    DeadlineItem[] = [
      {
        label: 'Normal',
        description:
          'Mais de 30 dias',
        quantity:
          summary.deadline
            .normal_quantity,
        tone: 'success',
      },
      {
        label: 'Atenção',
        description:
          'De 8 a 30 dias',
        quantity:
          summary.deadline
            .attention_quantity,
        tone: 'attention',
      },
      {
        label: 'Urgente',
        description:
          'Até 7 dias',
        quantity:
          summary.deadline
            .urgent_quantity,
        tone: 'urgent',
      },
      {
        label: 'Atrasado',
        description:
          'Prazo vencido',
        quantity:
          summary.deadline
            .overdue_quantity,
        tone: 'overdue',
      },
    ]

  const criticalQuantity =
    summary.deadline
      .urgent_quantity +
    summary.deadline
      .overdue_quantity

  return (
    <div className="page-stack">
      <PageHeader
        eyebrow="Visão geral"
        title={`Olá, ${firstName}.`}
        description="Acompanhe os principais indicadores do ciclo de cascos e identifique rapidamente o que exige atenção."
        actions={
          canViewTracking ? (
            <Button
              variant="secondary"
              type="button"
              onClick={() => {
                navigate(
                  '/acompanhamento',
                )
              }}
            >
              Ver acompanhamento

              <ArrowRight
                size={16}
              />
            </Button>
          ) : undefined
        }
      />

      <section
        className="dashboard-overview"
        aria-label="Resumo operacional"
      >
        <Card
          className="dashboard-primary-card"
          padding="lg"
        >
          <div className="dashboard-primary-card__icon">
            <Boxes
              size={25}
              strokeWidth={1.7}
            />
          </div>

          <div className="dashboard-primary-card__content">
            <span className="dashboard-card-label">
              Quantidade disponível
            </span>

            <strong className="dashboard-primary-card__value">
              {formatQuantity(
                summary
                  .total_available_quantity,
              )}
            </strong>

            <p>
              Cascos disponíveis nas
              origens atualmente
              acompanhadas.
            </p>
          </div>
        </Card>

        <Card
          className="dashboard-primary-card"
          padding="lg"
        >
          <div className="dashboard-primary-card__icon">
            <Warehouse
              size={25}
              strokeWidth={1.7}
            />
          </div>

          <div className="dashboard-primary-card__content">
            <span className="dashboard-card-label">
              Origens com saldo
            </span>

            <strong className="dashboard-primary-card__value">
              {formatQuantity(
                summary
                  .total_origin_count,
              )}
            </strong>

            <p>
              Origens consideradas na
              situação operacional atual.
            </p>
          </div>
        </Card>

        <Card
          className={[
            'dashboard-primary-card',
            criticalQuantity > 0
              ? 'dashboard-primary-card--critical'
              : '',
          ]
            .filter(Boolean)
            .join(' ')}
          padding="lg"
        >
          <div className="dashboard-primary-card__icon">
            <Clock3
              size={25}
              strokeWidth={1.7}
            />
          </div>

          <div className="dashboard-primary-card__content">
            <span className="dashboard-card-label">
              Exigem ação
            </span>

            <strong className="dashboard-primary-card__value">
              {formatQuantity(
                criticalQuantity,
              )}
            </strong>

            <p>
              Quantidade urgente ou
              atualmente atrasada.
            </p>
          </div>
        </Card>
      </section>

      <section className="dashboard-section">
        <div className="dashboard-section__heading">
          <div>
            <span>
              Posição operacional
            </span>

            <h2>
              Estoque e cascos
            </h2>
          </div>

          <p>
            Consulte onde estão as peças
            e os cascos de cada código
            cadastrado.
          </p>
        </div>

        <Card
          className="dashboard-stock-position"
          padding="none"
        >
          <div className="dashboard-stock-position__toolbar">
            <div className="dashboard-stock-search">
              <Search
                size={18}
                strokeWidth={1.8}
                aria-hidden="true"
              />

              <input
                type="search"
                value={stockSearch}
                placeholder="Buscar peça ou código"
                aria-label="Buscar posição de estoque"
                onChange={(event) => {
                  setStockSearch(
                    event.target.value,
                  )
                }}
              />
            </div>

            <span className="dashboard-stock-position__count">
              {filteredStockPosition.length}
              {' '}
              {filteredStockPosition.length ===
              1
                ? 'peça encontrada'
                : 'peças encontradas'}
            </span>
          </div>

          {filteredStockPosition.length ===
          0 ? (
            <div className="dashboard-stock-empty">
              <div className="dashboard-stock-empty__icon">
                <Boxes
                  size={22}
                  strokeWidth={1.7}
                />
              </div>

              <strong>
                Nenhuma peça encontrada
              </strong>

              <p>
                Não existem peças que
                correspondam à pesquisa
                informada.
              </p>
            </div>
          ) : (
            <div className="dashboard-stock-table-wrapper">
              <table className="dashboard-stock-table">
                <thead>
                  <tr>
                    <th>
                      Peça
                    </th>

                    <th>
                      Código
                    </th>

                    <th className="dashboard-stock-table__number">
                      Em estoque
                    </th>

                    <th className="dashboard-stock-table__number">
                      Na oficina
                    </th>

                    <th className="dashboard-stock-table__number">
                      Com clientes
                    </th>

                    <th
                      className="dashboard-stock-table__number"
                      title="Cascos retornados da oficina"
                    >
                      Ret. oficina
                    </th>

                    <th
                      className="dashboard-stock-table__number"
                      title="Cascos retornados do balcão"
                    >
                      Ret. balcão
                    </th>

                    <th
                      className="dashboard-stock-table__number"
                      title="Cascos disponíveis para devolução"
                    >
                      Disponíveis
                    </th>
                  </tr>
                </thead>

                <tbody>
                  {filteredStockPosition.map(
                    (item) => (
                      <tr
                        key={
                          item.part_id
                        }
                      >
                        <td>
                          <div className="dashboard-stock-table__part">
                            <div className="dashboard-stock-table__part-icon">
                              <Boxes
                                size={17}
                                strokeWidth={1.8}
                              />
                            </div>

                            <strong>
                              {
                                item.part_name
                              }
                            </strong>
                          </div>
                        </td>

                        <td>
                          <span className="dashboard-stock-table__code">
                            {
                              item.part_code
                            }
                          </span>
                        </td>

                        <td className="dashboard-stock-table__number">
                          <strong>
                            {formatQuantity(
                              item
                                .stock_quantity,
                            )}
                          </strong>
                        </td>

                        <td className="dashboard-stock-table__number">
                          {formatQuantity(
                            item
                              .workshop_pending_quantity,
                          )}
                        </td>

                        <td className="dashboard-stock-table__number">
                          {formatQuantity(
                            item
                              .customer_pending_quantity,
                          )}
                        </td>

                        <td className="dashboard-stock-table__number">
                          {formatQuantity(
                            item
                              .workshop_returned_quantity,
                          )}
                        </td>

                        <td className="dashboard-stock-table__number">
                          {formatQuantity(
                            item
                              .customer_returned_quantity,
                          )}
                        </td>

                        <td className="dashboard-stock-table__number">
                          <span
                            className={[
                              'dashboard-stock-table__available',
                              item
                                .available_core_quantity >
                              0
                                ? 'dashboard-stock-table__available--positive'
                                : '',
                            ]
                              .filter(
                                Boolean,
                              )
                              .join(' ')}
                          >
                            {formatQuantity(
                              item
                                .available_core_quantity,
                            )}
                          </span>
                        </td>
                      </tr>
                    ),
                  )}
                </tbody>
              </table>
            </div>
          )}
        </Card>
      </section>

      <section className="dashboard-section">
        <div className="dashboard-section__heading">
          <div>
            <span>
              Controle de prazos
            </span>

            <h2>
              Situação das devoluções
            </h2>
          </div>

          <p>
            Classificação da quantidade
            pendente conforme o prazo de
            devolução.
          </p>
        </div>

        <div className="dashboard-deadline-grid">
          {deadlineItems.map(
            (item) => (
              <Card
                key={item.label}
                className="dashboard-deadline-card"
                padding="md"
              >
                <div className="dashboard-deadline-card__header">
                  <StatusBadge
                    tone={item.tone}
                  >
                    {item.label}
                  </StatusBadge>

                  <span>
                    {item.description}
                  </span>
                </div>

                <strong>
                  {formatQuantity(
                    item.quantity,
                  )}
                </strong>

                <span className="dashboard-deadline-card__caption">
                  unidades
                </span>
              </Card>
            ),
          )}
        </div>
      </section>

      <section className="dashboard-section">
        <div className="dashboard-section__heading">
          <div>
            <span>
              Fluxo de retorno
            </span>

            <h2>
              Panorama das devoluções
            </h2>
          </div>

          <p>
            Resumo das principais etapas
            do retorno dos cascos.
          </p>
        </div>

        <div className="dashboard-flow-grid">
          <Card
            className="dashboard-flow-card"
            padding="lg"
          >
            <div className="dashboard-flow-card__header">
              <div className="dashboard-flow-card__icon">
                <RefreshCcw
                  size={20}
                />
              </div>

              <div>
                <span className="dashboard-card-label">
                  Clientes
                </span>

                <h3>
                  Devoluções recebidas
                </h3>
              </div>
            </div>

            <div className="dashboard-flow-card__main">
              <strong>
                {formatQuantity(
                  summary
                    .customer_returns
                    .pending_quantity,
                )}
              </strong>

              <span>
                unidades pendentes
              </span>
            </div>

            <div className="dashboard-flow-card__stats">
              <div>
                <span>
                  Saíram
                </span>

                <strong>
                  {formatQuantity(
                    summary
                      .customer_returns
                      .outbound_quantity,
                  )}
                </strong>
              </div>

              <div>
                <span>
                  Retornaram
                </span>

                <strong>
                  {formatQuantity(
                    summary
                      .customer_returns
                      .returned_quantity,
                  )}
                </strong>
              </div>

              <div>
                <span>
                  Concluídas
                </span>

                <strong>
                  {formatQuantity(
                    summary
                      .customer_returns
                      .completed_origin_count,
                  )}
                </strong>
              </div>
            </div>
          </Card>

          <Card
            className="dashboard-flow-card"
            padding="lg"
          >
            <div className="dashboard-flow-card__header">
              <div className="dashboard-flow-card__icon">
                <Truck
                  size={20}
                />
              </div>

              <div>
                <span className="dashboard-card-label">
                  Fornecedores
                </span>

                <h3>
                  Remessas de cascos
                </h3>
              </div>
            </div>

            <div className="dashboard-flow-card__main">
              <strong>
                {formatQuantity(
                  summary
                    .supplier_returns
                    .pending_quantity,
                )}
              </strong>

              <span>
                unidades pendentes
              </span>
            </div>

            <div className="dashboard-flow-card__stats dashboard-flow-card__stats--two">
              <div>
                <span>
                  Disponíveis
                </span>

                <strong>
                  {formatQuantity(
                    summary
                      .supplier_returns
                      .available_quantity,
                  )}
                </strong>
              </div>

              <div>
                <span>
                  Devolvidas
                </span>

                <strong>
                  {formatQuantity(
                    summary
                      .supplier_returns
                      .returned_quantity,
                  )}
                </strong>
              </div>
            </div>
          </Card>

          <Card
            className="dashboard-flow-card"
            padding="lg"
          >
            <div className="dashboard-flow-card__header">
              <div className="dashboard-flow-card__icon">
                <PackageCheck
                  size={20}
                />
              </div>

              <div>
                <span className="dashboard-card-label">
                  Transferências
                </span>

                <h3>
                  Retorno à origem
                </h3>
              </div>
            </div>

            <div className="dashboard-flow-card__main">
              <strong>
                {formatQuantity(
                  summary
                    .transfer_returns
                    .pending_quantity,
                )}
              </strong>

              <span>
                unidades pendentes
              </span>
            </div>

            <div className="dashboard-flow-card__stats dashboard-flow-card__stats--two">
              <div>
                <span>
                  Disponíveis
                </span>

                <strong>
                  {formatQuantity(
                    summary
                      .transfer_returns
                      .available_quantity,
                  )}
                </strong>
              </div>

              <div>
                <span>
                  Devolvidas
                </span>

                <strong>
                  {formatQuantity(
                    summary
                      .transfer_returns
                      .returned_quantity,
                  )}
                </strong>
              </div>
            </div>
          </Card>
        </div>
      </section>

      <section className="dashboard-customer-status">
        <Card
          className="dashboard-customer-status__card"
          padding="lg"
        >
          <div className="dashboard-customer-status__header">
            <div>
              <span className="dashboard-card-label">
                Devoluções de clientes
              </span>

              <h2>
                Situação das origens
              </h2>
            </div>

            <CheckCircle2
              size={22}
              strokeWidth={1.7}
              aria-hidden="true"
            />
          </div>

          <div className="dashboard-customer-status__grid">
            <div>
              <span>
                Pendentes
              </span>

              <strong>
                {formatQuantity(
                  summary
                    .customer_returns
                    .pending_origin_count,
                )}
              </strong>
            </div>

            <div>
              <span>
                Parciais
              </span>

              <strong>
                {formatQuantity(
                  summary
                    .customer_returns
                    .partial_origin_count,
                )}
              </strong>
            </div>

            <div>
              <span>
                Concluídas
              </span>

              <strong>
                {formatQuantity(
                  summary
                    .customer_returns
                    .completed_origin_count,
                )}
              </strong>
            </div>
          </div>
        </Card>
      </section>
    </div>
  )
}