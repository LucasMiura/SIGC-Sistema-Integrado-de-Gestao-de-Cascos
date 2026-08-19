import {
  AlertCircle,
  ArrowRight,
  LockKeyhole,
  UserRound,
  Eye,
  EyeOff,
} from 'lucide-react'
import {
  useState,
  type FormEvent,
} from 'react'
import {
  useLocation,
  useNavigate,
} from 'react-router'

import sigcLogo from '../assets/brand/sigc-logo-primary.png'
import loginIllustration from '../assets/illustrations/sigc-login-illustration.png'
import {
  Button,
} from '../components/ui/Button'
import {
  TextField,
} from '../components/ui/TextField'
import { useAuth } from '../hooks/useAuth'
import {
  ApiError,
} from '../services/httpClient'

interface LoginLocationState {
  from?: string
}

export function LoginPage() {
  const [
    loginValue,
    setLoginValue,
  ] = useState('')

  const [
    password,
    setPassword,
  ] = useState('')

  const [
    errorMessage,
    setErrorMessage,
  ] = useState<string | null>(
    null,
  )

  const [
    isSubmitting,
    setIsSubmitting,
  ] = useState(false)
  
  const [
    isPasswordVisible,
    setIsPasswordVisible,
  ] = useState(false)

  const {
    login,
  } = useAuth()

  const navigate = useNavigate()
  const location = useLocation()

  async function handleSubmit(
    event: FormEvent<HTMLFormElement>,
  ) {
    event.preventDefault()

    if (isSubmitting) {
      return
    }

    setErrorMessage(null)
    setIsSubmitting(true)

    try {
      await login({
        login: loginValue,
        password,
      })

      const state =
        location.state as
          | LoginLocationState
          | null

      const destination =
        state?.from &&
        state.from !== '/login'
          ? state.from
          : '/'

      navigate(
        destination,
        {
          replace: true,
        },
      )
    } catch (error) {
      if (error instanceof ApiError) {
        setErrorMessage(
          error.message,
        )
      } else {
        setErrorMessage(
          'Não foi possível conectar ao SIGC.',
        )
      }
    } finally {
      setIsSubmitting(false)
    }
  }

  return (
    <main className="login-page">
      <section
        className="login-visual"
        aria-label="Sistema Integrado de Gestão de Cascos"
      >
        <div className="login-visual__background">
          <img
            src={loginIllustration}
            alt=""
            className="login-visual__illustration"
            aria-hidden="true"
          />

          <div className="login-visual__overlay" />
        </div>

        <div className="login-visual__content">
          <img
            src={sigcLogo}
            alt="SIGC — Sistema Integrado de Gestão de Cascos"
            className="login-visual__logo"
          />

          <div className="login-visual__message">
            <span className="login-visual__eyebrow">
              Controle e rastreabilidade
            </span>

            <h1>
              Cada casco.
              <br />
              Cada movimento.
              <br />
              Sob controle.
            </h1>

            <p>
              Informação operacional organizada
              para acompanhar o ciclo completo
              das peças com segurança e
              precisão.
            </p>
          </div>

          <div className="login-visual__footer">
            <span>
              SIGC
            </span>

            <span
              className="login-visual__footer-divider"
              aria-hidden="true"
            />

            <span>
              Sistema interno
            </span>
          </div>
        </div>
      </section>

      <section className="login-access">
        <div className="login-access__inner">
          <header className="login-access__header">
            <span className="login-access__eyebrow">
              Bem-vindo
            </span>

            <h2>
              Acesse sua conta
            </h2>

            <p>
              Entre com suas credenciais para
              acessar o ambiente operacional.
            </p>
          </header>

          <form
            className="login-form"
            onSubmit={handleSubmit}
          >
            <div className="login-field-wrapper">
              <UserRound
                className="login-field-icon"
                size={18}
                strokeWidth={1.8}
                aria-hidden="true"
              />

              <TextField
                label="Username ou e-mail"
                type="text"
                name="login"
                autoComplete="username"
                value={loginValue}
                onChange={(event) => {
                  setLoginValue(
                    event.target.value,
                  )

                  if (errorMessage) {
                    setErrorMessage(null)
                  }
                }}
                disabled={isSubmitting}
                required
                autoFocus
              />
            </div>

            <div className="login-field-wrapper">
              <LockKeyhole
                className="login-field-icon"
                size={18}
                strokeWidth={1.8}
                aria-hidden="true"
              />

              <TextField
                label="Senha"
                type={
                  isPasswordVisible
                    ? 'text'
                    : 'password'
                }
                name="password"
                autoComplete="current-password"
                value={password}
                onChange={(event) => {
                  setPassword(
                    event.target.value,
                  )

                  if (errorMessage) {
                    setErrorMessage(null)
                  }
                }}
                disabled={isSubmitting}
                required
                trailingAction={
                  <button
                    type="button"
                    className="login-password-field__toggle"
                    aria-label={
                      isPasswordVisible
                        ? 'Ocultar senha'
                        : 'Mostrar senha'
                    }
                    aria-pressed={
                      isPasswordVisible
                    }
                    disabled={isSubmitting}
                    onClick={() => {
                      setIsPasswordVisible(
                        (currentValue) =>
                          !currentValue,
                      )
                    }}
                  >
                    {isPasswordVisible ? (
                      <EyeOff
                        size={18}
                        strokeWidth={1.8}
                      />
                    ) : (
                      <Eye
                        size={18}
                        strokeWidth={1.8}
                      />
                    )}
                  </button>
                }
              />
            </div>

            {errorMessage && (
              <div
                className="login-error"
                role="alert"
              >
                <AlertCircle
                  size={18}
                  strokeWidth={1.8}
                  aria-hidden="true"
                />

                <span>
                  {errorMessage}
                </span>
              </div>
            )}

            <Button
              type="submit"
              size="lg"
              fullWidth
              disabled={isSubmitting}
              className="login-submit"
            >
              <span>
                {isSubmitting
                  ? 'Entrando...'
                  : 'Entrar no SIGC'}
              </span>

              {!isSubmitting && (
                <ArrowRight
                  size={18}
                  strokeWidth={1.9}
                  aria-hidden="true"
                />
              )}
            </Button>
          </form>

          <footer className="login-access__footer">
            <div
              className="login-access__security"
              aria-hidden="true"
            >
              <LockKeyhole
                size={14}
                strokeWidth={1.8}
              />
            </div>

            <p>
              Acesso restrito a usuários
              autorizados.
            </p>
          </footer>
        </div>
      </section>
    </main>
  )
}