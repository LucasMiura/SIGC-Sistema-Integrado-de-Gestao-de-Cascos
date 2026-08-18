import {
  Construction,
} from 'lucide-react'

import {
  Card,
} from '../components/ui/Card'
import {
  PageHeader,
} from '../components/ui/PageHeader'

interface ModulePlaceholderPageProps {
  title: string
  description: string
}

export function ModulePlaceholderPage({
  title,
  description,
}: ModulePlaceholderPageProps) {
  return (
    <div className="page-stack">
      <PageHeader
        eyebrow="SIGC"
        title={title}
        description={description}
      />

      <Card
        className="module-placeholder"
        padding="lg"
      >
        <div className="module-placeholder__icon">
          <Construction
            size={28}
            strokeWidth={1.7}
          />
        </div>

        <div>
          <h2>
            Módulo preparado
          </h2>

          <p>
            A estrutura de navegação já está
            pronta. A implementação definitiva
            será adicionada na próxima fase do
            frontend.
          </p>
        </div>
      </Card>
    </div>
  )
}