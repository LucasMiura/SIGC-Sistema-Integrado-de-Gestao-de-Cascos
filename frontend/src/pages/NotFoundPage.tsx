import { Link } from 'react-router'

export function NotFoundPage() {
  return (
    <section>
      <h1>Página não encontrada</h1>

      <p>
        O endereço informado não existe
        no SIGC.
      </p>

      <Link to="/">
        Voltar para o início
      </Link>
    </section>
  )
}