# SIGC — Sistema Integrado de Gestão de Cascos

Sistema web interno para controle, gestão e rastreabilidade de cascos relacionados a peças de veículos pesados.

## Sobre o projeto

O SIGC controla o ciclo de vida de peças que possuem obrigação de devolução de casco, abrangendo:

- compras de peças;
- controle de estoque e origem;
- saídas para oficina e balcão;
- devoluções de clientes;
- remessas de cascos aos fornecedores;
- transferências entre filiais;
- devoluções às filiais de origem;
- acompanhamento de prazos;
- auditoria das operações;
- dashboard e consultas consolidadas.

A primeira versão utiliza SQLite e foi estruturada para uma implantação interna com poucos usuários simultâneos.

A especificação oficial do projeto está em:

```text
docs/SIGC_MASTER_SPECIFICATION.md
```

## Tecnologias

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Alembic
- Pydantic
- PyJWT
- Argon2
- Pytest
- Uvicorn

## Estrutura principal

```text
src/
├── api/
├── core/
├── database/
├── dtos/
├── models/
├── queries/
├── repositories/
├── schemas/
├── security/
└── services/

migrations/
scripts/
tests/
docs/
```

## Preparação do ambiente

### 1. Criar o ambiente virtual

No PowerShell:

```powershell
python -m venv .venv
```

Ative:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 2. Instalar as dependências

```powershell
python -m pip install -r requirements.txt
```

## Variáveis de ambiente

O arquivo:

```text
.env.example
```

documenta as variáveis utilizadas pela aplicação.

As configurações reais não devem ser versionadas.

### JWT

A variável abaixo é obrigatória:

```text
SIGC_JWT_SECRET_KEY
```

Ela deve possuir pelo menos 32 caracteres e deve ser diferente entre desenvolvimento e produção.

Exemplo temporário no PowerShell:

```powershell
$env:SIGC_JWT_SECRET_KEY = "substitua-por-uma-chave-local-segura-com-32-caracteres"
```

O tempo padrão do token é 30 minutos e pode ser alterado:

```powershell
$env:SIGC_ACCESS_TOKEN_MINUTES = "30"
```

### Banco de dados

Sem configuração adicional, a aplicação utiliza o banco local de desenvolvimento definido pelo backend.

Também é possível configurar:

```powershell
$env:DATABASE_URL = "sqlite:///data/sigc_dev.db"
```

### CORS

Para permitir acesso de um frontend executado em outra origem:

```powershell
$env:SIGC_CORS_ORIGINS = "http://localhost:5173"
```

Para múltiplas origens:

```powershell
$env:SIGC_CORS_ORIGINS = "http://localhost:5173,http://192.168.0.100:5173"
```

O backend não libera `*` por padrão.

## Banco e migrations

Aplicar todas as migrations:

```powershell
python -m alembic upgrade head
```

Verificar a revisão atual:

```powershell
python -m alembic current
```

Verificar divergências entre models e banco:

```powershell
python -m alembic check
```

## Primeiro Administrador Master

Em uma instalação nova, depois das migrations, crie o primeiro Administrador Master:

```powershell
python -m scripts.bootstrap_admin --full-name "Nome do Administrador" --username administrador --email administrador@empresa.com
```

A senha será solicitada de forma interativa.

O bootstrap deve ser utilizado somente quando ainda não houver Administrador Master cadastrado.

## Executar a API

Com o ambiente virtual ativo e as variáveis necessárias configuradas:

```powershell
python -m uvicorn src.main:app --reload
```

A API estará disponível, por padrão, em:

```text
http://127.0.0.1:8000
```

Documentação Swagger:

```text
http://127.0.0.1:8000/docs
```

Documentação ReDoc:

```text
http://127.0.0.1:8000/redoc
```

OpenAPI:

```text
http://127.0.0.1:8000/openapi.json
```

## Testes

Executar toda a suíte:

```powershell
python -m pytest
```

Exemplo de execução de um módulo específico:

```powershell
python -m pytest tests/api/test_user_route.py -v
```

## Backup

Criar backup do banco:

```powershell
python -m scripts.backup_database
```

Os backups são armazenados fora do versionamento Git.

O processo utiliza backup consistente do SQLite, valida a integridade do arquivo e calcula SHA-256.

## Restauração

A restauração deve ser executada apenas de forma controlada e com a aplicação parada.

Exemplo:

```powershell
python -m scripts.restore_database backups\ARQUIVO.db --user-id 1 --justification "Motivo da restauração"
```

Antes de substituir o banco atual, o processo cria um backup preventivo.

## Segurança

O SIGC utiliza:

- autenticação JWT;
- senhas armazenadas com hash seguro;
- autorização por perfil;
- auditoria das operações relevantes;
- justificativa obrigatória em operações sensíveis;
- foreign keys habilitadas no SQLite;
- configuração sensível fora do código;
- backup e restauração controlados.

Os perfis iniciais são:

- Administrador Master;
- Comprador;
- Vendedor.

## Estado atual do backend

O backend principal encontra-se funcional, com os módulos operacionais, autenticação, autorização, auditoria, consultas, dashboard, backup e migrations implementados e cobertos por testes automatizados.

A próxima etapa do projeto é a integração com o frontend.

## Autor

Lucas do Nascimento Miura