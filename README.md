# SIGC — Sistema Integrado de Gestão de Cascos

Sistema web para controle, gestão e rastreabilidade de cascos relacionados a peças de veículos pesados.

## Sobre o projeto

O SIGC tem como objetivo controlar o ciclo de vida dos cascos de peças que possuem obrigação de devolução, desde a aquisição da peça junto ao fornecedor, passando pela saída para oficina ou balcão, devolução do casco pelo cliente e posterior devolução ao fornecedor.

O sistema será desenvolvido inicialmente para uma única filial e poderá ser expandido futuramente para suportar múltiplas filiais.

A aplicação será desenvolvida inicialmente e executada localmente em ambiente Windows. Posteriormente, poderá ser implantada em um servidor Windows da empresa para acesso por diferentes computadores da rede interna.

## Tecnologias

* Python
* SQLite
* Framework web Python
* SQLAlchemy
* Git
* GitHub

## Banco de dados

O SQLite será utilizado inicialmente durante o desenvolvimento e a primeira etapa de implantação.

A arquitetura será preparada para permitir uma futura migração para um banco de dados cliente-servidor, caso o crescimento do sistema ou da infraestrutura exija essa evolução.

## Status

Em fase de configuração da estrutura inicial e preparação do ambiente de desenvolvimento.

## Documentação

A especificação oficial do projeto está disponível em:

`docs/SIGC_MASTER_SPECIFICATION.md`

Este documento representa a fonte oficial de verdade do projeto.

## Estrutura do projeto

* `docs/` — Documentação oficial do projeto.
* `src/` — Código-fonte da aplicação.
* `tests/` — Testes automatizados.
* `migrations/` — Controle de evolução do banco de dados.
* `scripts/` — Scripts auxiliares do projeto.

## Autor

Lucas do Nascimento Miura