# SIGC — Sistema Integrado de Gestão de Cascos

Sistema web interno para controle, gestão e rastreabilidade do ciclo de vida de cascos relacionados a peças de veículos pesados.

## Sobre o projeto

O SIGC foi desenvolvido para centralizar o controle de peças que possuem obrigação de devolução de casco, permitindo acompanhar todo o processo desde a compra da peça até a devolução final do casco ao fornecedor.

O sistema contempla:

- cadastro de peças;
- cadastro de fornecedores e seus contatos;
- compras de peças;
- controle de estoque e origem;
- saídas para oficina e balcão;
- devoluções de clientes;
- devoluções aos fornecedores;
- transferências entre filiais;
- devoluções às filiais de origem;
- acompanhamento de prazos;
- auditoria das operações;
- autenticação e autorização por perfil;
- dashboard e consultas consolidadas.

A primeira versão utiliza SQLite e foi projetada para implantação interna com poucos usuários simultâneos.

A especificação oficial do projeto está disponível em:

```text
docs/SIGC_MASTER_SPECIFICATION.md
```

---

## Arquitetura

O SIGC é dividido em duas aplicações principais:

```text
SIGC
│
├── Backend
│   ├── Python
│   ├── FastAPI
│   ├── SQLAlchemy
│   └── SQLite
│
└── Frontend
    ├── React
    ├── TypeScript
    └── Vite
```

O frontend se comunica com a API REST disponibilizada pelo backend.

---

## Tecnologias

### Backend

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

### Frontend

- React
- TypeScript
- Vite
- React Router
- Lucide React
- Manrope
- ESLint

---

## Estrutura principal

```text
SIGC/
│
├── docs/
│   └── SIGC_MASTER_SPECIFICATION.md
│
├── frontend/
│   ├── public/
│   ├── src/
│   ├── package.json
│   ├── package-lock.json
│   └── vite.config.ts
│
├── migrations/
├── scripts/
├── src/
│   ├── api/
│   ├── core/
│   ├── database/
│   ├── dtos/
│   ├── models/
│   ├── queries/
│   ├── repositories/
│   ├── schemas/
│   ├── security/
│   └── services/
│
├── tests/
├── alembic.ini
├── requirements.txt
└── README.md
```

---

# Preparação do ambiente

Para executar o SIGC em um computador novo, é necessário preparar separadamente o backend e o frontend.

## Pré-requisitos

Instale:

- Python;
- Node.js;
- npm;
- Git.

O npm normalmente é instalado junto com o Node.js.

---

# Backend

## 1. Criar o ambiente virtual

Na raiz do projeto:

```powershell
python -m venv .venv
```

Ative o ambiente virtual:

```powershell
.\.venv\Scripts\Activate.ps1
```

---

## 2. Instalar as dependências

Com o ambiente virtual ativo:

```powershell
python -m pip install -r requirements.txt
```

O arquivo `requirements.txt` contém as dependências Python utilizadas pelo backend.

---

## 3. Configurar as variáveis de ambiente

O arquivo:

```text
.env.example
```

documenta as variáveis utilizadas pela aplicação.

Informações sensíveis e configurações locais não devem ser versionadas.

### JWT

A variável abaixo é obrigatória:

```text
SIGC_JWT_SECRET_KEY
```

A chave deve possuir pelo menos 32 caracteres e deve ser diferente entre os ambientes de desenvolvimento e produção.

Exemplo temporário no PowerShell:

```powershell
$env:SIGC_JWT_SECRET_KEY = "substitua-por-uma-chave-local-segura-com-32-caracteres"
```

O tempo padrão do token é de 30 minutos e pode ser alterado:

```powershell
$env:SIGC_ACCESS_TOKEN_MINUTES = "30"
```

### Banco de dados

Sem configuração adicional, a aplicação utiliza o banco SQLite local definido pelo backend.

Também é possível configurar explicitamente:

```powershell
$env:DATABASE_URL = "sqlite:///data/sigc_dev.db"
```

### CORS

Durante o desenvolvimento, o frontend utiliza normalmente:

```text
http://localhost:5173
```

Configure o backend:

```powershell
$env:SIGC_CORS_ORIGINS = "http://localhost:5173"
```

Para múltiplas origens:

```powershell
$env:SIGC_CORS_ORIGINS = "http://localhost:5173,http://192.168.0.100:5173"
```

O backend não libera `*` por padrão.

---

## 4. Preparar o banco de dados

Aplique todas as migrations:

```powershell
python -m alembic upgrade head
```

Verifique a revisão atual:

```powershell
python -m alembic current
```

Para verificar divergências entre os models e o banco:

```powershell
python -m alembic check
```

---

## 5. Criar o primeiro Administrador Master

Em uma instalação nova, após aplicar as migrations, crie o primeiro Administrador Master:

```powershell
python -m scripts.bootstrap_admin --full-name "Nome do Administrador" --username administrador --email administrador@empresa.com
```

A senha será solicitada de forma interativa.

O bootstrap deve ser utilizado somente quando ainda não existir um Administrador Master cadastrado.

---

## 6. Executar o backend

Com o ambiente virtual ativo e as variáveis necessárias configuradas:

```powershell
python -m uvicorn src.main:app --reload
```

A API estará disponível em:

```text
http://127.0.0.1:8000
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

OpenAPI:

```text
http://127.0.0.1:8000/openapi.json
```

---

# Frontend

O frontend possui suas próprias dependências e não utiliza o `requirements.txt`.

As dependências JavaScript/TypeScript são controladas por:

```text
frontend/package.json
frontend/package-lock.json
```

## 1. Acessar o diretório

Abra outro terminal e execute:

```powershell
cd frontend
```

---

## 2. Instalar as dependências

Para uma instalação reproduzível utilizando o `package-lock.json`:

```powershell
npm ci
```

Durante o desenvolvimento, caso seja necessário atualizar dependências deliberadamente, o npm poderá atualizar o `package-lock.json` conforme a operação realizada.

---

## 3. Executar o frontend

```powershell
npm run dev
```

O Vite exibirá no terminal o endereço utilizado pela aplicação.

Normalmente:

```text
http://localhost:5173
```

O backend deverá estar em execução para que as funcionalidades que dependem da API funcionem corretamente.

---

# Inicialização diária para desenvolvimento

Depois que o ambiente já estiver preparado, não é necessário reinstalar as dependências a cada execução.

## Terminal 1 — Backend

Na raiz do projeto:

```powershell
.\.venv\Scripts\Activate.ps1

$env:SIGC_JWT_SECRET_KEY = "sua-chave-local-segura-com-pelo-menos-32-caracteres"
$env:SIGC_CORS_ORIGINS = "http://localhost:5173"

python -m uvicorn src.main:app --reload
```

## Terminal 2 — Frontend

```powershell
cd frontend
npm run dev
```

Depois, acesse no navegador o endereço informado pelo Vite.

---

# Testes e validação

## Backend

Executar toda a suíte:

```powershell
python -m pytest
```

Executar um módulo específico:

```powershell
python -m pytest tests/api/test_user_route.py -v
```

Após alterações localizadas, recomenda-se executar o teste específico e, em seguida, toda a suíte para verificar regressões.

---

## Frontend

Dentro de:

```text
frontend/
```

execute o lint:

```powershell
npm run lint
```

Depois execute o build:

```powershell
npm run build
```

Antes de considerar uma alteração do frontend concluída, ambos devem finalizar sem erros.

---

# Backup

Para criar um backup do banco:

```powershell
python -m scripts.backup_database
```

Os backups são armazenados fora do versionamento Git.

O processo utiliza backup consistente do SQLite, valida a integridade do arquivo e calcula SHA-256.

---

# Restauração

A restauração deve ser executada somente de forma controlada e com a aplicação parada.

Exemplo:

```powershell
python -m scripts.restore_database backups\ARQUIVO.db --user-id 1 --justification "Motivo da restauração"
```

Antes de substituir o banco atual, o processo cria um backup preventivo.

---

# Segurança

O SIGC utiliza:

- autenticação JWT;
- senhas armazenadas utilizando hash seguro;
- autorização baseada em perfil;
- proteção de rotas no backend e frontend;
- auditoria das operações relevantes;
- justificativa obrigatória para operações sensíveis;
- preservação de registros históricos;
- foreign keys habilitadas no SQLite;
- configurações sensíveis fora do código;
- backup e restauração controlados.

Os perfis iniciais são:

- Administrador Master;
- Comprador;
- Vendedor.

---

# Interface e experiência do usuário

O frontend utiliza um Design System próprio do SIGC, buscando manter consistência visual entre os módulos.

Entre os padrões utilizados estão:

- layout administrativo responsivo;
- sidebar de navegação;
- cabeçalho contextual;
- componentes reutilizáveis;
- cards e indicadores;
- modais e painéis padronizados;
- feedback visual de carregamento;
- mensagens de erro destacadas;
- notificações de sucesso por toast;
- filtros de status com seleção claramente identificável;
- distinção entre registros ativos e inativos;
- ordenação dos registros priorizando os mais recentes;
- confirmações para operações sensíveis;
- estados vazios e mensagens contextuais.

---

# Estado atual do projeto

O backend principal encontra-se funcional e possui:

- autenticação;
- autorização;
- usuários;
- fornecedores;
- contatos de fornecedores;
- peças;
- compras;
- saídas;
- devoluções de clientes;
- devoluções aos fornecedores;
- transferências;
- devoluções de transferências;
- auditoria;
- consultas;
- dashboard;
- controle de prazos;
- backup e restauração;
- migrations;
- testes automatizados.

O frontend encontra-se em desenvolvimento ativo e já possui integração funcional com a API para os módulos implementados na interface, incluindo:

- autenticação;
- controle de acesso;
- layout principal;
- dashboard;
- fornecedores;
- contatos de fornecedores;
- peças;
- compras.

Os demais fluxos operacionais serão incorporados progressivamente à interface mantendo os padrões de arquitetura, segurança e experiência do usuário definidos para o projeto.

---

# Documentação oficial

As regras de negócio, decisões arquiteturais e padrões oficiais do projeto devem permanecer documentados em:

```text
docs/SIGC_MASTER_SPECIFICATION.md
```

Alterações importantes no comportamento do sistema devem ser verificadas em relação à especificação antes da implementação.

---

# Autor

Lucas do Nascimento Miura