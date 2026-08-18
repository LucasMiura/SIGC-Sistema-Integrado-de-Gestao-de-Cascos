import {
  useState,
  type FormEvent,
} from 'react'
import {
  useLocation,
  useNavigate,
} from 'react-router'

import {
  ApiError,
} from '../services/httpClient'
import { useAuth } from '../hooks/useAuth'

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
      <section className="login-panel">
        <header>
          <p className="login-system-name">
            SIGC
          </p>

          <h1>
            Acessar sistema
          </h1>

          <p>
            Utilize seu username ou
            e-mail e sua senha.
          </p>
        </header>

        <form
          className="login-form"
          onSubmit={
            handleSubmit
          }
        >
          <label>
            <span>
              Username ou e-mail
            </span>

            <input
              type="text"
              name="login"
              autoComplete="username"
              value={loginValue}
              onChange={
                (event) => {
                  setLoginValue(
                    event.target.value,
                  )
                }
              }
              disabled={
                isSubmitting
              }
              required
              autoFocus
            />
          </label>

          <label>
            <span>
              Senha
            </span>

            <input
              type="password"
              name="password"
              autoComplete="current-password"
              value={password}
              onChange={
                (event) => {
                  setPassword(
                    event.target.value,
                  )
                }
              }
              disabled={
                isSubmitting
              }
              required
            />
          </label>

          {errorMessage && (
            <p
              className="login-error"
              role="alert"
            >
              {errorMessage}
            </p>
          )}

          <button
            type="submit"
            disabled={
              isSubmitting
            }
          >
            {isSubmitting
              ? 'Entrando...'
              : 'Entrar'}
          </button>
        </form>

        <p className="temporary-notice">
          Interface provisória.
          O Design System ainda será
          definido.
        </p>
      </section>
    </main>
  )
}