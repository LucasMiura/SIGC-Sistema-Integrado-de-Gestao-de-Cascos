# SIGC — Frontend

Frontend do **SIGC — Sistema Integrado de Gestão de Cascos**.

Esta aplicação fornece a interface web utilizada pelos usuários para acessar os recursos disponibilizados pela API do SIGC.

A documentação geral e as regras oficiais do projeto estão disponíveis na raiz do repositório e em:

```text
docs/SIGC_MASTER_SPECIFICATION.md
```

---

## Tecnologias

O frontend utiliza:

- React;
- TypeScript;
- Vite;
- React Router;
- Lucide React;
- Manrope;
- ESLint.

As dependências são controladas pelos arquivos:

```text
package.json
package-lock.json
```

---

## Pré-requisitos

Antes de executar o frontend, é necessário possuir:

- Node.js;
- npm.

O backend do SIGC também deve estar configurado e em execução para que as funcionalidades dependentes da API funcionem corretamente.

---

## Instalação

Acesse o diretório do frontend:

```powershell
cd frontend
```

Instale as dependências utilizando o `package-lock.json`:

```powershell
npm ci
```

O uso de `npm ci` é recomendado para novas instalações porque utiliza as versões registradas no `package-lock.json`, tornando o ambiente mais reproduzível entre computadores.

---

## Executar em desenvolvimento

Dentro de `frontend/`:

```powershell
npm run dev
```

O Vite exibirá o endereço da aplicação no terminal.

Normalmente:

```text
http://localhost:5173
```

---

## Backend

Durante o desenvolvimento local, o backend normalmente é executado em:

```text
http://127.0.0.1:8000
```

O backend deve permitir a origem utilizada pelo frontend através da configuração de CORS.

Exemplo no PowerShell:

```powershell
$env:SIGC_CORS_ORIGINS = "http://localhost:5173"
```

A configuração completa do backend está documentada no `README.md` localizado na raiz do projeto.

---

## Scripts

### Desenvolvimento

```powershell
npm run dev
```

Inicia o servidor de desenvolvimento do Vite.

### Lint

```powershell
npm run lint
```

Executa o ESLint para verificar problemas no código.

### Build

```powershell
npm run build
```

Executa a validação TypeScript e gera o build de produção.

### Preview

```powershell
npm run preview
```

Executa localmente uma prévia do build gerado.

---

## Validação antes de concluir alterações

Após alterações no frontend, execute:

```powershell
npm run lint
npm run build
```

Ambos devem finalizar sem erros antes que a alteração seja considerada concluída.

---

## Estrutura

A estrutura principal do frontend segue a organização:

```text
src/
│
├── assets/
├── components/
│   ├── layout/
│   ├── parts/
│   ├── purchases/
│   ├── suppliers/
│   └── ui/
│
├── hooks/
├── pages/
├── services/
├── styles/
└── main.tsx
```

A estrutura pode evoluir conforme novos módulos sejam incorporados.

---

## Arquitetura da interface

O frontend é organizado em páginas, componentes reutilizáveis, serviços responsáveis pela comunicação com a API e componentes compartilhados do Design System.

A separação busca evitar:

- duplicação de regras de interface;
- chamadas HTTP espalhadas pelos componentes;
- estilos inconsistentes;
- comportamentos diferentes para operações equivalentes.

Os módulos devem reutilizar os componentes e padrões existentes sempre que possível.

---

## Autenticação

O frontend possui integração com a autenticação do backend.

O fluxo inclui:

1. envio das credenciais para a API;
2. recebimento do token de acesso;
3. identificação do usuário autenticado;
4. proteção das rotas privadas;
5. controle de acesso conforme o perfil;
6. logout e encerramento da sessão.

A segurança das operações não depende apenas do frontend. O backend continua responsável por validar autenticação e autorização em todas as rotas protegidas.

---

## Design System

O SIGC utiliza um padrão visual próprio desenvolvido para manter consistência entre os módulos.

Entre os princípios adotados estão:

- hierarquia visual clara;
- baixa poluição visual;
- espaçamento consistente;
- componentes reutilizáveis;
- tipografia padronizada;
- contraste adequado;
- estados de interação perceptíveis;
- feedback imediato para ações do usuário;
- responsividade;
- acessibilidade básica dos controles.

---

## Feedback ao usuário

### Erros

Erros que impedem a conclusão de uma operação devem possuir destaque visual suficiente para serem percebidos imediatamente.

Quando ocorrerem dentro de formulários ou painéis com rolagem, o feedback não deve depender de o usuário localizar manualmente uma mensagem fora da área visível.

### Sucesso

Operações concluídas com sucesso utilizam notificações do tipo **toast**, permitindo confirmar a ação sem interromper o fluxo com um novo modal.

Exemplos:

```text
Fornecedor cadastrado com sucesso.
Peça atualizada com sucesso.
Contato desativado com sucesso.
Compra e itens registrados com sucesso.
```

### Filtros

O estado selecionado dos filtros deve possuir contraste evidente.

O usuário deve conseguir identificar imediatamente, por exemplo, se está visualizando:

```text
Ativos | Inativos
```

ou:

```text
Todas | Pendentes | Recebidas | Canceladas
```

---

## Ordenação das listagens

Como regra geral, listagens operacionais priorizam registros mais recentes.

Quando houver distinção entre registros ativos e inativos:

- ativos são apresentados por padrão;
- inativos podem ser consultados por meio do filtro correspondente.

Algumas listagens podem possuir regras adicionais conforme sua função operacional.

Por exemplo, contatos de fornecedores priorizam o contato principal antes dos demais registros.

---

## Modais e painéis

Modais e painéis devem seguir padrões consistentes de:

- largura;
- padding;
- bordas arredondadas;
- cabeçalho;
- botão de fechamento;
- área rolável;
- ações no rodapé;
- mensagens de erro;
- responsividade.

Quando fechar uma janela não significa cancelar uma operação já persistida, a interface deve deixar essa diferença clara.

No fluxo de itens de uma compra, por exemplo, existe uma ação explícita de **Concluir lançamento**, evitando que o usuário interprete o botão de fechar como cancelamento dos itens já registrados.

---

## Módulos implementados

Atualmente o frontend possui implementação funcional para:

### Autenticação

- login;
- logout;
- sessão autenticada;
- proteção de rotas;
- controle de acesso.

### Dashboard

- visão geral;
- indicadores operacionais;
- acompanhamento de prazos;
- acompanhamento dos fluxos de retorno.

### Fornecedores

- listagem;
- filtros;
- cadastro;
- edição;
- ativação;
- desativação;
- feedback das operações.

### Contatos de fornecedores

- listagem;
- cadastro;
- edição;
- contato principal;
- ativação;
- desativação;
- feedback das operações.

### Peças

- listagem;
- filtros;
- cadastro;
- edição;
- ativação;
- desativação;
- feedback das operações.

### Compras

- listagem;
- filtros por status;
- cadastro;
- edição;
- gerenciamento dos itens;
- recebimento;
- cancelamento;
- feedback das operações.

---

## Próximas implementações

Os demais fluxos já existentes no backend serão incorporados progressivamente ao frontend.

A implementação deverá preservar:

- regras de negócio existentes;
- permissões;
- auditoria;
- rastreabilidade;
- consistência do Design System;
- padrões de UX já consolidados.

---

## Documentação relacionada

Para instalação completa do sistema:

```text
../README.md
```

Para regras de negócio, arquitetura e decisões oficiais:

```text
../docs/SIGC_MASTER_SPECIFICATION.md
```