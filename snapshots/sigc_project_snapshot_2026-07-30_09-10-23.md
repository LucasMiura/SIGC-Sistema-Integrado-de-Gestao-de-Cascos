# Snapshot do projeto SIGC

Gerado em: `2026-07-30T09:10:24.711825`

Diretório do projeto: `C:\Users\estoquista.reg\Documents\SIGC-Sistema-Integrado-de-Gestao-de-Cascos`

## Avisos

- O conteúdo de `.env` não foi incluído.
- Bancos SQLite completos não foram incluídos.
- Foram incluídos apenas metadados e amostras necessárias para análise.
- `.venv`, `.git`, caches e arquivos binários foram ignorados.

## Árvore de arquivos

```text
- alembic.ini
    - SIGC_MASTER_SPECIFICATION.md
    - env.py
        - 003a3ca7193f_create_outbound_tables.py
        - 1f19757f07c6_create_roles_table.py
        - 330805b7930d_create_parts_suppliers_and_supplier_.py
        - 3909300e7597_create_customer_return_tables.py
        - 3e391eb4855b_fix_roles_created_at_nullable.py
        - 5920bd9270a0_create_core_movements_and_audit_logs_.py
        - 6905c4ac94c4_create_supplier_return_tables.py
        - b0195f114054_create_transfers_and_transfer_items_.py
        - b65ceb98865d_remove_unit_price_from_purchase_items.py
        - bb81601b41f6_create_purchases_and_purchase_items_.py
        - c27a0a62fa9e_add_supplier_and_return_deadline_to_.py
        - e0a0ee0f0559_create_users_table.py
- README.md
- requirements.txt
    - __init__.py
    - generate_project_snapshot.py
    - test_customer_return_service.py
    - test_database.py
    - test_outbound_service.py
    - test_purchase_service.py
    - test_purchase_tracking_query.py
    - test_supplier_return_fifo_service.py
    - test_supplier_return_service.py
    - __init__.py
        - __init__.py
            - __init__.py
            - outbound_route.py
            - part_route.py
            - purchase_route.py
            - purchase_tracking_route.py
            - supplier_contact_route.py
            - supplier_route.py
        - __init__.py
        - time.py
        - __init__.py
        - connection.py
        - __init__.py
        - customer_return_dto.py
        - outbound_dto.py
        - purchase_tracking.py
        - purchase_tracking_dto.py
        - supplier_return_dto.py
    - main.py
        - __init__.py
        - audit_log.py
        - core_movement.py
        - customer_return.py
        - customer_return_allocation.py
        - customer_return_item.py
        - outbound.py
        - outbound_item.py
        - outbound_purchase_allocation.py
        - part.py
        - purchase.py
        - purchase_item.py
        - role.py
        - supplier.py
        - supplier_contact.py
        - supplier_return.py
        - supplier_return_item.py
        - transfer.py
        - transfer_item.py
        - user.py
        - __init__.py
        - customer_return_query.py
        - dashboard_query.py
        - purchase_query.py
        - purchase_tracking_query.py
        - supplier_return_query.py
        - __init__.py
        - audit_log_repository.py
        - core_movement_repository.py
        - customer_return_allocation_repository.py
        - customer_return_item_repository.py
        - customer_return_repository.py
        - outbound_item_repository.py
        - outbound_purchase_allocation_repository.py
        - outbound_repository.py
        - part_repository.py
        - purchase_item_repository.py
        - purchase_repository.py
        - role_repository.py
        - supplier_contact_repository.py
        - supplier_repository.py
        - supplier_return_item_repository.py
        - supplier_return_repository.py
        - transfer_item_repository.py
        - transfer_repository.py
        - user_repository.py
        - __init__.py
        - outbound_schema.py
        - part_schema.py
        - purchase_schema.py
        - purchase_tracking_schema.py
        - supplier_contact_schema.py
        - supplier_schema.py
        - __init__.py
        - password.py
        - __init__.py
        - customer_return_service.py
        - outbound_service.py
        - part_service.py
        - purchase_service.py
        - purchase_tracking_service.py
        - role_service.py
        - supplier_contact_service.py
        - supplier_return_service.py
        - supplier_service.py
        - transfer_service.py
        - user_service.py
        - __init__.py
        - test_outbound_route.py
        - test_part_route.py
        - test_purchase_route.py
        - test_purchase_tracking_route.py
        - test_supplier_contact_route.py
        - test_supplier_route.py
        - __init__.py
        - test_outbound_service.py
        - test_part_service.py
        - test_purchase_service.py
        - test_purchase_tracking_service.py
        - test_supplier_contact_service.py
        - test_supplier_service.py
```

## Estado do Git

```text
## main...origin/main
 D create_snapshot.ps1
 D sigc_phase2_purchase_tracking.zip
 D sigc_project_snapshot.txt
 D snapshot_sigc.txt
```

## Últimos commits

```text
2b882af (HEAD -> main, origin/main, origin/HEAD) feat: implementa módulo completo de saídas
45e1185 feat(part): implement part API and tests
a2003f2 feat: implementa gerenciamento de contatos de fornecedores
ccff3ae feat: implementa CRUD completo de fornecedores
b050e59 feat: implementa acompanhamento de compras
2cc251e (tag: v1.1.0) feat: finalize backend core and update master specification v1.1.0
9ab4ca5 feat: implement supplier return workflow
2f53e10 fix: enforce roles created_at as not null
57ca78e refactor: centralize model timestamps
ca01d72 fix: remove unit price from purchase items
066769a feat: add cadastro services and repository updates
cda8555 feat: complete repository layer
78d5761 feat: implement core database schema and migrations
dd2c3a2 feat: add outbound tracking and purchase allocations
df11c27 feat: add purchase and purchase item models
```

## Alembic current

```text
c27a0a62fa9e (head)

STDERR:
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
```

## Alembic heads

```text
c27a0a62fa9e (head)
```

## Alembic history

```text
Rev: c27a0a62fa9e (head)
Parent: 6905c4ac94c4
Path: C:\Users\estoquista.reg\Documents\SIGC-Sistema-Integrado-de-Gestao-de-Cascos\migrations\versions\c27a0a62fa9e_add_supplier_and_return_deadline_to_.py

    add supplier and return deadline to parts
    
    Revision ID: c27a0a62fa9e
    Revises: 6905c4ac94c4
    Create Date: 2026-07-28 14:43:09.408031

Rev: 6905c4ac94c4
Parent: 3e391eb4855b
Path: C:\Users\estoquista.reg\Documents\SIGC-Sistema-Integrado-de-Gestao-de-Cascos\migrations\versions\6905c4ac94c4_create_supplier_return_tables.py

    create supplier return tables
    
    Revision ID: 6905c4ac94c4
    Revises: 3e391eb4855b
    Create Date: 2026-07-27 14:41:05.347807

Rev: 3e391eb4855b
Parent: b65ceb98865d
Path: C:\Users\estoquista.reg\Documents\SIGC-Sistema-Integrado-de-Gestao-de-Cascos\migrations\versions\3e391eb4855b_fix_roles_created_at_nullable.py

    fix roles created_at nullable
    
    Revision ID: 3e391eb4855b
    Revises: b65ceb98865d
    Create Date: 2026-07-27 14:26:17.809017

Rev: b65ceb98865d
Parent: 5920bd9270a0
Path: C:\Users\estoquista.reg\Documents\SIGC-Sistema-Integrado-de-Gestao-de-Cascos\migrations\versions\b65ceb98865d_remove_unit_price_from_purchase_items.py

    remove unit price from purchase items
    
    Revision ID: b65ceb98865d
    Revises: 5920bd9270a0
    Create Date: 2026-07-24 17:00:31.730691

Rev: 5920bd9270a0
Parent: b0195f114054
Path: C:\Users\estoquista.reg\Documents\SIGC-Sistema-Integrado-de-Gestao-de-Cascos\migrations\versions\5920bd9270a0_create_core_movements_and_audit_logs_.py

    create core movements and audit logs tables
    
    Revision ID: 5920bd9270a0
    Revises: b0195f114054
    Create Date: 2026-07-24 14:09:13.140851

Rev: b0195f114054
Parent: 3909300e7597
Path: C:\Users\estoquista.reg\Documents\SIGC-Sistema-Integrado-de-Gestao-de-Cascos\migrations\versions\b0195f114054_create_transfers_and_transfer_items_.py

    create transfers and transfer items tables
    
    Revision ID: b0195f114054
    Revises: 3909300e7597
    Create Date: 2026-07-24 13:28:40.877914

Rev: 3909300e7597
Parent: 003a3ca7193f
Path: C:\Users\estoquista.reg\Documents\SIGC-Sistema-Integrado-de-Gestao-de-Cascos\migrations\versions\3909300e7597_create_customer_return_tables.py

    create customer return tables
    
    Revision ID: 3909300e7597
    Revises: 003a3ca7193f
    Create Date: 2026-07-24 13:18:20.776774

Rev: 003a3ca7193f
Parent: bb81601b41f6
Path: C:\Users\estoquista.reg\Documents\SIGC-Sistema-Integrado-de-Gestao-de-Cascos\migrations\versions\003a3ca7193f_create_outbound_tables.py

    create outbound tables
    
    Revision ID: 003a3ca7193f
    Revises: bb81601b41f6
    Create Date: 2026-07-24 11:30:30.232706

Rev: bb81601b41f6
Parent: 330805b7930d
Path: C:\Users\estoquista.reg\Documents\SIGC-Sistema-Integrado-de-Gestao-de-Cascos\migrations\versions\bb81601b41f6_create_purchases_and_purchase_items_.py

    create purchases and purchase items tables
    
    Revision ID: bb81601b41f6
    Revises: 330805b7930d
    Create Date: 2026-07-24 11:21:13.953999

Rev: 330805b7930d
Parent: e0a0ee0f0559
Path: C:\Users\estoquista.reg\Documents\SIGC-Sistema-Integrado-de-Gestao-de-Cascos\migrations\versions\330805b7930d_create_parts_suppliers_and_supplier_.py

    create parts suppliers and supplier contacts tables
    
    Revision ID: 330805b7930d
    Revises: e0a0ee0f0559
    Create Date: 2026-07-24 11:11:55.270859

Rev: e0a0ee0f0559
Parent: 1f19757f07c6
Path: C:\Users\estoquista.reg\Documents\SIGC-Sistema-Integrado-de-Gestao-de-Cascos\migrations\versions\e0a0ee0f0559_create_users_table.py

    create users table
    
    Revision ID: e0a0ee0f0559
    Revises: 1f19757f07c6
    Create Date: 2026-07-24 10:48:39.896922

Rev: 1f19757f07c6
Parent: <base>
Path: C:\Users\estoquista.reg\Documents\SIGC-Sistema-Integrado-de-Gestao-de-Cascos\migrations\versions\1f19757f07c6_create_roles_table.py

    create roles table
    
    Revision ID: 1f19757f07c6
    Revises:
    Create Date: 2026-07-24 10:09:54.706300
```

# Banco de dados

Nenhum arquivo SQLite foi encontrado automaticamente.

# Conteúdo dos arquivos

## `alembic.ini`

```ini
# A generic, single database configuration.

[alembic]
# path to migration scripts.
# this is typically a path given in POSIX (e.g. forward slashes)
# format, relative to the token %(here)s which refers to the location of this
# ini file
script_location = %(here)s/migrations

# template used to generate migration file names; The default value is %%(rev)s_%%(slug)s
# Uncomment the line below if you want the files to be prepended with date and time
# see https://alembic.sqlalchemy.org/en/latest/tutorial.html#editing-the-ini-file
# for all available tokens
# file_template = %%(year)d_%%(month).2d_%%(day).2d_%%(hour).2d%%(minute).2d-%%(rev)s_%%(slug)s
# Or organize into date-based subdirectories (requires recursive_version_locations = true)
# file_template = %%(year)d/%%(month).2d/%%(day).2d_%%(hour).2d%%(minute).2d_%%(second).2d_%%(rev)s_%%(slug)s

# sys.path path, will be prepended to sys.path if present.
# defaults to the current working directory.  for multiple paths, the path separator
# is defined by "path_separator" below.
prepend_sys_path = .


# timezone to use when rendering the date within the migration file
# as well as the filename.
# If specified, requires the tzdata library which can be installed by adding
# `alembic[tz]` to the pip requirements.
# string value is passed to ZoneInfo()
# leave blank for localtime
# timezone =

# max length of characters to apply to the "slug" field
# truncate_slug_length = 40

# set to 'true' to run the environment during
# the 'revision' command, regardless of autogenerate
# revision_environment = false

# set to 'true' to allow .pyc and .pyo files without
# a source .py file to be detected as revisions in the
# versions/ directory
# sourceless = false

# version location specification; This defaults
# to <script_location>/versions.  When using multiple version
# directories, initial revisions must be specified with --version-path.
# The path separator used here should be the separator specified by "path_separator"
# below.
# version_locations = %(here)s/bar:%(here)s/bat:%(here)s/alembic/versions

# path_separator; This indicates what character is used to split lists of file
# paths, including version_locations and prepend_sys_path within configparser
# files such as alembic.ini.
# The default rendered in new alembic.ini files is "os", which uses os.pathsep
# to provide os-dependent path splitting.
#
# Note that in order to support legacy alembic.ini files, this default does NOT
# take place if path_separator is not present in alembic.ini.  If this
# option is omitted entirely, fallback logic is as follows:
#
# 1. Parsing of the version_locations option falls back to using the legacy
#    "version_path_separator" key, which if absent then falls back to the legacy
#    behavior of splitting on spaces and/or commas.
# 2. Parsing of the prepend_sys_path option falls back to the legacy
#    behavior of splitting on spaces, commas, or colons.
#
# Valid values for path_separator are:
#
# path_separator = :
# path_separator = ;
# path_separator = space
# path_separator = newline
#
# Use os.pathsep. Default configuration used for new projects.
path_separator = os

# set to 'true' to search source files recursively
# in each "version_locations" directory
# new in Alembic version 1.10
# recursive_version_locations = false

# the output encoding used when revision files
# are written from script.py.mako
# output_encoding = utf-8

# database URL.  This is consumed by the user-maintained env.py script only.
# other means of configuring database URLs may be customized within the env.py
# file.
sqlalchemy.url = driver://user:pass@localhost/dbname


[post_write_hooks]
# post_write_hooks defines scripts or Python functions that are run
# on newly generated revision scripts.  See the documentation for further
# detail and examples

# format using "black" - use the console_scripts runner, against the "black" entrypoint
# hooks = black
# black.type = console_scripts
# black.entrypoint = black
# black.options = -l 79 REVISION_SCRIPT_FILENAME

# lint with attempts to fix using "ruff" - use the module runner, against the "ruff" module
# hooks = ruff
# ruff.type = module
# ruff.module = ruff
# ruff.options = check --fix REVISION_SCRIPT_FILENAME

# Alternatively, use the exec runner to execute a binary found on your PATH
# hooks = ruff
# ruff.type = exec
# ruff.executable = ruff
# ruff.options = check --fix REVISION_SCRIPT_FILENAME

# Logging configuration.  This is also consumed by the user-maintained
# env.py script only.
[loggers]
keys = root,sqlalchemy,alembic

[handlers]
keys = console

[formatters]
keys = generic

[logger_root]
level = WARNING
handlers = console
qualname =

[logger_sqlalchemy]
level = WARNING
handlers =
qualname = sqlalchemy.engine

[logger_alembic]
level = INFO
handlers =
qualname = alembic

[handler_console]
class = StreamHandler
args = (sys.stderr,)
level = NOTSET
formatter = generic

[formatter_generic]
format = %(levelname)-5.5s [%(name)s] %(message)s
datefmt = %H:%M:%S
```

## `docs\SIGC_MASTER_SPECIFICATION.md`

```markdown
# SIGC — Sistema Integrado de Gestão de Cascos

**Sistema Integrado de Gestão de Cascos**

---

## Informações do Projeto

| Informação              | Valor                                 |
| ----------------------- | ------------------------------------- |
| Nome do sistema         | SIGC                                  |
| Nome completo           | Sistema Integrado de Gestão de Cascos |
| Autor                   | Lucas do Nascimento Miura             |
| Status                  | Em fase de implementação              |
| Versão da especificação | 1.1.0                                 |
| Data de criação         | 23/07/2026                            |
| Plataforma inicial      | Aplicação Web Interna                 |
| Linguagem principal     | Python                                |
| Banco de dados          | SQLite                                |
| Escopo inicial          | Uma única filial                      |

---

# 1. Identidade do Projeto

## 1.1 Nome

SIGC — Sistema Integrado de Gestão de Cascos.

## 1.2 Autor

Lucas do Nascimento Miura.

## 1.3 Descrição resumida

O SIGC é uma aplicação web interna desenvolvida para controlar o ciclo de vida de cascos relacionados a peças de veículos pesados, especialmente caminhões, desde a aquisição da peça junto ao fornecedor até a devolução do casco ao fornecedor.

O sistema será utilizado inicialmente por uma única filial de uma concessionária Volkswagen, funcionará de forma independente do sistema principal da empresa e será acessado pelos usuários por meio de navegadores conectados à rede interna.

A aplicação será executada inicialmente em um servidor Windows da empresa, utilizando Python, FastAPI, SQLAlchemy e SQLite. Sua arquitetura deverá permitir futuras evoluções, incluindo a migração para um banco de dados cliente-servidor e a disponibilização de formas controladas de acesso remoto.

---

# 2. Visão Geral

O SIGC — Sistema Integrado de Gestão de Cascos é uma aplicação web interna desenvolvida para auxiliar no controle, rastreamento e gerenciamento do ciclo de vida de cascos relacionados a peças de veículos pesados, especialmente caminhões.

A aplicação será executada de forma centralizada em um servidor Windows da empresa e será acessada pelos usuários por meio de navegadores conectados à rede interna. Essa estrutura permitirá centralizar as regras de negócio, o acesso ao banco de dados, a autenticação, a auditoria e a manutenção do sistema, sem exigir a instalação completa da aplicação em cada computador.

O sistema será utilizado inicialmente em uma única filial de uma concessionária Volkswagen e funcionará de forma independente do sistema principal da empresa. Seu objetivo é complementar os processos existentes, concentrando exclusivamente as informações necessárias para o controle dos cascos que precisam ser devolvidos aos fornecedores.

O ciclo controlado pelo SIGC inicia-se na aquisição de peças que possuem obrigação de devolução de casco. Essas peças são registradas juntamente com as informações necessárias para o controle, incluindo sua descrição, código original, fornecedor, quantidade adquirida, data da compra e prazo para devolução.

Após a aquisição, as peças podem ser utilizadas em operações de venda para clientes da oficina ou do balcão. O sistema deverá registrar a saída da peça, associando-a à respectiva Ordem de Serviço ou Nota Fiscal e identificando o cliente de forma simplificada.

Quando o cliente devolver o casco, o usuário autorizado deverá registrar a devolução no sistema. O SIGC deverá controlar devoluções totais e parciais, mantendo o vínculo com a saída original e impedindo que sejam registradas quantidades superiores à quantidade pendente de devolução.

Após o recebimento do casco, o sistema deverá controlar sua disponibilidade para devolução ao fornecedor. As devoluções ao fornecedor poderão ser realizadas de forma total ou parcial e poderão conter diferentes peças provenientes da mesma Nota Fiscal de compra.

O sistema deverá utilizar a lógica FIFO (First In, First Out) para associar automaticamente as saídas às compras mais antigas disponíveis, priorizando as peças adquiridas primeiro. Essa regra tem como objetivo reduzir o risco de vencimento dos prazos de devolução dos cascos.

O SIGC também deverá fornecer dashboards, consultas e relatórios que permitam aos usuários acompanhar os cascos pendentes, devolvidos, parcialmente devolvidos, urgentes e atrasados.

A aplicação será projetada com foco em segurança, rastreabilidade, auditoria, preservação do histórico e facilidade de utilização. Todas as operações relevantes deverão ser associadas ao usuário responsável e alterações ou cancelamentos não deverão eliminar fisicamente informações históricas.

O projeto será desenvolvido inicialmente para uma única filial, porém sua arquitetura deverá permitir futuras melhorias e adaptações, incluindo a possibilidade de expansão para múltiplas filiais e a criação de permissões personalizadas pelo Administrador Master.

---

# 3. Problema

A operação de uma concessionária de veículos pesados envolve a aquisição de peças que possuem a obrigação de devolução de cascos aos respectivos fornecedores. Esses cascos podem permanecer temporariamente em estoque, ser utilizados em serviços realizados pela oficina ou ser comercializados através do balcão de peças.

O controle desse processo exige o acompanhamento de diversas etapas relacionadas entre si. É necessário identificar a compra de origem da peça, controlar o prazo de devolução do casco ao fornecedor, registrar a saída da peça para o cliente, acompanhar a devolução posterior do casco e, finalmente, controlar a devolução do casco ao fornecedor.

O sistema principal utilizado pela empresa possui recursos para controle de estoque, vendas de peças e gerenciamento de Ordens de Serviço, porém não possui funcionalidades específicas para controlar o ciclo de vida dos cascos. Por esse motivo, o SIGC será desenvolvido como um sistema independente e especializado nesse processo.

A ausência de um controle específico pode dificultar a identificação dos cascos que ainda estão pendentes de devolução, dos cascos que permanecem com clientes, dos cascos que já foram devolvidos e dos cascos disponíveis para devolução aos fornecedores.

Outro fator relevante é que os prazos de devolução são relacionados à data de emissão da Nota Fiscal de compra. Dessa forma, o controle inadequado da origem das peças pode dificultar a priorização correta das saídas e aumentar o risco de perda de prazos.

Uma mesma Nota Fiscal de compra pode conter diferentes peças sujeitas à devolução de casco e múltiplas unidades de um mesmo item. Além disso, uma determinada peça pode ser utilizada em diferentes momentos e suas unidades podem ser vinculadas a diferentes vendas ou Ordens de Serviço.

Também podem ocorrer devoluções parciais por parte dos clientes e devoluções parciais ao fornecedor. Dessa forma, o controle exige que as quantidades sejam acompanhadas de forma precisa em cada etapa do processo, evitando registros superiores às quantidades efetivamente disponíveis ou pendentes.

A utilização de controles manuais ou dispersos pode aumentar o risco de inconsistências, perda de informações, dificuldade de auditoria e atraso na identificação de situações urgentes ou vencidas.

O SIGC surge, portanto, com o objetivo de centralizar e organizar as informações relacionadas aos cascos, permitindo rastrear suas movimentações desde a compra da peça até a devolução final ao fornecedor.

O sistema deverá proporcionar maior visibilidade sobre os cascos pendentes, facilitar o acompanhamento das devoluções dos clientes, auxiliar no controle dos prazos de devolução aos fornecedores e preservar o histórico das operações realizadas.

---

# 4. Objetivos

## 4.1 Objetivo Geral

Desenvolver um sistema desktop especializado no controle e rastreamento do ciclo de vida de cascos relacionados a peças de veículos pesados, permitindo acompanhar as etapas desde a aquisição da peça junto ao fornecedor até a devolução final do casco, com controle de prazos, quantidades, origem, movimentações, devoluções e histórico das operações.

O SIGC deverá centralizar as informações necessárias para o controle de cascos em um sistema independente do sistema principal da empresa, proporcionando maior organização, rastreabilidade, segurança das informações e visibilidade sobre as obrigações de devolução.

---

## 4.2 Objetivos Específicos

O SIGC deverá:

1. Permitir o cadastro das peças que possuem obrigação de devolução de casco, contendo as informações necessárias para o controle, como descrição, código original, fornecedor e prazo para devolução.

2. Permitir o cadastro de fornecedores e de múltiplos contatos associados a cada fornecedor, facilitando a comunicação relacionada às devoluções.

3. Registrar as compras de peças que possuem obrigação de devolução de casco, incluindo a Nota Fiscal de compra, a data de emissão, o fornecedor, os itens e as respectivas quantidades.

4. Controlar individualmente os itens relevantes para o processo de devolução de cascos, sem substituir ou duplicar as funcionalidades de estoque, vendas ou gerenciamento de Ordens de Serviço existentes no sistema principal da empresa.

5. Calcular os prazos de devolução dos cascos com base na data de emissão da Nota Fiscal de compra e no prazo aplicável à peça ou à operação de transferência.

6. Utilizar a lógica FIFO (First In, First Out) para priorizar automaticamente as peças adquiridas há mais tempo durante o registro de saídas.

7. Permitir o registro de saídas destinadas à oficina ou ao balcão, associando a operação ao número da Ordem de Serviço ou da Nota Fiscal correspondente.

8. Permitir o controle simplificado das informações do cliente relacionadas à saída, mantendo o sistema focado no controle dos cascos e não no cadastro completo de clientes.

9. Permitir o registro de devoluções de cascos realizadas pelos clientes, vinculando-as à saída original e controlando devoluções totais e parciais.

10. Impedir o registro de devoluções de clientes em quantidade superior à quantidade pendente relacionada à saída original.

11. Permitir o registro de devoluções de cascos aos fornecedores, incluindo devoluções totais ou parciais.

12. Permitir que uma única operação de devolução ao fornecedor contenha diferentes peças provenientes da mesma Nota Fiscal de compra.

13. Impedir o registro de devoluções ao fornecedor em quantidade superior à quantidade disponível para devolução.

14. Permitir a consulta do status de devolução a partir da Nota Fiscal de compra, apresentando as informações relacionadas à origem, saídas, devoluções de clientes e devoluções ao fornecedor.

15. Permitir o controle de transferências excepcionais entre filiais, possibilitando o registro de prazos específicos para essas operações sem alterar o prazo padrão cadastrado para a peça.

16. Fornecer dashboards e indicadores que permitam acompanhar os cascos pendentes, parcialmente devolvidos, próximos do vencimento, urgentes e atrasados.

17. Utilizar classificações de prazo que permitam identificar as seguintes situações:

    * **Normal:** mais de 30 dias restantes;
    * **Atenção:** até 30 dias restantes;
    * **Urgente:** até 7 dias restantes;
    * **Atrasado:** prazo vencido.

18. Registrar as operações realizadas pelos usuários, permitindo identificar o responsável, a data e a hora de cada operação relevante.

19. Preservar o histórico das operações, evitando a exclusão física de registros que já tenham participado de processos do sistema.

20. Permitir correções e cancelamentos controlados, mantendo o histórico da alteração e ajustando corretamente as quantidades relacionadas às operações.

21. Utilizar autenticação segura, incluindo armazenamento protegido das senhas e controle de usuários ativos e inativos.

22. Permitir que o Administrador Master gerencie usuários e, futuramente, crie permissões personalizadas conforme a necessidade da organização.

23. Disponibilizar mecanismos de backup e recuperação de dados para reduzir o risco de perda das informações do sistema.

24. Possibilitar futuras melhorias e expansões do sistema sem comprometer os dados históricos já registrados.

25. Manter uma interface moderna, intuitiva e consistente, utilizando um padrão visual unificado em todas as telas e priorizando clareza, facilidade de uso e baixa poluição visual.

---

# 5. Escopo do Sistema

O SIGC será desenvolvido como um sistema especializado no controle e rastreamento do ciclo de vida de cascos relacionados a peças de veículos pesados.

O escopo inicial será limitado a uma única filial de uma concessionária Volkswagen, com possibilidade de expansão futura para múltiplas filiais e novos recursos, desde que as alterações sejam planejadas e compatíveis com a preservação dos dados históricos.

---

## 5.1 Cadastros

O sistema deverá permitir o gerenciamento dos cadastros necessários para o controle dos cascos.

### 5.1.1 Peças

O cadastro de peças deverá conter apenas as informações relevantes para o controle de cascos:

* Descrição da peça;
* Código original;
* Fornecedor;
* Prazo para devolução do casco;
* Status do cadastro.

Uma peça poderá ser desativada sem que seus registros históricos sejam excluídos.

O cadastro deverá permitir que diferentes combinações de peça, código original e fornecedor possuam prazos diferentes de devolução.

---

### 5.1.2 Fornecedores

O sistema deverá permitir o cadastro de fornecedores relacionados às peças com obrigação de devolução de casco.

O cadastro poderá conter:

* Nome ou razão social;
* Dados de identificação necessários;
* Status;
* Um ou mais contatos;
* Nome dos contatos;
* Endereços de e-mail dos contatos.

A existência de múltiplos contatos permitirá que as informações de devolução sejam direcionadas ao contato adequado do fornecedor.

---

### 5.1.3 Usuários

O sistema deverá permitir o gerenciamento dos usuários responsáveis pelas operações.

Inicialmente, serão considerados os seguintes perfis:

* Administrador Master;
* Comprador;
* Vendedor.

O Administrador Master será responsável pelo gerenciamento dos usuários e das permissões disponíveis.

A arquitetura deverá permitir futuramente a criação de permissões personalizadas.

Usuários que já tenham realizado operações não deverão ser excluídos fisicamente do sistema.

---

## 5.2 Controle de Compras

O sistema deverá permitir o registro de Notas Fiscais de compra que contenham peças sujeitas à devolução de casco.

Uma mesma Nota Fiscal poderá conter:

* Diferentes peças com obrigação de devolução;
* Várias unidades da mesma peça;
* Outros itens que não serão cadastrados no SIGC.

O comprador deverá cadastrar somente os itens relevantes para o controle de cascos.

Cada item da compra deverá manter seu vínculo com:

* Nota Fiscal de origem;
* Data de emissão;
* Peça;
* Código original;
* Fornecedor;
* Quantidade;
* Prazo aplicável;
* Data limite para devolução.

O prazo aplicado à compra deverá ser preservado historicamente, mesmo que o prazo padrão da peça seja alterado futuramente.

---

## 5.3 Controle de Saídas

O sistema deverá permitir o registro da saída de peças destinadas a:

* Oficina;
* Balcão.

A escolha do destino deverá determinar o campo de referência correspondente:

* Oficina: número da Ordem de Serviço;
* Balcão: número da Nota Fiscal.

O registro deverá conter informações simplificadas do cliente, suficientes para facilitar sua identificação no contexto do controle de cascos.

O sistema não deverá substituir o sistema principal da empresa para consulta completa de dados de clientes, vendas ou Ordens de Serviço.

---

## 5.4 Controle FIFO

As saídas deverão utilizar automaticamente a lógica FIFO (First In, First Out).

O sistema deverá priorizar as peças provenientes das compras mais antigas ainda disponíveis.

Quando a quantidade de uma saída ultrapassar a quantidade disponível na compra mais antiga, o sistema deverá consumir automaticamente as compras seguintes.

Exemplo:

```text
Compra A — 5 unidades
Compra B — 10 unidades

Saída — 8 unidades

Resultado:
Compra A → 5 unidades
Compra B → 3 unidades
```

Cada quantidade consumida deverá permanecer vinculada à sua respectiva origem para que os prazos de devolução sejam controlados corretamente.

---

## 5.5 Controle de Devoluções dos Clientes

O sistema deverá permitir o registro da devolução de cascos pelos clientes.

A devolução deverá ser vinculada à saída original.

Deverá ser possível registrar:

* Devolução total;
* Devolução parcial;
* Data da devolução;
* Quantidade devolvida;
* Observações;
* Usuário responsável.

O sistema deverá impedir que a quantidade total devolvida seja superior à quantidade originalmente registrada como saída.

Quando a quantidade devolvida for inferior à quantidade da saída, a operação deverá permanecer com status de devolução parcial.

Não será exigida uma Nota Fiscal de devolução emitida pelo cliente para o registro da devolução do casco.

---

## 5.6 Controle de Remessas de Cascos aos Fornecedores

O sistema deverá permitir o registro da devolução dos cascos aos fornecedores.

As devoluções poderão ser:

* Totais;
* Parciais;
* Realizadas em diferentes operações para uma mesma Nota Fiscal de compra.

Uma única operação de devolução ao fornecedor poderá conter vários itens diferentes provenientes da mesma Nota Fiscal de compra.

O registro deverá conter:

* Data da devolução;
* Número da Nota Fiscal de Simples Remessa;
* Itens enviados;
* Quantidades;
* Nota Fiscal de compra de origem;
* Observações;
* Usuário responsável.

A Nota Fiscal de Simples Remessa será emitida pela própria empresa para formalizar o envio dos cascos ao fornecedor e deverá conter as peças, as respectivas quantidades e a Nota Fiscal de compra de origem.

O sistema deverá impedir que a quantidade devolvida seja superior à quantidade disponível para devolução.

Cada item enviado ao fornecedor deverá manter vínculo com o item de compra de
origem por meio do campo `purchase_item_id`.

A utilização do `purchase_item_id` permitirá identificar:

* A peça;
* A Nota Fiscal de compra;
* O fornecedor;
* A quantidade adquirida;
* A origem utilizada no consumo FIFO.

A quantidade disponível para remessa ao fornecedor deverá ser calculada da
seguinte forma:

```text
Quantidade devolvida pelos clientes atribuída ao item de compra
− quantidade já remetida ao fornecedor para o item de compra
= quantidade disponível para nova remessa
```

O sistema deverá permitir remessas parciais, mantendo o saldo restante
disponível para remessas posteriores.

O mesmo item de compra não deverá aparecer mais de uma vez na mesma operação
de remessa ao fornecedor.

---

## 5.7 Controle de Transferências

O sistema deverá permitir o registro de transferências excepcionais entre filiais.

A filial de origem continuará responsável pela devolução do casco ao fornecedor.

A filial que receber a peça ficará responsável por devolver o casco à filial de origem.

A operação de transferência deverá permitir o registro de:

* Nota Fiscal de transferência;
* Filial de origem;
* Data da operação;
* Peça;
* Código original;
* Quantidade;
* Prazo específico para devolução.

O prazo específico da transferência deverá ser informado manualmente quando necessário e não deverá alterar o prazo padrão cadastrado para a peça.

---

## 5.8 Controle de Prazos

O sistema deverá calcular os prazos de devolução dos cascos com base na data de emissão da Nota Fiscal de compra ou na data aplicável à operação de transferência.

Os prazos deverão ser classificados da seguinte forma:

| Situação | Regra                     |
| -------- | ------------------------- |
| Normal   | Mais de 30 dias restantes |
| Atenção  | Até 30 dias restantes     |
| Urgente  | Até 7 dias restantes      |
| Atrasado | Prazo vencido             |

A classificação deverá ser utilizada nos dashboards, consultas e relatórios.

---

## 5.9 Consultas

O sistema deverá permitir a consulta do status de devolução a partir da Nota Fiscal de compra.

A consulta deverá permitir visualizar, quando aplicável:

* Dados da compra;
* Itens cadastrados;
* Quantidades adquiridas;
* Saídas relacionadas;
* Quantidades ainda disponíveis;
* Devoluções realizadas pelos clientes;
* Quantidades pendentes de devolução pelos clientes;
* Quantidades disponíveis para devolução ao fornecedor;
* Devoluções realizadas ao fornecedor;
* Quantidades ainda pendentes;
* Prazos;
* Status;
* Histórico das operações.

---

## 5.10 Dashboards

O sistema deverá disponibilizar dashboards adequados aos perfis de usuário.

Os dashboards deverão apresentar informações relevantes para o acompanhamento dos cascos, evitando excesso de informações desnecessárias.

Entre os indicadores previstos estão:

* Cascos pendentes;
* Devoluções parciais;
* Prazos próximos do vencimento;
* Casos urgentes;
* Casos atrasados;
* Devoluções recentes;
* Informações relacionadas às obrigações com fornecedores.

---

## 5.11 Auditoria e Histórico

As operações relevantes deverão manter informações de auditoria.

O sistema deverá registrar, quando aplicável:

* Usuário responsável;
* Data;
* Hora;
* Operação realizada;
* Registro afetado;
* Alterações realizadas.

Correções e cancelamentos deverão preservar o histórico da operação original.

Registros históricos não deverão ser excluídos fisicamente quando já tiverem participado de operações do sistema.

---

## 5.12 Backup

O sistema deverá possuir mecanismos de backup para reduzir o risco de perda de informações.

Os backups do ambiente de produção deverão ser realizados de forma independente do banco de dados principal e armazenados em local separado e protegido, conforme a infraestrutura disponível e a política de backup definida para o ambiente da empresa.

A estratégia de backup deverá contemplar, quando aplicável:

* Execução automática ou programada;
* Histórico de backups;
* Identificação de data e hora;
* Identificação de falhas;
* Verificação de integridade;
* Recuperação dos dados quando necessário.

A frequência, o período de retenção, o local específico de armazenamento e o método de execução da estratégia de backup serão definidos conforme a infraestrutura disponível e a política oficial da empresa.

A implementação da estratégia de backup deverá preservar os dados operacionais e históricos do SIGC.

---

## 5.13 Evolução Futura

O sistema deverá ser desenvolvido de forma que permita futuras melhorias e adaptações.

Possíveis evoluções incluem:

* Suporte a múltiplas filiais;
* Permissões personalizadas;
* Novos tipos de relatórios;
* Melhorias nos dashboards;
* Novos mecanismos de backup;
* Aprimoramentos na interface;
* Novas formas de consulta;
* Integrações futuras, caso sejam avaliadas e aprovadas.

As evoluções futuras deverão preservar a integridade e o histórico dos dados existentes.

---

# 6. Fora do Escopo

O SIGC será desenvolvido com foco específico no controle e rastreamento de cascos relacionados a peças de veículos pesados. Portanto, as funcionalidades descritas nesta seção não fazem parte do escopo inicial do sistema.

A definição de itens fora do escopo tem como objetivo evitar a duplicação de funcionalidades já existentes no sistema principal da empresa e manter o projeto concentrado em seu objetivo principal.

---

## 6.1 Controle Geral de Estoque

O SIGC não substituirá o sistema principal da empresa para controle geral de estoque.

O sistema não deverá controlar:

* Estoque geral de peças;
* Movimentações de peças sem obrigação de devolução de casco;
* Inventário geral;
* Localização física de todas as peças;
* Entradas e saídas gerais de estoque.

O controle realizado pelo SIGC será restrito às informações necessárias para o acompanhamento dos cascos.

---

## 6.2 Sistema Completo de Vendas

O SIGC não será um sistema de vendas.

O sistema não deverá substituir o sistema principal para:

* Emissão de vendas;
* Emissão de Notas Fiscais de venda;
* Controle financeiro de vendas;
* Formação de preços;
* Controle de pagamentos;
* Gestão comercial completa.

O SIGC registrará apenas as informações necessárias para vincular a saída de uma peça ao controle do casco correspondente.

---

## 6.3 Sistema de Ordens de Serviço

O SIGC não substituirá o sistema principal de gerenciamento de Ordens de Serviço.

O sistema deverá utilizar o número da OS como referência da saída quando a peça for destinada à oficina, mas não deverá controlar:

* Abertura de Ordens de Serviço;
* Serviços realizados;
* Mecânicos responsáveis;
* Mão de obra;
* Orçamentos;
* Status completo da OS;
* Histórico completo do veículo.

Essas informações continuarão sendo controladas pelo sistema principal da empresa.

---

## 6.4 Cadastro Completo de Clientes

O SIGC não terá como objetivo substituir o cadastro de clientes existente no sistema principal.

O sistema deverá armazenar apenas as informações simplificadas necessárias para facilitar a identificação da operação e o acompanhamento da devolução do casco.

O SIGC não deverá manter um cadastro completo e independente de clientes com a mesma finalidade do sistema principal.

---

## 6.5 Controle Financeiro e Contábil

O SIGC não realizará:

* Contas a pagar;
* Contas a receber;
* Fluxo de caixa;
* Controle contábil;
* Apuração fiscal;
* Controle de custos;
* Conciliação financeira.

As informações fiscais relacionadas às Notas Fiscais serão registradas apenas quando necessárias para a rastreabilidade das operações de cascos.

---

## 6.6 Integração com o Sistema Principal

O SIGC não terá integração com o sistema principal da empresa em sua versão inicial.

As informações necessárias para o controle dos cascos serão lançadas diretamente no SIGC pelos usuários autorizados.

A possibilidade de integração futura poderá ser avaliada posteriormente, mas não faz parte do escopo inicial.

---

## 6.7 Controle de Compras Geral

O SIGC não substituirá um sistema completo de compras.

O sistema deverá registrar somente as informações relacionadas às compras de peças que possuam obrigação de devolução de casco.

Não serão controlados:

* Negociação com fornecedores;
* Cotação;
* Aprovação de pedidos de compra;
* Condições comerciais;
* Pagamentos;
* Processos gerais de compras.

---

## 6.8 Emissão de Documentos Fiscais

O SIGC não será responsável pela emissão de documentos fiscais.

No caso das remessas de cascos aos fornecedores, o sistema deverá registrar os dados da Nota Fiscal de Simples Remessa emitida pela empresa, incluindo sua relação com as peças e a Nota Fiscal de compra de origem.

A emissão fiscal continuará sendo realizada pelos processos e sistemas apropriados da empresa.

---

## 6.9 Gestão Geral de Filiais

A primeira versão do SIGC será desenvolvida para uma única filial.

O suporte completo a múltiplas filiais não fará parte do escopo inicial, embora a arquitetura do sistema deverá ser planejada para permitir essa expansão futuramente.

---

## 6.10 Aplicação Mobile

A primeira versão do SIGC será desenvolvida como uma aplicação web interna responsiva para utilização prioritária em computadores por meio de navegadores conectados à rede interna da empresa.

O desenvolvimento de uma aplicação mobile nativa para Android ou iOS não faz parte do escopo inicial.

Embora determinadas telas possam futuramente ser adaptadas para acesso por navegadores em dispositivos móveis, essa possibilidade dependerá de avaliação de segurança, usabilidade e necessidade operacional.

---

## 6.11 Automação de Processos Externos

O SIGC não deverá realizar automaticamente ações externas como:

* Envio automático de e-mails aos fornecedores;
* Emissão automática de documentos fiscais;
* Comunicação automática com clientes;
* Atualização automática do sistema principal;
* Integração automática com sistemas de terceiros.

Essas funcionalidades poderão ser avaliadas em versões futuras, caso sejam necessárias e tecnicamente viáveis.

---

## 6.12 Limite de Responsabilidade do Sistema

O SIGC deverá fornecer informações para auxiliar o controle e a tomada de decisão dos usuários, mas não substituirá a responsabilidade operacional dos envolvidos.

O sistema poderá alertar sobre:

* Prazos próximos;
* Prazos urgentes;
* Prazos vencidos;
* Quantidades pendentes;
* Divergências nos lançamentos.

Entretanto, as ações operacionais necessárias, como entrar em contato com o cliente, solicitar o casco ou realizar a remessa ao fornecedor, continuarão dependendo dos usuários responsáveis.

---

# 7. Usuários e Perfis

O SIGC deverá possuir um sistema de autenticação individual para identificar os usuários responsáveis pelas operações realizadas.

Cada usuário deverá possuir sua própria conta de acesso. As operações realizadas deverão ser associadas ao usuário autenticado, permitindo rastreabilidade e auditoria.

A existência de diferentes usuários não significa necessariamente a existência de diferentes perfis. Usuários que desempenham funções semelhantes poderão utilizar o mesmo perfil de acesso, mantendo contas individuais e históricos independentes.

---

## 7.1 Administrador Master

O sistema deverá possuir inicialmente um único Administrador Master.

O Administrador Master terá acesso completo às funcionalidades administrativas e operacionais do sistema.

Suas responsabilidades incluirão:

* Cadastrar usuários;
* Alterar dados dos usuários;
* Desativar usuários;
* Reativar usuários quando necessário;
* Redefinir senhas;
* Gerenciar os perfis e permissões disponíveis;
* Acessar todas as funcionalidades do sistema;
* Consultar históricos e registros de auditoria;
* Corrigir ou cancelar operações conforme as regras do sistema;
* Administrar configurações gerais do sistema.

Inicialmente, haverá apenas um Administrador Master, responsável pela administração geral do SIGC.

A arquitetura deverá permitir que essa estrutura seja ampliada futuramente, caso seja necessário criar mais administradores ou níveis administrativos.

---

## 7.2 Comprador

O perfil Comprador será destinado aos usuários responsáveis pelas operações relacionadas à aquisição das peças e ao controle dos cascos perante os fornecedores.

O Comprador poderá:

* Cadastrar peças;
* Cadastrar fornecedores;
* Cadastrar contatos de fornecedores;
* Registrar compras;
* Cadastrar os itens relevantes de uma Nota Fiscal de compra;
* Informar quantidades;
* Controlar prazos;
* Registrar remessas de cascos aos fornecedores;
* Consultar o status das devoluções;
* Registrar devoluções de cascos de clientes;
* Consultar dashboards e informações relacionadas aos cascos.

O Comprador também poderá registrar devoluções de cascos provenientes da oficina ou do balcão quando necessário, especialmente em situações de ausência dos vendedores responsáveis.

Todas essas operações deverão ser registradas em seu histórico de auditoria.

---

## 7.3 Vendedor

O perfil Vendedor será utilizado pelos usuários responsáveis pelo registro das saídas de peças e pelo acompanhamento da devolução dos cascos pelos clientes.

O perfil Vendedor será único para todos os vendedores, independentemente do setor em que trabalham.

A distinção entre uma operação de oficina e uma operação de balcão será realizada durante o lançamento da saída.

O Vendedor poderá:

* Registrar saídas de peças;
* Informar se a saída é destinada à oficina ou ao balcão;
* Informar o número da Ordem de Serviço quando a saída for destinada à oficina;
* Informar o número da Nota Fiscal quando a saída for destinada ao balcão;
* Informar a peça e a quantidade vendida;
* Informar um nome simplificado para identificação do cliente;
* Consultar o prazo de devolução relacionado ao casco;
* Registrar devoluções de cascos realizadas pelos clientes;
* Registrar devoluções totais ou parciais;
* Consultar as operações sob sua responsabilidade.

O Vendedor deverá acompanhar a devolução do casco por parte do cliente.

O sistema deverá apresentar ao Vendedor informações relacionadas ao prazo de devolução do casco ao fornecedor, permitindo que ele compreenda a urgência da recuperação do casco junto ao cliente.

---

## 7.4 Usuários Distintos com o Mesmo Perfil

Vendedores de setores diferentes poderão possuir contas distintas utilizando o mesmo perfil Vendedor.

Por exemplo:

```text
Usuário: João
Perfil: Vendedor
Setor: Oficina

Usuário: Maria
Perfil: Vendedor
Setor: Balcão
```

Ambos utilizarão o mesmo conjunto de permissões do perfil Vendedor, porém:

* Possuirão credenciais próprias;
* Terão históricos individuais;
* Poderão ser desativados individualmente;
* Suas operações serão registradas separadamente.

A identificação do setor poderá ser utilizada para facilitar a organização interna e os filtros de consulta, sem criar perfis de acesso diferentes.

---

## 7.5 Autenticação

O acesso ao sistema deverá exigir autenticação individual.

O usuário deverá informar suas credenciais para acessar o sistema.

O sistema deverá:

* Validar as credenciais;
* Impedir o acesso de usuários desativados;
* Registrar o último acesso;
* Registrar o histórico de acessos relevantes;
* Associar as operações ao usuário autenticado.

As senhas não deverão ser armazenadas em texto puro.

O sistema deverá utilizar mecanismos seguros para armazenamento e validação das senhas.

---

## 7.6 Alteração e Redefinição de Senhas

O usuário poderá alterar sua própria senha mediante autenticação adequada.

O Administrador Master poderá redefinir a senha de um usuário quando necessário.

A redefinição de senha deverá ser registrada no histórico de auditoria.

A senha atual do usuário não deverá ser exibida ao Administrador Master.

---

## 7.7 Ativação e Desativação de Usuários

Usuários poderão ser desativados sem serem excluídos fisicamente do sistema.

Um usuário desativado:

* Não poderá realizar login;
* Não poderá realizar novas operações;
* Continuará associado às operações históricas realizadas anteriormente.

A desativação não deverá apagar ou modificar o histórico de operações do usuário.

A reativação poderá ser realizada por um usuário autorizado.

---

## 7.8 Exclusão de Usuários

Usuários que já tenham realizado operações no sistema não deverão ser excluídos fisicamente.

Essa regra é necessária para preservar a rastreabilidade e a auditoria.

Quando um usuário deixar de utilizar o sistema, sua conta deverá ser desativada.

A exclusão física poderá ser considerada somente para usuários que nunca tenham realizado qualquer operação, desde que essa operação seja autorizada e não comprometa a integridade dos dados.

---

## 7.9 Registro do Último Acesso

O sistema deverá registrar o último acesso realizado por cada usuário.

Quando aplicável, poderão ser registrados:

* Data do último acesso;
* Hora do último acesso;
* Resultado da tentativa de acesso;
* Informações técnicas necessárias para auditoria.

O registro do último acesso deverá ser utilizado para auxiliar o controle administrativo e a segurança do sistema.

---

## 7.10 Auditoria de Usuários

As operações realizadas pelos usuários deverão ser rastreáveis.

O sistema deverá permitir identificar:

* Qual usuário realizou a operação;
* Qual operação foi realizada;
* Qual registro foi afetado;
* Quando a operação ocorreu;
* Quais alterações foram realizadas, quando aplicável.

A auditoria deverá permanecer preservada mesmo quando uma operação for posteriormente corrigida ou cancelada.

---

## 7.11 Permissões Futuras

Inicialmente, as permissões serão organizadas por perfis de acesso.

O sistema deverá ser desenvolvido de forma que futuramente o Administrador Master possa criar permissões personalizadas.

Essa evolução poderá permitir, por exemplo:

* Permitir determinada operação a um usuário específico;
* Restringir determinadas funcionalidades;
* Criar novos perfis;
* Combinar permissões de diferentes áreas;
* Definir permissões específicas para determinadas operações.

A implementação de permissões personalizadas poderá ser realizada em uma versão futura, sem comprometer a estrutura inicial de usuários e perfis.

---

# 8. Regras de Negócio

As regras de negócio definem o comportamento obrigatório do SIGC e devem ser respeitadas tanto pela interface quanto pela lógica interna do sistema.

Nenhuma operação deverá ser considerada válida apenas por ter sido inserida na interface. As regras deverão ser validadas pela camada responsável pela lógica de negócio, garantindo que operações realizadas por diferentes telas ou futuramente por outros meios obedeçam às mesmas restrições.

---

## 8.1 Regras Gerais

### RN-001 — Escopo de controle

O SIGC deverá controlar exclusivamente peças que possuam obrigação de devolução de casco.

Peças que não necessitem de controle de casco não deverão ser cadastradas como itens controlados pelo sistema.

---

### RN-002 — Independência do sistema principal

O SIGC não deverá depender de integração com o sistema principal da empresa para realizar suas operações.

As informações necessárias deverão ser registradas diretamente no SIGC por usuários autorizados.

---

### RN-003 — Preservação do histórico

Informações que já tenham participado de operações do sistema não deverão ser excluídas fisicamente quando a exclusão comprometer a rastreabilidade histórica.

---

### RN-004 — Rastreabilidade

Toda operação relevante deverá ser associada ao usuário responsável, à data e à hora da operação.

---

### RN-005 — Alterações controladas

Correções em informações ou operações já registradas deverão preservar o histórico da alteração.

---

## 8.2 Regras de Cadastro de Peças

### RN-006 — Informações mínimas da peça

O cadastro de uma peça controlada deverá conter:

* Descrição;
* Código original;
* Fornecedor;
* Prazo para devolução do casco.

---

### RN-007 — Prazo associado à peça

O prazo de devolução deverá ser associado à combinação aplicável entre a peça, o código original e o fornecedor.

Uma mesma descrição de peça poderá possuir diferentes prazos quando estiver associada a diferentes códigos originais ou fornecedores.

---

### RN-008 — Desativação de peças

Uma peça que já tenha participado de operações não deverá ser excluída fisicamente.

Quando necessário, deverá ser desativada.

Peças desativadas não deverão ser utilizadas em novas operações, mas deverão permanecer disponíveis para consulta histórica.

---

## 8.3 Regras de Fornecedores

### RN-009 — Cadastro de fornecedores

Um fornecedor poderá possuir várias peças associadas.

---

### RN-010 — Múltiplos contatos

Um fornecedor poderá possuir vários contatos.

Cada contato poderá conter, entre outras informações necessárias:

* Nome;
* E-mail;
* Status.

---

### RN-011 — Preservação de contatos históricos

A alteração ou desativação de um contato não deverá modificar informações históricas de operações já realizadas.

---

## 8.4 Regras de Compras

### RN-012 — Registro de compra

Uma compra deverá ser registrada através de sua Nota Fiscal de origem.

---

### RN-013 — Múltiplos itens

Uma Nota Fiscal de compra poderá conter vários itens controlados pelo SIGC.

---

### RN-014 — Quantidade de itens

Uma Nota Fiscal poderá conter várias unidades de uma mesma peça.

---

### RN-015 — Itens não controlados

Itens da Nota Fiscal que não possuam obrigação de devolução de casco não deverão ser cadastrados no SIGC.

---

### RN-016 — Data de origem do prazo

O prazo de devolução do casco deverá ser calculado com base na data de emissão da Nota Fiscal de compra.

---

### RN-017 — Preservação do prazo histórico

O prazo aplicável a uma compra deverá ser preservado no momento do registro da operação.

Alterações futuras no prazo padrão da peça não deverão modificar automaticamente prazos de compras já registradas.

---

### RN-018 — Data limite

A data limite para devolução deverá ser calculada a partir da data de emissão da Nota Fiscal de compra e do prazo aplicável à peça.

---

### RN-019 — Compra como origem

Toda quantidade controlada deverá manter vínculo com sua compra de origem.

---

## 8.5 Regras FIFO e Saídas

### RN-020 — Prioridade FIFO

As saídas deverão consumir prioritariamente as quantidades provenientes das compras mais antigas ainda disponíveis.

---

### RN-021 — Consumo de múltiplas compras

Quando uma saída ultrapassar a quantidade disponível da compra mais antiga, o sistema deverá consumir automaticamente a quantidade restante das compras seguintes.

---

### RN-022 — Rastreabilidade da saída

Uma saída deverá manter vínculo com as compras de origem utilizadas para compor sua quantidade.

---

### RN-023 — Saída para oficina

Quando o destino da saída for Oficina, o número da Ordem de Serviço deverá ser informado.

---

### RN-024 — Saída para balcão

Quando o destino da saída for Balcão, o número da Nota Fiscal deverá ser informado.

---

### RN-025 — Destino obrigatório

Toda saída deverá possuir um destino válido entre as opções disponíveis no sistema.

---

### RN-026 — Identificação simplificada do cliente

A saída deverá permitir o registro de um nome simplificado para facilitar a identificação do cliente.

---

### RN-027 — Consulta externa

O SIGC não deverá exigir o cadastro completo do cliente, uma vez que essas informações permanecem disponíveis no sistema principal da empresa.

---

### RN-028 — Quantidade válida

A quantidade de uma saída deverá ser maior que zero.

---

### RN-029 — Quantidade disponível

O sistema não deverá permitir uma saída superior à quantidade disponível para o item controlado.

---

## 8.6 Regras de Devolução do Cliente

### RN-030 — Registro de devolução

Uma devolução de casco pelo cliente deverá estar vinculada a uma saída previamente registrada.

---

### RN-031 — Devolução total

Quando a quantidade devolvida for igual à quantidade pendente da saída, a devolução deverá ser considerada total.

---

### RN-032 — Devolução parcial

Quando a quantidade devolvida for inferior à quantidade pendente da saída, a operação deverá permanecer como parcialmente devolvida.

---

### RN-033 — Múltiplas devoluções

Uma mesma saída poderá possuir mais de um lançamento de devolução até que a quantidade total pendente seja zerada.

---

### RN-034 — Limite de devolução

O sistema deverá impedir que a quantidade total devolvida ultrapasse a quantidade originalmente saída e ainda pendente de devolução.

---

### RN-035 — Bloqueio de excesso

Caso o usuário tente registrar uma quantidade superior à quantidade pendente, o sistema deverá bloquear a operação e informar a quantidade máxima permitida.

---

### RN-036 — Nota Fiscal de devolução do cliente

Não será exigida uma Nota Fiscal de devolução de casco emitida pelo cliente.

---

### RN-037 — Dados da devolução

Uma devolução do cliente deverá permitir o registro de:

* Data da devolução;
* Quantidade devolvida;
* Observação;
* Usuário responsável.

---

### RN-038 — Disponibilidade após devolução

A quantidade de casco recebida do cliente deverá tornar-se disponível para futura remessa ao fornecedor, respeitando sua origem e rastreabilidade.

---

### RN-039 — Responsabilidade pelo acompanhamento

O Vendedor deverá acompanhar a devolução do casco pelo cliente, mas o Comprador também poderá registrar a devolução quando necessário.

---

### RN-040 — Rastreabilidade FIFO na devolução

Quando uma saída tiver consumido quantidades provenientes de mais de uma compra, as devoluções dos clientes deverão ser associadas automaticamente às origens da saída seguindo a ordem FIFO.

A devolução deverá consumir primeiro a quantidade vinculada à compra mais antiga ainda disponível para devolução.

---

### RN-041 — Devolução distribuída entre origens

Quando a quantidade devolvida ultrapassar a quantidade restante vinculada à origem mais antiga, o sistema deverá continuar automaticamente a associação da devolução às origens seguintes.

---

### Exemplo

Uma saída de 8 unidades foi composta por:

Compra A:

* 5 unidades

Compra B:

* 3 unidades

O cliente devolve 6 unidades.

O sistema deverá registrar:

Compra A:

* 5 cascos devolvidos

Compra B:

* 1 casco devolvido

A operação deverá manter a rastreabilidade das duas origens.

---

### RN-042 — Proibição de escolha manual da origem

O usuário não deverá precisar selecionar manualmente a compra de origem do casco devolvido quando a origem puder ser determinada automaticamente pela rastreabilidade FIFO da saída.

---

### RN-043 — Preservação da origem

A associação entre a devolução e a origem da compra deverá ser preservada para permitir o controle correto dos prazos e das futuras remessas ao fornecedor.

---

## 8.7 Regras de Remessa ao Fornecedor

### RN-044 — Registro da remessa

A remessa de cascos ao fornecedor deverá ser registrada no SIGC quando os cascos forem enviados pela empresa.

---

### RN-045 — Documento da remessa

A remessa deverá ser vinculada à Nota Fiscal de Simples Remessa emitida pela própria empresa.

---

### RN-046 — Origem da remessa

A remessa deverá manter vínculo com a Nota Fiscal de compra de origem dos itens enviados.

---

### RN-047 — Múltiplos itens

Uma única remessa poderá conter vários itens diferentes provenientes da mesma Nota Fiscal de compra.

---

### RN-048 — Devolução parcial ao fornecedor

Uma Nota Fiscal de compra poderá possuir remessas parciais realizadas em diferentes momentos.

---

### RN-049 — Quantidade máxima

O sistema não deverá permitir o registro de uma remessa em quantidade superior à quantidade disponível para remessa ao fornecedor.

---

### RN-050 — Quantidade disponível para remessa

A quantidade disponível para remessa deverá considerar os cascos efetivamente recebidos dos clientes e ainda não enviados ao fornecedor.

---

### RN-051 — Dados da remessa

A remessa deverá permitir o registro de:

* Data;
* Número da Nota Fiscal de Simples Remessa;
* Nota Fiscal de compra de origem;
* Peças;
* Quantidades;
* Observações;
* Usuário responsável.

---

### RN-052 — Remessas múltiplas

A mesma Nota Fiscal de compra poderá possuir mais de uma remessa ao fornecedor até que todas as quantidades necessárias sejam remetidas.

---

### RN-053 — Atualização de status

O registro de uma remessa deverá atualizar as quantidades e o status de devolução correspondentes.

---

## 8.8 Regras de Transferências

### RN-054 — Transferências excepcionais

O sistema deverá permitir o registro de transferências excepcionais entre filiais.

---

### RN-055 — Responsabilidade da filial de origem

A filial de origem continuará responsável pela devolução do casco ao fornecedor.

---

### RN-056 — Responsabilidade da filial de destino

A filial de destino será responsável por devolver o casco à filial de origem.

---

### RN-057 — Nota Fiscal de transferência

A transferência deverá ser identificada pela Nota Fiscal de transferência.

---

### RN-058 — Prazo específico

Uma transferência poderá possuir um prazo de devolução específico informado manualmente.

---

### RN-059 — Não alteração do prazo padrão

O prazo específico de uma transferência não deverá alterar o prazo padrão cadastrado para a peça.

---

### RN-060 — Rastreabilidade da transferência

A transferência deverá manter vínculo com a peça, quantidade, filial de origem e Nota Fiscal correspondente.

---

## 8.9 Regras de Prazos e Status

### RN-061 — Cálculo do prazo

O prazo deverá ser calculado com base na data de origem aplicável à operação e no prazo definido para a peça ou transferência.

---

### RN-062 — Status Normal

Uma operação com mais de 30 dias restantes deverá ser classificada como Normal.

---

### RN-063 — Status Atenção

Uma operação com até 30 dias restantes deverá ser classificada como Atenção.

---

### RN-064 — Status Urgente

Uma operação com até 7 dias restantes deverá ser classificada como Urgente.

---

### RN-065 — Status Atrasado

Uma operação cujo prazo tenha vencido deverá ser classificada como Atrasado.

---

### RN-066 — Prioridade do status

Quando uma operação se enquadrar em mais de uma condição de prazo, deverá ser aplicado o status de maior urgência.

---

## 8.10 Regras de Usuários

### RN-067 — Conta individual

Cada usuário deverá possuir sua própria conta de acesso.

---

### RN-068 — Perfis iniciais

Os perfis iniciais serão:

* Administrador Master;
* Comprador;
* Vendedor.

---

### RN-069 — Vendedores de setores diferentes

Vendedores de Oficina e Balcão poderão possuir contas diferentes, mas utilizarão o mesmo perfil Vendedor.

---

### RN-070 — Usuário desativado

Usuários desativados não poderão realizar login ou novas operações.

---

### RN-071 — Preservação do usuário histórico

Usuários que já tenham realizado operações não deverão ser excluídos fisicamente.

---

### RN-072 — Alteração de senha

O usuário poderá alterar sua própria senha.

---

### RN-073 — Redefinição de senha

O Administrador Master poderá redefinir a senha de um usuário.

---

### RN-074 — Último acesso

O sistema deverá registrar o último acesso do usuário.

---

## 8.11 Regras de Auditoria

### RN-075 — Registro de operações

Operações relevantes deverão registrar o usuário responsável, data e hora.

---

### RN-076 — Histórico de alterações

Alterações realizadas em registros deverão preservar informações suficientes para auditoria.

---

### RN-077 — Histórico de cancelamentos

Cancelamentos deverão preservar o registro da operação original e registrar o cancelamento.

---

### RN-078 — Identificação do responsável

O histórico deverá permitir identificar o usuário responsável por cada operação.

---

## 8.12 Regras de Correções e Cancelamentos

### RN-079 — Correção controlada

O sistema deverá permitir a correção de lançamentos conforme as permissões do usuário.

---

### RN-080 — Histórico da correção

A correção não deverá apagar o histórico do lançamento original.

---

### RN-081 — Cancelamento controlado

O sistema deverá permitir o cancelamento de operações conforme as permissões do usuário.

---

### RN-082 — Reversão de quantidades

Quando uma operação for cancelada, as quantidades relacionadas deverão retornar ao estado correspondente anterior à operação cancelada.

---

### RN-083 — Correção de quantidades

Quando uma operação tiver sua quantidade corrigida, o sistema deverá ajustar os saldos relacionados de acordo com a nova quantidade válida.

---

### RN-084 — Auditoria das correções

Correções e cancelamentos deverão registrar o usuário responsável, data, hora e motivo ou justificativa quando aplicável.

---

## 8.13 Regras de Segurança e Integridade

### RN-085 — Senhas protegidas

As senhas não deverão ser armazenadas em texto puro.

---

### RN-086 — Validação centralizada

As regras de negócio deverão ser validadas na lógica interna do sistema, independentemente da tela utilizada.

---

### RN-087 — Integridade das quantidades

O sistema deverá impedir operações que resultem em quantidades negativas ou inconsistentes.

---

### RN-088 — Integridade das origens

As quantidades deverão permanecer rastreáveis até sua origem sempre que aplicável.

---

### RN-089 — Preservação dos dados

Operações históricas não deverão ser removidas de forma que comprometam a auditoria do sistema.

---

## 8.14 Regras de Evolução

### RN-090 — Compatibilidade futura

A estrutura do sistema deverá permitir futuras evoluções sem perda dos dados históricos.

---

### RN-091 — Novas permissões

O sistema deverá permitir futura expansão para permissões personalizadas.

---

### RN-092 — Expansão para filiais

A arquitetura deverá permitir futura expansão para múltiplas filiais.

---

### RN-093 — Alteração das regras

Alterações relevantes nas regras de negócio deverão ser documentadas e registradas no histórico da especificação do projeto.

---

# 9. Fluxos Operacionais

Os fluxos operacionais descrevem a sequência esperada para as principais operações do SIGC.

Os fluxos deverão representar o funcionamento real do controle de cascos e servirão como referência para o desenvolvimento da interface, das regras de negócio e dos testes do sistema.

---

## 9.1 Fluxo Geral do Casco

O ciclo básico de controle de um casco será:

```text
Compra da peça
      ↓
Registro da compra no SIGC
      ↓
Peça disponível para saída
      ↓
Saída para Oficina ou Balcão
      ↓
Cliente recebe a peça
      ↓
Cliente devolve o casco
      ↓
Casco recebido pela empresa
      ↓
Casco disponível para remessa
      ↓
Empresa emite NF de Simples Remessa
      ↓
Casco enviado ao fornecedor
      ↓
Ciclo concluído
```

---

## 9.2 Fluxo de Cadastro de Peça

### Responsável

Comprador ou usuário autorizado.

### Etapas

1. Acessar o cadastro de peças.
2. Selecionar a opção de criar novo cadastro.
3. Informar a descrição da peça.
4. Informar o código original.
5. Selecionar o fornecedor.
6. Informar o prazo de devolução do casco.
7. Confirmar o cadastro.
8. O sistema deverá validar os dados.
9. O sistema deverá registrar a peça.

### Validações

* A descrição deverá ser informada;
* O código original deverá ser informado;
* O fornecedor deverá ser selecionado;
* O prazo deverá ser válido;
* O cadastro não deverá criar duplicidade indevida.

---

## 9.3 Fluxo de Cadastro de Fornecedor

### Responsável

Comprador ou usuário autorizado.

### Etapas

1. Acessar o cadastro de fornecedores.
2. Criar um novo fornecedor.
3. Informar os dados necessários.
4. Salvar o fornecedor.
5. Adicionar um ou mais contatos.
6. Informar o nome do contato.
7. Informar o e-mail do contato.
8. Salvar o contato.

Um fornecedor poderá possuir vários contatos ativos ou históricos.

---

## 9.4 Fluxo de Registro de Compra

### Responsável

Comprador.

### Etapas

1. Acessar o módulo de compras.
2. Criar um novo registro de compra.
3. Informar o número da Nota Fiscal de compra.
4. Informar a data de emissão da Nota Fiscal.
5. Selecionar o fornecedor.
6. Adicionar os itens controlados pelo SIGC.
7. Selecionar a peça.
8. Informar a quantidade.
9. Confirmar os itens.
10. O sistema deverá calcular a data limite de devolução.
11. O sistema deverá registrar a compra.

Itens da Nota Fiscal que não possuam obrigação de devolução de casco não deverão ser adicionados ao SIGC.

---

## 9.5 Fluxo de Saída para Oficina

### Responsável

Vendedor ou usuário autorizado.

### Etapas

1. Acessar o módulo de saídas.
2. Selecionar o destino Oficina.
3. Informar o número da Ordem de Serviço.
4. Informar o nome simplificado do cliente.
5. Selecionar a peça.
6. Informar a quantidade.
7. Confirmar a operação.
8. O sistema deverá verificar a disponibilidade.
9. O sistema deverá aplicar a regra FIFO.
10. O sistema deverá vincular a saída às compras de origem.
11. O sistema deverá atualizar os saldos.
12. O sistema deverá apresentar o prazo relacionado ao casco.

---

## 9.6 Fluxo de Saída para Balcão

### Responsável

Vendedor ou usuário autorizado.

### Etapas

1. Acessar o módulo de saídas.
2. Selecionar o destino Balcão.
3. Informar o número da Nota Fiscal.
4. Informar o nome simplificado do cliente.
5. Selecionar a peça.
6. Informar a quantidade.
7. Confirmar a operação.
8. O sistema deverá verificar a disponibilidade.
9. O sistema deverá aplicar a regra FIFO.
10. O sistema deverá vincular a saída às compras de origem.
11. O sistema deverá atualizar os saldos.
12. O sistema deverá apresentar o prazo relacionado ao casco.

---

## 9.7 Fluxo FIFO

Quando uma saída utilizar mais de uma compra, o sistema deverá dividir internamente o consumo entre as origens.

### Exemplo

```text
Compra A
Data: 01/01
Quantidade: 5

Compra B
Data: 15/01
Quantidade: 10

Saída
Quantidade: 8
```

Resultado:

```text
Compra A
Consumido: 5

Compra B
Consumido: 3
```

A saída deverá permanecer vinculada às duas compras.

Cada origem deverá manter seu próprio controle de prazo.

---

## 9.8 Fluxo de Devolução do Cliente

### Responsável

Vendedor ou Comprador.

### Etapas

1. Acessar o módulo de devoluções.
2. Localizar a saída original.
3. Conferir a peça.
4. Informar a data da devolução.
5. Informar a quantidade devolvida.
6. Adicionar observação, quando necessário.
7. Confirmar a operação.
8. O sistema deverá validar a quantidade.
9. O sistema deverá atualizar a quantidade pendente.
10. O sistema deverá atualizar o status da saída.
11. O casco recebido deverá ficar disponível para futura remessa ao fornecedor.

---

## 9.9 Fluxo de Devolução Parcial do Cliente

### Exemplo

```text
Saída original: 6 unidades
```

Primeira devolução:

```text
Devolvido: 4
Pendente: 2
Status: Parcialmente devolvido
```

Segunda devolução:

```text
Devolvido: 2
Pendente: 0
Status: Totalmente devolvido
```

O sistema deverá permitir múltiplos lançamentos relacionados à mesma saída.

---

## 9.10 Fluxo de Bloqueio de Excesso na Devolução

### Exemplo

```text
Quantidade vendida: 6
Quantidade já devolvida: 4
Quantidade pendente: 2
```

Se o usuário tentar registrar:

```text
Nova devolução: 3
```

O sistema deverá:

1. Bloquear a operação;
2. Informar que a quantidade máxima permitida é 2;
3. Solicitar a correção da quantidade;
4. Não alterar os saldos.

---

## 9.11 Fluxo de Remessa ao Fornecedor

### Responsável

Comprador ou usuário autorizado.

### Etapas

1. Acessar o módulo de remessas.
2. Criar uma nova remessa.
3. Informar a data da remessa.
4. Informar o número da Nota Fiscal de Simples Remessa.
5. Selecionar a Nota Fiscal de compra de origem.
6. Selecionar os itens que serão remetidos.
7. Informar as quantidades.
8. O sistema deverá verificar a quantidade disponível.
9. Confirmar a remessa.
10. O sistema deverá atualizar os saldos.
11. O sistema deverá atualizar o status das devoluções.
12. O sistema deverá manter o vínculo com a NF de origem.

---

## 9.12 Fluxo de Remessa Parcial ao Fornecedor

### Exemplo

```text
Compra:
10 unidades

Cascos recebidos dos clientes:
10 unidades
```

Primeira remessa:

```text
Remetido: 6
Pendente: 4
```

Segunda remessa:

```text
Remetido: 4
Pendente: 0
```

O sistema deverá manter as duas operações separadamente, preservando o histórico de cada remessa.

---

## 9.13 Fluxo de Bloqueio de Excesso na Remessa

### Exemplo

```text
Disponível para remessa: 5
```

Se o usuário tentar registrar:

```text
Quantidade da remessa: 6
```

O sistema deverá:

1. Bloquear a operação;
2. Informar a quantidade máxima disponível;
3. Solicitar a correção;
4. Não alterar os saldos.

---

## 9.14 Fluxo de Transferência entre Filiais

### Responsável

Usuário autorizado.

### Etapas

1. Registrar a necessidade de transferência.
2. Informar a filial de origem.
3. Informar a Nota Fiscal de transferência.
4. Selecionar a peça.
5. Informar a quantidade.
6. Informar o prazo específico, quando aplicável.
7. Confirmar a transferência.
8. O sistema deverá registrar a operação.
9. A filial de origem continuará responsável perante o fornecedor.
10. A filial de destino ficará responsável pela devolução do casco à filial de origem.

---

## 9.15 Fluxo de Consulta por Nota Fiscal de Compra

### Responsável

Usuário autorizado.

### Etapas

1. Acessar o módulo de consultas.
2. Informar ou pesquisar o número da Nota Fiscal de compra.
3. Selecionar a compra.
4. O sistema deverá apresentar:

* Dados da compra;
* Fornecedor;
* Data de emissão;
* Itens controlados;
* Quantidades adquiridas;
* Saídas relacionadas;
* Quantidades devolvidas pelos clientes;
* Quantidades pendentes de devolução;
* Remessas ao fornecedor;
* Quantidades pendentes de remessa;
* Prazos;
* Status;
* Histórico.

---

## 9.16 Fluxo de Correção de Operação

### Etapas

1. Usuário autorizado localiza a operação.
2. Solicita a correção.
3. O sistema registra o estado anterior.
4. O usuário altera os dados permitidos.
5. O sistema valida as regras de negócio.
6. O sistema recalcula as quantidades relacionadas.
7. O sistema registra a alteração.
8. O histórico permanece preservado.

---

## 9.17 Fluxo de Cancelamento de Operação

### Etapas

1. Usuário autorizado localiza a operação.
2. Solicita o cancelamento.
3. O sistema solicita confirmação.
4. O sistema registra o cancelamento.
5. O sistema preserva a operação original no histórico.
6. As quantidades relacionadas retornam ao estado correspondente.
7. O status da operação é alterado para Cancelada.

---

## 9.18 Fluxo de Login

### Etapas

1. Usuário informa suas credenciais.
2. O sistema verifica a existência da conta.
3. O sistema verifica se o usuário está ativo.
4. O sistema valida a senha.
5. O sistema registra o acesso.
6. O sistema atualiza o último acesso.
7. O sistema libera as funcionalidades permitidas pelo perfil.

Usuários desativados não poderão acessar o sistema.

---

## 9.19 Fluxo de Alteração de Senha

### Usuário

Qualquer usuário ativo.

### Etapas

1. Acessar a alteração de senha.
2. Informar a senha atual.
3. Informar a nova senha.
4. Confirmar a nova senha.
5. O sistema validar as informações.
6. A senha será alterada.
7. A operação será registrada no histórico de auditoria.

---

## 9.20 Fluxo de Redefinição de Senha

### Responsável

Administrador Master.

### Etapas

1. Localizar o usuário.
2. Solicitar redefinição.
3. Definir uma nova senha temporária ou mecanismo seguro de recuperação.
4. Confirmar a operação.
5. Registrar a ação na auditoria.

A senha anterior não deverá ser exibida.

---

## 9.21 Fluxo de Desativação de Usuário

### Responsável

Administrador Master.

### Etapas

1. Localizar o usuário.
2. Solicitar a desativação.
3. Confirmar a operação.
4. O usuário perde a capacidade de realizar login.
5. O histórico das operações permanece preservado.

---

## 9.22 Fluxo de Consulta de Status

O sistema deverá permitir que o usuário consulte o status das operações.

As classificações serão:

```text
NORMAL
    Mais de 30 dias restantes

ATENÇÃO
    Até 30 dias restantes

URGENTE
    Até 7 dias restantes

ATRASADO
    Prazo vencido
```

Os status deverão ser exibidos de forma visualmente clara e padronizada.

---

## 9.23 Fluxo Geral de Auditoria

As operações relevantes deverão seguir o seguinte padrão:

```text
Usuário realiza operação
          ↓
Sistema valida regras
          ↓
Operação é executada
          ↓
Dados são atualizados
          ↓
Histórico é registrado
          ↓
Usuário responsável é identificado
```

Correções e cancelamentos deverão preservar os registros anteriores.

---

# 10. Requisitos Funcionais

Os requisitos funcionais definem as funcionalidades que o SIGC deverá disponibilizar aos usuários.

Cada requisito funcional deverá representar uma capacidade concreta do sistema e deverá ser implementado respeitando as regras de negócio definidas neste documento.

---

## 10.1 Autenticação

### RF-001 — Login

O sistema deverá permitir que usuários cadastrados realizem login utilizando suas credenciais.

---

### RF-002 — Validação de credenciais

O sistema deverá validar as credenciais informadas pelo usuário antes de permitir o acesso.

---

### RF-003 — Bloqueio de usuários desativados

O sistema não deverá permitir o login de usuários desativados.

---

### RF-004 — Registro de acesso

O sistema deverá registrar os acessos dos usuários.

---

### RF-005 — Registro do último acesso

O sistema deverá atualizar e armazenar a data e hora do último acesso realizado pelo usuário.

---

### RF-006 — Encerramento de sessão

O sistema deverá permitir que o usuário encerre sua sessão.

---

## 10.2 Usuários

### RF-007 — Cadastro de usuários

O Administrador Master deverá poder cadastrar novos usuários.

---

### RF-008 — Edição de usuários

O Administrador Master deverá poder editar os dados permitidos dos usuários.

---

### RF-009 — Desativação de usuários

O Administrador Master deverá poder desativar usuários.

---

### RF-010 — Reativação de usuários

O Administrador Master deverá poder reativar usuários desativados.

---

### RF-011 — Consulta de usuários

O Administrador Master deverá poder consultar os usuários cadastrados.

---

### RF-012 — Consulta do histórico do usuário

O sistema deverá permitir a consulta das operações realizadas por determinado usuário, conforme as permissões disponíveis.

---

### RF-013 — Alteração da própria senha

O usuário deverá poder alterar sua própria senha.

---

### RF-014 — Redefinição de senha

O Administrador Master deverá poder redefinir a senha de um usuário.

---

### RF-015 — Perfis de acesso

O sistema deverá possuir inicialmente os perfis:

* Administrador Master;
* Comprador;
* Vendedor.

---

### RF-016 — Permissões futuras

A estrutura do sistema deverá permitir a futura criação de permissões personalizadas.

---

## 10.3 Cadastro de Peças

### RF-017 — Cadastro de peça

O sistema deverá permitir o cadastro de peças que necessitem de controle de casco.

---

### RF-018 — Dados da peça

O sistema deverá permitir o registro de:

* Descrição;
* Código original;
* Fornecedor;
* Prazo para devolução do casco.

---

### RF-019 — Consulta de peças

O sistema deverá permitir a consulta das peças cadastradas.

---

### RF-020 — Pesquisa de peças

O sistema deverá permitir a pesquisa por informações relevantes, como:

* Descrição;
* Código original;
* Fornecedor.

---

### RF-021 — Desativação de peças

O sistema deverá permitir a desativação de peças que não devam mais ser utilizadas em novas operações.

---

### RF-022 — Histórico de peças

O sistema deverá preservar o histórico das peças que já tenham participado de operações.

---

## 10.4 Fornecedores

### RF-023 — Cadastro de fornecedor

O sistema deverá permitir o cadastro de fornecedores.

---

### RF-024 — Dados do fornecedor

O sistema deverá permitir o registro dos dados necessários do fornecedor para o controle dos cascos.

---

### RF-025 — Associação de peças

O sistema deverá permitir associar peças aos fornecedores.

---

### RF-026 — Múltiplos contatos

O sistema deverá permitir o cadastro de vários contatos para um mesmo fornecedor.

---

### RF-027 — Dados de contato

O sistema deverá permitir o registro de:

* Nome;
* E-mail;
* Status do contato.

---

### RF-028 — Consulta de contatos

O sistema deverá permitir a consulta dos contatos associados a um fornecedor.

---

### RF-029 — Desativação de contatos

O sistema deverá permitir desativar contatos sem apagar seu histórico.

---

## 10.5 Compras

### RF-030 — Cadastro de compra

O sistema deverá permitir o registro de compras que contenham peças controladas pelo SIGC.

---

### RF-031 — Dados da Nota Fiscal de compra

O sistema deverá permitir o registro de:

* Número da Nota Fiscal;
* Data de emissão;
* Fornecedor;
* Itens controlados.

---

### RF-032 — Múltiplos itens

O sistema deverá permitir que uma compra possua vários itens controlados.

---

### RF-033 — Quantidade por item

O sistema deverá permitir informar a quantidade adquirida de cada item.

---

### RF-034 — Cálculo de prazo

O sistema deverá calcular automaticamente a data limite de devolução do casco.

---

### RF-035 — Origem da compra

O sistema deverá manter a relação entre cada quantidade registrada e sua Nota Fiscal de compra de origem.

---

### RF-036 — Consulta de compras

O sistema deverá permitir consultar compras cadastradas.

---

### RF-037 — Consulta por Nota Fiscal

O sistema deverá permitir localizar uma compra através do número da Nota Fiscal.

---

## 10.6 Saídas

### RF-038 — Registro de saída

O sistema deverá permitir registrar a saída de peças controladas.

---

### RF-039 — Seleção do destino

O sistema deverá permitir selecionar:

* Oficina;
* Balcão.

---

### RF-040 — Saída para Oficina

Quando o destino for Oficina, o sistema deverá permitir informar o número da Ordem de Serviço.

---

### RF-041 — Saída para Balcão

Quando o destino for Balcão, o sistema deverá permitir informar o número da Nota Fiscal.

---

### RF-042 — Identificação do cliente

O sistema deverá permitir informar um nome simplificado para facilitar a identificação do cliente.

---

### RF-043 — Seleção da peça

O sistema deverá permitir selecionar a peça que está sendo retirada.

---

### RF-044 — Quantidade da saída

O sistema deverá permitir informar a quantidade retirada.

---

### RF-045 — Verificação de disponibilidade

O sistema deverá verificar a quantidade disponível antes de confirmar a saída.

---

### RF-046 — Aplicação automática do FIFO

O sistema deverá identificar automaticamente as compras mais antigas disponíveis para compor a saída.

---

### RF-047 — Consumo de múltiplas compras

O sistema deverá permitir que uma única saída consuma quantidades provenientes de várias compras.

---

### RF-048 — Rastreabilidade da saída

O sistema deverá manter a relação entre a saída e cada compra utilizada como origem.

---

### RF-049 — Exibição do prazo

O sistema deverá exibir ao usuário as informações relevantes sobre o prazo de devolução do casco.

---

## 10.7 Devoluções de Clientes

### RF-050 — Registro de devolução

O sistema deverá permitir registrar devoluções de cascos realizadas pelos clientes.

---

### RF-051 — Localização da saída

O sistema deverá permitir localizar a saída relacionada à devolução.

---

### RF-052 — Data da devolução

O sistema deverá permitir informar a data em que o casco foi devolvido.

---

### RF-053 — Quantidade devolvida

O sistema deverá permitir informar a quantidade devolvida.

---

### RF-054 — Observação

O sistema deverá permitir registrar observações relacionadas à devolução.

---

### RF-055 — Validação da quantidade

O sistema deverá validar se a quantidade informada não ultrapassa a quantidade pendente da saída.

---

### RF-056 — Bloqueio de excesso

O sistema deverá bloquear devoluções que ultrapassem a quantidade permitida.

---

### RF-057 — Devolução parcial

O sistema deverá permitir o registro de devoluções parciais.

---

### RF-058 — Múltiplas devoluções

O sistema deverá permitir registrar várias devoluções para uma mesma saída.

---

### RF-059 — Aplicação do FIFO na devolução

O sistema deverá associar automaticamente a devolução às origens da saída seguindo a ordem FIFO.

---

### RF-060 — Atualização de status

O sistema deverá atualizar o status da saída após o registro de uma devolução.

---

### RF-061 — Disponibilidade do casco

O sistema deverá disponibilizar para remessa os cascos efetivamente recebidos dos clientes e ainda não remetidos ao fornecedor.

---

## 10.8 Remessas ao Fornecedor

### RF-062 — Registro de remessa

O sistema deverá permitir registrar remessas de cascos aos fornecedores.

---

### RF-063 — Nota Fiscal de Simples Remessa

O sistema deverá permitir registrar o número da Nota Fiscal de Simples Remessa emitida pela empresa.

---

### RF-064 — Data da remessa

O sistema deverá permitir registrar a data da remessa.

---

### RF-065 — Associação à compra

O sistema deverá permitir associar a remessa à Nota Fiscal de compra de origem.

---

### RF-066 — Múltiplos itens na remessa

O sistema deverá permitir que uma remessa contenha vários itens diferentes da mesma compra.

---

### RF-067 — Quantidade remetida

O sistema deverá permitir informar a quantidade remetida de cada item.

---

### RF-068 — Validação da quantidade

O sistema deverá verificar se a quantidade remetida está disponível para remessa.

---

### RF-069 — Bloqueio de excesso

O sistema deverá bloquear remessas que ultrapassem a quantidade disponível.

---

### RF-070 — Remessas parciais

O sistema deverá permitir várias remessas relacionadas à mesma Nota Fiscal de compra.

---

### RF-071 — Atualização de status da remessa

O sistema deverá atualizar os saldos e status relacionados após o registro da remessa.

---

### RF-072 — Consulta de remessas

O sistema deverá permitir consultar remessas realizadas.

---

## 10.9 Transferências entre Filiais

### RF-073 — Registro de transferência

O sistema deverá permitir registrar transferências excepcionais entre filiais.

---

### RF-074 — Filial de origem

O sistema deverá permitir informar a filial de origem.

---

### RF-075 — Nota Fiscal de transferência

O sistema deverá permitir informar a Nota Fiscal de transferência.

---

### RF-076 — Peça transferida

O sistema deverá permitir selecionar a peça transferida.

---

### RF-077 — Quantidade transferida

O sistema deverá permitir informar a quantidade transferida.

---

### RF-078 — Prazo específico

O sistema deverá permitir informar um prazo específico para a transferência quando necessário.

---

### RF-079 — Preservação do prazo padrão

O prazo específico da transferência não deverá alterar o prazo padrão cadastrado para a peça.

---

## 10.10 Consultas

### RF-080 — Consulta por Nota Fiscal de compra

O sistema deverá permitir consultar todas as informações relacionadas a uma Nota Fiscal de compra.

---

### RF-081 — Detalhamento da compra

A consulta deverá apresentar:

* Fornecedor;
* Data de emissão;
* Itens;
* Quantidades.

---

### RF-082 — Histórico de saídas

A consulta deverá apresentar as saídas relacionadas à compra.

---

### RF-083 — Histórico de devoluções

A consulta deverá apresentar as devoluções de clientes relacionadas às saídas.

---

### RF-084 — Histórico de remessas

A consulta deverá apresentar as remessas realizadas ao fornecedor.

---

### RF-085 — Quantidades pendentes

A consulta deverá apresentar as quantidades pendentes de devolução e remessa.

---

### RF-086 — Status

A consulta deverá apresentar o status atual das operações relacionadas.

---

### RF-087 — Histórico completo

A consulta deverá permitir visualizar o histórico das operações relacionadas à compra.

---

## 10.11 Dashboards

### RF-088 — Dashboard geral

O sistema deverá disponibilizar um dashboard com informações resumidas sobre o controle de cascos.

---

### RF-089 — Indicadores de prazo

O dashboard deverá apresentar informações sobre:

* Operações normais;
* Operações em atenção;
* Operações urgentes;
* Operações atrasadas.

---

### RF-090 — Indicadores de devolução

O dashboard deverá apresentar informações sobre:

* Cascos pendentes de devolução pelos clientes;
* Cascos devolvidos parcialmente;
* Cascos totalmente devolvidos.

---

### RF-091 — Indicadores de remessa

O dashboard deverá apresentar informações sobre:

* Cascos disponíveis para remessa;
* Cascos já remetidos;
* Quantidades pendentes de remessa.

---

### RF-092 — Filtros

O sistema deverá permitir filtrar informações relevantes por critérios aplicáveis, como:

* Período;
* Fornecedor;
* Peça;
* Status;
* Origem da operação.

---

## 10.12 Auditoria

### RF-093 — Registro de auditoria

O sistema deverá registrar as operações relevantes realizadas pelos usuários.

---

### RF-094 — Usuário responsável

O sistema deverá identificar o usuário responsável por cada operação auditável.

---

### RF-095 — Data e hora

O sistema deverá registrar a data e hora das operações auditáveis.

---

### RF-096 — Histórico de alterações

O sistema deverá registrar alterações relevantes realizadas nos dados.

---

### RF-097 — Histórico de cancelamentos

O sistema deverá preservar o histórico de operações canceladas.

---

### RF-098 — Consulta de auditoria

Usuários autorizados deverão poder consultar registros de auditoria.

---

## 10.13 Correções e Cancelamentos

### RF-099 — Correção de lançamento

O sistema deverá permitir a correção de lançamentos conforme as permissões do usuário.

---

### RF-100 — Preservação do lançamento original

O sistema deverá preservar o histórico do lançamento antes da correção.

---

### RF-101 — Cancelamento de lançamento

O sistema deverá permitir o cancelamento de lançamentos conforme as permissões do usuário.

---

### RF-102 — Reversão de quantidades

O sistema deverá ajustar automaticamente as quantidades relacionadas após um cancelamento.

---

### RF-103 — Reprocessamento de saldos

O sistema deverá recalcular os saldos afetados por correções ou cancelamentos.

---

### RF-104 — Registro da justificativa

O sistema deverá permitir registrar o motivo da correção ou cancelamento quando aplicável.

---

## 10.14 Configurações

### RF-105 — Configuração de parâmetros

O sistema deverá permitir que parâmetros configuráveis sejam centralizados.

---

### RF-106 — Prazos de status

Os limites utilizados para classificação dos status de prazo deverão ser configuráveis futuramente.

---

### RF-107 — Estrutura preparada para expansão

A estrutura do sistema deverá permitir futuras alterações de regras e configurações sem perda do histórico existente.

---

# 11. Requisitos Não Funcionais

Os requisitos não funcionais definem características de qualidade, segurança, desempenho, usabilidade, manutenção e confiabilidade que deverão ser observadas durante o desenvolvimento do SIGC.

O sistema deverá ser desenvolvido com foco em uso profissional, facilidade de manutenção, segurança dos dados e possibilidade de evolução futura.

---

## 11.1 Usabilidade

### RNF-001 — Interface intuitiva

A interface deverá ser intuitiva, permitindo que usuários com diferentes níveis de conhecimento técnico utilizem o sistema sem necessidade de conhecimentos avançados em informática.

---

### RNF-002 — Padronização visual

As telas do sistema deverão seguir um padrão visual consistente.

Elementos como:

* Botões;
* Campos;
* Tabelas;
* Menus;
* Mensagens;
* Indicadores;
* Janelas de confirmação;

deverão possuir comportamento e aparência padronizados.

---

### RNF-003 — Interface limpa

As telas deverão apresentar somente as informações necessárias para a tarefa atual.

Informações secundárias deverão ser apresentadas apenas quando necessárias ou solicitadas pelo usuário.

---

### RNF-004 — Clareza das ações

Os botões deverão possuir nomes claros e representar diretamente a ação que executam.

A interface deverá evitar botões ambíguos ou cuja função não seja evidente.

---

### RNF-005 — Feedback das operações

O sistema deverá informar claramente o resultado das operações realizadas.

O usuário deverá ser informado quando:

* Uma operação for concluída;
* Uma operação for bloqueada;
* Um erro ocorrer;
* Uma informação estiver incorreta;
* Uma ação exigir confirmação.

---

### RNF-006 — Prevenção de erros

A interface deverá auxiliar o usuário a evitar erros de preenchimento.

Sempre que possível, o sistema deverá:

* Validar dados antes da confirmação;
* Impedir valores inválidos;
* Exibir mensagens claras;
* Solicitar confirmação para operações críticas.

---

## 11.2 Consistência Visual

### RNF-007 — Identidade visual

O sistema deverá possuir uma identidade visual consistente e profissional.

A identidade visual deverá ser facilmente ajustável futuramente sem necessidade de reescrever individualmente cada tela.

---

### RNF-008 — Componentes reutilizáveis

Componentes visuais comuns deverão ser reutilizáveis.

Exemplos:

* Botões;
* Campos de entrada;
* Tabelas;
* Cartões de indicadores;
* Diálogos;
* Mensagens;
* Componentes de status.

---

### RNF-009 — Padrão de navegação

A navegação entre as principais áreas do sistema deverá seguir uma estrutura consistente.

O usuário deverá conseguir identificar facilmente:

* Onde está;
* Qual módulo está utilizando;
* Como retornar;
* Qual ação está realizando.

---

## 11.3 Desempenho

### RNF-010 — Resposta das operações

As operações comuns do sistema deverão apresentar resposta adequada ao usuário, evitando esperas desnecessárias.

---

### RNF-011 — Consultas

Consultas e filtros deverão ser executados de maneira eficiente, mesmo com o crescimento do volume de dados.

---

### RNF-012 — Processamento local

As operações principais deverão ser processadas localmente, utilizando o banco de dados SQLite.

---

## 11.4 Segurança

### RNF-013 — Autenticação

O sistema deverá exigir autenticação para acesso às funcionalidades protegidas.

---

### RNF-014 — Senhas protegidas

As senhas não deverão ser armazenadas em texto puro.

---

### RNF-015 — Controle de permissões

O sistema deverá impedir que usuários executem operações não permitidas para seus perfis.

---

### RNF-016 — Auditoria

Operações relevantes deverão ser registradas para permitir rastreabilidade.

---

### RNF-017 — Proteção contra alterações indevidas

As operações críticas deverão possuir validações e controles para reduzir o risco de alterações acidentais ou indevidas.

---

## 11.5 Integridade dos Dados

### RNF-018 — Consistência

O sistema deverá preservar a consistência dos dados durante as operações.

---

### RNF-019 — Operações atômicas

Operações que envolvam múltiplas alterações relacionadas deverão ser executadas de forma que não deixem o sistema em estado parcialmente atualizado.

---

### RNF-020 — Integridade referencial

Os relacionamentos entre peças, compras, saídas, devoluções e remessas deverão ser preservados.

---

### RNF-021 — Validação centralizada

As regras de negócio deverão ser aplicadas independentemente da interface utilizada.

---

## 11.6 Confiabilidade

### RNF-022 — Preservação do histórico

O sistema deverá preservar informações necessárias para auditoria e rastreabilidade.

---

### RNF-023 — Recuperação após falhas

O sistema deverá ser desenvolvido de forma a reduzir o risco de perda de dados em caso de falhas inesperadas.

---

### RNF-024 — Tratamento de erros

Erros inesperados deverão ser tratados de forma controlada.

O sistema deverá evitar o encerramento abrupto sem informar o usuário ou registrar informações técnicas relevantes.

---

## 11.7 Banco de Dados

### RNF-025 — Banco local

O sistema deverá utilizar SQLite como banco de dados local na versão inicial.

---

### RNF-026 — Integridade do banco

O banco de dados deverá utilizar mecanismos de integridade e validação disponíveis no SQLite.

---

### RNF-027 — Evolução do banco

A estrutura do banco deverá permitir alterações futuras por meio de migrações controladas.

---

### RNF-028 — Não alteração manual

Usuários comuns não deverão precisar acessar ou alterar diretamente o banco de dados para utilizar o sistema.

---

## 11.8 Funcionamento em Rede

### RNF-029 — Pasta compartilhada

O sistema deverá ser disponibilizado em uma pasta compartilhada da rede interna da empresa.

---

### RNF-030 — Execução em diferentes computadores

Usuários autorizados deverão poder utilizar o sistema a partir de diferentes computadores da rede, respeitando as limitações da arquitetura adotada.

---

### RNF-031 — Proteção dos arquivos

Os arquivos internos do sistema deverão possuir proteção adequada contra alterações acidentais.

---

### RNF-032 — Arquivos internos

Arquivos utilizados internamente pelo sistema deverão ser organizados de forma que não fiquem expostos desnecessariamente aos usuários.

---

### RNF-033 — Concorrência de acesso

A arquitetura deverá considerar a possibilidade de múltiplos usuários utilizando o sistema simultaneamente.

A solução deverá ser avaliada durante a definição da arquitetura técnica, considerando as limitações do SQLite em ambiente de rede compartilhada.

---

## 11.9 Backup e Recuperação

### RNF-034 — Backup dos dados

O sistema deverá possuir uma estratégia de backup dos dados.

---

### RNF-035 — Preservação dos backups

Os backups deverão ser armazenados de forma separada do arquivo principal de dados sempre que possível.

---

### RNF-036 — Recuperação

Deverá existir um procedimento documentado para restauração dos dados a partir de um backup válido.

---

### RNF-037 — Identificação dos backups

Os backups deverão possuir identificação que permita determinar sua data e origem.

---

## 11.10 Manutenibilidade

### RNF-038 — Código organizado

O código deverá ser organizado em módulos com responsabilidades bem definidas.

---

### RNF-039 — Separação de responsabilidades

A interface, a lógica de negócio, o acesso ao banco de dados e as regras de segurança deverão ser mantidos preferencialmente em camadas separadas.

---

### RNF-040 — Código documentado

Partes relevantes do código deverão possuir documentação suficiente para facilitar sua manutenção.

---

### RNF-041 — Padrões de desenvolvimento

O projeto deverá seguir padrões consistentes de:

* Nomenclatura;
* Organização de arquivos;
* Formatação;
* Tratamento de erros;
* Commits;
* Documentação.

---

### RNF-042 — Identificação de autoria

A documentação técnica, estrutura do projeto e elementos apropriados do código poderão conter identificação de autoria e informações relacionadas ao autor do projeto, sem comprometer a organização ou a funcionalidade do sistema.

---

## 11.11 Versionamento

### RNF-043 — Controle de versão

O projeto deverá utilizar Git para controle de versão.

---

### RNF-044 — Repositório remoto

O código deverá ser mantido em um repositório remoto no GitHub.

---

### RNF-045 — Histórico de alterações

As alterações relevantes deverão ser registradas no histórico do projeto.

---

### RNF-046 — Commits organizados

Os commits deverão possuir mensagens claras e representar alterações coerentes.

---

### RNF-047 — Branches

O projeto poderá utilizar branches para desenvolvimento de funcionalidades específicas ou experimentais.

---

## 11.12 Portabilidade

### RNF-048 — Sistema operacional

A primeira versão deverá priorizar o ambiente Windows, considerando o ambiente de utilização da empresa.

---

### RNF-049 — Execução como aplicação

O sistema deverá ser preparado para execução como aplicação, reduzindo a necessidade de configuração técnica para os usuários finais.

---

### RNF-050 — Dependências

As dependências necessárias para execução deverão ser documentadas e controladas.

---

## 11.13 Escalabilidade

### RNF-051 — Crescimento de dados

O sistema deverá ser estruturado considerando o crescimento gradual do número de:

* Compras;
* Peças;
* Saídas;
* Devoluções;
* Remessas;
* Usuários;
* Registros de auditoria.

---

### RNF-052 — Expansão futura

A arquitetura deverá permitir futuras evoluções, incluindo:

* Suporte a múltiplas filiais;
* Permissões personalizadas;
* Novos dashboards;
* Novos tipos de operação;
* Possíveis integrações futuras.

---

## 11.14 Evolução Visual

### RNF-053 — Tema visual configurável

A identidade visual deverá ser organizada de forma centralizada sempre que tecnicamente possível.

Alterações futuras de:

* Cores;
* Tipografia;
* Espaçamentos;
* Componentes;
* Ícones;

deverão poder ser realizadas sem necessidade de alterações extensas em todas as telas.

---

### RNF-054 — Consistência futura

Novas telas e funcionalidades deverão seguir os padrões visuais existentes no sistema.

---

## 11.15 Documentação

### RNF-055 — Documentação técnica

O projeto deverá possuir documentação técnica suficiente para permitir sua manutenção e evolução.

---

### RNF-056 — Documentação como referência

A documentação principal do projeto deverá ser considerada a fonte oficial das decisões e regras do SIGC.

---

### RNF-057 — Atualização da documentação

Alterações relevantes no comportamento, arquitetura ou regras do sistema deverão ser refletidas na documentação.

---

## 11.16 Limitações Conhecidas

### RNF-058 — Ambiente de rede compartilhada

A utilização de SQLite em uma pasta compartilhada deverá ser analisada cuidadosamente durante a definição da arquitetura.

A solução deverá considerar possíveis problemas relacionados a:

* Acesso simultâneo;
* Bloqueio de arquivos;
* Corrupção de dados;
* Disponibilidade da rede;
* Backup;
* Recuperação após falhas.

A decisão final sobre a forma de utilização do banco deverá ser tomada antes da implementação da arquitetura definitiva.

---

### RNF-059 — Evolução da arquitetura

Caso o volume de usuários ou operações ultrapasse as limitações da solução inicial, o sistema deverá poder evoluir para uma arquitetura mais adequada, sem perda dos dados históricos.

---

# 12. Arquitetura do Sistema

A arquitetura do SIGC deverá ser organizada de forma modular e baseada em responsabilidades bem definidas, permitindo a separação entre interface, aplicação, regras de negócio, acesso aos dados e infraestrutura.

A arquitetura deverá priorizar:

* Organização;
* Manutenibilidade;
* Segurança;
* Testabilidade;
* Reutilização;
* Integridade dos dados;
* Suporte a múltiplos usuários;
* Evolução futura.

O SIGC utilizará uma arquitetura cliente-servidor, na qual os computadores dos usuários executarão a aplicação cliente e um servidor central da rede interna será responsável pela API e pelo acesso ao banco de dados.

---

## 12.1 Arquitetura Cliente-Servidor

A arquitetura principal do SIGC será baseada no modelo cliente-servidor.

Os computadores dos usuários executarão a aplicação cliente, responsável pela interface e pela interação com o sistema.

Um servidor central da rede interna será responsável por executar a API do SIGC e realizar o acesso ao banco de dados.

A comunicação deverá seguir o fluxo:

```text
Usuário
   ↓
Aplicação Cliente
   ↓
Rede Interna
   ↓
API do SIGC
   ↓
Regras de Negócio
   ↓
Banco de Dados
```

Os computadores dos usuários não deverão acessar diretamente o arquivo do banco de dados.

Essa abordagem deverá:

* Centralizar as regras de negócio;
* Evitar acesso direto ao banco pelos usuários;
* Melhorar o controle de acesso;
* Reduzir riscos de conflitos de escrita;
* Facilitar a auditoria;
* Permitir múltiplos usuários simultâneos;
* Facilitar futuras atualizações;
* Preparar o sistema para expansão futura.

---

## 12.2 Arquitetura em Camadas

O sistema deverá utilizar uma arquitetura baseada em camadas com responsabilidades bem definidas.

A estrutura conceitual será:

```text
┌──────────────────────────────────────┐
│          CAMADA DE APRESENTAÇÃO      │
│              Interface (UI)          │
└────────────────────┬─────────────────┘
                     │
┌────────────────────▼─────────────────┐
│           CAMADA DE APLICAÇÃO        │
│       Casos de uso e orquestração    │
└────────────────────┬─────────────────┘
                     │
┌────────────────────▼─────────────────┐
│          CAMADA DE DOMÍNIO           │
│        Regras de negócio do SIGC     │
└────────────────────┬─────────────────┘
                     │
┌────────────────────▼─────────────────┐
│          CAMADA DE INFRAESTRUTURA    │
│      Banco, arquivos e serviços      │
└──────────────────────────────────────┘
```

A aplicação cliente será responsável principalmente pela camada de apresentação.

A API do SIGC concentrará as camadas de aplicação, domínio e infraestrutura.

---

## 12.3 Aplicação Cliente

A aplicação cliente será executada nos computadores dos usuários.

Suas principais responsabilidades serão:

* Exibir a interface;
* Receber dados do usuário;
* Enviar solicitações para a API;
* Exibir resultados;
* Apresentar mensagens;
* Exibir dashboards;
* Permitir a navegação entre os módulos do sistema.

A aplicação cliente não deverá implementar diretamente as regras centrais do negócio.

---

## 12.4 Camada de Apresentação

A camada de apresentação será responsável pela interação com o usuário.

Suas responsabilidades incluirão:

* Exibição das telas;
* Formulários;
* Tabelas;
* Dashboards;
* Mensagens;
* Validações visuais;
* Navegação;
* Exibição de status.

A camada de apresentação não deverá conter regras complexas de negócio.

Por exemplo, a interface não deverá ser responsável diretamente por decidir qual compra deve ser consumida pelo FIFO.

Essa decisão deverá pertencer à camada responsável pelas regras de negócio.

---

## 12.5 Camada de Aplicação

A camada de aplicação será responsável por coordenar os casos de uso do sistema.

Exemplos de casos de uso:

* Registrar compra;
* Registrar saída;
* Registrar devolução;
* Registrar remessa;
* Registrar transferência;
* Cancelar operação;
* Corrigir lançamento;
* Consultar uma Nota Fiscal de compra.

Essa camada deverá:

1. Receber a solicitação da interface;
2. Validar as condições necessárias;
3. Acionar as regras de negócio;
4. Solicitar operações de persistência;
5. Registrar operações de auditoria quando aplicável;
6. Retornar o resultado para a interface.

---

## 12.6 Camada de Domínio

A camada de domínio deverá concentrar as principais regras de negócio do SIGC.

Exemplos de regras:

* FIFO;
* Controle de quantidades;
* Devolução parcial;
* Bloqueio de excesso;
* Controle de prazos;
* Classificação de status;
* Rastreabilidade;
* Reversão de operações.

Essa camada deverá ser independente da interface visual.

O objetivo é permitir que as regras do SIGC continuem válidas mesmo que a interface seja alterada futuramente.

---

## 12.7 Camada de Infraestrutura

A camada de infraestrutura será responsável pelos recursos externos utilizados pelo sistema.

Incluem-se:

* Banco de dados;
* Sistema de arquivos;
* Backups;
* Configurações;
* Logs técnicos;
* Comunicação com recursos necessários para execução.

Essa camada deverá fornecer os recursos necessários para as demais camadas sem expor detalhes técnicos desnecessários.

---

## 12.8 Servidor Central

O servidor central deverá executar os componentes responsáveis pelo funcionamento central do SIGC.

Inicialmente, deverá conter:

* API do SIGC;
* Banco de dados;
* Arquivos de configuração;
* Sistema de logs;
* Estrutura de backups ou integração com a política de backup existente.

O servidor deverá permanecer disponível durante o período de utilização do sistema.

---

## 12.9 Comunicação entre Cliente e API

A aplicação cliente deverá se comunicar com a API do SIGC por meio da rede interna.

A API será responsável por:

1. Receber a solicitação;
2. Validar a autenticação;
3. Validar as permissões;
4. Executar as regras de negócio;
5. Consultar ou alterar os dados;
6. Registrar a auditoria quando aplicável;
7. Retornar o resultado ao cliente.

O fluxo geral será:

```text
Usuário
   ↓
Aplicação Cliente
   ↓
Solicitação
   ↓
API SIGC
   ↓
Autenticação e Permissões
   ↓
Regras de Negócio
   ↓
Banco de Dados
   ↓
Resposta
   ↓
Aplicação Cliente
   ↓
Usuário
```

---

## 12.10 Acesso ao Banco de Dados

Somente a API do SIGC deverá acessar diretamente o banco de dados.

Os computadores dos usuários não deverão possuir acesso direto ao arquivo do banco.

Essa regra deverá ser mantida para preservar:

* A integridade dos dados;
* A segurança das informações;
* O controle das operações;
* A consistência das regras de negócio.

---

## 12.11 Acesso ao Banco de Dados por Repositórios

O acesso ao banco de dados deverá ser separado da lógica de negócio.

A lógica de negócio não deverá executar diretamente comandos SQL espalhados pelo código.

O acesso deverá ser centralizado em componentes específicos.

Exemplo conceitual:

```text
Serviço de Compras
       ↓
Repositório de Compras
       ↓
Banco de Dados
```

---

## 12.12 Repositórios

Os repositórios deverão ser responsáveis pelas operações de persistência.

Exemplos:

* Repositório de usuários;
* Repositório de peças;
* Repositório de fornecedores;
* Repositório de contatos;
* Repositório de compras;
* Repositório de saídas;
* Repositório de devoluções;
* Repositório de remessas;
* Repositório de transferências.

Os repositórios deverão abstrair os detalhes de acesso ao banco de dados.

---

## 12.13 Serviços de Aplicação

Os serviços deverão representar operações relevantes do sistema.

Exemplos conceituais:

```text
AuthenticationService
UserService
PartService
SupplierService
PurchaseService
SaleService
CustomerReturnService
SupplierShipmentService
TransferService
AuditService
DashboardService
```

Os serviços deverão coordenar os fluxos do sistema sem concentrar responsabilidades não relacionadas.

---

## 12.14 Domínio do SIGC

O domínio deverá representar os conceitos fundamentais do sistema.

Entre os principais conceitos estão:

* Usuário;
* Perfil;
* Peça;
* Fornecedor;
* Contato;
* Compra;
* Item da compra;
* Saída;
* Origem da saída;
* Devolução do cliente;
* Remessa ao fornecedor;
* Transferência;
* Auditoria.

Esses conceitos deverão ser refletidos na estrutura interna do sistema e no modelo de dados.

---

## 12.15 Fluxo de uma Operação

Uma operação deverá seguir, conceitualmente, o seguinte fluxo:

```text
Usuário
   ↓
Interface
   ↓
Caso de Uso
   ↓
Regras de Negócio
   ↓
Repositório
   ↓
Banco de Dados
   ↓
Auditoria
   ↓
Resposta ao Usuário
```

Exemplo de uma devolução:

```text
Vendedor registra devolução
          ↓
Tela recebe os dados
          ↓
Solicitação enviada à API
          ↓
API valida o usuário
          ↓
API verifica as permissões
          ↓
Serviço de devolução é acionado
          ↓
Sistema verifica a quantidade pendente
          ↓
Sistema aplica FIFO
          ↓
Sistema atualiza os registros
          ↓
Sistema registra a auditoria
          ↓
Resultado é retornado ao cliente
          ↓
Resultado é exibido ao usuário
```

---

## 12.16 Transações

Operações que envolvam múltiplas alterações relacionadas deverão utilizar transações de banco de dados.

Exemplo de uma saída:

```text
1. Registrar a saída;
2. Identificar as compras de origem;
3. Consumir a quantidade seguindo FIFO;
4. Registrar os vínculos de origem;
5. Atualizar os saldos;
6. Registrar a auditoria.
```

Essas operações deverão ser tratadas como uma unidade lógica.

Caso uma etapa essencial falhe, o sistema deverá evitar que apenas parte da operação seja persistida.

---

## 12.17 Tratamento de Erros

Os erros deverão ser tratados em camadas apropriadas.

A aplicação deverá:

* Evitar expor detalhes técnicos desnecessários ao usuário;
* Apresentar mensagens claras;
* Registrar informações técnicas quando necessário;
* Evitar deixar dados parcialmente alterados;
* Permitir a identificação de falhas para manutenção.

---

## 12.18 Configuração

As configurações do sistema deverão ser separadas do código sempre que possível.

Poderão incluir:

* Endereço da API;
* Porta de comunicação;
* Caminhos de arquivos;
* Caminho de backups;
* Configurações de execução;
* Parâmetros do sistema.

Informações sensíveis não deverão ser armazenadas diretamente no código-fonte.

---

## 12.19 Distribuição da Aplicação Cliente

A aplicação cliente deverá ser preparada para ser distribuída como um programa executável no ambiente Windows.

A distribuição deverá considerar:

* Arquivos necessários para execução;
* Dependências;
* Configurações;
* Comunicação com a API;
* Atualizações futuras.

A aplicação cliente deverá ser instalada ou disponibilizada nos computadores autorizados da empresa.

---

## 12.20 Execução da API

A API do SIGC deverá ser executada no servidor central da rede interna.

A API deverá:

* Permanecer disponível durante o horário de utilização;
* Ser iniciada de forma controlada;
* Possuir configuração documentada;
* Permitir monitoramento básico de sua disponibilidade;
* Ser protegida contra alterações indevidas.

---

## 12.21 Concorrência

A arquitetura deverá permitir que múltiplos usuários utilizem o sistema simultaneamente.

As operações críticas deverão ser processadas centralmente pela API, reduzindo o risco de conflitos entre operações simultâneas.

Operações relacionadas a quantidades, FIFO, devoluções, remessas e saldos deverão possuir tratamento adequado de concorrência.

---

## 12.22 Disponibilidade

A disponibilidade do SIGC dependerá da disponibilidade do servidor central e da rede interna.

Caso o servidor esteja indisponível, a aplicação cliente deverá informar claramente ao usuário que não foi possível estabelecer comunicação com o serviço.

O sistema não deverá realizar alterações locais não sincronizadas que possam gerar inconsistências com o banco de dados central.

---

## 12.23 Banco de Dados Inicial

A versão inicial do SIGC deverá utilizar SQLite como banco de dados.

O arquivo do banco deverá permanecer localizado no servidor central e não deverá ser acessado diretamente pelas aplicações clientes.

A API será responsável por realizar todas as operações de leitura e escrita.

---

## 12.24 Evolução do Banco de Dados

A arquitetura deverá permitir a futura substituição do SQLite por um sistema de gerenciamento de banco de dados mais adequado ao crescimento do sistema, caso necessário.

Essa possível evolução poderá incluir bancos de dados servidor, como PostgreSQL ou outra solução adequada.

A aplicação cliente deverá permanecer desacoplada da implementação específica do banco de dados.

---

## 12.25 Segurança da Comunicação

A comunicação entre a aplicação cliente e a API deverá ser protegida de acordo com as possibilidades da infraestrutura da rede interna.

A arquitetura deverá permitir a adoção futura de mecanismos adicionais de segurança, incluindo:

* Autenticação de requisições;
* Controle de sessões;
* Tokens;
* Comunicação criptografada;
* Controle de origem das requisições.

---

## 12.26 Preparação para Múltiplas Filiais

Embora a primeira versão seja destinada a uma única filial, a arquitetura deverá ser preparada para futura expansão.

A evolução poderá incluir:

* Cadastro de filiais;
* Identificação da filial responsável;
* Transferências entre filiais;
* Controle de responsabilidades;
* Prazos específicos;
* Relatórios por filial.

A implementação inicial não deverá adicionar complexidade desnecessária que não seja necessária para a primeira versão.

---

## 12.27 Preparação para Permissões Personalizadas

Inicialmente, o sistema utilizará os perfis definidos no projeto.

Entretanto, sua estrutura deverá permitir futuramente:

* Criação de permissões personalizadas;
* Associação de permissões a usuários;
* Associação de permissões a perfis;
* Controle individual de acesso a funcionalidades.

Essa possibilidade deverá ser considerada na estrutura de autenticação e autorização.

---

## 12.28 Independência entre Interface e Regras

As regras de negócio deverão permanecer independentes da tecnologia visual utilizada.

Isso permitirá que uma futura alteração da interface não exija a reescrita das regras centrais do SIGC.

---

## 12.29 Organização das Responsabilidades

Cada componente deverá possuir uma responsabilidade clara.

O sistema deverá evitar:

* Funções gigantes;
* Classes com responsabilidades excessivas;
* SQL espalhado pela interface;
* Regras de negócio duplicadas;
* Código difícil de testar;
* Dependências desnecessárias entre módulos.

---

## 12.30 Arquitetura Inicial Recomendada

A arquitetura inicial recomendada será:

```text
SIGC
│
├── Cliente
│   ├── Interface
│   ├── Telas
│   ├── Componentes
│   ├── Dashboards
│   └── Comunicação com a API
│
├── API
│   ├── Rotas
│   ├── Autenticação
│   ├── Serviços
│   ├── Casos de uso
│   ├── Regras de negócio
│   └── Validações
│
├── Domínio
│   ├── Entidades
│   ├── Regras
│   └── Validações
│
├── Infraestrutura
│   ├── Banco de dados
│   ├── Repositórios
│   ├── Backups
│   ├── Configurações
│   └── Logs
│
└── Testes
    ├── Unitários
    ├── Integração
    └── Aceitação
```

---

## 12.31 Princípio Arquitetural

O SIGC deverá ser desenvolvido com o princípio de que:

> A interface poderá mudar, a tecnologia poderá evoluir e novos módulos poderão ser adicionados, mas as regras fundamentais de controle dos cascos deverão permanecer centralizadas, testáveis e protegidas contra duplicação.

---

## 12.32 Princípio de Evolução

A arquitetura deverá permitir a evolução gradual do SIGC sem exigir a reescrita completa do sistema.

A primeira versão deverá priorizar:

* Controle correto dos cascos;
* Integridade dos dados;
* Segurança;
* Usabilidade;
* Rastreabilidade;
* Manutenibilidade.

Funcionalidades futuras deverão ser adicionadas de forma incremental, preservando os dados e o histórico já existentes.

---

# 13. AUDITORIA E HISTÓRICO

## 13.1 Objetivo

O SIGC deverá possuir um mecanismo permanente de auditoria e histórico capaz de registrar as operações relevantes realizadas no sistema.

A auditoria tem como objetivo garantir:

* Rastreabilidade das operações;
* Identificação do usuário responsável;
* Registro de alterações;
* Registro de correções;
* Registro de cancelamentos;
* Preservação do histórico operacional;
* Apoio à investigação de divergências;
* Transparência para o Administrador Master.

Os registros de auditoria deverão ser tratados como históricos permanentes e não poderão ser apagados ou alterados pelos usuários do sistema.

---

## 13.2 Operações que deverão ser auditadas

O sistema deverá registrar, no mínimo, as seguintes operações:

### Usuários e autenticação

* Login realizado com sucesso;
* Tentativa de login malsucedida;
* Logout;
* Alteração de senha pelo próprio usuário;
* Redefinição de senha pelo Administrador Master;
* Ativação de usuário;
* Desativação de usuário;
* Alterações relevantes nos dados do usuário;
* Alterações de permissões.

### Cadastros

* Criação de peça;
* Alteração de peça;
* Desativação de peça;
* Criação de fornecedor;
* Alteração de fornecedor;
* Desativação de fornecedor;
* Criação, alteração e desativação de contatos de fornecedores;
* Alteração do prazo padrão de devolução de uma peça para determinado fornecedor.

### Compras

* Criação de uma Nota Fiscal de compra;
* Alteração de dados de uma compra;
* Cancelamento de uma compra;
* Alteração de itens ou quantidades;
* Alterações que afetem o controle de saldo ou rastreabilidade.

### Saídas

* Criação de uma saída;
* Alteração de uma saída;
* Cancelamento de uma saída;
* Alteração da quantidade de peças;
* Alteração da origem da saída entre oficina e balcão;
* Alterações que afetem o consumo das compras mais antigas.

### Devoluções de clientes

* Criação de devolução;
* Alteração de devolução;
* Cancelamento de devolução;
* Alteração de quantidade;
* Alteração de observações;
* Alterações que afetem a rastreabilidade da origem do casco.

### Devoluções ao fornecedor

* Criação de uma remessa de simples remessa;
* Alteração da remessa;
* Cancelamento da remessa;
* Alteração de quantidade;
* Alteração de nota fiscal de origem;
* Alterações que afetem a quantidade disponível para devolução.

### Transferências entre filiais

* Criação de transferência;
* Alteração de transferência;
* Cancelamento de transferência;
* Alteração da quantidade;
* Alteração da nota fiscal de transferência;
* Alteração do prazo excepcional;
* Alterações relacionadas à filial de origem.

---

## 13.3 Informações mínimas registradas

Cada registro de auditoria deverá conter, quando aplicável:

* Identificador do usuário responsável;
* Tipo da ação realizada;
* Módulo afetado;
* Tipo da entidade afetada;
* Identificador do registro afetado;
* Descrição da operação;
* Valores anteriores;
* Novos valores;
* Justificativa;
* Data e hora da operação.

A estrutura deverá permitir identificar:

> Quem realizou a operação, o que foi alterado, quando ocorreu e por qual motivo.

---

## 13.4 Correções e alterações

O sistema deverá permitir a correção de lançamentos quando necessário.

Entretanto, nenhuma correção deverá apagar silenciosamente o histórico anterior.

Quando uma operação for corrigida:

1. O registro original deverá permanecer preservado no histórico;
2. O novo valor deverá ser registrado;
3. O usuário responsável deverá ser identificado;
4. A data e hora da alteração deverão ser registradas;
5. Uma justificativa deverá ser informada;
6. O impacto da alteração sobre os saldos e relacionamentos deverá ser recalculado pelo sistema.

Exemplo:

```text
Quantidade original: 6
Quantidade corrigida: 5
Justificativa:
Quantidade informada incorretamente no lançamento original.
```

---

## 13.5 Cancelamentos

O cancelamento de uma operação não deverá resultar na exclusão física do registro.

O registro deverá permanecer no sistema com status de cancelado.

O cancelamento deverá registrar:

* Usuário responsável;
* Data e hora;
* Justificativa obrigatória;
* Operação afetada;
* Impactos decorrentes do cancelamento.

Quando necessário, o sistema deverá reverter os efeitos da operação cancelada.

Exemplo:

```text
Saída registrada:
6 unidades

Saída cancelada:
Quantidade retorna ao controle disponível,
conforme as regras de rastreabilidade do sistema.
```

---

## 13.6 Integridade do histórico

Os registros de auditoria deverão ser protegidos contra:

* Exclusão manual;
* Alteração manual;
* Modificação do usuário responsável;
* Modificação da data original;
* Alteração dos valores históricos;
* Alteração da justificativa original.

O sistema deverá permitir somente a criação de novos registros de auditoria.

A auditoria deverá funcionar de forma essencialmente append-only, ou seja:

> novos eventos podem ser adicionados, mas registros históricos não devem ser alterados ou removidos.

---

## 13.7 Auditoria de eventos automáticos

O sistema poderá registrar eventos realizados automaticamente pela aplicação.

Exemplos:

* Alteração automática de status para `ATENÇÃO`;
* Alteração automática de status para `URGENTE`;
* Alteração automática de status para `ATRASADO`;
* Consumo automático da compra mais antiga;
* Consumo automático de uma compra subsequente quando a anterior não possuir saldo suficiente;
* Reversão automática de movimentações após cancelamento ou correção.

Quando não houver um usuário diretamente responsável pela ação automática, o registro deverá identificar que a operação foi realizada pelo sistema.

---

## 13.8 Consultas simples

Consultas simples não deverão gerar registros de auditoria individualmente.

Exemplos:

* Abrir a tela de uma peça;
* Consultar um fornecedor;
* Pesquisar uma Nota Fiscal;
* Consultar o status de uma devolução.

Essa regra evita a geração de um volume desnecessário de informações e mantém a auditoria focada em eventos relevantes.

---

## 13.9 Visualização da auditoria

O Administrador Master deverá possuir acesso aos registros de auditoria.

A consulta deverá permitir, quando aplicável, filtrar por:

* Usuário;
* Data inicial;
* Data final;
* Módulo;
* Tipo de ação;
* Registro afetado;
* Tipo de operação.

O objetivo é permitir a investigação de qualquer alteração relevante realizada no sistema.

---

## 13.10 Rastreabilidade das movimentações

Além da auditoria administrativa, o SIGC deverá preservar a rastreabilidade operacional dos cascos.

A origem e o destino das peças deverão permanecer identificáveis por meio dos relacionamentos entre:

```text
Nota Fiscal de compra
        ↓
Item comprado
        ↓
Saída para cliente
        ↓
Devolução do cliente
        ↓
Remessa ao fornecedor
```

Quando houver transferência entre filiais:

```text
Origem
   ↓
Nota Fiscal de transferência
   ↓
Filial atual
   ↓
Retorno à filial de origem
```

O sistema deverá preservar a origem das quantidades movimentadas sempre que possível.

---

## 13.11 Histórico permanente

O SIGC não deverá apagar fisicamente registros que possuam histórico operacional.

Isso se aplica especialmente a:

* Usuários;
* Peças;
* Fornecedores;
* Contatos;
* Compras;
* Saídas;
* Devoluções;
* Transferências;
* Movimentações;
* Registros de auditoria.

Quando uma entidade deixar de ser utilizada, deverá ser preferencialmente desativada ou cancelada conforme a natureza do registro.

Essa abordagem preserva a integridade histórica e evita que operações antigas percam suas referências.

---

## 13.12 Regras de Negócio relacionadas

### RN-094 — Registro de auditoria

Toda operação relevante realizada no SIGC deverá gerar um registro de auditoria.

### RN-095 — Identificação do usuário

O sistema deverá registrar o usuário responsável por cada operação realizada por um usuário autenticado.

### RN-096 — Registro de alterações

Alterações relevantes deverão preservar os valores anteriores e registrar os novos valores quando aplicável.

### RN-097 — Justificativa obrigatória

Correções e cancelamentos deverão exigir uma justificativa antes de serem concluídos.

### RN-098 — Histórico permanente

Registros de auditoria não poderão ser excluídos ou alterados pelos usuários.

### RN-099 — Cancelamento sem exclusão física

O cancelamento de uma operação não deverá apagar fisicamente o registro original.

### RN-100 — Reversão de efeitos

Correções e cancelamentos deverão ajustar os efeitos operacionais da operação conforme as regras de negócio do SIGC.

### RN-101 — Auditoria de eventos automáticos

Eventos automáticos relevantes realizados pelo sistema poderão ser registrados na auditoria.

### RN-102 — Consultas simples

Consultas simples não deverão gerar registros individuais de auditoria, salvo se posteriormente houver necessidade específica definida em uma evolução do sistema.

### RN-103 — Rastreabilidade operacional

O sistema deverá preservar a rastreabilidade das movimentações de cascos desde sua origem até sua devolução ao fornecedor ou transferência entre filiais.

### RN-104 — Preservação de referências

Registros com histórico operacional não deverão ser excluídos de forma que cause a perda de referências históricas.

### RN-105 — Acesso à auditoria

A consulta completa dos registros de auditoria deverá ser restrita aos usuários que possuírem a permissão correspondente.

### RN-106 — Integridade da auditoria

O sistema deverá impedir alterações manuais nos dados históricos originais dos registros de auditoria.

---

# 14. BACKUP E RECUPERAÇÃO DE DADOS

## 14.1 Objetivo

O SIGC deverá possuir uma estratégia de backup e recuperação capaz de preservar os dados operacionais e históricos do sistema.

A estratégia deverá considerar a separação entre:

* Ambiente de desenvolvimento;
* Ambiente de produção.

O objetivo principal é evitar a perda de dados, permitir a recuperação após falhas e preservar o histórico operacional da empresa.

---

## 14.2 Separação entre desenvolvimento e produção

O ambiente de desenvolvimento será utilizado inicialmente no computador do desenvolvedor.

Esse ambiente poderá conter dados fictícios ou dados utilizados exclusivamente para testes.

O ambiente de produção será executado posteriormente no servidor Windows da empresa e conterá os dados reais do SIGC.

Os ambientes deverão utilizar configurações e bancos de dados separados.

Exemplo:

```text
Ambiente de desenvolvimento:
sigc_dev.db

Ambiente de produção:
sigc_prod.db
```

O banco de dados de desenvolvimento nunca deverá substituir diretamente o banco de dados de produção.

---

## 14.3 Banco de dados de produção

O banco de dados de produção deverá ser mantido no servidor oficial da empresa.

Os computadores dos usuários não deverão acessar diretamente o arquivo físico do banco de dados.

O acesso deverá ocorrer por meio da aplicação SIGC:

```text
Computador do usuário
        ↓
Navegador
        ↓
Aplicação SIGC no servidor
        ↓
Banco de dados de produção
```

Essa arquitetura permite centralizar:

* Controle de acesso;
* Regras de negócio;
* Auditoria;
* Validações;
* Operações de banco de dados.

---

## 14.4 Backups do ambiente de desenvolvimento

O ambiente de desenvolvimento poderá utilizar backups locais para evitar a perda do trabalho realizado.

Esses backups não deverão ser considerados backups oficiais dos dados da empresa.

Os dados utilizados no desenvolvimento deverão ser preferencialmente fictícios ou anonimizados.

---

## 14.5 Backups do ambiente de produção

O ambiente de produção deverá possuir backups independentes do banco de dados oficial.

Os backups deverão:

* Ser realizados em local separado do banco principal;
* Preservar múltiplas versões quando possível;
* Possuir identificação de data e hora;
* Ser protegidos contra alterações indevidas;
* Ser submetidos a verificações de integridade quando aplicável.

Exemplo:

```text
SIGC/
├── database/
│   └── sigc_prod.db
│
└── backups/
    ├── sigc_prod_2026-07-23_080000.db
    ├── sigc_prod_2026-07-24_080000.db
    └── sigc_prod_2026-07-25_080000.db
```

---

## 14.6 Política de backup

O SIGC deverá possuir uma estratégia própria de backup, que posteriormente poderá ser integrada à política geral de backup da empresa.

A frequência e o período de retenção deverão ser definidos conforme a infraestrutura disponível e a política oficial da empresa.

O sistema deverá ser projetado para permitir a evolução futura da estratégia de backup sem alteração das regras de negócio.

---

## 14.7 Backup antes de operações críticas

Antes de operações potencialmente destrutivas ou de alto impacto, deverá ser considerado um backup preventivo.

Exemplos:

* Restauração de banco de dados;
* Migração de estrutura;
* Alterações estruturais importantes;
* Atualizações críticas da aplicação.

---

## 14.8 Recuperação de dados

A recuperação de um backup deverá ser uma operação controlada.

Sempre que possível, antes da restauração, o sistema deverá:

1. Preservar uma cópia do banco de dados atual;
2. Validar o arquivo de backup;
3. Confirmar a operação;
4. Registrar a restauração na auditoria.

A restauração não deverá ocorrer de forma silenciosa.

---

## 14.9 Preservação do histórico

A recuperação de um backup deverá considerar a preservação dos dados históricos existentes no momento correspondente ao backup.

Os registros de:

* Compras;
* Saídas;
* Devoluções;
* Transferências;
* Movimentações;
* Auditoria;

deverão ser preservados conforme o conteúdo do backup restaurado.

---

## 14.10 Migração futura do banco de dados

O SIGC deverá ser desenvolvido de forma a permitir uma futura migração do SQLite para um banco de dados cliente-servidor, como PostgreSQL ou outra tecnologia adequada.

A migração futura deverá preservar, quando tecnicamente possível:

* Dados operacionais;
* Histórico;
* Auditoria;
* Relacionamentos;
* Identificadores;
* Integridade dos registros.

A aplicação deverá evitar dependência excessiva de características exclusivas do SQLite quando isso dificultar uma futura migração.

---

## 14.11 Regras de Negócio relacionadas

### RN-107 — Separação de ambientes

Os ambientes de desenvolvimento e produção deverão utilizar bancos de dados separados.

### RN-108 — Proteção do banco de produção

O banco de dados de produção não deverá ser substituído diretamente pelo banco de desenvolvimento.

### RN-109 — Acesso centralizado

Os usuários não deverão acessar diretamente o arquivo físico do banco de dados de produção.

### RN-110 — Backup de produção

O ambiente de produção deverá possuir uma estratégia de backup independente do banco de dados principal.

### RN-111 — Preservação de versões

Sempre que possível, os backups deverão preservar múltiplas versões do banco de dados.

### RN-112 — Recuperação controlada

A restauração de um backup deverá ser realizada de forma controlada e registrada quando aplicável.

### RN-113 — Preservação histórica

A estratégia de backup e recuperação deverá preservar os dados históricos existentes no momento do backup.

### RN-114 — Migração futura

A arquitetura deverá permitir a futura migração do banco de dados para uma solução cliente-servidor sem perda intencional dos dados históricos.

---

# 15. ARQUITETURA TÉCNICA

## 15.1 Objetivo

A arquitetura técnica do SIGC deverá fornecer uma estrutura organizada, segura, modular e preparada para evolução futura.

O sistema deverá ser desenvolvido de forma que:

* As regras de negócio não dependam diretamente da interface;
* O banco de dados não seja acessado diretamente pelos usuários;
* O código seja organizado em camadas;
* O ambiente de desenvolvimento seja separado do ambiente de produção;
* O sistema possa ser transferido do computador de desenvolvimento para o servidor da empresa;
* A aplicação possa evoluir futuramente para uma arquitetura mais robusta sem necessidade de reescrever integralmente as regras de negócio.

---

## 15.2 Arquitetura geral

O SIGC será inicialmente desenvolvido como uma aplicação web interna.

A arquitetura geral será:

```text
┌──────────────────────────────┐
│      COMPUTADORES USUÁRIOS   │
│                              │
│  Navegador Web               │
│  Usuário 1                   │
│  Usuário 2                   │
│  Usuário 3                   │
│  Usuário 4                   │
└──────────────┬───────────────┘
               │
               │ Rede interna
               ▼
┌──────────────────────────────┐
│      SERVIDOR WINDOWS        │
│                              │
│  Aplicação SIGC              │
│  Python                      │
│  FastAPI                     │
│  SQLAlchemy                  │
│                              │
│  Camada de Interface         │
│  Camada de Serviços          │
│  Regras de Negócio           │
│  Repositórios                │
│                              │
│  Banco SQLite                │
│  Backups                     │
└──────────────────────────────┘
```

---

## 15.3 Ambiente de desenvolvimento

Inicialmente, o sistema será desenvolvido e testado localmente em um único computador.

O ambiente de desenvolvimento será utilizado para:

* Criar funcionalidades;
* Executar testes;
* Corrigir erros;
* Validar regras de negócio;
* Utilizar dados fictícios;
* Preparar novas versões.

A estrutura inicial será:

```text
Computador do desenvolvedor
        │
        ├── Código do SIGC
        ├── Banco de desenvolvimento
        ├── Testes
        └── Backups de desenvolvimento
```

O banco de desenvolvimento deverá ser separado do banco de produção.

---

## 15.4 Ambiente de produção

Quando o acesso ao servidor da empresa estiver disponível, o SIGC será implantado no servidor Windows.

O ambiente de produção será responsável por:

* Executar a aplicação oficial;
* Armazenar o banco de dados real;
* Atender os usuários da empresa;
* Executar os processos de backup;
* Preservar o histórico operacional.

A estrutura será:

```text
Servidor Windows
        │
        ├── Aplicação SIGC
        ├── Banco de produção
        └── Backups
```

---

## 15.5 Execução da aplicação

A aplicação deverá funcionar como um serviço web interno.

O servidor deverá executar a aplicação SIGC e disponibilizá-la para os computadores conectados à rede interna.

O fluxo será:

```text
Usuário
   ↓
Navegador
   ↓
Rede interna
   ↓
Servidor Windows
   ↓
Aplicação SIGC
   ↓
Banco de dados
```

A aplicação deverá ser configurada para permanecer disponível enquanto o servidor estiver em funcionamento.

Sempre que tecnicamente possível, a inicialização da aplicação deverá ser automatizada junto à inicialização do ambiente de produção.

---

## 15.6 Camadas da aplicação

A aplicação deverá ser organizada em camadas.

### 15.6.1 Camada de apresentação

Responsável por:

* Páginas;
* Formulários;
* Tabelas;
* Botões;
* Mensagens;
* Validações visuais;
* Navegação.

Essa camada não deverá conter regras complexas de negócio.

---

### 15.6.2 Camada de serviços

Responsável por executar casos de uso do sistema.

Exemplos:

* Registrar compra;
* Registrar saída;
* Registrar devolução;
* Registrar transferência;
* Corrigir lançamento;
* Cancelar operação;
* Consultar histórico.

Essa camada deverá coordenar as operações entre a interface e as regras de negócio.

---

### 15.6.3 Camada de regras de negócio

Responsável pelas regras específicas do SIGC.

Exemplos:

* Controle de saldo;
* Consumo da compra mais antiga;
* Controle de devoluções;
* Validação de quantidades;
* Controle de prazos;
* Permissões;
* Rastreabilidade;
* Auditoria.

As regras de negócio deverão permanecer independentes da interface sempre que possível.

---

### 15.6.4 Camada de repositórios

Responsável pelo acesso ao banco de dados.

Essa camada deverá:

* Consultar dados;
* Inserir registros;
* Atualizar registros permitidos;
* Executar transações;
* Recuperar informações.

A interface não deverá executar comandos SQL diretamente.

---

### 15.6.5 Camada de modelos

Responsável por representar as entidades do sistema.

Exemplos:

* Usuário;
* Peça;
* Fornecedor;
* Compra;
* Saída;
* Devolução;
* Transferência;
* Auditoria.

---

## 15.7 Fluxo de uma operação

Uma operação deverá seguir, preferencialmente, o seguinte fluxo:

```text
Usuário
   ↓
Interface
   ↓
Rota / Controlador
   ↓
Serviço
   ↓
Regra de negócio
   ↓
Repositório
   ↓
Banco de dados
```

Exemplo:

```text
Usuário registra saída
        ↓
Sistema recebe os dados
        ↓
Valida a operação
        ↓
Verifica saldo disponível
        ↓
Aplica regra FIFO
        ↓
Registra a saída
        ↓
Atualiza os saldos
        ↓
Registra auditoria
        ↓
Retorna confirmação
```

---

## 15.8 Controle de configuração

As configurações da aplicação deverão ser separadas do código sempre que possível.

A aplicação deverá ser capaz de diferenciar ambientes.

Exemplo:

```text
development
    ↓
sigc_dev.db

production
    ↓
sigc_prod.db
```

Informações sensíveis não deverão ser armazenadas diretamente no código-fonte.

---

## 15.9 Controle de acesso ao banco

Os usuários não deverão acessar diretamente o arquivo físico do banco de dados.

O acesso deverá ocorrer exclusivamente através da aplicação SIGC.

```text
❌ Usuário
   ↓
   sigc_prod.db

✅ Usuário
   ↓
   SIGC
   ↓
   sigc_prod.db
```

---

## 15.10 Evolução futura

A arquitetura deverá permitir futuras evoluções, como:

* Migração do SQLite para PostgreSQL;
* Acesso remoto seguro;
* Expansão para outras filiais;
* Integração com e-mail;
* Integração com outros sistemas;
* Criação de APIs;
* Ampliação do controle de permissões;
* Relatórios avançados.

A expansão futura não deverá exigir a reescrita completa das regras de negócio existentes.

---

## 15.11 Possibilidade de expansão para múltiplas filiais

O escopo inicial será limitado a uma única filial.

Entretanto, a arquitetura deverá evitar decisões que impeçam a expansão futura.

A implementação inicial não deverá adicionar complexidade desnecessária relacionada a múltiplas filiais.

A expansão deverá ser realizada futuramente mediante alteração planejada da arquitetura e da estrutura do banco de dados.

---

## 15.12 Segurança da arquitetura

A aplicação deverá adotar, no mínimo:

* Autenticação de usuários;
* Senhas armazenadas de forma segura;
* Controle de permissões;
* Validação de dados;
* Controle de sessão;
* Auditoria;
* Separação entre ambientes;
* Proteção do banco de produção.

A aplicação não deverá confiar exclusivamente nas validações realizadas pelo navegador.

As regras críticas deverão ser validadas no servidor.

---

## 15.13 Regras de Negócio relacionadas

### RN-115 — Aplicação centralizada

O SIGC deverá funcionar inicialmente como uma aplicação centralizada no servidor de produção.

### RN-116 — Acesso por navegador

Os usuários deverão acessar o SIGC por meio de um navegador conectado à rede interna.

### RN-117 — Separação entre ambientes

O ambiente de desenvolvimento deverá permanecer separado do ambiente de produção.

### RN-118 — Banco de produção

O banco de dados de produção deverá permanecer no ambiente oficial do servidor da empresa.

### RN-119 — Acesso intermediado

Os usuários não deverão acessar diretamente o arquivo físico do banco de dados.

### RN-120 — Separação de responsabilidades

A aplicação deverá separar, sempre que possível, apresentação, serviços, regras de negócio e persistência.

### RN-121 — Validação no servidor

Regras críticas deverão ser validadas no servidor, independentemente das validações realizadas na interface.

### RN-122 — Inicialização da aplicação

A aplicação deverá ser configurada para permanecer disponível enquanto o servidor de produção estiver em funcionamento.

### RN-123 — Evolução tecnológica

A arquitetura deverá permitir futuras evoluções tecnológicas sem necessidade de reescrita integral das regras de negócio.

### RN-124 — Escopo inicial

A primeira versão do SIGC deverá operar com uma única filial.

### RN-125 — Expansão futura

A arquitetura deverá permitir futura expansão para outras filiais mediante evolução planejada do sistema.

### RN-126 — Proteção de configurações

Informações sensíveis e configurações específicas do ambiente não deverão ser armazenadas diretamente no código-fonte quando isso representar risco de segurança.

### RN-127 — Separação de dados

Dados de desenvolvimento e dados de produção deverão permanecer separados.

### RN-128 — Integridade arquitetural

Novas funcionalidades deverão respeitar a separação entre interface, serviços, regras de negócio e persistência.

---

## 15.14 Tecnologias principais da aplicação

A primeira versão do SIGC utilizará as seguintes tecnologias principais:

| Componente             | Tecnologia |
| ---------------------- | ---------- |
| Linguagem principal    | Python     |
| Framework web          | FastAPI    |
| Persistência e ORM     | SQLAlchemy |
| Banco de dados inicial | SQLite     |
| Controle de versão     | Git        |
| Repositório remoto     | GitHub     |

A arquitetura deverá manter separadas as responsabilidades da aplicação, permitindo a evolução futura das tecnologias sem necessidade de reescrever integralmente as regras de negócio.

---

# 16. BANCO DE DADOS

## 16.1 Tecnologia

O banco de dados inicial do SIGC será o SQLite.

O SQLite será utilizado inicialmente devido à sua simplicidade de implantação, baixo custo operacional e adequação ao ambiente inicial do sistema.

O banco será acessado exclusivamente pela aplicação SIGC.

Os usuários não deverão acessar diretamente o arquivo físico do banco de dados.

O sistema deverá ser desenvolvido de forma a permitir futura migração para um banco de dados cliente-servidor, como PostgreSQL, sem necessidade de reescrever integralmente as regras de negócio.

---

## 16.2 Princípios do banco de dados

O banco deverá priorizar:

* Integridade dos dados;
* Preservação do histórico;
* Rastreabilidade;
* Controle de relacionamentos;
* Auditoria;
* Não exclusão destrutiva;
* Consistência das quantidades;
* Controle de transações;
* Possibilidade de evolução futura.

Os registros que possuírem histórico operacional não deverão ser apagados fisicamente.

Quando um cadastro deixar de ser utilizado, deverá ser preferencialmente desativado.

---

# 16.3 Convenções gerais

As tabelas deverão utilizar nomes em inglês e em `snake_case`.

Exemplo:

```text
purchase_items
supplier_contacts
audit_logs
```

Os identificadores internos deverão ser gerados pelo sistema.

As datas deverão ser armazenadas em formato compatível com ISO 8601.

Exemplo:

```text
2026-07-23 14:30:00
```

Embora o SQLite não possua um tipo `DATE` ou `DATETIME` rígido como outros bancos relacionais, o formato ISO 8601 permite:

* Ordenação correta;
* Comparações;
* Cálculos;
* Filtragem por período;
* Migração futura para outros bancos.

---

# 16.4 Tabela `users`

Armazena os usuários do sistema.

| Campo           | Tipo    | Descrição                           |
| --------------- | ------- | ----------------------------------- |
| `id`            | INTEGER | Identificador interno               |
| `full_name`     | TEXT    | Nome completo                       |
| `username`      | TEXT    | Login único                         |
| `email`         | TEXT    | E-mail cadastrado                   |
| `password_hash` | TEXT    | Senha armazenada de forma protegida |
| `role_id`       | INTEGER | Perfil de acesso                    |
| `is_active`     | INTEGER | Indica se o usuário está ativo      |
| `last_login_at` | TEXT    | Último acesso                       |
| `created_at`    | TEXT    | Data de criação                     |
| `updated_at`    | TEXT    | Última alteração                    |

Usuários que já tenham realizado operações não deverão ser excluídos fisicamente.

Quando necessário, deverão ser desativados.

---

# 16.5 Tabela `roles`

Armazena os perfis de acesso do sistema.

Inicialmente serão utilizados:

* Administrador Master;
* Vendedor;
* Comprador.

O sistema deverá permitir futura expansão para permissões personalizadas.

| Campo         | Tipo    | Descrição             |
| ------------- | ------- | --------------------- |
| `id`          | INTEGER | Identificador interno |
| `name`        | TEXT    | Nome do perfil        |
| `description` | TEXT    | Descrição             |
| `created_at`  | TEXT    | Data de criação       |

Os vendedores de oficina e balcão possuem o mesmo perfil de permissões.

A diferença entre oficina e balcão ocorre no momento do registro da saída.

---

# 16.6 Tabela `permissions`

Armazena permissões individuais.

| Campo         | Tipo    | Descrição           |
| ------------- | ------- | ------------------- |
| `id`          | INTEGER | Identificador       |
| `code`        | TEXT    | Código da permissão |
| `name`        | TEXT    | Nome da permissão   |
| `description` | TEXT    | Descrição           |

Exemplos:

```text
purchase.create
outbound.create
customer_return.create
supplier_return.create
audit.view
user.manage
```

---

# 16.7 Tabela `role_permissions`

Relaciona perfis às permissões.

| Campo           | Tipo    | Descrição |
| --------------- | ------- | --------- |
| `role_id`       | INTEGER | Perfil    |
| `permission_id` | INTEGER | Permissão |

Essa estrutura permitirá futuramente que o Administrador Master crie permissões personalizadas.

---

# 16.8 Tabela `parts`

Armazena as peças controladas pelo SIGC.

| Campo         | Tipo    | Descrição             |
| ------------- | ------- | --------------------- |
| `id`          | INTEGER | Identificador interno |
| `part_code`   | TEXT    | Código da peça        |
| `name`        | TEXT    | Nome da peça          |
| `description` | TEXT    | Descrição             |
| `is_active`   | INTEGER | Status do cadastro    |
| `created_at`  | TEXT    | Data de criação       |
| `updated_at`  | TEXT    | Última alteração      |

A quantidade disponível não deverá ser tratada como uma informação isolada e sem histórico.

O saldo deverá ser obtido considerando as movimentações registradas.

---

# 16.9 Tabela `suppliers`

Armazena os fornecedores.

| Campo        | Tipo    | Descrição            |
| ------------ | ------- | -------------------- |
| `id`         | INTEGER | Identificador        |
| `name`       | TEXT    | Nome ou razão social |
| `document`   | TEXT    | Documento            |
| `address`    | TEXT    | Endereço             |
| `notes`      | TEXT    | Observações          |
| `is_active`  | INTEGER | Status               |
| `created_at` | TEXT    | Data de criação      |
| `updated_at` | TEXT    | Última alteração     |

Fornecedores com histórico não deverão ser excluídos fisicamente.

---

# 16.10 Tabela `supplier_contacts`

Permite múltiplos contatos por fornecedor.

| Campo         | Tipo    | Descrição         |
| ------------- | ------- | ----------------- |
| `id`          | INTEGER | Identificador     |
| `supplier_id` | INTEGER | Fornecedor        |
| `name`        | TEXT    | Nome do contato   |
| `email`       | TEXT    | E-mail            |
| `phone`       | TEXT    | Telefone          |
| `position`    | TEXT    | Cargo ou função   |
| `is_primary`  | INTEGER | Contato principal |
| `is_active`   | INTEGER | Status            |
| `created_at`  | TEXT    | Data de criação   |

Um fornecedor poderá possuir mais de um contato.

---

# 16.11 Tabela `purchases`

Representa uma Nota Fiscal de compra.

| Campo            | Tipo    | Descrição             |
| ---------------- | ------- | --------------------- |
| `id`             | INTEGER | Identificador interno |
| `supplier_id`    | INTEGER | Fornecedor            |
| `invoice_number` | TEXT    | Número da NF          |
| `invoice_series` | TEXT    | Série                 |
| `issue_date`     | TEXT    | Data de emissão       |
| `received_at`    | TEXT    | Data de recebimento   |
| `notes`          | TEXT    | Observações           |
| `created_by`     | INTEGER | Usuário responsável   |
| `created_at`     | TEXT    | Data do lançamento    |
| `updated_at`     | TEXT    | Última alteração      |
| `status`         | TEXT    | Status da compra      |

A Nota Fiscal de compra poderá conter vários itens diferentes.

---

# 16.12 Tabela `purchase_items`

Representa os itens de uma compra.

| Campo                | Tipo    | Descrição             |
| -------------------- | ------- | --------------------- |
| `id`                 | INTEGER | Identificador         |
| `purchase_id`        | INTEGER | Compra                |
| `part_id`            | INTEGER | Peça                  |
| `quantity_purchased` | INTEGER | Quantidade comprada   |
| `quantity_available` | INTEGER | Quantidade disponível |
| `created_at`         | TEXT    | Data de criação       |

A quantidade disponível deverá ser controlada pelo sistema.

A utilização de uma quantidade deverá respeitar a rastreabilidade da compra de origem.

---

# 16.13 Tabela `outbounds`

Representa uma saída de peças.

A saída deverá indicar se foi realizada para:

```text
WORKSHOP
```

ou:

```text
COUNTER
```

| Campo                  | Tipo    | Descrição           |
| ---------------------- | ------- | ------------------- |
| `id`                   | INTEGER | Identificador       |
| `destination_type`     | TEXT    | Oficina ou balcão   |
| `work_order_number`    | TEXT    | Número da OS        |
| `sales_invoice_number` | TEXT    | Número da nota      |
| `created_by`           | INTEGER | Usuário responsável |
| `created_at`           | TEXT    | Data                |
| `updated_at`           | TEXT    | Última alteração    |
| `status`               | TEXT    | Status              |

Quando a saída for para a oficina, deverá ser informado o número da OS.

Quando a saída for para o balcão, deverá ser informado o número da nota correspondente.

O sistema deverá liberar somente o campo correspondente ao tipo de saída selecionado.

---

# 16.14 Tabela `outbound_items`

Representa os itens de uma saída.

| Campo         | Tipo    | Descrição     |
| ------------- | ------- | ------------- |
| `id`          | INTEGER | Identificador |
| `outbound_id` | INTEGER | Saída         |
| `part_id`     | INTEGER | Peça          |
| `quantity`    | INTEGER | Quantidade    |
| `created_at`  | TEXT    | Data          |

Uma saída poderá conter várias peças diferentes.

---

# 16.15 Tabela `outbound_purchase_allocations`

Relaciona uma saída às compras consumidas.

Essa tabela é necessária para implementar o consumo da compra mais antiga.

| Campo                | Tipo    | Descrição            |
| -------------------- | ------- | -------------------- |
| `id`                 | INTEGER | Identificador        |
| `outbound_item_id`   | INTEGER | Item da saída        |
| `purchase_item_id`   | INTEGER | Item da compra       |
| `quantity_allocated` | INTEGER | Quantidade consumida |

Exemplo:

```text
Compra A:
10 unidades

Saída:
15 unidades

Resultado:

Compra A → 10 unidades
Compra B → 5 unidades
```

O sistema deverá consumir automaticamente a próxima compra quando o saldo da compra mais antiga não for suficiente.

---

# 16.16 Tabela `customer_returns`

Representa uma devolução realizada por um cliente.

A devolução poderá ser realizada por:

* Vendedor;
* Comprador.

O comprador poderá registrar devoluções tanto relacionadas à oficina quanto ao balcão.

| Campo              | Tipo    | Descrição              |
| ------------------ | ------- | ---------------------- |
| `id`               | INTEGER | Identificador          |
| `return_type`      | TEXT    | Oficina ou balcão      |
| `reference_number` | TEXT    | OS ou nota relacionada |
| `customer_name`    | TEXT    | Cliente                |
| `created_by`       | INTEGER | Usuário responsável    |
| `created_at`       | TEXT    | Data                   |
| `updated_at`       | TEXT    | Última alteração       |
| `status`           | TEXT    | Status                 |
| `notes`            | TEXT    | Observações            |

A devolução deverá possuir histórico completo.

---

# 16.17 Tabela `customer_return_items`

Representa os itens devolvidos pelo cliente.

| Campo                | Tipo    | Descrição            |
| -------------------- | ------- | -------------------- |
| `id`                 | INTEGER | Identificador        |
| `customer_return_id` | INTEGER | Devolução            |
| `part_id`            | INTEGER | Peça                 |
| `quantity`           | INTEGER | Quantidade devolvida |

O sistema deverá bloquear a devolução quando a quantidade devolvida for superior à quantidade vendida ou registrada como saída.

---

# 16.18 Tabela `customer_return_allocations`

Relaciona a devolução às saídas de origem.

| Campo                     | Tipo    | Descrição              |
| ------------------------- | ------- | ---------------------- |
| `id`                      | INTEGER | Identificador          |
| `customer_return_item_id` | INTEGER | Item devolvido         |
| `outbound_item_id`        | INTEGER | Item da saída          |
| `quantity_allocated`      | INTEGER | Quantidade relacionada |

Essa tabela permite rastrear a origem da devolução.

---

# 16.19 Tabela `supplier_returns`

Representa uma devolução ao fornecedor.

O documento utilizado será uma Nota Fiscal de simples remessa emitida pela própria empresa.

A remessa deverá conter:

* Peças;
* Quantidades;
* Nota Fiscal de origem.

Uma única remessa poderá conter vários itens diferentes da mesma Nota Fiscal de compra.

Também será possível realizar devoluções parciais de uma Nota Fiscal de compra.

| Campo                     | Tipo    | Descrição                       |
| ------------------------- | ------- | ------------------------------- |
| `id`                      | INTEGER | Identificador                   |
| `supplier_id`             | INTEGER | Fornecedor                      |
| `dispatch_invoice_number` | TEXT    | Número da NF de simples remessa |
| `dispatch_invoice_series` | TEXT    | Série                           |
| `issue_date`              | TEXT    | Data                            |
| `created_by`              | INTEGER | Usuário                         |
| `created_at`              | TEXT    | Data do registro                |
| `updated_at`              | TEXT    | Última alteração                |
| `status`                  | TEXT    | Status                          |
| `notes`                   | TEXT    | Observações                     |

Uma remessa deverá pertencer a um único fornecedor.

A Nota Fiscal de Simples Remessa será o documento emitido pela empresa para
formalizar o envio dos cascos ao fornecedor.

Uma remessa poderá ser realizada parcialmente.

Todos os itens de uma mesma remessa deverão possuir origem na mesma Nota Fiscal
de compra.

Uma remessa não deverá conter o mesmo item de compra mais de uma vez.

---

# 16.20 Tabela `supplier_return_items`

Representa os itens enviados ao fornecedor em uma remessa de cascos.

| Campo                | Tipo    | Descrição                              |
| -------------------- | ------- | -------------------------------------- |
| `id`                 | INTEGER | Identificador                          |
| `supplier_return_id` | INTEGER | Remessa ao fornecedor                  |
| `purchase_item_id`   | INTEGER | Item de compra que representa a origem |
| `quantity`           | INTEGER | Quantidade enviada ao fornecedor       |
| `created_at`         | TEXT    | Data e hora de criação                 |

O campo `purchase_item_id` deverá preservar a origem exata da quantidade
enviada ao fornecedor.

A partir do item de compra, o sistema poderá identificar:

* A peça;
* A compra;
* A Nota Fiscal de compra;
* O fornecedor;
* A quantidade adquirida;
* A origem utilizada no consumo FIFO.

Os campos `part_id` e `purchase_id` não deverão ser armazenados nesta tabela,
pois essas informações já poderão ser obtidas através do
`purchase_item_id`.

O sistema não deverá permitir uma quantidade superior à quantidade disponível
para remessa ao fornecedor.

O mesmo `purchase_item_id` não deverá ser adicionado mais de uma vez na mesma
remessa.

---

# 16.21 Tabela `transfers`

Representa transferências entre filiais.

Embora o escopo inicial seja uma única filial, a estrutura deverá permitir evolução futura.

| Campo                   | Tipo    | Descrição                     |
| ----------------------- | ------- | ----------------------------- |
| `id`                    | INTEGER | Identificador                 |
| `origin_branch_id`      | INTEGER | Filial de origem              |
| `destination_branch_id` | INTEGER | Filial de destino             |
| `invoice_number`        | TEXT    | Número da NF de transferência |
| `issue_date`            | TEXT    | Data                          |
| `status`                | TEXT    | Status                        |
| `created_by`            | INTEGER | Usuário                       |
| `created_at`            | TEXT    | Data de criação               |

O identificador interno será utilizado para controle interno do sistema.

A Nota Fiscal de transferência deverá ser utilizada para transparência e rastreabilidade da movimentação.

---

# 16.22 Tabela `transfer_items`

Representa os itens de uma transferência.

| Campo         | Tipo    | Descrição     |
| ------------- | ------- | ------------- |
| `id`          | INTEGER | Identificador |
| `transfer_id` | INTEGER | Transferência |
| `part_id`     | INTEGER | Peça          |
| `quantity`    | INTEGER | Quantidade    |

---

# 16.23 Tabela `core_movements`

Representa o histórico consolidado das movimentações de cascos.

| Campo            | Tipo    | Descrição                   |
| ---------------- | ------- | --------------------------- |
| `id`             | INTEGER | Identificador               |
| `part_id`        | INTEGER | Peça                        |
| `movement_type`  | TEXT    | Tipo da movimentação        |
| `quantity`       | INTEGER | Quantidade                  |
| `reference_type` | TEXT    | Tipo do documento de origem |
| `reference_id`   | INTEGER | Identificador da origem     |
| `created_by`     | INTEGER | Usuário responsável         |
| `created_at`     | TEXT    | Data                        |

Essa tabela deverá permitir consultar a movimentação histórica de uma peça.

Exemplos de movimentação:

```text
PURCHASE
OUTBOUND
CUSTOMER_RETURN
SUPPLIER_RETURN
TRANSFER_OUT
TRANSFER_IN
ADJUSTMENT
```

---

# 16.24 Tabela `audit_logs`

Armazena o histórico de auditoria.

| Campo           | Tipo    | Descrição           |
| --------------- | ------- | ------------------- |
| `id`            | INTEGER | Identificador       |
| `user_id`       | INTEGER | Usuário responsável |
| `action`        | TEXT    | Ação realizada      |
| `module`        | TEXT    | Módulo afetado      |
| `entity_type`   | TEXT    | Tipo da entidade    |
| `entity_id`     | INTEGER | Registro afetado    |
| `old_values`    | TEXT    | Valores anteriores  |
| `new_values`    | TEXT    | Novos valores       |
| `justification` | TEXT    | Justificativa       |
| `created_at`    | TEXT    | Data e hora         |

Os registros de auditoria não deverão ser apagados ou alterados manualmente.

---

# 16.25 Relacionamentos principais

A estrutura deverá permitir os seguintes relacionamentos:

```text
Fornecedor
    ↓
Compra
    ↓
Itens da compra
    ↓
Saída
    ↓
Devolução do cliente
    ↓
Devolução ao fornecedor
```

Além disso:

```text
Compra
    ↓
Item comprado
    ↓
Alocação de saída
    ↓
Saída
```

E:

```text
Saída
    ↓
Alocação de devolução
    ↓
Devolução do cliente
```

---

# 16.26 Integridade referencial

O banco deverá utilizar chaves estrangeiras para manter a integridade dos relacionamentos.

A aplicação deverá ativar:

```sql
PRAGMA foreign_keys = ON;
```

em cada conexão com o SQLite.

As operações que alterem múltiplos registros relacionados deverão utilizar transações.

Exemplo:

```text
Registrar saída
    ↓
Validar saldo
    ↓
Consumir compra mais antiga
    ↓
Consumir próxima compra se necessário
    ↓
Registrar alocações
    ↓
Registrar movimentação
    ↓
Registrar auditoria
```

Todas essas operações deverão ser tratadas de forma consistente.

---

# 16.27 Evolução do banco de dados

Alterações estruturais futuras deverão ser realizadas de forma controlada.

O sistema deverá utilizar migrations ou mecanismo equivalente para:

* Criar tabelas;
* Alterar tabelas;
* Adicionar campos;
* Criar índices;
* Evoluir a estrutura.

O banco de produção não deverá ser substituído pelo banco de desenvolvimento para aplicar alterações estruturais.

---

# 16.28 Regras de Negócio relacionadas

### RN-129 — Banco inicial

O SIGC deverá utilizar SQLite como banco de dados inicial.

### RN-130 — Acesso ao banco

O banco de dados deverá ser acessado exclusivamente pela aplicação.

### RN-131 — Preservação histórica

Registros com histórico operacional não deverão ser excluídos fisicamente.

### RN-132 — Integridade referencial

Relacionamentos importantes deverão utilizar mecanismos de integridade referencial.

### RN-133 — Transações

Operações que alterem múltiplos registros relacionados deverão utilizar transações.

### RN-134 — Controle de compras

As compras deverão permitir a identificação dos itens e quantidades adquiridas.

### RN-135 — Consumo cronológico

As saídas deverão consumir prioritariamente os saldos das compras mais antigas.

### RN-136 — Consumo de múltiplas compras

Uma única saída poderá consumir quantidades provenientes de mais de uma compra.

### RN-137 — Rastreabilidade da saída

O sistema deverá manter a relação entre a saída e as compras utilizadas.

### RN-138 — Controle de devolução

As devoluções de clientes deverão ser relacionadas às respectivas saídas quando aplicável.

### RN-139 — Limite da devolução

O sistema não deverá permitir devolução superior à quantidade que possa ser validamente devolvida.

### RN-140 — Devolução ao fornecedor

Uma devolução ao fornecedor poderá conter múltiplos itens da mesma Nota Fiscal de compra.

### RN-141 — Devolução parcial

O sistema deverá permitir devoluções parciais de uma Nota Fiscal de compra.

### RN-142 — Simples remessa

A devolução ao fornecedor deverá preservar a referência à Nota Fiscal de simples remessa emitida pela empresa.

### RN-143 — Transferência

Transferências deverão preservar a identificação da Nota Fiscal correspondente.

### RN-144 — Histórico de movimentações

O sistema deverá preservar o histórico das movimentações relevantes das peças.

### RN-145 — Evolução estrutural

Alterações na estrutura do banco deverão ser realizadas de forma controlada e sem substituição destrutiva do banco de produção.

### RN-146 — Migração futura

A estrutura deverá permitir futura migração para um banco cliente-servidor.

---

# 17. INTERFACE E DESIGN SYSTEM

## 17.1 Objetivo

A interface do SIGC deverá ser moderna, profissional, intuitiva e consistente.

Todas as telas deverão seguir um padrão visual único, evitando diferenças desnecessárias de estilo, posicionamento ou comportamento entre os módulos.

A interface deverá priorizar:

* Clareza;
* Simplicidade;
* Consistência;
* Eficiência operacional;
* Boa organização visual;
* Facilidade de aprendizado;
* Redução de erros;
* Acesso rápido às funções mais utilizadas.

---

## 17.2 Princípios gerais

A interface deverá seguir os seguintes princípios:

### Clareza

Cada elemento deverá possuir uma finalidade clara.

Botões, campos e mensagens deverão utilizar textos objetivos.

Exemplos:

```text
Registrar compra
Registrar saída
Salvar alteração
Cancelar operação
Confirmar devolução
```

Deverão ser evitados textos vagos como:

```text
OK
Continuar
Executar
Processar
```

quando uma descrição mais clara for possível.

---

### Simplicidade

A tela deverá exibir apenas as informações necessárias para a tarefa atual.

Informações secundárias poderão ser acessadas por:

* Detalhes;
* Expansão;
* Filtros;
* Abas;
* Histórico.

A interface não deverá ser poluída com informações que não sejam necessárias para a operação atual.

---

### Consistência

Elementos com a mesma função deverão possuir:

* Mesmo estilo;
* Mesmo posicionamento relativo;
* Mesmo comportamento;
* Mesma nomenclatura.

Por exemplo, o botão de salvar deverá seguir o mesmo padrão em todas as telas.

---

### Prevenção de erros

O sistema deverá prevenir erros antes que a operação seja concluída.

Exemplos:

* Bloqueio de quantidade inválida;
* Validação de campos obrigatórios;
* Confirmação antes de cancelamentos;
* Aviso de operação irreversível;
* Validação de quantidade disponível.

---

# 17.3 Estrutura geral da aplicação

A aplicação deverá possuir uma estrutura de navegação centralizada.

Exemplo:

```text
┌────────────────────────────────────────────┐
│ LOGO / SIGC                 Usuário        │
├───────────────┬────────────────────────────┤
│               │                            │
│ Dashboard     │                            │
│               │                            │
│ Cadastros     │       Conteúdo principal   │
│               │                            │
│ Operações     │                            │
│               │                            │
│ Consultas     │                            │
│               │                            │
│ Administração │                            │
│               │                            │
└───────────────┴────────────────────────────┘
```

O menu deverá exibir somente as funções permitidas ao usuário atual.

---

# 17.4 Dashboard

O dashboard deverá apresentar um resumo das informações mais relevantes.

A tela não deverá tentar exibir todos os dados do sistema simultaneamente.

Poderá apresentar informações como:

* Quantidade total disponível;
* Movimentações recentes;
* Alertas;
* Pendências;
* Operações recentes;
* Indicadores importantes.

A quantidade de informações deverá ser controlada para evitar poluição visual.

---

# 17.5 Navegação

A navegação deverá ser previsível.

O usuário deverá conseguir identificar facilmente:

* Onde está;
* Qual módulo está utilizando;
* Qual operação está realizando;
* Como retornar à tela anterior.

A aplicação deverá utilizar títulos e elementos de navegação consistentes.

---

# 17.6 Formulários

Os formulários deverão ser organizados por grupos lógicos.

Exemplo:

```text
Dados principais
────────────────────────

Fornecedor
Número da NF
Data de emissão


Itens
────────────────────────

Peça
Quantidade
Valor


Ações
────────────────────────

[Cancelar]    [Salvar]
```

Os campos deverão:

* Possuir rótulos claros;
* Indicar campos obrigatórios;
* Possuir validações;
* Exibir mensagens próximas ao problema;
* Evitar solicitações duplicadas.

---

# 17.7 Botões

Os botões deverão possuir localização e finalidade claras.

As ações principais deverão possuir destaque visual superior às ações secundárias.

Exemplo:

```text
[Cancelar]                 [Registrar compra]
```

A ação principal deverá ser facilmente identificável.

Ações destrutivas ou potencialmente perigosas deverão possuir confirmação.

Exemplo:

```text
Cancelar lançamento?

Esta ação será registrada no histórico.

[Voltar]    [Confirmar cancelamento]
```

---

# 17.8 Cores e significado

As cores deverão ser utilizadas de forma consistente.

A cor não deverá ser o único meio de transmitir uma informação.

Exemplo:

```text
Status:
[Ativo]
[Cancelado]
[Pendente]
[Concluído]
```

Além da cor, o status deverá possuir texto.

As cores deverão ser utilizadas principalmente para:

* Destaque;
* Estado;
* Alertas;
* Confirmação;
* Erros.

O sistema deverá evitar excesso de cores.

---

# 17.9 Tabelas

As tabelas deverão apresentar informações de forma organizada.

Deverão possuir:

* Cabeçalhos claros;
* Colunas relevantes;
* Ordenação quando aplicável;
* Filtros quando necessário;
* Paginação quando houver grande volume de dados;
* Acesso aos detalhes.

A tabela não deverá exibir todas as informações disponíveis de um registro na tela inicial.

Informações adicionais deverão estar disponíveis na tela de detalhes.

---

# 17.10 Pesquisas e filtros

Os módulos com grande volume de dados deverão possuir mecanismos de busca e filtragem.

Exemplos:

* Número da NF;
* Fornecedor;
* Peça;
* Período;
* Usuário;
* Status;
* Número da OS.

Os filtros deverão ser simples e objetivos.

---

# 17.11 Mensagens do sistema

As mensagens deverão ser claras e orientadas à ação.

### Sucesso

```text
Compra registrada com sucesso.
```

### Erro

```text
Não foi possível registrar a saída.
Verifique a quantidade disponível.
```

### Aviso

```text
A quantidade informada é superior ao saldo disponível.
```

### Confirmação

```text
Deseja realmente cancelar este lançamento?
A operação será registrada no histórico.
```

Mensagens técnicas internas não deverão ser exibidas diretamente ao usuário.

---

# 17.12 Estados dos registros

Os registros deverão possuir estados claros quando aplicável.

Exemplos:

```text
ATIVO
INATIVO
PENDENTE
CONCLUÍDO
CANCELADO
CORRIGIDO
```

O estado deverá ser apresentado de forma clara.

---

# 17.13 Correções e cancelamentos

Quando um lançamento puder ser corrigido ou cancelado:

1. O sistema deverá solicitar justificativa;
2. A ação deverá ser registrada;
3. O histórico anterior deverá ser preservado;
4. Os saldos deverão ser recalculados ou ajustados corretamente;
5. O usuário deverá receber confirmação da operação.

O sistema não deverá apagar silenciosamente o lançamento original.

---

# 17.14 Responsividade

Inicialmente, o sistema será priorizado para computadores conectados à rede interna.

A interface deverá ser desenvolvida de forma que possa futuramente ser adaptada para diferentes tamanhos de tela.

A prioridade inicial será:

1. Desktop;
2. Notebook;
3. Tablets;
4. Dispositivos móveis, futuramente.

---

# 17.15 Acessibilidade

Sempre que possível, a interface deverá:

* Utilizar textos legíveis;
* Possuir contraste adequado;
* Evitar depender exclusivamente de cores;
* Possuir elementos claramente identificáveis;
* Permitir navegação lógica;
* Utilizar labels adequados.

---

# 17.16 Padronização visual

O sistema deverá possuir componentes reutilizáveis.

Exemplos:

* Botões;
* Campos;
* Cards;
* Tabelas;
* Modais;
* Alertas;
* Badges de status;
* Mensagens.

Uma alteração futura no estilo de um componente deverá poder ser aplicada de forma centralizada.

---

# 17.17 Design System

O SIGC deverá possuir um Design System próprio.

O Design System deverá definir:

* Tipografia;
* Espaçamentos;
* Tamanhos;
* Botões;
* Campos;
* Cores;
* Status;
* Cards;
* Tabelas;
* Modais;
* Mensagens;
* Ícones.

As definições poderão evoluir futuramente sem necessidade de reescrever individualmente todas as telas.

---

# 17.18 Identidade visual

A identidade visual deverá transmitir:

* Profissionalismo;
* Organização;
* Confiabilidade;
* Controle;
* Tecnologia.

O sistema deverá evitar estilos excessivamente decorativos que prejudiquem a operação.

O visual deverá ser moderno, porém funcional.

---

# 17.19 Regras de Negócio relacionadas

### RN-147 — Padronização visual

Todas as telas deverão seguir um padrão visual consistente.

### RN-148 — Clareza das ações

Os botões deverão possuir textos claros e indicar sua finalidade.

### RN-149 — Prevenção de erros

A interface deverá prevenir operações inválidas sempre que possível.

### RN-150 — Confirmação de ações críticas

Operações críticas deverão solicitar confirmação quando aplicável.

### RN-151 — Registro de alterações

Correções e cancelamentos deverão preservar o histórico da operação original.

### RN-152 — Mensagens orientativas

Mensagens de erro e aviso deverão orientar o usuário sobre o problema e, quando possível, como corrigi-lo.

### RN-153 — Consistência

Componentes com a mesma finalidade deverão possuir comportamento consistente em todo o sistema.

### RN-154 — Redução de poluição visual

Informações não essenciais não deverão ser exibidas desnecessariamente.

### RN-155 — Design System

A interface deverá utilizar componentes padronizados e reutilizáveis.

### RN-156 — Evolução visual

Alterações futuras de estilo deverão ser realizadas preferencialmente de forma centralizada.

### RN-157 — Acessibilidade

A interface deverá evitar depender exclusivamente de cores para comunicar informações importantes.

---

# 18. GITHUB E CONTROLE DE VERSÃO

## 18.1 Objetivo

O GitHub será utilizado como plataforma oficial para:

* Armazenamento do código-fonte;
* Controle de versões;
* Organização do projeto;
* Registro de alterações;
* Backup do código e da documentação;
* Desenvolvimento em diferentes computadores;
* Construção do portfólio profissional do projeto.

O GitHub não deverá ser utilizado para armazenar dados reais e sensíveis da empresa.

---

## 18.2 Repositório oficial

O projeto SIGC deverá possuir um repositório oficial.

O repositório deverá conter:

```text
Código-fonte
Documentação
Configurações de exemplo
Testes
Migrations
Arquivos auxiliares
```

A estrutura poderá evoluir conforme o projeto crescer.

---

## 18.3 Organização inicial do projeto

A estrutura inicial recomendada será semelhante a:

```text
SIGC/
│
├── docs/
│   └── SIGC_MASTER_SPECIFICATION.md
│
├── app/
│   ├── routes/
│   ├── services/
│   ├── repositories/
│   ├── models/
│   └── templates/
│
├── tests/
│
├── migrations/
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── config/
│
├── .gitignore
├── README.md
├── requirements.txt
└── run.py
```

A estrutura definitiva poderá ser ajustada durante a implementação.

---

## 18.4 Documentação oficial

O arquivo:

```text
SIGC_MASTER_SPECIFICATION.md
```

será considerado a especificação oficial do projeto.

Ele deverá conter:

* Regras de negócio;
* Decisões técnicas;
* Arquitetura;
* Banco de dados;
* Design System;
* Decisões pendentes;
* Histórico de alterações.

Nenhuma alteração importante deverá ser implementada sem verificar a compatibilidade com essa especificação.

---

## 18.5 Arquivos que não deverão ser enviados ao GitHub

O repositório deverá utilizar um `.gitignore`.

Não deverão ser enviados ao repositório:

```text
Banco de dados de produção
Senhas
Tokens
Chaves secretas
Arquivos de configuração sensíveis
Backups reais
Logs com dados sensíveis
Arquivos temporários
Ambientes virtuais
```

Exemplos:

```text
.env
*.db
*.sqlite
__pycache__/
.venv/
logs/
backups/
```

A regra deverá ser ajustada conforme a necessidade do projeto.

---

## 18.6 Configurações de ambiente

As configurações específicas de cada ambiente deverão ser separadas do código.

Exemplo:

```text
Desenvolvimento:
DATABASE_URL=sigc_dev.db

Produção:
DATABASE_URL=sigc_prod.db
```

As configurações reais de produção não deverão ser publicadas no repositório.

Deverá existir, quando necessário, um arquivo de exemplo:

```text
.env.example
```

contendo apenas a estrutura esperada.

---

## 18.7 Commits

Os commits deverão ser realizados de forma organizada.

Cada commit deverá representar uma alteração lógica.

Exemplos:

```text
feat: add supplier registration
fix: correct FIFO allocation
docs: update database specification
refactor: reorganize service layer
test: add purchase validation tests
```

Deverão ser evitados commits genéricos como:

```text
alterações
mudanças
final
teste
coisas
```

---

## 18.8 Frequência dos commits

Não será obrigatório realizar um commit a cada pequena alteração.

A recomendação será realizar um commit quando uma unidade lógica de trabalho estiver concluída.

Exemplo:

```text
Criar tabela de fornecedores
        ↓
Implementar cadastro
        ↓
Testar cadastro
        ↓
Commit
```

O objetivo é manter o histórico útil e compreensível.

---

## 18.9 Branch principal

A branch principal deverá representar uma versão estável do projeto.

Inicialmente poderá ser utilizada:

```text
main
```

Alterações maiores poderão ser desenvolvidas em branches separadas.

Exemplo:

```text
main
│
├── feature/supplier-module
├── feature/purchase-module
└── fix/fifo-calculation
```

---

## 18.10 Branches de funcionalidades

Quando uma funcionalidade possuir grande impacto, poderá ser criada uma branch específica.

Exemplo:

```text
feature/customer-returns
```

Após testes e validação, a alteração poderá ser integrada à branch principal.

---

## 18.11 Versionamento

O SIGC deverá utilizar versionamento organizado.

Exemplo:

```text
v1.0.0
v1.1.0
v1.1.1
```

A versão poderá seguir o padrão:

```text
MAJOR.MINOR.PATCH
```

### MAJOR

Alterações incompatíveis ou de grande impacto.

### MINOR

Novas funcionalidades compatíveis com a versão anterior.

### PATCH

Correções de erros e ajustes menores.

---

## 18.12 Documentação de alterações

Alterações importantes deverão ser registradas na especificação oficial.

Exemplo:

```text
Versão 1.1.0
Data: 2026-08-10

Alteração:
Adicionado módulo de devolução ao fornecedor.

Motivo:
Necessidade operacional identificada durante os testes.
```

---

## 18.13 Desenvolvimento em computadores diferentes

O projeto deverá permitir que o desenvolvimento seja retomado em outro computador.

O fluxo esperado será:

```text
GitHub
   ↓
Clone do repositório
   ↓
Configuração do ambiente
   ↓
Instalação das dependências
   ↓
Execução do projeto
```

O projeto deverá possuir documentação suficiente para permitir a configuração de um novo ambiente.

---

## 18.14 README

O repositório deverá possuir um `README.md` contendo, inicialmente:

* Nome do projeto;
* Descrição;
* Objetivo;
* Tecnologias;
* Como instalar;
* Como executar;
* Estrutura do projeto;
* Como contribuir para o projeto;
* Referência à especificação oficial.

O README deverá evoluir junto com o projeto.

---

## 18.15 Controle de dados reais

Dados reais da empresa deverão permanecer fora do repositório público ou privado, salvo decisão específica e devidamente avaliada.

O código e os dados deverão ser tratados separadamente.

```text
GitHub
    ↓
Código e documentação

Servidor
    ↓
Banco de produção
    ↓
Dados reais
```

---

## 18.16 Backup do código

O GitHub será uma das formas de preservação do código-fonte.

Entretanto, o GitHub não deverá ser considerado o único backup de toda a infraestrutura do sistema.

A empresa deverá manter estratégias próprias para:

* Banco de dados;
* Backups de produção;
* Configurações;
* Infraestrutura.

---

## 18.17 Segurança do repositório

O repositório deverá ser configurado de acordo com a sensibilidade do projeto.

Deverão ser consideradas:

* Visibilidade do repositório;
* Controle de acesso;
* Autenticação em dois fatores;
* Proteção da branch principal;
* Revisão de alterações importantes.

A visibilidade do repositório poderá ser alterada futuramente conforme o objetivo de portfólio e as necessidades de segurança.

---

## 18.18 Regras de Governança do Código

Alterações importantes deverão:

1. Ser compatíveis com a especificação;
2. Ser testadas quando aplicável;
3. Ser registradas no Git;
4. Possuir commit descritivo;
5. Preservar dados históricos;
6. Evitar alterações destrutivas não planejadas.

---

## 18.19 Regras de Negócio relacionadas

### RN-158 — Versionamento

O código-fonte deverá ser versionado utilizando Git.

### RN-159 — Repositório oficial

O projeto deverá possuir um repositório oficial para controle do código e da documentação.

### RN-160 — Proteção de dados

Dados reais, senhas e informações sensíveis não deverão ser armazenados no repositório.

### RN-161 — Commits organizados

Os commits deverão representar alterações lógicas e possuir mensagens descritivas.

### RN-162 — Especificação oficial

A `SIGC_MASTER_SPECIFICATION.md` deverá ser considerada a fonte oficial de verdade do projeto.

### RN-163 — Compatibilidade

Alterações no código deverão respeitar as regras estabelecidas na especificação.

### RN-164 — Desenvolvimento multiplataforma

O projeto deverá permitir a continuidade do desenvolvimento em diferentes computadores mediante configuração adequada do ambiente.

### RN-165 — Histórico

Alterações importantes deverão possuir rastreabilidade por meio do histórico do Git e da documentação.

### RN-166 — Proteção da branch principal

A branch principal deverá representar uma versão considerada estável do projeto.

### RN-167 — Dados fora do código

Dados de produção deverão permanecer separados do código-fonte.

### RN-168 — Reprodutibilidade

O projeto deverá possuir informações suficientes para permitir a reconstrução do ambiente de desenvolvimento.

### RN-169 — Origem do item da remessa

Cada item enviado ao fornecedor deverá manter vínculo com um
`purchase_item_id`.

Essa referência deverá preservar a peça, a compra, o fornecedor e a Nota Fiscal
de origem.

### RN-170 — Saldo disponível para remessa

O sistema deverá permitir o envio ao fornecedor somente de quantidades que já
tenham sido devolvidas pelos clientes e ainda não tenham sido remetidas.

### RN-171 — Remessa parcial ao fornecedor

O sistema deverá permitir que uma quantidade disponível seja remetida
parcialmente ao fornecedor.

O saldo restante deverá continuar disponível para uma remessa posterior.

### RN-172 — Bloqueio de excesso na remessa

O sistema deverá impedir que uma remessa contenha quantidade superior ao saldo
disponível para o item de compra.

A mensagem de erro deverá informar a quantidade máxima disponível.

### RN-173 — Item duplicado na remessa

O mesmo `purchase_item_id` não deverá aparecer mais de uma vez na mesma remessa
ao fornecedor.

### RN-174 — Fornecedor da remessa

Todos os itens incluídos em uma remessa deverão pertencer ao fornecedor
informado no cabeçalho da remessa.

### RN-175 — Nota Fiscal de compra da remessa

Todos os itens incluídos em uma mesma remessa deverão possuir origem na mesma
Nota Fiscal de compra.

### RN-176 — Distribuição FIFO das devoluções

Quando uma saída tiver sido alocada em mais de um item de compra, as quantidades
devolvidas pelo cliente deverão ser atribuídas às origens seguindo a mesma
ordem FIFO utilizada na saída.

---

# 19. DECISÕES TÉCNICAS

Esta seção registra as principais decisões técnicas adotadas para o desenvolvimento do SIGC.

As decisões aqui registradas deverão ser consideradas em conjunto com as demais regras da `SIGC_MASTER_SPECIFICATION.md`.

Alterações futuras deverão ser discutidas e registradas no histórico de alterações.

---

## DT-001 — Linguagem de programação

### Decisão

O SIGC será desenvolvido utilizando Python como linguagem principal.

### Motivo

Python foi escolhido por:

* Facilidade de desenvolvimento;
* Grande quantidade de bibliotecas;
* Boa produtividade;
* Adequação ao desenvolvimento web;
* Facilidade de manutenção;
* Possibilidade de evolução futura.

---

## DT-002 — Tipo de aplicação

### Decisão

O SIGC será desenvolvido inicialmente como uma aplicação web.

### Motivo

A aplicação web permitirá que diferentes usuários acessem o sistema por meio de navegadores, sem necessidade de instalar o sistema completo em cada computador.

---

## DT-003 — Ambiente inicial de produção

### Decisão

O ambiente de produção inicial será um servidor Windows da empresa.

### Motivo

A empresa já possui infraestrutura de servidor e rede interna.

A utilização do servidor da empresa evita, inicialmente, a necessidade de contratação de hospedagem externa.

---

## DT-004 — Ambiente inicial de desenvolvimento

### Decisão

O desenvolvimento será realizado inicialmente em um único computador local.

### Motivo

O acesso ao servidor da empresa está temporariamente indisponível.

O desenvolvimento local permite iniciar imediatamente a implementação sem depender da disponibilidade da infraestrutura de produção.

---

## DT-005 — Migração para produção

### Decisão

Após a conclusão e validação do sistema localmente, a aplicação será transferida e configurada no servidor Windows da empresa.

### Motivo

A separação entre desenvolvimento e produção permite:

* Testar novas funcionalidades sem afetar os dados reais;
* Corrigir erros antes da implantação;
* Preservar a estabilidade do sistema em produção.

---

## DT-006 — Banco de dados inicial

### Decisão

O banco de dados inicial será SQLite.

### Motivo

O SQLite é adequado ao ambiente inicial do projeto por possuir:

* Baixa complexidade de implantação;
* Ausência de necessidade de servidor de banco separado;
* Facilidade de backup;
* Boa integração com Python;
* Adequação ao número inicial de usuários.

---

## DT-007 — Migração futura do banco

### Decisão

A arquitetura deverá permitir futura migração para um banco de dados cliente-servidor, como PostgreSQL.

### Motivo

A migração poderá ser necessária caso o sistema cresça em:

* Número de usuários;
* Volume de dados;
* Número de filiais;
* Complexidade das operações;
* Necessidade de acesso remoto.

---

## DT-008 — Acesso ao banco de dados

### Decisão

Os usuários não acessarão diretamente o arquivo físico do banco de dados.

O acesso ocorrerá exclusivamente através da aplicação SIGC.

### Motivo

Essa decisão melhora:

* Segurança;
* Integridade;
* Controle de permissões;
* Auditoria;
* Centralização das regras de negócio.

---

## DT-009 — Arquitetura em camadas

### Decisão

A aplicação será organizada preferencialmente em camadas.

A estrutura deverá separar:

* Apresentação;
* Rotas e controladores;
* Serviços;
* Regras de negócio;
* Repositórios;
* Modelos;
* Banco de dados.

### Motivo

A separação facilita:

* Manutenção;
* Testes;
* Evolução;
* Correção de erros;
* Migração futura de tecnologias.

---

## DT-010 — Separação entre desenvolvimento e produção

### Decisão

O ambiente de desenvolvimento e o ambiente de produção utilizarão bancos separados.

Exemplo:

```text
Desenvolvimento:
sigc_dev.db

Produção:
sigc_prod.db
```

### Motivo

Evitar que:

* Dados de teste sejam misturados com dados reais;
* Testes alterem o banco de produção;
* O banco real seja substituído acidentalmente.

---

## DT-011 — Controle de versão

### Decisão

O código e a documentação serão versionados utilizando Git e armazenados no GitHub.

O GitHub será utilizado para preservar o histórico do código-fonte e da documentação.

O GitHub não será considerado o sistema oficial de backup do banco de dados de produção ou da infraestrutura do SIGC.

### Motivo

Permitir:

* Histórico de alterações;
* Versionamento do código;
* Preservação do código e da documentação;
* Desenvolvimento em computadores diferentes;
* Organização profissional;
* Construção de portfólio.

O backup do banco de dados de produção e da infraestrutura deverá possuir estratégia própria e independente do repositório de código.

---

## DT-012 — Proteção de dados reais

### Decisão

Dados reais da empresa não deverão ser armazenados no repositório do GitHub.

### Motivo

O código-fonte e os dados da empresa deverão permanecer separados.

O banco de produção deverá permanecer no ambiente de produção.

---

## DT-013 — Especificação oficial

### Decisão

A `SIGC_MASTER_SPECIFICATION.md` será a fonte oficial de verdade do projeto.

### Motivo

Centralizar:

* Regras de negócio;
* Decisões técnicas;
* Arquitetura;
* Estrutura do banco;
* Design System;
* Decisões pendentes;
* Histórico de alterações.

---

## DT-014 — Preservação de dados históricos

### Decisão

O sistema deverá priorizar a preservação dos dados históricos.

Registros operacionais não deverão ser apagados fisicamente quando já possuírem histórico relevante.

### Motivo

O SIGC deverá manter rastreabilidade das operações realizadas.

---

## DT-015 — Correções e cancelamentos

### Decisão

Operações poderão ser corrigidas ou canceladas quando permitido pelas regras do sistema.

A ação deverá:

* Exigir justificativa quando aplicável;
* Preservar o histórico;
* Registrar o usuário responsável;
* Registrar data e hora;
* Ajustar corretamente os saldos.

### Motivo

Permitir correções operacionais sem perder a rastreabilidade.

---

## DT-016 — Auditoria

### Decisão

Operações relevantes deverão ser registradas em histórico de auditoria.

### Motivo

Permitir identificar:

* Quem realizou a operação;
* Quando realizou;
* Qual registro foi alterado;
* Qual era o valor anterior;
* Qual foi o novo valor;
* Qual foi a justificativa, quando aplicável.

---

## DT-017 — Transações em operações críticas

### Decisão

Operações que alterem múltiplos registros relacionados deverão ser executadas dentro de transações de banco de dados.

Quando uma operação não puder ser concluída integralmente, suas alterações deverão ser revertidas sempre que tecnicamente possível.

Essa regra deverá ser aplicada especialmente a operações como:

* Registro de compras;
* Registro de saídas;
* Consumo cronológico de compras;
* Devoluções;
* Transferências;
* Correções;
* Cancelamentos;
* Atualizações de saldo.

### Motivo

Garantir que operações relacionadas não deixem o banco de dados em estado parcialmente atualizado.

Por exemplo, uma saída que consuma quantidades de diferentes compras deverá ser concluída integralmente ou revertida em caso de falha.

Essa decisão é especialmente importante para preservar a integridade dos saldos, da rastreabilidade e do histórico operacional.

---

## DT-018 — Consumo cronológico de compras

### Decisão

O sistema deverá consumir prioritariamente as compras mais antigas disponíveis.

Caso uma compra não possua quantidade suficiente, a operação deverá consumir automaticamente a próxima compra necessária.

### Motivo

Preservar a rastreabilidade das peças e controlar corretamente a origem do estoque.

---

## DT-019 — Arquitetura preparada para expansão

### Decisão

O sistema será inicialmente desenvolvido para uma única filial, mas a arquitetura deverá permitir evolução futura.

Possíveis expansões:

* Múltiplas filiais;
* Acesso remoto;
* Banco cliente-servidor;
* Permissões personalizadas;
* Integrações;
* Relatórios avançados.

### Motivo

Evitar decisões técnicas que impeçam a evolução futura do sistema.

---

## DT-020 — Design System

### Decisão

O SIGC utilizará um padrão visual centralizado e consistente.

### Motivo

Garantir que todas as telas possuam:

* Identidade visual uniforme;
* Componentes padronizados;
* Navegação consistente;
* Aparência profissional.

---

## DT-021 — Interface

### Decisão

A interface deverá ser moderna, profissional, intuitiva e limpa.

### Motivo

O sistema será utilizado durante operações reais e deverá priorizar produtividade e redução de erros.

---

## DT-022 — Desenvolvimento incremental

### Decisão

O sistema será desenvolvido por etapas.

Cada etapa deverá ser:

1. Planejada;
2. Implementada;
3. Testada;
4. Validada;
5. Versionada.

### Motivo

Reduzir riscos e permitir correções durante o desenvolvimento.

---

## DT-023 — Migrações de banco de dados

### Decisão

Alterações estruturais do banco deverão ser realizadas de forma controlada, utilizando migrations ou mecanismo equivalente.

### Motivo

Permitir que o banco de produção evolua sem substituição destrutiva dos dados existentes.

---

## DT-024 — Configurações por ambiente

### Decisão

As configurações específicas do ambiente deverão ser separadas do código sempre que possível.

### Motivo

Permitir que a mesma aplicação seja executada em diferentes ambientes sem alterar diretamente o código-fonte.

---

## DT-025 — Segurança das senhas

### Decisão

Senhas não deverão ser armazenadas em texto puro.

Deverão ser utilizadas técnicas adequadas de hashing e proteção.

### Motivo

Reduzir o impacto de eventual exposição indevida do banco de dados.

---

## DT-026 — Usuários inativos

### Decisão

Usuários que já tenham realizado operações não deverão ser apagados fisicamente.

Deverão ser desativados quando necessário.

### Motivo

Preservar a identificação histórica das operações realizadas.

---

## DT-027 — Administração do sistema

### Decisão

Inicialmente haverá um único Administrador Master.

O sistema deverá permitir futura expansão das permissões.

### Motivo

Atender à estrutura inicial da empresa sem impedir evolução futura.

---

## DT-028 — Acesso simultâneo

### Decisão

A arquitetura deverá suportar aproximadamente quatro usuários simultâneos, considerando que normalmente nem todos estarão conectados ao mesmo tempo.

### Motivo

Atender à necessidade operacional atual da empresa sem adicionar complexidade desnecessária.

---

## DT-029 — Acesso pela rede interna

### Decisão

A primeira implantação de produção será disponibilizada pela rede interna da empresa.

### Motivo

A rede interna é estável e os usuários utilizarão computadores diferentes conectados à infraestrutura da empresa.

---

## DT-030 — Acesso remoto futuro

### Decisão

O acesso remoto pela internet não fará parte obrigatoriamente da primeira implantação.

A arquitetura deverá permitir uma futura evolução para acesso remoto seguro.

### Motivo

Priorizar inicialmente segurança, estabilidade e implantação controlada.

---

## DT-031 — Backup

### Decisão

O banco de produção deverá possuir uma estratégia de backup independente do banco principal.

### Motivo

Reduzir o risco de perda de dados.

---

## DT-032 — Não substituição do banco de produção

### Decisão

O banco de desenvolvimento não deverá substituir diretamente o banco de produção.

### Motivo

Evitar a perda de dados reais.

---

## DT-033 — Fonte de verdade técnica

### Decisão

Quando existir conflito entre uma nova sugestão e uma regra já estabelecida na especificação, a alteração deverá ser tratada como uma possível mudança de requisito.

A alteração não deverá ser implementada automaticamente.

### Motivo

Preservar a governança do projeto e evitar mudanças acidentais de regras de negócio.

---

## 19.1 Resumo das decisões

A arquitetura inicial do SIGC será:

```text
DESENVOLVIMENTO

Computador local
        ↓
Python
        ↓
Aplicação Web
        ↓
SQLite de desenvolvimento
        ↓
Git
        ↓
GitHub
```

Posteriormente:

```text
PRODUÇÃO

Usuários
        ↓
Navegador
        ↓
Rede interna
        ↓
Servidor Windows
        ↓
Aplicação SIGC
        ↓
SQLite de produção
        ↓
Backups
```

E futuramente, se necessário:

```text
EVOLUÇÃO

Acesso remoto seguro
        ↓
Aplicação centralizada
        ↓
PostgreSQL ou banco equivalente
        ↓
Expansão para múltiplas filiais
```

---

# 20. DECISÕES PENDENTES

Esta seção registra decisões ainda não definidas ou que deverão ser refinadas durante a evolução do projeto.

Uma decisão pendente não deverá impedir o desenvolvimento das partes que não dependem dela.

Quando uma decisão for tomada, ela deverá:

1. Ser removida desta seção ou marcada como resolvida;
2. Ser registrada na seção correspondente da especificação;
3. Ser adicionada às decisões técnicas quando aplicável;
4. Ser registrada no histórico de alterações quando representar uma mudança relevante.

---

## DP-001 — Framework web

### Status

Pendente.

### Descrição

O framework web definitivo ainda deverá ser escolhido.

A decisão deverá considerar:

* Facilidade de desenvolvimento;
* Organização do projeto;
* Suporte ao Python;
* Manutenção;
* Segurança;
* Possibilidade de evolução.

### Momento recomendado

Antes do início da implementação da aplicação web.

---

## DP-002 — Estratégia definitiva de execução em produção

### Status

Pendente.

### Descrição

Deverá ser definido o método definitivo para manter a aplicação SIGC disponível no servidor Windows.

As possibilidades incluem:

* Execução como processo;
* Serviço do Windows;
* Servidor WSGI;
* Outra solução adequada ao ambiente.

### Momento recomendado

Antes da implantação no servidor da empresa.

---

## DP-003 — Endereço de acesso na rede interna

### Status

Pendente.

### Descrição

Deverá ser definido como os usuários acessarão o sistema na rede interna.

Possibilidades:

```text
http://IP_DO_SERVIDOR:PORTA
```

ou:

```text
http://nome-do-servidor
```

### Momento recomendado

Durante a implantação em produção.

---

## DP-004 — Domínio ou endereço para acesso futuro

### Status

Pendente.

### Descrição

Caso o sistema futuramente seja disponibilizado pela internet, deverá ser definido:

* Domínio;
* DNS;
* Certificado HTTPS;
* Estratégia de acesso seguro.

### Momento recomendado

Somente quando o acesso remoto for efetivamente planejado.

---

## DP-005 — Migração futura do banco

### Status

Pendente.

### Descrição

A necessidade de migração do SQLite para um banco cliente-servidor deverá ser reavaliada conforme o crescimento do sistema.

Possíveis opções:

* PostgreSQL;
* Outro banco relacional adequado.

### Momento recomendado

Quando houver necessidade técnica ou operacional.

---

## DP-006 — Sistema de backup

### Status

Pendente de detalhamento.

### Descrição

A estratégia definitiva de backup deverá definir:

* Frequência;
* Quantidade de cópias;
* Local de armazenamento;
* Retenção;
* Restauração;
* Testes de recuperação.

### Momento recomendado

Antes da entrada em produção.

---

## DP-007 — Local secundário dos backups

### Status

Pendente.

### Descrição

Deverá ser definido onde serão armazenadas as cópias de backup.

Possibilidades:

* Outro computador;
* Dispositivo externo;
* Servidor secundário;
* Serviço de armazenamento em nuvem;
* Outra infraestrutura adequada.

### Momento recomendado

Durante a definição da estratégia de backup.

---

## DP-008 — Identidade visual definitiva

### Status

Pendente.

### Descrição

Ainda deverão ser definidos:

* Logo;
* Cor principal;
* Paleta de cores;
* Tipografia;
* Ícones;
* Tema visual definitivo.

### Momento recomendado

Antes da finalização da interface principal.

---

## DP-009 — Tema claro ou escuro

### Status

Pendente.

### Descrição

Deverá ser definido se o sistema utilizará:

* Tema claro;
* Tema escuro;
* Alternância entre temas.

### Momento recomendado

Durante a criação do Design System.

---

## DP-010 — Framework de interface

### Status

Pendente.

### Descrição

Deverá ser definido o conjunto de tecnologias utilizado para a construção da interface.

A escolha deverá considerar:

* Integração com o backend;
* Facilidade de manutenção;
* Reutilização de componentes;
* Necessidade de JavaScript;
* Complexidade do projeto.

### Momento recomendado

Antes da implementação da primeira tela.

---

## DP-011 — Sistema de notificações

### Status

Pendente.

### Descrição

Deverá ser definido o mecanismo de notificações do sistema.

Possibilidades futuras:

* Notificações internas;
* Alertas no dashboard;
* E-mail;
* Outras integrações.

O envio automático de e-mails não faz parte da implementação inicial.

### Momento recomendado

Quando houver necessidade operacional.

---

## DP-012 — Integração com e-mail

### Status

Pendente.

### Descrição

O sistema poderá futuramente enviar e-mails relacionados a:

* Alertas;
* Pendências;
* Notificações;
* Eventos importantes.

Essa funcionalidade não será implementada inicialmente.

### Momento recomendado

Após a conclusão da versão inicial do sistema.

---

## DP-013 — Integração com sistemas externos

### Status

Pendente.

### Descrição

Ainda não foi definida a necessidade de integração com outros sistemas da empresa.

Possíveis integrações futuras poderão envolver:

* Sistemas administrativos;
* Sistemas financeiros;
* Sistemas fiscais;
* APIs;
* Outros sistemas internos.

### Momento recomendado

Somente quando houver necessidade concreta.

---

## DP-014 — Controle de múltiplas filiais

### Status

Pendente para implementação futura.

### Descrição

O sistema será inicialmente utilizado por uma única filial.

A expansão para múltiplas filiais poderá ser implementada futuramente.

### Momento recomendado

Quando existir necessidade operacional.

---

## DP-015 — Acesso remoto

### Status

Pendente para implementação futura.

### Descrição

O acesso remoto pela internet não fará parte da primeira implantação.

Futuramente deverá ser avaliada uma solução segura.

### Momento recomendado

Quando o acesso externo for necessário.

---

## DP-016 — Política de expiração de senha

### Status

Pendente.

### Descrição

Deverá ser definido se as senhas:

* Nunca expiram;
* Expiram após determinado período;
* Podem ser redefinidas pelo Administrador Master.

### Momento recomendado

Durante a implementação do módulo de usuários.

---

## DP-017 — Política de bloqueio de acesso

### Status

Pendente.

### Descrição

Deverá ser definido o comportamento após múltiplas tentativas de login inválidas.

Possibilidades:

* Bloqueio temporário;
* Bloqueio permanente até intervenção administrativa;
* Limitação progressiva de tentativas.

### Momento recomendado

Durante a implementação da autenticação.

---

## DP-018 — Tempo de sessão

### Status

Pendente.

### Descrição

Deverá ser definido por quanto tempo uma sessão poderá permanecer ativa sem interação.

### Momento recomendado

Durante a implementação da autenticação.

---

## DP-019 — Relatórios avançados

### Status

Pendente.

### Descrição

Deverá ser definido quais relatórios avançados serão necessários.

Possibilidades:

* Relatório de movimentações;
* Relatório de consumo;
* Relatório de devoluções;
* Relatório por fornecedor;
* Relatório por período;
* Relatório de auditoria.

### Momento recomendado

Após a implementação dos módulos principais.

---

## DP-020 — Exportação de dados

### Status

Pendente.

### Descrição

Deverá ser definido se o sistema permitirá exportação de dados.

Possíveis formatos:

* CSV;
* Excel;
* PDF.

### Momento recomendado

Durante a implementação dos relatórios.

---

## DP-021 — Impressão de documentos

### Status

Pendente.

### Descrição

Deverá ser definido se o sistema deverá gerar documentos para impressão.

Possibilidades:

* Relatórios;
* Comprovantes;
* Resumos de movimentação;
* Documentos operacionais.

### Momento recomendado

Após a definição dos relatórios.

---

## DP-022 — Estratégia de testes automatizados

### Status

Pendente de detalhamento.

### Descrição

Deverá ser definida a estratégia de testes automatizados.

A estrutura poderá incluir:

* Testes unitários;
* Testes de integração;
* Testes de regras de negócio;
* Testes de interface.

### Momento recomendado

Antes ou durante a implementação dos primeiros módulos.

---

## DP-023 — Estratégia de atualização em produção

### Status

Pendente.

### Descrição

Deverá ser definido o processo de atualização do sistema no servidor.

O processo deverá considerar:

1. Backup;
2. Teste;
3. Atualização;
4. Verificação;
5. Possibilidade de retorno à versão anterior.

### Momento recomendado

Antes da primeira atualização de produção.

---

## DP-024 — Monitoramento da aplicação

### Status

Pendente.

### Descrição

Deverá ser avaliada a necessidade de monitoramento de:

* Disponibilidade;
* Erros;
* Logs;
* Uso de recursos;
* Banco de dados.

### Momento recomendado

Após a entrada em produção.

---

## DP-025 — Política de retenção de logs

### Status

Pendente.

### Descrição

Deverá ser definido por quanto tempo os logs técnicos deverão ser preservados.

A política deverá diferenciar:

* Logs técnicos;
* Logs de auditoria;
* Dados operacionais.

### Momento recomendado

Durante a definição da infraestrutura de produção.

---

# 20.1 Decisões já resolvidas

As seguintes decisões não deverão mais ser tratadas como pendentes:

* Linguagem Python;
* Aplicação web;
* SQLite como banco inicial;
* Desenvolvimento local inicial;
* Produção em servidor Windows;
* Acesso inicial pela rede interna;
* Aproximadamente quatro usuários simultâneos;
* Git e GitHub;
* Separação entre desenvolvimento e produção;
* Preservação do histórico;
* Controle de auditoria;
* Consumo cronológico das compras;
* Devolução ao fornecedor por Nota Fiscal de simples remessa;
* Um único perfil de vendedor para oficina e balcão;
* Perfil de comprador com permissões diferentes;
* Administrador Master;
* Envio de e-mail não faz parte da implementação inicial.

---

# 20.2 Regra para decisões pendentes

Uma decisão pendente somente deverá ser considerada resolvida quando:

1. A decisão for tomada;
2. A decisão for compatível com as regras existentes;
3. O impacto for avaliado;
4. A especificação for atualizada;
5. O histórico for atualizado quando necessário.

Nenhuma decisão pendente deverá ser implementada de forma definitiva sem avaliação de seu impacto no sistema.

---

# 21. HISTÓRICO DE ALTERAÇÕES

### Revisão técnica da versão 1.1.0

* Revisada a definição de backup da Seção 5.12.
* Diferenciada a função do GitHub como ferramenta de versionamento e preservação do código da estratégia de backup do banco de dados de produção.
* Reforçada a necessidade de transações em operações críticas que alterem múltiplos registros relacionados.
* Mantida a estratégia definitiva de backup como decisão pendente até a definição da infraestrutura de produção.
* Revisada a coerência entre as seções de backup, arquitetura, banco de dados e decisões técnicas.

---

### 2026-07-28 — Consolidação da arquitetura web interna

* Corrigida a identificação da plataforma inicial, anteriormente descrita incorretamente como aplicação desktop.
* Consolidada a definição do SIGC como aplicação web interna.
* Definido que a aplicação será executada centralmente em um servidor Windows da empresa.
* Definido que os usuários acessarão o sistema por meio de navegadores conectados à rede interna.
* Reforçado que os computadores dos usuários não deverão acessar diretamente o arquivo SQLite.
* Consolidada a arquitetura em camadas formada por interface web, FastAPI, services, queries, repositories, SQLAlchemy e SQLite.
* Mantida a aplicação mobile nativa fora do escopo inicial.
* Mantida a possibilidade futura de migração do SQLite para PostgreSQL ou outro banco cliente-servidor.

---

## Versão 1.1.0 — 23/07/2026

### Documentação e planejamento

* Consolidada a estrutura geral da especificação oficial do SIGC.
* Definida a documentação como fonte oficial de verdade do projeto.
* Definidas regras para preservação de histórico e rastreabilidade.
* Definida a governança das alterações da especificação.

### Regras de negócio

* Consolidadas as regras relacionadas a compras.
* Consolidadas as regras relacionadas ao consumo cronológico das compras.
* Definida a possibilidade de uma saída consumir itens de múltiplas compras.
* Consolidadas as regras de devolução de clientes.
* Consolidadas as regras de devolução ao fornecedor.
* Definido que a devolução ao fornecedor utilizará Nota Fiscal de simples remessa emitida pela própria empresa.
* Definido que a Nota Fiscal de simples remessa deverá conter as peças, quantidades e referência à Nota Fiscal de origem.
* Definida a possibilidade de devoluções parciais.
* Consolidadas as regras de transferência entre filiais.
* Consolidadas as regras de correção e cancelamento de operações.
* Definida a obrigatoriedade de justificativa para ações que exigirem alteração ou cancelamento.
* Definida a preservação do histórico das operações alteradas ou canceladas.

### Usuários e permissões

* Confirmada a existência de um único perfil de vendedor para vendedores de oficina e balcão.
* Definido que vendedores de oficina e balcão possuirão as mesmas permissões.
* Definido que o tipo de operação determinará se a saída será destinada à oficina ou ao balcão.
* Confirmado que o comprador possuirá permissões diferentes dos vendedores.
* Confirmada a existência do perfil de Administrador Master.
* Definida a possibilidade de evolução futura para permissões mais personalizadas.
* Definida a preservação histórica dos usuários que já tenham realizado operações.

### Arquitetura técnica

* Definido o desenvolvimento inicial como aplicação web.
* Definido Python como linguagem principal.
* Definido o desenvolvimento inicial em um computador local.
* Definido o ambiente de produção inicial em servidor Windows da empresa.
* Definida a futura implantação na rede interna da empresa.
* Definida a separação entre ambiente de desenvolvimento e ambiente de produção.
* Definido o suporte inicial a aproximadamente quatro usuários simultâneos.
* Definida a possibilidade de futura expansão para acesso remoto.
* Definida a possibilidade de futura migração para um banco de dados cliente-servidor.

### Banco de dados

* Definido SQLite como banco de dados inicial.
* Definida a separação entre banco de desenvolvimento e banco de produção.
* Definida a utilização de integridade referencial.
* Definida a utilização de transações para operações que alterem múltiplos registros.
* Definida a utilização de migrations ou mecanismo equivalente para evolução da estrutura do banco.
* Definida a preservação de dados históricos.
* Definida a separação entre dados reais e código-fonte.
* Definida a preparação da arquitetura para futura migração para PostgreSQL ou tecnologia equivalente.

### Auditoria

* Definida a criação de registros de auditoria para operações relevantes.
* Definido o registro do usuário responsável pela operação.
* Definido o registro de data e hora.
* Definido o registro de alterações realizadas.
* Definido o registro de justificativas quando aplicável.
* Definido que os registros de auditoria não deverão ser apagados ou alterados manualmente.

### Interface e Design System

* Definida a necessidade de uma interface moderna, profissional e intuitiva.
* Definida a necessidade de padronização visual entre as telas.
* Definidos princípios de clareza, simplicidade e prevenção de erros.
* Definida a utilização de componentes reutilizáveis.
* Definida a necessidade de um Design System próprio.
* Definida a prioridade inicial para uso em computadores e notebooks.
* Definida a possibilidade de evolução futura para diferentes dispositivos.

### GitHub e controle de versão

* Definido o uso do Git para controle de versões.
* Definido o uso do GitHub para armazenamento do código e documentação.
* Definida a separação entre código-fonte e dados reais.
* Definida a utilização de `.gitignore`.
* Definida a organização de commits por unidades lógicas de trabalho.
* Definida a utilização da branch principal para versões estáveis.
* Definida a possibilidade de utilização de branches para funcionalidades específicas.
* Definida a necessidade de documentação suficiente para reconstrução do ambiente de desenvolvimento.

### Segurança

* Definido que senhas não deverão ser armazenadas em texto puro.
* Definida a utilização de hashing para armazenamento de senhas.
* Definida a necessidade de separação entre configurações e código.
* Definida a necessidade de proteção de informações sensíveis.
* Definida a separação entre dados de desenvolvimento e dados de produção.

### Decisões pendentes

* Criada a seção específica para decisões ainda não definidas.
* Registrada a necessidade de definir futuramente o framework web.
* Registrada a necessidade de definir a estratégia definitiva de execução no servidor Windows.
* Registrada a necessidade de definir a estratégia de backup.
* Registrada a possibilidade de futura integração com e-mail.
* Registrada a possibilidade de futura migração do banco de dados.
* Registrada a possibilidade de futura implementação de acesso remoto.
* Registrada a necessidade de definir detalhes de autenticação e segurança durante a implementação.
* Registrada a necessidade de definir relatórios e exportações durante a evolução do sistema.

---

## Versão 1.0.0 — 23/07/2026

* Criada a especificação inicial do projeto SIGC.
* Definido o nome do sistema.
* Definido o objetivo geral do projeto.
* Definido o autor do projeto.
* Definido o escopo inicial de uma única filial.
* Definido Python como linguagem principal.
* Definido SQLite como banco de dados inicial.
* Criada a estrutura inicial da especificação oficial.

---

### 2026-07-24 — Remoção do controle de preços

O SIGC não deverá registrar preços, valores unitários ou custos financeiros relacionados às compras.

O registro de compras será limitado às informações necessárias para o controle de cascos, incluindo:

* Fornecedor;
* Nota Fiscal de origem;
* Data;
* Peças controladas;
* Quantidades;
* Quantidades disponíveis;
* Rastreabilidade das origens;
* Regras de consumo FIFO.

O campo `unit_price` foi removido da definição de `purchase_items`.

O SIGC continuará fora do escopo de controle financeiro, formação de preços e controle de custos.

---

# 22. Regra de Governança da Especificação

Este documento representa a fonte oficial de verdade do projeto SIGC.

Nenhuma implementação, alteração técnica ou nova regra de negócio deverá contrariar as informações estabelecidas neste documento sem que a alteração seja previamente discutida, aprovada e registrada no histórico de alterações.

Alterações futuras deverão preservar a rastreabilidade das informações existentes e evitar a perda de dados históricos.

Quando uma regra for alterada, a alteração deverá ser registrada de forma clara, incluindo:

* Versão da alteração;
* Data;
* Regra anterior, quando aplicável;
* Nova regra;
* Motivo da alteração.

---

# 23. Instruções para Continuidade do Projeto

Ao retomar o desenvolvimento do SIGC em uma nova conversa ou com outro assistente, este documento deverá ser fornecido como referência principal.

A orientação deverá ser:

> Este documento contém a especificação oficial do projeto SIGC — Sistema Integrado de Gestão de Cascos. Considere todas as informações, regras de negócio, decisões técnicas e restrições contidas neste arquivo antes de sugerir alterações ou implementar novas funcionalidades.

Qualquer sugestão que contradiga uma regra existente deverá ser identificada como uma possível alteração da especificação, e não implementada automaticamente.

---

**Fim da especificação inicial.**

<!-- Documentação oficial do projeto SIGC — versão 1.1.0 -->
```

## `migrations\env.py`

```python
from logging.config import fileConfig

from alembic import context
from sqlalchemy import pool
from sqlalchemy.engine import Connection
from sqlalchemy.engine import engine_from_config

from src.database.connection import Base, engine

from src.models.part import Part
from src.models.purchase import Purchase
from src.models.purchase_item import PurchaseItem
from src.models.role import Role
from src.models.supplier import Supplier
from src.models.supplier_contact import SupplierContact
from src.models.supplier_return import SupplierReturn
from src.models.supplier_return_item import SupplierReturnItem
from src.models.user import User
from src.models.outbound import Outbound
from src.models.outbound_item import OutboundItem
from src.models.outbound_purchase_allocation import (
    OutboundPurchaseAllocation,
)
from src.models.customer_return import CustomerReturn
from src.models.customer_return_allocation import (
    CustomerReturnAllocation,
)
from src.models.customer_return_item import CustomerReturnItem
from src.models.transfer import Transfer
from src.models.transfer_item import TransferItem
from src.models.core_movement import CoreMovement
from src.models.audit_log import AuditLog

config = context.config


if config.config_file_name is not None:
    fileConfig(config.config_file_name)


target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Executa as migrações em modo offline."""

    context.configure(
        url=str(engine.url),
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection: Connection) -> None:
    """Executa as migrações utilizando uma conexão existente."""

    context.configure(
        connection=connection,
        target_metadata=target_metadata,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Executa as migrações em modo online."""

    with engine.connect() as connection:
        do_run_migrations(connection)


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
```

## `migrations\versions\003a3ca7193f_create_outbound_tables.py`

```python
"""create outbound tables

Revision ID: 003a3ca7193f
Revises: bb81601b41f6
Create Date: 2026-07-24 11:30:30.232706

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '003a3ca7193f'
down_revision: Union[str, Sequence[str], None] = 'bb81601b41f6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('outbounds',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('destination_type', sa.String(length=50), nullable=False),
    sa.Column('work_order_number', sa.String(length=100), nullable=True),
    sa.Column('sales_invoice_number', sa.String(length=100), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.String(length=30), nullable=False),
    sa.Column('updated_at', sa.String(length=30), nullable=False),
    sa.Column('status', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['created_by'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('outbound_items',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('outbound_id', sa.Integer(), nullable=False),
    sa.Column('part_id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.String(length=30), nullable=False),
    sa.ForeignKeyConstraint(['outbound_id'], ['outbounds.id'], ),
    sa.ForeignKeyConstraint(['part_id'], ['parts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('outbound_purchase_allocations',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('outbound_item_id', sa.Integer(), nullable=False),
    sa.Column('purchase_item_id', sa.Integer(), nullable=False),
    sa.Column('quantity_allocated', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['outbound_item_id'], ['outbound_items.id'], ),
    sa.ForeignKeyConstraint(['purchase_item_id'], ['purchase_items.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('outbound_purchase_allocations')
    op.drop_table('outbound_items')
    op.drop_table('outbounds')
    # ### end Alembic commands ###
```

## `migrations\versions\1f19757f07c6_create_roles_table.py`

```python
"""create roles table

Revision ID: 1f19757f07c6
Revises:
Create Date: 2026-07-24 10:09:54.706300
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op


revision: str = "1f19757f07c6"
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Cria a tabela de perfis de acesso."""

    op.create_table(
        "roles",
        sa.Column(
            "id",
            sa.Integer(),
            autoincrement=True,
            nullable=False,
        ),
        sa.Column(
            "name",
            sa.String(length=100),
            nullable=True,
        ),
        sa.Column(
            "description",
            sa.Text(),
            nullable=True,
        ),
        sa.Column(
            "created_at",
            sa.String(length=30),
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    """Remove a tabela de perfis de acesso."""

    op.drop_table("roles")
```

## `migrations\versions\330805b7930d_create_parts_suppliers_and_supplier_.py`

```python
"""create parts suppliers and supplier contacts tables

Revision ID: 330805b7930d
Revises: e0a0ee0f0559
Create Date: 2026-07-24 11:11:55.270859

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '330805b7930d'
down_revision: Union[str, Sequence[str], None] = 'e0a0ee0f0559'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('parts',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('part_code', sa.String(length=100), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('is_active', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.String(length=30), nullable=False),
    sa.Column('updated_at', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('suppliers',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('document', sa.String(length=50), nullable=True),
    sa.Column('address', sa.Text(), nullable=True),
    sa.Column('notes', sa.Text(), nullable=True),
    sa.Column('is_active', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.String(length=30), nullable=False),
    sa.Column('updated_at', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('supplier_contacts',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('supplier_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('phone', sa.String(length=50), nullable=True),
    sa.Column('position', sa.String(length=100), nullable=True),
    sa.Column('is_primary', sa.Integer(), nullable=False),
    sa.Column('is_active', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.String(length=30), nullable=False),
    sa.ForeignKeyConstraint(['supplier_id'], ['suppliers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('supplier_contacts')
    op.drop_table('suppliers')
    op.drop_table('parts')
    # ### end Alembic commands ###
```

## `migrations\versions\3909300e7597_create_customer_return_tables.py`

```python
"""create customer return tables

Revision ID: 3909300e7597
Revises: 003a3ca7193f
Create Date: 2026-07-24 13:18:20.776774

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3909300e7597'
down_revision: Union[str, Sequence[str], None] = '003a3ca7193f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customer_returns',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('return_type', sa.String(length=50), nullable=False),
    sa.Column('reference_number', sa.String(length=100), nullable=False),
    sa.Column('customer_name', sa.String(length=200), nullable=False),
    sa.Column('created_by', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.String(length=30), nullable=False),
    sa.Column('updated_at', sa.String(length=30), nullable=False),
    sa.Column('status', sa.String(length=50), nullable=False),
    sa.Column('notes', sa.String(length=1000), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('customer_return_items',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('customer_return_id', sa.Integer(), nullable=False),
    sa.Column('part_id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['customer_return_id'], ['customer_returns.id'], ),
    sa.ForeignKeyConstraint(['part_id'], ['parts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('customer_return_allocations',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('customer_return_item_id', sa.Integer(), nullable=False),
    sa.Column('outbound_item_id', sa.Integer(), nullable=False),
    sa.Column('quantity_allocated', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['customer_return_item_id'], ['customer_return_items.id'], ),
    sa.ForeignKeyConstraint(['outbound_item_id'], ['outbound_items.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('customer_return_allocations')
    op.drop_table('customer_return_items')
    op.drop_table('customer_returns')
    # ### end Alembic commands ###
```

## `migrations\versions\3e391eb4855b_fix_roles_created_at_nullable.py`

```python
"""fix roles created_at nullable

Revision ID: 3e391eb4855b
Revises: b65ceb98865d
Create Date: 2026-07-27 14:26:17.809017

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3e391eb4855b'
down_revision: Union[str, Sequence[str], None] = 'b65ceb98865d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        """
        UPDATE roles
        SET created_at = strftime(
            '%Y-%m-%dT%H:%M:%f',
            'now'
        )
        WHERE created_at IS NULL
        """
    )

    with op.batch_alter_table(
        "roles",
        schema=None,
    ) as batch_op:
        batch_op.alter_column(
            "created_at",
            existing_type=sa.String(length=30),
            nullable=False,
        )


def downgrade() -> None:
    with op.batch_alter_table(
        "roles",
        schema=None,
    ) as batch_op:
        batch_op.alter_column(
            "created_at",
            existing_type=sa.String(length=30),
            nullable=True,
        )
    # ### end Alembic commands ###
```

## `migrations\versions\5920bd9270a0_create_core_movements_and_audit_logs_.py`

```python
"""create core movements and audit logs tables

Revision ID: 5920bd9270a0
Revises: b0195f114054
Create Date: 2026-07-24 14:09:13.140851

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5920bd9270a0'
down_revision: Union[str, Sequence[str], None] = 'b0195f114054'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('audit_logs',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('action', sa.String(length=100), nullable=False),
    sa.Column('module', sa.String(length=100), nullable=False),
    sa.Column('entity_type', sa.String(length=100), nullable=False),
    sa.Column('entity_id', sa.Integer(), nullable=False),
    sa.Column('old_values', sa.Text(), nullable=True),
    sa.Column('new_values', sa.Text(), nullable=True),
    sa.Column('justification', sa.Text(), nullable=True),
    sa.Column('created_at', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('core_movements',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('part_id', sa.Integer(), nullable=False),
    sa.Column('movement_type', sa.String(length=50), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('reference_type', sa.String(length=50), nullable=False),
    sa.Column('reference_id', sa.Integer(), nullable=False),
    sa.Column('created_by', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('core_movements')
    op.drop_table('audit_logs')
    # ### end Alembic commands ###
```

## `migrations\versions\6905c4ac94c4_create_supplier_return_tables.py`

```python
"""create supplier return tables

Revision ID: 6905c4ac94c4
Revises: 3e391eb4855b
Create Date: 2026-07-27 14:41:05.347807

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "6905c4ac94c4"
down_revision: Union[str, Sequence[str], None] = "3e391eb4855b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Cria as tabelas de remessas de cascos aos fornecedores."""

    op.create_table(
        "supplier_returns",
        sa.Column(
            "id",
            sa.Integer(),
            autoincrement=True,
            nullable=False,
        ),
        sa.Column(
            "supplier_id",
            sa.Integer(),
            nullable=False,
        ),
        sa.Column(
            "dispatch_invoice_number",
            sa.String(length=100),
            nullable=False,
        ),
        sa.Column(
            "dispatch_invoice_series",
            sa.String(length=50),
            nullable=True,
        ),
        sa.Column(
            "issue_date",
            sa.String(length=30),
            nullable=False,
        ),
        sa.Column(
            "created_by",
            sa.Integer(),
            nullable=False,
        ),
        sa.Column(
            "created_at",
            sa.String(length=30),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.String(length=30),
            nullable=False,
        ),
        sa.Column(
            "status",
            sa.String(length=50),
            nullable=False,
        ),
        sa.Column(
            "notes",
            sa.String(length=1000),
            nullable=True,
        ),
        sa.ForeignKeyConstraint(
            ["created_by"],
            ["users.id"],
        ),
        sa.ForeignKeyConstraint(
            ["supplier_id"],
            ["suppliers.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "supplier_return_items",
        sa.Column(
            "id",
            sa.Integer(),
            autoincrement=True,
            nullable=False,
        ),
        sa.Column(
            "supplier_return_id",
            sa.Integer(),
            nullable=False,
        ),
        sa.Column(
            "purchase_item_id",
            sa.Integer(),
            nullable=False,
        ),
        sa.Column(
            "quantity",
            sa.Integer(),
            nullable=False,
        ),
        sa.Column(
            "created_at",
            sa.String(length=30),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["purchase_item_id"],
            ["purchase_items.id"],
        ),
        sa.ForeignKeyConstraint(
            ["supplier_return_id"],
            ["supplier_returns.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    """Remove as tabelas de remessas aos fornecedores."""

    op.drop_table("supplier_return_items")
    op.drop_table("supplier_returns")
```

## `migrations\versions\b0195f114054_create_transfers_and_transfer_items_.py`

```python
"""create transfers and transfer items tables

Revision ID: b0195f114054
Revises: 3909300e7597
Create Date: 2026-07-24 13:28:40.877914

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b0195f114054'
down_revision: Union[str, Sequence[str], None] = '3909300e7597'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('transfers',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('origin_branch_id', sa.Integer(), nullable=False),
    sa.Column('destination_branch_id', sa.Integer(), nullable=False),
    sa.Column('invoice_number', sa.String(length=100), nullable=False),
    sa.Column('issue_date', sa.String(length=30), nullable=False),
    sa.Column('status', sa.String(length=50), nullable=False),
    sa.Column('created_by', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.String(length=30), nullable=False),
    sa.ForeignKeyConstraint(['created_by'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('transfer_items',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('transfer_id', sa.Integer(), nullable=False),
    sa.Column('part_id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['part_id'], ['parts.id'], ),
    sa.ForeignKeyConstraint(['transfer_id'], ['transfers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transfer_items')
    op.drop_table('transfers')
    # ### end Alembic commands ###
```

## `migrations\versions\b65ceb98865d_remove_unit_price_from_purchase_items.py`

```python
"""remove unit price from purchase items

Revision ID: b65ceb98865d
Revises: 5920bd9270a0
Create Date: 2026-07-24 17:00:31.730691

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b65ceb98865d'
down_revision: Union[str, Sequence[str], None] = '5920bd9270a0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Remove o campo de preço dos itens de compra."""
    with op.batch_alter_table(
        "purchase_items"
    ) as batch_op:
        batch_op.drop_column("unit_price")


def downgrade() -> None:
    """Restaura o campo de preço dos itens de compra."""
    with op.batch_alter_table(
        "purchase_items"
    ) as batch_op:
        batch_op.add_column(
            sa.Column(
                "unit_price",
                sa.Numeric(
                    precision=12,
                    scale=2,
                ),
                nullable=False,
            )
        )
```

## `migrations\versions\bb81601b41f6_create_purchases_and_purchase_items_.py`

```python
"""create purchases and purchase items tables

Revision ID: bb81601b41f6
Revises: 330805b7930d
Create Date: 2026-07-24 11:21:13.953999

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bb81601b41f6'
down_revision: Union[str, Sequence[str], None] = '330805b7930d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('purchases',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('supplier_id', sa.Integer(), nullable=False),
    sa.Column('invoice_number', sa.String(length=100), nullable=False),
    sa.Column('invoice_series', sa.String(length=50), nullable=True),
    sa.Column('issue_date', sa.String(length=30), nullable=False),
    sa.Column('received_at', sa.String(length=30), nullable=True),
    sa.Column('notes', sa.String(length=1000), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.String(length=30), nullable=False),
    sa.Column('updated_at', sa.String(length=30), nullable=False),
    sa.Column('status', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['created_by'], ['users.id'], ),
    sa.ForeignKeyConstraint(['supplier_id'], ['suppliers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('purchase_items',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('purchase_id', sa.Integer(), nullable=False),
    sa.Column('part_id', sa.Integer(), nullable=False),
    sa.Column('quantity_purchased', sa.Integer(), nullable=False),
    sa.Column('quantity_available', sa.Integer(), nullable=False),
    sa.Column('unit_price', sa.Numeric(precision=12, scale=2), nullable=False),
    sa.Column('created_at', sa.String(length=30), nullable=False),
    sa.ForeignKeyConstraint(['part_id'], ['parts.id'], ),
    sa.ForeignKeyConstraint(['purchase_id'], ['purchases.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('purchase_items')
    op.drop_table('purchases')
    # ### end Alembic commands ###
```

## `migrations\versions\c27a0a62fa9e_add_supplier_and_return_deadline_to_.py`

```python
"""add supplier and return deadline to parts

Revision ID: c27a0a62fa9e
Revises: 6905c4ac94c4
Create Date: 2026-07-28 14:43:09.408031
"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op


revision: str = "c27a0a62fa9e"
down_revision: str | Sequence[str] | None = "6905c4ac94c4"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Adiciona fornecedor e prazo de devolução às peças."""

    with op.batch_alter_table(
        "parts",
        schema=None,
    ) as batch_op:
        batch_op.add_column(
            sa.Column(
                "supplier_id",
                sa.Integer(),
                nullable=False,
            )
        )

        batch_op.add_column(
            sa.Column(
                "return_deadline_days",
                sa.Integer(),
                nullable=False,
            )
        )

        batch_op.create_unique_constraint(
            "uq_parts_supplier_id_part_code",
            [
                "supplier_id",
                "part_code",
            ],
        )

        batch_op.create_foreign_key(
            "fk_parts_supplier_id_suppliers",
            "suppliers",
            ["supplier_id"],
            ["id"],
        )


def downgrade() -> None:
    """Remove fornecedor e prazo de devolução das peças."""

    with op.batch_alter_table(
        "parts",
        schema=None,
    ) as batch_op:
        batch_op.drop_constraint(
            "fk_parts_supplier_id_suppliers",
            type_="foreignkey",
        )

        batch_op.drop_constraint(
            "uq_parts_supplier_id_part_code",
            type_="unique",
        )

        batch_op.drop_column(
            "return_deadline_days",
        )

        batch_op.drop_column(
            "supplier_id",
        )
```

## `migrations\versions\e0a0ee0f0559_create_users_table.py`

```python
"""create users table

Revision ID: e0a0ee0f0559
Revises: 1f19757f07c6
Create Date: 2026-07-24 10:48:39.896922

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e0a0ee0f0559'
down_revision: Union[str, Sequence[str], None] = '1f19757f07c6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('full_name', sa.String(length=200), nullable=False),
    sa.Column('username', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('password_hash', sa.String(length=255), nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.Column('is_active', sa.Integer(), nullable=False),
    sa.Column('last_login_at', sa.String(length=30), nullable=True),
    sa.Column('created_at', sa.String(length=30), nullable=False),
    sa.Column('updated_at', sa.String(length=30), nullable=False),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
```

## `README.md`

```markdown
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
```

## `requirements.txt`

```text
ÿþa l e m b i c = = 1 . 1 8 . 5 
 
 a n n o t a t e d - d o c = = 0 . 0 . 4 
 
 a n n o t a t e d - t y p e s = = 0 . 8 . 0 
 
 a n y i o = = 4 . 1 4 . 2 
 
 a r g o n 2 - c f f i = = 2 5 . 1 . 0 
 
 a r g o n 2 - c f f i - b i n d i n g s = = 2 5 . 1 . 0 
 
 c f f i = = 2 . 1 . 0 
 
 c l i c k = = 8 . 4 . 2 
 
 c o l o r a m a = = 0 . 4 . 6 
 
 f a s t a p i = = 0 . 1 3 9 . 2 
 
 g r e e n l e t = = 3 . 5 . 4 
 
 h 1 1 = = 0 . 1 6 . 0 
 
 i d n a = = 3 . 1 8 
 
 i n i c o n f i g = = 2 . 3 . 0 
 
 M a k o = = 1 . 3 . 1 2 
 
 M a r k u p S a f e = = 3 . 0 . 3 
 
 p a c k a g i n g = = 2 6 . 2 
 
 p l u g g y = = 1 . 6 . 0 
 
 p w d l i b = = 0 . 3 . 0 
 
 p y c p a r s e r = = 3 . 0 
 
 p y d a n t i c = = 2 . 1 3 . 4 
 
 p y d a n t i c _ c o r e = = 2 . 4 6 . 4 
 
 P y g m e n t s = = 2 . 2 0 . 0 
 
 p y t e s t = = 9 . 1 . 1 
 
 S Q L A l c h e m y = = 2 . 0 . 5 1 
 
 s t a r l e t t e = = 1 . 3 . 1 
 
 t y p i n g - i n s p e c t i o n = = 0 . 4 . 2 
 
 t y p i n g _ e x t e n s i o n s = = 4 . 1 6 . 0 
 
 u v i c o r n = = 0 . 5 1 . 0 
 
 
```

## `scripts\__init__.py`

```python

```

## `scripts\generate_project_snapshot.py`

```python
from __future__ import annotations

import os
import sqlite3
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Iterable


PROJECT_ROOT = Path(__file__).resolve().parent.parent

OUTPUT_DIRECTORY = PROJECT_ROOT / "snapshots"

TIMESTAMP = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

OUTPUT_FILE = (
    OUTPUT_DIRECTORY
    / f"sigc_project_snapshot_{TIMESTAMP}.md"
)


IGNORED_DIRECTORIES = {
    ".git",
    ".idea",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    ".venv",
    ".vscode",
    "__pycache__",
    "build",
    "dist",
    "htmlcov",
    "node_modules",
    "snapshots",
}


IGNORED_FILES = {
    ".coverage",
    ".env",
    ".env.local",
    ".env.production",
    ".env.test",
    "coverage.xml",
}


IGNORED_SUFFIXES = {
    ".db",
    ".db-journal",
    ".exe",
    ".gif",
    ".ico",
    ".jpeg",
    ".jpg",
    ".log",
    ".pdf",
    ".png",
    ".pyc",
    ".pyo",
    ".sqlite",
    ".sqlite3",
    ".svg",
    ".webp",
    ".zip",
}


ALLOWED_FILES_WITHOUT_SUFFIX = {
    "Dockerfile",
    "LICENSE",
    "Makefile",
    "Procfile",
}


ALLOWED_SUFFIXES = {
    ".cfg",
    ".css",
    ".csv",
    ".html",
    ".ini",
    ".js",
    ".json",
    ".md",
    ".ps1",
    ".py",
    ".sql",
    ".toml",
    ".txt",
    ".yaml",
    ".yml",
}


MAX_FILE_SIZE_BYTES = 500_000


PREFERRED_DATABASE_NAMES = (
    "sigc.db",
    "database.db",
    "app.db",
    "sqlite.db",
    "sigc.sqlite",
    "database.sqlite",
    "app.sqlite",
)


def should_ignore_path(path: Path) -> bool:
    """Verifica se um arquivo ou diretório deve ser ignorado."""

    relative_parts = path.relative_to(PROJECT_ROOT).parts

    if any(
        part in IGNORED_DIRECTORIES
        for part in relative_parts
    ):
        return True

    if path.name in IGNORED_FILES:
        return True

    if path.suffix.lower() in IGNORED_SUFFIXES:
        return True

    return False


def should_include_file(path: Path) -> bool:
    """Verifica se o arquivo deve aparecer no snapshot."""

    if not path.is_file():
        return False

    if should_ignore_path(path):
        return False

    if path.stat().st_size > MAX_FILE_SIZE_BYTES:
        return False

    if path.name in ALLOWED_FILES_WITHOUT_SUFFIX:
        return True

    return path.suffix.lower() in ALLOWED_SUFFIXES


def get_project_files() -> list[Path]:
    """Retorna os arquivos textuais relevantes do projeto."""

    files = [
        path
        for path in PROJECT_ROOT.rglob("*")
        if should_include_file(path)
    ]

    return sorted(
        files,
        key=lambda item: str(
            item.relative_to(PROJECT_ROOT)
        ).lower(),
    )


def build_directory_tree(files: Iterable[Path]) -> str:
    """Monta uma árvore simples dos arquivos incluídos."""

    lines: list[str] = []

    for path in files:
        relative_path = path.relative_to(PROJECT_ROOT)
        depth = len(relative_path.parts) - 1
        indentation = "    " * depth

        lines.append(
            f"{indentation}- {relative_path.name}"
        )

    return "\n".join(lines)


def read_text_file(path: Path) -> str:
    """Lê um arquivo textual usando codificações comuns."""

    encodings = (
        "utf-8",
        "utf-8-sig",
        "latin-1",
    )

    for encoding in encodings:
        try:
            return path.read_text(encoding=encoding)
        except UnicodeDecodeError:
            continue

    return (
        "[Arquivo não pôde ser decodificado "
        "como texto.]"
    )


def detect_language(path: Path) -> str:
    """Retorna a linguagem para o bloco Markdown."""

    language_by_suffix = {
        ".cfg": "ini",
        ".css": "css",
        ".csv": "csv",
        ".html": "html",
        ".ini": "ini",
        ".js": "javascript",
        ".json": "json",
        ".md": "markdown",
        ".ps1": "powershell",
        ".py": "python",
        ".sql": "sql",
        ".toml": "toml",
        ".txt": "text",
        ".yaml": "yaml",
        ".yml": "yaml",
    }

    if path.name == "Dockerfile":
        return "dockerfile"

    if path.name == "Makefile":
        return "makefile"

    return language_by_suffix.get(
        path.suffix.lower(),
        "text",
    )


def run_command(command: list[str]) -> str:
    """Executa um comando e retorna sua saída."""

    try:
        result = subprocess.run(
            command,
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=False,
        )
    except FileNotFoundError:
        return (
            f"Comando não encontrado: "
            f"{' '.join(command)}"
        )
    except Exception as error:
        return (
            "Erro ao executar o comando "
            f"{' '.join(command)}: {error}"
        )

    output_parts: list[str] = []

    if result.stdout.strip():
        output_parts.append(result.stdout.strip())

    if result.stderr.strip():
        output_parts.append(
            "STDERR:\n"
            f"{result.stderr.strip()}"
        )

    if not output_parts:
        output_parts.append(
            f"Comando finalizado com código "
            f"{result.returncode}, sem saída."
        )

    return "\n\n".join(output_parts)


def find_sqlite_database() -> Path | None:
    """
    Procura um banco SQLite do projeto.

    A busca não inclui ambientes virtuais, snapshots,
    caches ou diretórios ignorados.
    """

    for database_name in PREFERRED_DATABASE_NAMES:
        candidate = PROJECT_ROOT / database_name

        if candidate.exists():
            return candidate

    candidates: list[Path] = []

    for suffix in ("*.db", "*.sqlite", "*.sqlite3"):
        for path in PROJECT_ROOT.rglob(suffix):
            if should_ignore_path(path):
                continue

            if path.is_file():
                candidates.append(path)

    if not candidates:
        return None

    return sorted(
        candidates,
        key=lambda item: str(item).lower(),
    )[0]


def quote_sqlite_identifier(identifier: str) -> str:
    """Escapa identificadores usados em consultas SQLite."""

    return '"' + identifier.replace('"', '""') + '"'


def get_database_snapshot(
    database_path: Path,
) -> str:
    """
    Coleta somente metadados e contagens do SQLite.

    Os registros completos não são exportados.
    """

    lines: list[str] = []

    relative_database_path = database_path.relative_to(
        PROJECT_ROOT
    )

    lines.append(
        f"Banco detectado: `{relative_database_path}`"
    )
    lines.append("")

    try:
        connection = sqlite3.connect(database_path)
        connection.row_factory = sqlite3.Row
    except sqlite3.Error as error:
        return (
            "Não foi possível abrir o banco SQLite: "
            f"{error}"
        )

    try:
        cursor = connection.cursor()

        tables = cursor.execute(
            """
            SELECT name
            FROM sqlite_master
            WHERE type = 'table'
              AND name NOT LIKE 'sqlite_%'
            ORDER BY name
            """
        ).fetchall()

        if not tables:
            lines.append(
                "Nenhuma tabela encontrada no banco."
            )
            return "\n".join(lines)

        for table_row in tables:
            table_name = str(table_row["name"])
            quoted_table = quote_sqlite_identifier(
                table_name
            )

            lines.append(f"## Tabela `{table_name}`")
            lines.append("")

            try:
                total = cursor.execute(
                    f"SELECT COUNT(*) FROM {quoted_table}"
                ).fetchone()[0]

                lines.append(
                    f"Quantidade de registros: `{total}`"
                )
                lines.append("")
            except sqlite3.Error as error:
                lines.append(
                    "Não foi possível contar os registros: "
                    f"`{error}`"
                )
                lines.append("")

            lines.append("### Colunas")
            lines.append("")
            lines.append(
                "```text"
            )

            columns = cursor.execute(
                f"PRAGMA table_info({quoted_table})"
            ).fetchall()

            for column in columns:
                lines.append(
                    " | ".join(
                        [
                            f"cid={column['cid']}",
                            f"name={column['name']}",
                            f"type={column['type']}",
                            f"notnull={column['notnull']}",
                            f"default={column['dflt_value']}",
                            f"pk={column['pk']}",
                        ]
                    )
                )

            lines.append("```")
            lines.append("")

            lines.append("### Índices")
            lines.append("")
            lines.append("```text")

            indexes = cursor.execute(
                f"PRAGMA index_list({quoted_table})"
            ).fetchall()

            if not indexes:
                lines.append("Nenhum índice encontrado.")
            else:
                for index in indexes:
                    lines.append(str(tuple(index)))

                    index_name = str(index["name"])
                    quoted_index = quote_sqlite_identifier(
                        index_name
                    )

                    index_columns = cursor.execute(
                        f"PRAGMA index_info({quoted_index})"
                    ).fetchall()

                    for index_column in index_columns:
                        lines.append(
                            "    "
                            f"{tuple(index_column)}"
                        )

            lines.append("```")
            lines.append("")

            lines.append("### Chaves estrangeiras")
            lines.append("")
            lines.append("```text")

            foreign_keys = cursor.execute(
                f"PRAGMA foreign_key_list({quoted_table})"
            ).fetchall()

            if not foreign_keys:
                lines.append(
                    "Nenhuma chave estrangeira encontrada."
                )
            else:
                for foreign_key in foreign_keys:
                    lines.append(str(tuple(foreign_key)))

            lines.append("```")
            lines.append("")

        if any(
            str(table["name"]) == "parts"
            for table in tables
        ):
            lines.append(
                "## Diagnóstico específico de `parts`"
            )
            lines.append("")

            duplicate_codes = cursor.execute(
                """
                SELECT
                    part_code,
                    COUNT(*) AS total
                FROM parts
                GROUP BY part_code
                HAVING COUNT(*) > 1
                ORDER BY part_code
                """
            ).fetchall()

            lines.append("### Códigos duplicados")
            lines.append("")
            lines.append("```text")

            if not duplicate_codes:
                lines.append(
                    "Nenhum part_code duplicado."
                )
            else:
                for row in duplicate_codes:
                    lines.append(
                        f"{row['part_code']} | "
                        f"total={row['total']}"
                    )

            lines.append("```")
            lines.append("")

            sample_parts = cursor.execute(
                """
                SELECT
                    id,
                    part_code,
                    name,
                    description,
                    is_active,
                    created_at,
                    updated_at
                FROM parts
                ORDER BY id
                LIMIT 30
                """
            ).fetchall()

            lines.append(
                "### Peças existentes"
            )
            lines.append("")
            lines.append(
                "A amostra abaixo ajuda a identificar "
                "a origem e o significado dos 26 registros."
            )
            lines.append("")
            lines.append("```text")

            if not sample_parts:
                lines.append(
                    "Nenhuma peça cadastrada."
                )
            else:
                for row in sample_parts:
                    lines.append(
                        " | ".join(
                            [
                                f"id={row['id']}",
                                f"part_code={row['part_code']}",
                                f"name={row['name']}",
                                (
                                    "description="
                                    f"{row['description']}"
                                ),
                                (
                                    "is_active="
                                    f"{row['is_active']}"
                                ),
                                (
                                    "created_at="
                                    f"{row['created_at']}"
                                ),
                                (
                                    "updated_at="
                                    f"{row['updated_at']}"
                                ),
                            ]
                        )
                    )

            lines.append("```")
            lines.append("")

    except sqlite3.Error as error:
        lines.append(
            "Erro durante a leitura do SQLite: "
            f"`{error}`"
        )
    finally:
        connection.close()

    return "\n".join(lines)


def generate_snapshot() -> Path:
    """Gera o snapshot completo em Markdown."""

    OUTPUT_DIRECTORY.mkdir(
        parents=True,
        exist_ok=True,
    )

    project_files = get_project_files()

    sections: list[str] = [
        "# Snapshot do projeto SIGC",
        "",
        f"Gerado em: `{datetime.now().isoformat()}`",
        "",
        f"Diretório do projeto: `{PROJECT_ROOT}`",
        "",
        "## Avisos",
        "",
        "- O conteúdo de `.env` não foi incluído.",
        "- Bancos SQLite completos não foram incluídos.",
        "- Foram incluídos apenas metadados e amostras "
        "necessárias para análise.",
        "- `.venv`, `.git`, caches e arquivos binários "
        "foram ignorados.",
        "",
        "## Árvore de arquivos",
        "",
        "```text",
        build_directory_tree(project_files),
        "```",
        "",
        "## Estado do Git",
        "",
        "```text",
        run_command(
            ["git", "status", "--short", "--branch"]
        ),
        "```",
        "",
        "## Últimos commits",
        "",
        "```text",
        run_command(
            [
                "git",
                "log",
                "--oneline",
                "--decorate",
                "-15",
            ]
        ),
        "```",
        "",
        "## Alembic current",
        "",
        "```text",
        run_command(
            [
                os.fspath(
                    PROJECT_ROOT
                    / ".venv"
                    / "Scripts"
                    / "python.exe"
                ),
                "-m",
                "alembic",
                "current",
            ]
        ),
        "```",
        "",
        "## Alembic heads",
        "",
        "```text",
        run_command(
            [
                os.fspath(
                    PROJECT_ROOT
                    / ".venv"
                    / "Scripts"
                    / "python.exe"
                ),
                "-m",
                "alembic",
                "heads",
            ]
        ),
        "```",
        "",
        "## Alembic history",
        "",
        "```text",
        run_command(
            [
                os.fspath(
                    PROJECT_ROOT
                    / ".venv"
                    / "Scripts"
                    / "python.exe"
                ),
                "-m",
                "alembic",
                "history",
                "--verbose",
            ]
        ),
        "```",
        "",
    ]

    database_path = find_sqlite_database()

    sections.extend(
        [
            "# Banco de dados",
            "",
        ]
    )

    if database_path is None:
        sections.extend(
            [
                "Nenhum arquivo SQLite foi encontrado "
                "automaticamente.",
                "",
            ]
        )
    else:
        sections.extend(
            [
                get_database_snapshot(database_path),
                "",
            ]
        )

    sections.extend(
        [
            "# Conteúdo dos arquivos",
            "",
        ]
    )

    for path in project_files:
        relative_path = path.relative_to(PROJECT_ROOT)
        language = detect_language(path)
        content = read_text_file(path)

        sections.extend(
            [
                f"## `{relative_path}`",
                "",
                f"```{language}",
                content.rstrip(),
                "```",
                "",
            ]
        )

    OUTPUT_FILE.write_text(
        "\n".join(sections),
        encoding="utf-8",
    )

    return OUTPUT_FILE


def main() -> None:
    """Ponto de entrada do script."""

    try:
        snapshot_path = generate_snapshot()
    except Exception as error:
        print(
            "Não foi possível gerar o snapshot."
        )
        print(
            f"Erro: {type(error).__name__}: {error}"
        )
        raise SystemExit(1) from error

    print("Snapshot gerado com sucesso:")
    print(snapshot_path)


if __name__ == "__main__":
    main()
```

## `scripts\test_customer_return_service.py`

```python
from datetime import datetime

from src.database.connection import SessionLocal
from src.models.part import Part
from src.models.supplier import Supplier
from src.repositories.customer_return_allocation_repository import (
    CustomerReturnAllocationRepository,
)
from src.repositories.customer_return_item_repository import (
    CustomerReturnItemRepository,
)
from src.repositories.customer_return_repository import (
    CustomerReturnRepository,
)
from src.repositories.outbound_item_repository import (
    OutboundItemRepository,
)
from src.repositories.outbound_purchase_allocation_repository import (
    OutboundPurchaseAllocationRepository,
)
from src.repositories.outbound_repository import (
    OutboundRepository,
)
from src.repositories.part_repository import PartRepository
from src.repositories.purchase_item_repository import (
    PurchaseItemRepository,
)
from src.repositories.purchase_repository import (
    PurchaseRepository,
)
from src.repositories.supplier_repository import (
    SupplierRepository,
)
from src.services.customer_return_service import (
    CustomerReturnService,
)
from src.services.outbound_service import OutboundService
from src.services.purchase_service import PurchaseService


def main() -> None:
    session = SessionLocal()

    try:
        supplier_repository = SupplierRepository(session)
        part_repository = PartRepository(session)
        purchase_repository = PurchaseRepository(session)
        purchase_item_repository = (
            PurchaseItemRepository(session)
        )

        outbound_repository = OutboundRepository(session)
        outbound_item_repository = (
            OutboundItemRepository(session)
        )
        outbound_purchase_allocation_repository = (
            OutboundPurchaseAllocationRepository(session)
        )

        customer_return_repository = (
            CustomerReturnRepository(session)
        )
        customer_return_item_repository = (
            CustomerReturnItemRepository(session)
        )
        customer_return_allocation_repository = (
            CustomerReturnAllocationRepository(session)
        )

        suppliers = supplier_repository.list_all()

        if not suppliers:
            supplier_entity = Supplier(
                name="Fornecedor de Teste Devolucao",
                document="00.000.000/0001-02",
                address="Endereco de Teste",
                notes=(
                    "Registro criado para teste "
                    "de devolucao de cliente."
                ),
                is_active=1,
            )

            supplier_entity = supplier_repository.add(
                supplier_entity
            )
        else:
            supplier_entity = suppliers[0]

        test_suffix = datetime.now().strftime(
            "%Y%m%d%H%M%S"
        )

        part_entity = Part(
            part_code=(
                f"TEST-RETURN-{test_suffix}"
            ),
            name="Peca de Teste Devolucao",
            description=(
                "Peca criada exclusivamente para "
                "teste de devolucao de cliente."
            ),
            is_active=1,
        )

        part_entity = part_repository.add(
            part_entity
        )

        purchase_service = PurchaseService(
            purchase_repository=purchase_repository,
            purchase_item_repository=(
                purchase_item_repository
            ),
            supplier_repository=supplier_repository,
            part_repository=part_repository,
        )

        first_purchase = (
            purchase_service.create_purchase(
                supplier_id=supplier_entity.id,
                invoice_number=(
                    f"NF-RETURN-001-{test_suffix}"
                ),
                invoice_series="1",
                issue_date="2026-07-24",
                created_by=1,
                status="RECEIVED",
                notes=(
                    "Primeira compra criada para "
                    "teste de devolucao."
                ),
            )
        )

        first_purchase_item = (
            purchase_service.add_item(
                purchase_id=first_purchase.id,
                part_id=part_entity.id,
                quantity_purchased=5,
            )
        )

        second_purchase = (
            purchase_service.create_purchase(
                supplier_id=supplier_entity.id,
                invoice_number=(
                    f"NF-RETURN-002-{test_suffix}"
                ),
                invoice_series="1",
                issue_date="2026-07-25",
                created_by=1,
                status="RECEIVED",
                notes=(
                    "Segunda compra criada para "
                    "teste de devolucao."
                ),
            )
        )

        second_purchase_item = (
            purchase_service.add_item(
                purchase_id=second_purchase.id,
                part_id=part_entity.id,
                quantity_purchased=10,
            )
        )

        outbound_service = OutboundService(
            outbound_repository=outbound_repository,
            outbound_item_repository=(
                outbound_item_repository
            ),
            outbound_purchase_allocation_repository=(
                outbound_purchase_allocation_repository
            ),
            purchase_item_repository=(
                purchase_item_repository
            ),
            part_repository=part_repository,
        )

        outbound = outbound_service.create_outbound(
            destination_type="WORKSHOP",
            work_order_number=(
                f"OS-RETURN-{test_suffix}"
            ),
            created_by=1,
            status="COMPLETED",
        )

        outbound_item = outbound_service.add_item(
            outbound_id=outbound.id,
            part_id=part_entity.id,
            quantity=8,
        )

        outbound_allocations = (
            outbound_purchase_allocation_repository
            .list_by_outbound_item(
                outbound_item.id
            )
        )

        customer_return_service = (
            CustomerReturnService(
                customer_return_repository=(
                    customer_return_repository
                ),
                customer_return_item_repository=(
                    customer_return_item_repository
                ),
                customer_return_allocation_repository=(
                    customer_return_allocation_repository
                ),
                outbound_item_repository=(
                    outbound_item_repository
                ),
                part_repository=part_repository,
            )
        )

        customer_return = (
            customer_return_service
            .create_customer_return(
                return_type="CUSTOMER",
                reference_number=(
                    f"DEV-RETURN-{test_suffix}"
                ),
                customer_name=(
                    "Cliente de Teste"
                ),
                created_by=1,
                status="COMPLETED",
                notes=(
                    "Devolucao criada para teste "
                    "de rastreabilidade."
                ),
            )
        )

        customer_return_item = (
            customer_return_service.add_item(
                customer_return_id=(
                    customer_return.id
                ),
                part_id=part_entity.id,
                quantity=6,
            )
        )

        return_allocations = (
            customer_return_allocation_repository
            .list_by_return_item(
                customer_return_item.id
            )
        )

        session.commit()

        print(
            "Devolucao de cliente criada "
            "com sucesso!"
        )

        print(
            f"ID da devolucao: "
            f"{customer_return.id}"
        )

        print(
            f"ID do item devolvido: "
            f"{customer_return_item.id}"
        )

        print(
            f"Quantidade devolvida: "
            f"{customer_return_item.quantity}"
        )

        print()
        print(
            "Alocacoes da saida:"
        )

        for allocation in outbound_allocations:
            print(
                f"- PurchaseItem "
                f"{allocation.purchase_item_id}: "
                f"{allocation.quantity_allocated} "
                "unidade(s)"
            )

        print()
        print(
            "Alocacoes da devolucao:"
        )

        for allocation in return_allocations:
            print(
                f"- OutboundItem "
                f"{allocation.outbound_item_id}: "
                f"{allocation.quantity_allocated} "
                "unidade(s)"
            )

        print()
        print(
            "Resultado esperado:"
        )

        print(
            "- Saida de 8 unidades criada."
        )

        print(
            "- Devolucao de 6 unidades criada."
        )

        print(
            "- As 6 unidades foram vinculadas "
            "ao OutboundItem da saida."
        )

        print()
        print(
            "Quantidade disponivel das compras "
            "apos a saida:"
        )

        print(
            f"- PurchaseItem "
            f"{first_purchase_item.id}: "
            f"{first_purchase_item.quantity_available}"
        )

        print(
            f"- PurchaseItem "
            f"{second_purchase_item.id}: "
            f"{second_purchase_item.quantity_available}"
        )

    except Exception:
        session.rollback()
        raise

    finally:
        session.close()

if __name__ == "__main__":
    main()
```

## `scripts\test_database.py`

```python
from sqlalchemy import inspect

from src.database.connection import engine


def main() -> None:
    inspector = inspect(engine)

    tables = inspector.get_table_names()

    print("Tabelas encontradas:")
    for table in tables:
        print(f"- {table}")

    tables_to_check = [
        "roles",
        "users",
        "parts",
        "suppliers",
        "supplier_contacts",
    ]

    for table in tables_to_check:
        print(f"\nColunas de {table}:")
        for column in inspector.get_columns(table):
            print(f"- {column['name']}")

    print("\nChaves estrangeiras:")
    for table in tables_to_check:
        foreign_keys = inspector.get_foreign_keys(table)

        for foreign_key in foreign_keys:
            print(
                f"- {table}.{foreign_key['constrained_columns']} "
                f"-> {foreign_key['referred_table']}."
                f"{foreign_key['referred_columns']}"
            )


if __name__ == "__main__":
    main()
```

## `scripts\test_outbound_service.py`

```python
from datetime import datetime

from src.database.connection import SessionLocal
from src.models.part import Part
from src.models.purchase import Purchase
from src.models.supplier import Supplier
from src.repositories.outbound_item_repository import (
    OutboundItemRepository,
)
from src.repositories.outbound_purchase_allocation_repository import (
    OutboundPurchaseAllocationRepository,
)
from src.repositories.outbound_repository import (
    OutboundRepository,
)
from src.repositories.part_repository import PartRepository
from src.repositories.purchase_item_repository import (
    PurchaseItemRepository,
)
from src.repositories.purchase_repository import (
    PurchaseRepository,
)
from src.repositories.supplier_repository import (
    SupplierRepository,
)
from src.services.outbound_service import OutboundService
from src.services.purchase_service import PurchaseService


def main() -> None:
    session = SessionLocal()

    try:
        supplier_repository = SupplierRepository(session)
        part_repository = PartRepository(session)
        purchase_repository = PurchaseRepository(session)
        purchase_item_repository = (
            PurchaseItemRepository(session)
        )

        outbound_repository = OutboundRepository(session)
        outbound_item_repository = (
            OutboundItemRepository(session)
        )
        outbound_purchase_allocation_repository = (
            OutboundPurchaseAllocationRepository(session)
        )

        suppliers = supplier_repository.list_all()

        if not suppliers:
            supplier_entity = Supplier(
                name="Fornecedor de Teste FIFO",
                document="00.000.000/0001-01",
                address="Endereço de Teste",
                notes="Registro criado para teste FIFO.",
                is_active=1,
            )

            supplier_entity = supplier_repository.add(
                supplier_entity
            )
        else:
            supplier_entity = suppliers[0]

        test_suffix = datetime.now().strftime(
            "%Y%m%d%H%M%S"
        )

        part_entity = Part(
            part_code=f"TEST-FIFO-{test_suffix}",
            name="Peça de Teste FIFO",
            description=(
                "Peça criada exclusivamente para "
                "teste da regra FIFO."
            ),
            is_active=1,
        )

        part_entity = part_repository.add(
            part_entity
        )

        purchase_service = PurchaseService(
            purchase_repository=purchase_repository,
            purchase_item_repository=(
                purchase_item_repository
            ),
            supplier_repository=supplier_repository,
            part_repository=part_repository,
        )

        first_purchase = (
            purchase_service.create_purchase(
                supplier_id=supplier_entity.id,
                invoice_number=(
                    f"NF-FIFO-001-{test_suffix}"
                ),
                invoice_series="1",
                issue_date="2026-07-24",
                created_by=1,
                status="RECEIVED",
                notes=(
                    "Primeira compra criada para "
                    "teste FIFO."
                ),
            )
        )

        first_purchase_item = (
            purchase_service.add_item(
                purchase_id=first_purchase.id,
                part_id=part_entity.id,
                quantity_purchased=5,
            )
        )

        second_purchase = (
            purchase_service.create_purchase(
                supplier_id=supplier_entity.id,
                invoice_number=(
                    f"NF-FIFO-002-{test_suffix}"
                ),
                invoice_series="1",
                issue_date="2026-07-25",
                created_by=1,
                status="RECEIVED",
                notes=(
                    "Segunda compra criada para "
                    "teste FIFO."
                ),
            )
        )

        second_purchase_item = (
            purchase_service.add_item(
                purchase_id=second_purchase.id,
                part_id=part_entity.id,
                quantity_purchased=10,
            )
        )

        outbound_service = OutboundService(
            outbound_repository=outbound_repository,
            outbound_item_repository=(
                outbound_item_repository
            ),
            outbound_purchase_allocation_repository=(
                outbound_purchase_allocation_repository
            ),
            purchase_item_repository=(
                purchase_item_repository
            ),
            part_repository=part_repository,
        )

        outbound = outbound_service.create_outbound(
            destination_type="WORKSHOP",
            work_order_number=(
                f"OS-FIFO-{test_suffix}"
            ),
            created_by=1,
            status="COMPLETED",
        )

        outbound_item = outbound_service.add_item(
            outbound_id=outbound.id,
            part_id=part_entity.id,
            quantity=8,
        )

        allocations = (
            outbound_purchase_allocation_repository
            .list_by_outbound_item(
                outbound_item.id
            )
        )

        session.commit()

        print("Saída criada com sucesso!")
        print(
            f"ID da saída: {outbound.id}"
        )
        print(
            "ID do item de saída: "
            f"{outbound_item.id}"
        )
        print(
            "Quantidade retirada: "
            f"{outbound_item.quantity}"
        )

        print()
        print("Alocações FIFO:")

        for allocation in allocations:
            print(
                f"- PurchaseItem "
                f"{allocation.purchase_item_id}: "
                f"{allocation.quantity_allocated} "
                "unidade(s)"
            )

        print()
        print(
            "Quantidade disponível após a saída:"
        )

        print(
            f"- PurchaseItem "
            f"{first_purchase_item.id}: "
            f"{first_purchase_item.quantity_available}"
        )

        print(
            f"- PurchaseItem "
            f"{second_purchase_item.id}: "
            f"{second_purchase_item.quantity_available}"
        )

    except Exception:
        session.rollback()
        raise

    finally:
        session.close()


if __name__ == "__main__":
    main()
```

## `scripts\test_purchase_service.py`

```python
from src.database.connection import SessionLocal
from src.models.part import Part
from src.models.purchase import Purchase
from src.models.supplier import Supplier
from src.repositories.part_repository import PartRepository
from src.repositories.purchase_item_repository import (
    PurchaseItemRepository,
)
from src.repositories.purchase_repository import PurchaseRepository
from src.repositories.supplier_repository import SupplierRepository
from src.services.purchase_service import PurchaseService


def main() -> None:
    session = SessionLocal()

    try:
        supplier_repository = SupplierRepository(session)
        part_repository = PartRepository(session)
        purchase_repository = PurchaseRepository(session)
        purchase_item_repository = PurchaseItemRepository(session)

        suppliers = supplier_repository.list_all()

        if not suppliers:
            supplier_entity = Supplier(
                name="Fornecedor de Teste",
                document="00.000.000/0001-00",
                address="Endereço de Teste",
                notes="Registro criado para teste.",
                is_active=1,
            )

            supplier_entity = supplier_repository.add(
                supplier_entity
            )
        else:
            supplier_entity = suppliers[0]

        parts = part_repository.list_all()

        if not parts:
            part_entity = Part(
                part_code="TEST-001",
                name="Peça de Teste",
                description="Registro criado para teste.",
                is_active=1,
            )

            part_entity = part_repository.add(
                part_entity
            )
        else:
            part_entity = parts[0]

        purchase_service = PurchaseService(
            purchase_repository=purchase_repository,
            purchase_item_repository=purchase_item_repository,
            supplier_repository=supplier_repository,
            part_repository=part_repository,
        )

        purchase = purchase_service.create_purchase(
            supplier_id=supplier_entity.id,
            invoice_number="NF-TEST-001",
            invoice_series="1",
            issue_date="2026-07-24",
            created_by=1,
            status="RECEIVED",
            notes="Compra criada através de teste.",
        )

        purchase_item = purchase_service.add_item(
            purchase_id=purchase.id,
            part_id=part_entity.id,
            quantity_purchased=10,
        )

        session.commit()

        print("Compra criada com sucesso!")
        print(f"ID da compra: {purchase.id}")
        print(f"ID do item: {purchase_item.id}")
        print(
            "Quantidade comprada: "
            f"{purchase_item.quantity_purchased}"
        )
        print(
            "Quantidade disponível: "
            f"{purchase_item.quantity_available}"
        )

    except Exception:
        session.rollback()
        raise

    finally:
        session.close()


if __name__ == "__main__":
    main()
```

## `scripts\test_purchase_tracking_query.py`

```python
from src.database.connection import SessionLocal
from src.queries.purchase_tracking_query import PurchaseTrackingQuery
from src.repositories.purchase_repository import PurchaseRepository
from src.services.purchase_tracking_service import PurchaseTrackingService


def main() -> None:
    session = SessionLocal()

    try:
        purchases = PurchaseRepository(session).list_all()

        if not purchases:
            print(
                "Nenhuma compra cadastrada. Execute primeiro "
                "scripts/test_purchase_service.py."
            )
            return

        query = PurchaseTrackingQuery(session)
        service = PurchaseTrackingService(query)

        tracking = service.get_purchase_tracking(
            purchases[0].id
        )

        print("Acompanhamento da compra")
        print(f"Compra: {tracking.purchase_id}")
        print(
            "Nota Fiscal: "
            f"{tracking.invoice_number}"
            f"/{tracking.invoice_series or '-'}"
        )
        print(f"Fornecedor: {tracking.supplier_name}")
        print(f"Data de emissão: {tracking.issue_date}")
        print(f"Status da compra: {tracking.purchase_status}")

        for item in tracking.items:
            assert item.quantity_outbound >= 0
            assert item.quantity_returned_by_customer >= 0
            assert item.quantity_returned_to_supplier >= 0
            assert (
                item.quantity_returned_by_customer
                <= item.quantity_outbound
            )
            assert (
                item.quantity_returned_to_supplier
                <= item.quantity_returned_by_customer
            )

            print("-")
            print(
                f"Item {item.purchase_item_id}: "
                f"{item.part_code} - {item.part_name}"
            )
            print(f"Comprada: {item.quantity_purchased}")
            print(f"Saída: {item.quantity_outbound}")
            print(
                "Devolvida pelo cliente: "
                f"{item.quantity_returned_by_customer}"
            )
            print(
                "Pendente com cliente: "
                f"{item.quantity_pending_customer_return}"
            )
            print(
                "Disponível para fornecedor: "
                f"{item.quantity_available_for_supplier_return}"
            )
            print(
                "Remetida ao fornecedor: "
                f"{item.quantity_returned_to_supplier}"
            )
            print(
                "Pendente de encerramento: "
                f"{item.quantity_pending_supplier_return}"
            )
            print(f"Status: {item.lifecycle_status}")

        print("Teste concluído com sucesso.")

    finally:
        session.close()


if __name__ == "__main__":
    main()
```

## `scripts\test_supplier_return_fifo_service.py`

```python
from datetime import datetime

from src.database.connection import SessionLocal
from src.models.part import Part
from src.models.supplier import Supplier
from src.repositories.customer_return_allocation_repository import (
    CustomerReturnAllocationRepository,
)
from src.repositories.customer_return_item_repository import (
    CustomerReturnItemRepository,
)
from src.repositories.customer_return_repository import (
    CustomerReturnRepository,
)
from src.repositories.outbound_item_repository import (
    OutboundItemRepository,
)
from src.repositories.outbound_purchase_allocation_repository import (
    OutboundPurchaseAllocationRepository,
)
from src.repositories.outbound_repository import (
    OutboundRepository,
)
from src.repositories.part_repository import PartRepository
from src.repositories.purchase_item_repository import (
    PurchaseItemRepository,
)
from src.repositories.purchase_repository import (
    PurchaseRepository,
)
from src.repositories.supplier_repository import (
    SupplierRepository,
)
from src.repositories.supplier_return_item_repository import (
    SupplierReturnItemRepository,
)
from src.repositories.supplier_return_repository import (
    SupplierReturnRepository,
)
from src.services.customer_return_service import (
    CustomerReturnService,
)
from src.services.outbound_service import OutboundService
from src.services.purchase_service import PurchaseService
from src.services.supplier_return_service import (
    SupplierReturnService,
)


def main() -> None:
    session = SessionLocal()

    try:
        supplier_repository = SupplierRepository(session)
        part_repository = PartRepository(session)

        purchase_repository = PurchaseRepository(session)
        purchase_item_repository = PurchaseItemRepository(session)

        outbound_repository = OutboundRepository(session)
        outbound_item_repository = OutboundItemRepository(session)
        outbound_purchase_allocation_repository = (
            OutboundPurchaseAllocationRepository(session)
        )

        customer_return_repository = CustomerReturnRepository(session)
        customer_return_item_repository = (
            CustomerReturnItemRepository(session)
        )
        customer_return_allocation_repository = (
            CustomerReturnAllocationRepository(session)
        )

        supplier_return_repository = (
            SupplierReturnRepository(session)
        )
        supplier_return_item_repository = (
            SupplierReturnItemRepository(session)
        )

        suppliers = supplier_repository.list_all()

        if not suppliers:
            supplier = Supplier(
                name="Fornecedor Teste FIFO",
                document="00.000.000/0001-04",
                address="Endereco de Teste",
                notes="Fornecedor criado para teste FIFO.",
                is_active=1,
            )

            supplier = supplier_repository.add(supplier)

        else:
            supplier = suppliers[0]

        suffix = datetime.now().strftime("%Y%m%d%H%M%S%f")

        part = Part(
            part_code=f"TEST-SR-FIFO-{suffix}",
            name="Peca Teste FIFO Remessa",
            description="Peca criada para teste FIFO de remessa.",
            is_active=1,
        )

        part = part_repository.add(part)

        purchase_service = PurchaseService(
            purchase_repository=purchase_repository,
            purchase_item_repository=purchase_item_repository,
            supplier_repository=supplier_repository,
            part_repository=part_repository,
        )

        outbound_service = OutboundService(
            outbound_repository=outbound_repository,
            outbound_item_repository=outbound_item_repository,
            outbound_purchase_allocation_repository=(
                outbound_purchase_allocation_repository
            ),
            purchase_item_repository=purchase_item_repository,
            part_repository=part_repository,
        )

        customer_return_service = CustomerReturnService(
            customer_return_repository=customer_return_repository,
            customer_return_item_repository=(
                customer_return_item_repository
            ),
            customer_return_allocation_repository=(
                customer_return_allocation_repository
            ),
            outbound_item_repository=outbound_item_repository,
            part_repository=part_repository,
        )

        supplier_return_service = SupplierReturnService(
            supplier_return_repository=supplier_return_repository,
            supplier_return_item_repository=(
                supplier_return_item_repository
            ),
            supplier_repository=supplier_repository,
            purchase_repository=purchase_repository,
            purchase_item_repository=purchase_item_repository,
            outbound_purchase_allocation_repository=(
                outbound_purchase_allocation_repository
            ),
            customer_return_allocation_repository=(
                customer_return_allocation_repository
            ),
        )

        purchase_a = purchase_service.create_purchase(
            supplier_id=supplier.id,
            invoice_number=f"NF-FIFO-A-{suffix}",
            invoice_series="1",
            issue_date="2026-07-27",
            created_by=1,
            status="RECEIVED",
            notes="Primeira compra do teste FIFO.",
        )

        purchase_item_a = purchase_service.add_item(
            purchase_id=purchase_a.id,
            part_id=part.id,
            quantity_purchased=5,
        )

        purchase_b = purchase_service.create_purchase(
            supplier_id=supplier.id,
            invoice_number=f"NF-FIFO-B-{suffix}",
            invoice_series="1",
            issue_date="2026-07-28",
            created_by=1,
            status="RECEIVED",
            notes="Segunda compra do teste FIFO.",
        )

        purchase_item_b = purchase_service.add_item(
            purchase_id=purchase_b.id,
            part_id=part.id,
            quantity_purchased=5,
        )

        outbound = outbound_service.create_outbound(
            destination_type="WORKSHOP",
            work_order_number=f"OS-FIFO-{suffix}",
            created_by=1,
            status="ACTIVE",
        )

        outbound_item = outbound_service.add_item(
            outbound_id=outbound.id,
            part_id=part.id,
            quantity=8,
        )

        customer_return = (
            customer_return_service.create_customer_return(
                return_type="WORKSHOP",
                reference_number=f"OS-FIFO-{suffix}",
                customer_name="Cliente Teste FIFO",
                created_by=1,
                status="ACTIVE",
                notes="Devolucao criada para teste FIFO.",
            )
        )

        customer_return_service.add_item(
            customer_return_id=customer_return.id,
            part_id=part.id,
            quantity=6,
        )

        available_a = (
            supplier_return_service.get_available_quantity(
                purchase_item_a.id
            )
        )

        available_b = (
            supplier_return_service.get_available_quantity(
                purchase_item_b.id
            )
        )

        assert available_a == 5, (
            "A primeira origem deveria possuir 5 unidades "
            f"disponiveis, mas possui {available_a}."
        )

        assert available_b == 1, (
            "A segunda origem deveria possuir 1 unidade "
            f"disponivel, mas possui {available_b}."
        )

        outbound_allocations = (
            outbound_purchase_allocation_repository
            .list_by_outbound_item(outbound_item.id)
        )

        session.commit()

        print("\nTeste FIFO de remessa concluido com sucesso!")

        print("\nCompras:")
        print(
            f"- PurchaseItem {purchase_item_a.id}: "
            "5 unidades compradas"
        )
        print(
            f"- PurchaseItem {purchase_item_b.id}: "
            "5 unidades compradas"
        )

        print("\nAlocacoes FIFO da saida:")

        for allocation in outbound_allocations:
            print(
                f"- PurchaseItem "
                f"{allocation.purchase_item_id}: "
                f"{allocation.quantity_allocated} unidade(s)"
            )

        print("\nDevolucao do cliente:")
        print("- Quantidade devolvida: 6")

        print("\nDisponivel para remessa:")
        print(
            f"- PurchaseItem {purchase_item_a.id}: "
            f"{available_a} unidade(s)"
        )
        print(
            f"- PurchaseItem {purchase_item_b.id}: "
            f"{available_b} unidade(s)"
        )

        print("\nResultado esperado:")
        print("- A saida consumiu 5 unidades da primeira compra.")
        print("- A saida consumiu 3 unidades da segunda compra.")
        print("- A devolucao de 6 unidades foi distribuida em FIFO.")
        print("- Primeira compra: 5 unidades disponiveis.")
        print("- Segunda compra: 1 unidade disponivel.")

    except Exception:
        session.rollback()
        raise

    finally:
        session.close()


if __name__ == "__main__":
    main()
```

## `scripts\test_supplier_return_service.py`

```python
from datetime import datetime

from src.database.connection import SessionLocal
from src.models.part import Part
from src.models.supplier import Supplier
from src.repositories.customer_return_allocation_repository import (
    CustomerReturnAllocationRepository,
)
from src.repositories.customer_return_item_repository import (
    CustomerReturnItemRepository,
)
from src.repositories.customer_return_repository import (
    CustomerReturnRepository,
)
from src.repositories.outbound_item_repository import (
    OutboundItemRepository,
)
from src.repositories.outbound_purchase_allocation_repository import (
    OutboundPurchaseAllocationRepository,
)
from src.repositories.outbound_repository import (
    OutboundRepository,
)
from src.repositories.part_repository import PartRepository
from src.repositories.purchase_item_repository import (
    PurchaseItemRepository,
)
from src.repositories.purchase_repository import (
    PurchaseRepository,
)
from src.repositories.supplier_repository import (
    SupplierRepository,
)
from src.repositories.supplier_return_item_repository import (
    SupplierReturnItemRepository,
)
from src.repositories.supplier_return_repository import (
    SupplierReturnRepository,
)
from src.services.customer_return_service import (
    CustomerReturnService,
)
from src.services.outbound_service import OutboundService
from src.services.purchase_service import PurchaseService
from src.services.supplier_return_service import (
    SupplierReturnService,
)


def main() -> None:
    session = SessionLocal()

    try:
        supplier_repository = SupplierRepository(session)
        part_repository = PartRepository(session)

        purchase_repository = PurchaseRepository(session)
        purchase_item_repository = (
            PurchaseItemRepository(session)
        )

        outbound_repository = OutboundRepository(session)
        outbound_item_repository = (
            OutboundItemRepository(session)
        )
        outbound_purchase_allocation_repository = (
            OutboundPurchaseAllocationRepository(session)
        )

        customer_return_repository = (
            CustomerReturnRepository(session)
        )
        customer_return_item_repository = (
            CustomerReturnItemRepository(session)
        )
        customer_return_allocation_repository = (
            CustomerReturnAllocationRepository(session)
        )

        supplier_return_repository = (
            SupplierReturnRepository(session)
        )
        supplier_return_item_repository = (
            SupplierReturnItemRepository(session)
        )

        suppliers = supplier_repository.list_all()

        if not suppliers:
            supplier_entity = Supplier(
                name="Fornecedor Teste Remessa",
                document="00.000.000/0001-03",
                address="Endereco de Teste",
                notes=(
                    "Fornecedor criado para teste "
                    "de remessa de cascos."
                ),
                is_active=1,
            )

            supplier_entity = supplier_repository.add(
                supplier_entity
            )
        else:
            supplier_entity = suppliers[0]

        test_suffix = datetime.now().strftime(
            "%Y%m%d%H%M%S%f"
        )

        part_entity = Part(
            part_code=(
                f"TEST-SUPPLIER-RETURN-{test_suffix}"
            ),
            name="Peca Teste Remessa Fornecedor",
            description=(
                "Peca criada exclusivamente para teste "
                "de remessa ao fornecedor."
            ),
            is_active=1,
        )

        part_entity = part_repository.add(
            part_entity
        )

        purchase_service = PurchaseService(
            purchase_repository=purchase_repository,
            purchase_item_repository=(
                purchase_item_repository
            ),
            supplier_repository=supplier_repository,
            part_repository=part_repository,
        )

        outbound_service = OutboundService(
            outbound_repository=outbound_repository,
            outbound_item_repository=(
                outbound_item_repository
            ),
            outbound_purchase_allocation_repository=(
                outbound_purchase_allocation_repository
            ),
            purchase_item_repository=(
                purchase_item_repository
            ),
            part_repository=part_repository,
        )

        customer_return_service = CustomerReturnService(
            customer_return_repository=(
                customer_return_repository
            ),
            customer_return_item_repository=(
                customer_return_item_repository
            ),
            customer_return_allocation_repository=(
                customer_return_allocation_repository
            ),
            outbound_item_repository=(
                outbound_item_repository
            ),
            part_repository=part_repository,
        )

        supplier_return_service = SupplierReturnService(
            supplier_return_repository=(
                supplier_return_repository
            ),
            supplier_return_item_repository=(
                supplier_return_item_repository
            ),
            supplier_repository=supplier_repository,
            purchase_repository=purchase_repository,
            purchase_item_repository=(
                purchase_item_repository
            ),
            outbound_purchase_allocation_repository=(
                outbound_purchase_allocation_repository
            ),
            customer_return_allocation_repository=(
                customer_return_allocation_repository
            ),
        )

        purchase = purchase_service.create_purchase(
            supplier_id=supplier_entity.id,
            invoice_number=(
                f"NF-PURCHASE-SR-{test_suffix}"
            ),
            invoice_series="1",
            issue_date="2026-07-27",
            created_by=1,
            status="RECEIVED",
            notes=(
                "Compra criada para teste de "
                "remessa ao fornecedor."
            ),
        )

        purchase_item = purchase_service.add_item(
            purchase_id=purchase.id,
            part_id=part_entity.id,
            quantity_purchased=8,
        )

        outbound = outbound_service.create_outbound(
            destination_type="WORKSHOP",
            work_order_number=(
                f"OS-SR-{test_suffix}"
            ),
            created_by=1,
            status="ACTIVE",
        )

        outbound_item = outbound_service.add_item(
            outbound_id=outbound.id,
            part_id=part_entity.id,
            quantity=8,
        )

        customer_return = (
            customer_return_service.create_customer_return(
                return_type="WORKSHOP",
                reference_number=(
                    f"OS-SR-{test_suffix}"
                ),
                customer_name="Cliente Teste Remessa",
                created_by=1,
                status="ACTIVE",
                notes=(
                    "Devolucao criada para teste de "
                    "remessa ao fornecedor."
                ),
            )
        )

        customer_return_item = (
            customer_return_service.add_item(
                customer_return_id=customer_return.id,
                part_id=part_entity.id,
                quantity=6,
            )
        )

        available_before = (
            supplier_return_service.get_available_quantity(
                purchase_item.id
            )
        )

        assert available_before == 6, (
            "A quantidade disponível antes da remessa "
            f"deveria ser 6, mas foi {available_before}."
        )

        supplier_return = (
            supplier_return_service.create_supplier_return(
                supplier_id=supplier_entity.id,
                dispatch_invoice_number=(
                    f"NF-REMESSA-{test_suffix}"
                ),
                dispatch_invoice_series="1",
                issue_date="2026-07-27",
                created_by=1,
                status="ACTIVE",
                notes=(
                    "Remessa parcial criada pelo teste."
                ),
            )
        )

        supplier_return_item = (
            supplier_return_service.add_item(
                supplier_return_id=supplier_return.id,
                purchase_item_id=purchase_item.id,
                quantity=4,
            )
        )

        duplicate_blocked = False

        try:
            supplier_return_service.add_item(
                supplier_return_id=supplier_return.id,
                purchase_item_id=purchase_item.id,
                quantity=1,
            )

        except ValueError as error:
            duplicate_blocked = True

            print(
                "\nBloqueio de item duplicado realizado "
                "com sucesso!"
            )
            print(f"Mensagem: {error}")

        assert duplicate_blocked, (
            "O sistema deveria bloquear o mesmo item "
            "de compra duas vezes na mesma remessa."
        )

        available_after = (
            supplier_return_service.get_available_quantity(
                purchase_item.id
            )
        )

        assert available_after == 2, (
            "A quantidade disponível após a remessa "
            f"deveria ser 2, mas foi {available_after}."
        )

        # excess_blocked = False

        # try:
        #     supplier_return_service.add_item(
        #         supplier_return_id=supplier_return.id,
        #         purchase_item_id=purchase_item.id,
        #         quantity=3,
        #     )

        # except ValueError as error:
        #     excess_blocked = True

        #     print(
        #         "\nBloqueio de excesso realizado com sucesso!"
        #     )
        #     print(f"Mensagem: {error}")

        # assert excess_blocked, (
        #     "O sistema deveria bloquear uma remessa "
        #     "superior ao saldo disponível."
        # )

        session.commit()

        print(
            "\nRemessa ao fornecedor criada com sucesso!"
        )
        print(
            f"ID da compra: {purchase.id}"
        )
        print(
            f"ID do item da compra: {purchase_item.id}"
        )
        print(
            f"ID da saida: {outbound.id}"
        )
        print(
            f"ID do item da saida: {outbound_item.id}"
        )
        print(
            f"ID da devolucao do cliente: "
            f"{customer_return.id}"
        )
        print(
            f"ID do item devolvido: "
            f"{customer_return_item.id}"
        )
        print(
            f"ID da remessa: {supplier_return.id}"
        )
        print(
            f"ID do item da remessa: "
            f"{supplier_return_item.id}"
        )

        print(
            "\nQuantidades:"
        )
        print(
            "- Quantidade comprada: 8"
        )
        print(
            "- Quantidade retirada: 8"
        )
        print(
            "- Quantidade devolvida pelo cliente: 6"
        )
        print(
            "- Quantidade remetida ao fornecedor: 4"
        )
        print(
            f"- Saldo disponível para nova remessa: "
            f"{available_after}"
        )

        print(
            "\nResultado esperado:"
        )
        print(
            "- A quantidade inicial disponível para "
            "remessa era 6."
        )
        print(
            "- Foram remetidas 4 unidades."
        )
        print(
            "- Restaram 2 unidades disponíveis."
        )
        print(
            "- A tentativa de remeter 3 unidades "
            "foi bloqueada."
        )

    except Exception:
        session.rollback()
        raise

    finally:
        session.close()


if __name__ == "__main__":
    main()
```

## `src\__init__.py`

```python

```

## `src\api\__init__.py`

```python

```

## `src\api\routes\__init__.py`

```python
"""Rotas HTTP da aplicação."""

from src.api.routes.outbound_route import (
    router as outbound_router,
)
from src.api.routes.part_route import (
    router as part_router,
)
from src.api.routes.purchase_route import (
    router as purchase_router,
)
from src.api.routes.purchase_tracking_route import (
    router as purchase_tracking_router,
)
from src.api.routes.supplier_contact_route import (
    router as supplier_contact_router,
)
from src.api.routes.supplier_route import (
    router as supplier_router,
)


__all__ = [
    "outbound_router",
    "part_router",
    "purchase_router",
    "purchase_tracking_router",
    "supplier_contact_router",
    "supplier_router",
]
```

## `src\api\routes\outbound_route.py`

```python
from typing import Annotated, NoReturn

from fastapi import (
    APIRouter,
    Body,
    Depends,
    HTTPException,
    Path,
    Query,
    status,
)
from sqlalchemy.orm import Session

from src.database.connection import get_session
from src.repositories.outbound_item_repository import (
    OutboundItemRepository,
)
from src.repositories.outbound_purchase_allocation_repository import (
    OutboundPurchaseAllocationRepository,
)
from src.repositories.outbound_repository import (
    OutboundRepository,
)
from src.repositories.part_repository import (
    PartRepository,
)
from src.repositories.purchase_item_repository import (
    PurchaseItemRepository,
)
from src.schemas.outbound_schema import (
    OutboundCreateRequest,
    OutboundItemCreateRequest,
    OutboundItemResponse,
    OutboundResponse,
    OutboundStatus,
    OutboundUpdateRequest,
)
from src.services.outbound_service import (
    OutboundService,
)


router = APIRouter(
    prefix="/outbounds",
    tags=["Outbounds"],
)


SessionDependency = Annotated[
    Session,
    Depends(get_session),
]


def get_outbound_service(
    session: SessionDependency,
) -> OutboundService:
    """
    Monta o serviço de saídas com seus repositórios.
    """

    outbound_repository = OutboundRepository(
        session
    )

    outbound_item_repository = (
        OutboundItemRepository(
            session
        )
    )

    allocation_repository = (
        OutboundPurchaseAllocationRepository(
            session
        )
    )

    purchase_item_repository = (
        PurchaseItemRepository(
            session
        )
    )

    part_repository = PartRepository(
        session
    )

    return OutboundService(
        outbound_repository=(
            outbound_repository
        ),
        outbound_item_repository=(
            outbound_item_repository
        ),
        outbound_purchase_allocation_repository=(
            allocation_repository
        ),
        purchase_item_repository=(
            purchase_item_repository
        ),
        part_repository=part_repository,
    )


OutboundServiceDependency = Annotated[
    OutboundService,
    Depends(get_outbound_service),
]


NOT_FOUND_MESSAGES = {
    "Saída não encontrada.",
    "Peça não encontrada.",
    (
        "Item de compra relacionado "
        "à saída não encontrado."
    ),
}


def raise_http_error(
    error: ValueError,
) -> NoReturn:
    """
    Converte erros de negócio em erros HTTP.
    """

    message = str(error)

    if message in NOT_FOUND_MESSAGES:
        raise HTTPException(
            status_code=(
                status.HTTP_404_NOT_FOUND
            ),
            detail=message,
        ) from error

    raise HTTPException(
        status_code=(
            status.HTTP_400_BAD_REQUEST
        ),
        detail=message,
    ) from error


@router.post(
    "",
    response_model=OutboundResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Cadastrar uma saída",
)
def create_outbound(
    payload: Annotated[
        OutboundCreateRequest,
        Body(...),
    ],
    session: SessionDependency,
    service: OutboundServiceDependency,
) -> OutboundResponse:
    """
    Cadastra uma nova saída de peças.

    A saída deve possuir uma Ordem de Serviço,
    uma Nota Fiscal de venda ou ambas.
    """

    try:
        outbound = service.create_outbound(
            destination_type=(
                payload.destination_type
            ),
            work_order_number=(
                payload.work_order_number
            ),
            sales_invoice_number=(
                payload.sales_invoice_number
            ),
            created_by=payload.created_by,
            status=payload.status.value,
        )

        session.commit()
        session.refresh(outbound)

        return OutboundResponse.model_validate(
            outbound
        )

    except ValueError as error:
        session.rollback()
        raise_http_error(error)

    except Exception:
        session.rollback()
        raise


@router.get(
    "",
    response_model=list[OutboundResponse],
    status_code=status.HTTP_200_OK,
    summary="Listar saídas",
)
def list_outbounds(
    service: OutboundServiceDependency,
    outbound_status: OutboundStatus | None = Query(
        default=None,
        alias="status",
        description="Filtrar pelo status da saída",
    ),
    destination_type: str | None = Query(
        default=None,
        min_length=1,
        max_length=50,
        description=(
            "Filtrar pelo tipo de destino"
        ),
    ),
) -> list[OutboundResponse]:
    """
    Lista todas as saídas.

    Pode ser utilizado um filtro por status ou
    por tipo de destino. Apenas um filtro pode
    ser enviado por vez.
    """

    try:
        outbounds = service.list_outbounds(
            status=(
                outbound_status.value
                if outbound_status is not None
                else None
            ),
            destination_type=destination_type,
        )

        return [
            OutboundResponse.model_validate(
                outbound
            )
            for outbound in outbounds
        ]

    except ValueError as error:
        raise_http_error(error)


@router.get(
    "/{outbound_id}",
    response_model=OutboundResponse,
    status_code=status.HTTP_200_OK,
    summary="Consultar uma saída",
)
def get_outbound(
    service: OutboundServiceDependency,
    outbound_id: int = Path(
        ...,
        gt=0,
        description=(
            "Identificador da saída"
        ),
    ),
) -> OutboundResponse:
    """
    Retorna uma saída pelo identificador.
    """

    try:
        outbound = service.get_outbound(
            outbound_id
        )

        return OutboundResponse.model_validate(
            outbound
        )

    except ValueError as error:
        raise_http_error(error)


@router.patch(
    "/{outbound_id}",
    response_model=OutboundResponse,
    status_code=status.HTTP_200_OK,
    summary="Atualizar uma saída",
)
def update_outbound(
    payload: Annotated[
        OutboundUpdateRequest,
        Body(...),
    ],
    session: SessionDependency,
    service: OutboundServiceDependency,
    outbound_id: int = Path(
        ...,
        gt=0,
        description=(
            "Identificador da saída"
        ),
    ),
) -> OutboundResponse:
    """
    Atualiza parcialmente uma saída.

    Saídas canceladas não podem ser alteradas.
    O cancelamento deve utilizar o endpoint
    específico.
    """

    try:
        update_data = payload.model_dump(
            exclude_unset=True
        )

        outbound_status = update_data.get(
            "status"
        )

        if outbound_status is not None:
            update_data["status"] = (
                outbound_status.value
            )

        outbound = service.update_outbound(
            outbound_id=outbound_id,
            **update_data,
        )

        session.commit()
        session.refresh(outbound)

        return OutboundResponse.model_validate(
            outbound
        )

    except ValueError as error:
        session.rollback()
        raise_http_error(error)

    except Exception:
        session.rollback()
        raise


@router.patch(
    "/{outbound_id}/cancel",
    response_model=OutboundResponse,
    status_code=status.HTTP_200_OK,
    summary="Cancelar uma saída",
)
def cancel_outbound(
    session: SessionDependency,
    service: OutboundServiceDependency,
    outbound_id: int = Path(
        ...,
        gt=0,
        description=(
            "Identificador da saída"
        ),
    ),
) -> OutboundResponse:
    """
    Cancela uma saída e devolve ao estoque as
    quantidades anteriormente consumidas.
    """

    try:
        outbound = service.cancel_outbound(
            outbound_id
        )

        session.commit()
        session.refresh(outbound)

        return OutboundResponse.model_validate(
            outbound
        )

    except ValueError as error:
        session.rollback()
        raise_http_error(error)

    except Exception:
        session.rollback()
        raise


@router.post(
    "/{outbound_id}/items",
    response_model=OutboundItemResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Adicionar item à saída",
)
def add_outbound_item(
    payload: Annotated[
        OutboundItemCreateRequest,
        Body(...),
    ],
    session: SessionDependency,
    service: OutboundServiceDependency,
    outbound_id: int = Path(
        ...,
        gt=0,
        description=(
            "Identificador da saída"
        ),
    ),
) -> OutboundItemResponse:
    """
    Adiciona uma peça à saída.

    A quantidade é consumida automaticamente
    dos itens de compra por ordem FIFO.
    """

    try:
        outbound_item = service.add_item(
            outbound_id=outbound_id,
            part_id=payload.part_id,
            quantity=payload.quantity,
        )

        session.commit()
        session.refresh(outbound_item)

        return (
            OutboundItemResponse.model_validate(
                outbound_item
            )
        )

    except ValueError as error:
        session.rollback()
        raise_http_error(error)

    except Exception:
        session.rollback()
        raise


@router.get(
    "/{outbound_id}/items",
    response_model=list[OutboundItemResponse],
    status_code=status.HTTP_200_OK,
    summary="Listar itens de uma saída",
)
def list_outbound_items(
    service: OutboundServiceDependency,
    outbound_id: int = Path(
        ...,
        gt=0,
        description=(
            "Identificador da saída"
        ),
    ),
) -> list[OutboundItemResponse]:
    """
    Lista todos os itens pertencentes a uma saída.
    """

    try:
        outbound_items = (
            service.list_outbound_items(
                outbound_id
            )
        )

        return [
            OutboundItemResponse.model_validate(
                outbound_item
            )
            for outbound_item
            in outbound_items
        ]

    except ValueError as error:
        raise_http_error(error)
```

## `src\api\routes\part_route.py`

```python
from typing import Annotated, NoReturn

from fastapi import (
    APIRouter,
    Body,
    Depends,
    HTTPException,
    Path,
    Query,
    status,
)
from sqlalchemy.orm import Session

from src.database.connection import get_session
from src.repositories.part_repository import PartRepository
from src.repositories.supplier_repository import (
    SupplierRepository,
)
from src.schemas.part_schema import (
    PartCreateRequest,
    PartResponse,
    PartUpdateRequest,
)
from src.services.part_service import PartService


router = APIRouter(
    prefix="/parts",
    tags=["Parts"],
)


SessionDependency = Annotated[
    Session,
    Depends(get_session),
]


def get_part_service(
    session: SessionDependency,
) -> PartService:
    """Cria o serviço de peças com suas dependências."""

    part_repository = PartRepository(session)

    supplier_repository = SupplierRepository(
        session
    )

    return PartService(
        part_repository=part_repository,
        supplier_repository=supplier_repository,
    )


PartServiceDependency = Annotated[
    PartService,
    Depends(get_part_service),
]


def raise_part_http_exception(
    error: ValueError,
) -> NoReturn:
    """Converte erros de negócio em respostas HTTP."""

    message = str(error)

    not_found_messages = {
        "Peça não encontrada.",
        "Fornecedor não encontrado.",
    }

    if message in not_found_messages:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=message,
        ) from error

    if message == (
        "Já existe uma peça com este código "
        "para o fornecedor informado."
    ):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=message,
        ) from error

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=message,
    ) from error


@router.post(
    "",
    response_model=PartResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Cadastrar peça",
)
def create_part(
    request: Annotated[
        PartCreateRequest,
        Body(...),
    ],
    session: SessionDependency,
    service: PartServiceDependency,
) -> PartResponse:
    """Cadastra uma peça controlada pelo SIGC."""

    try:
        part = service.create(
            supplier_id=request.supplier_id,
            part_code=request.part_code,
            name=request.name,
            description=request.description,
            return_deadline_days=(
                request.return_deadline_days
            ),
        )

        session.commit()
        session.refresh(part)

        return PartResponse.model_validate(part)

    except ValueError as error:
        session.rollback()
        raise_part_http_exception(error)

    except Exception:
        session.rollback()
        raise


@router.get(
    "",
    response_model=list[PartResponse],
    status_code=status.HTTP_200_OK,
    summary="Listar peças",
)
def list_parts(
    service: PartServiceDependency,
    supplier_id: int | None = Query(
        default=None,
        gt=0,
        description=(
            "Filtra as peças pelo identificador "
            "do fornecedor"
        ),
    ),
) -> list[PartResponse]:
    """Lista todas as peças ou filtra por fornecedor."""

    try:
        if supplier_id is None:
            parts = service.list_all()
        else:
            parts = service.list_by_supplier(
                supplier_id
            )

        return [
            PartResponse.model_validate(part)
            for part in parts
        ]

    except ValueError as error:
        raise_part_http_exception(error)


@router.get(
    "/{part_id}",
    response_model=PartResponse,
    status_code=status.HTTP_200_OK,
    summary="Consultar peça",
)
def get_part(
    service: PartServiceDependency,
    part_id: int = Path(
        ...,
        gt=0,
        description="Identificador da peça",
    ),
) -> PartResponse:
    """Consulta uma peça pelo identificador."""

    try:
        part = service.get_required(part_id)

        return PartResponse.model_validate(part)

    except ValueError as error:
        raise_part_http_exception(error)


@router.put(
    "/{part_id}",
    response_model=PartResponse,
    status_code=status.HTTP_200_OK,
    summary="Atualizar peça",
)
def update_part(
    request: Annotated[
        PartUpdateRequest,
        Body(...),
    ],
    session: SessionDependency,
    service: PartServiceDependency,
    part_id: int = Path(
        ...,
        gt=0,
        description="Identificador da peça",
    ),
) -> PartResponse:
    """Atualiza parcialmente uma peça existente."""

    try:
        update_data = request.model_dump(
            exclude_unset=True
        )

        part = service.update(
            part_id=part_id,
            **update_data,
        )

        session.commit()
        session.refresh(part)

        return PartResponse.model_validate(part)

    except ValueError as error:
        session.rollback()
        raise_part_http_exception(error)

    except Exception:
        session.rollback()
        raise


@router.patch(
    "/{part_id}/activate",
    response_model=PartResponse,
    status_code=status.HTTP_200_OK,
    summary="Ativar peça",
)
def activate_part(
    session: SessionDependency,
    service: PartServiceDependency,
    part_id: int = Path(
        ...,
        gt=0,
        description="Identificador da peça",
    ),
) -> PartResponse:
    """Ativa uma peça inativa."""

    try:
        part = service.activate(part_id)

        session.commit()
        session.refresh(part)

        return PartResponse.model_validate(part)

    except ValueError as error:
        session.rollback()
        raise_part_http_exception(error)

    except Exception:
        session.rollback()
        raise


@router.patch(
    "/{part_id}/deactivate",
    response_model=PartResponse,
    status_code=status.HTTP_200_OK,
    summary="Desativar peça",
)
def deactivate_part(
    session: SessionDependency,
    service: PartServiceDependency,
    part_id: int = Path(
        ...,
        gt=0,
        description="Identificador da peça",
    ),
) -> PartResponse:
    """Desativa uma peça ativa."""

    try:
        part = service.deactivate(part_id)

        session.commit()
        session.refresh(part)

        return PartResponse.model_validate(part)

    except ValueError as error:
        session.rollback()
        raise_part_http_exception(error)

    except Exception:
        session.rollback()
        raise
```

## `src\api\routes\purchase_route.py`

```python
from typing import Annotated, NoReturn

from fastapi import (
    APIRouter,
    Body,
    Depends,
    HTTPException,
    Path,
    Query,
    status,
)
from sqlalchemy.orm import Session

from src.database.connection import get_session
from src.repositories.part_repository import (
    PartRepository,
)
from src.repositories.purchase_item_repository import (
    PurchaseItemRepository,
)
from src.repositories.purchase_repository import (
    PurchaseRepository,
)
from src.repositories.supplier_repository import (
    SupplierRepository,
)
from src.schemas.purchase_schema import (
    PurchaseCreateRequest,
    PurchaseItemCreateRequest,
    PurchaseItemResponse,
    PurchaseResponse,
    PurchaseUpdateRequest,
)
from src.services.purchase_service import (
    PurchaseService,
)


router = APIRouter(
    prefix="/purchases",
    tags=["Purchases"],
)


SessionDependency = Annotated[
    Session,
    Depends(get_session),
]


def get_purchase_service(
    session: SessionDependency,
) -> PurchaseService:
    """
    Cria o serviço de compras com suas dependências.
    """

    purchase_repository = PurchaseRepository(
        session
    )

    purchase_item_repository = (
        PurchaseItemRepository(
            session
        )
    )

    supplier_repository = SupplierRepository(
        session
    )

    part_repository = PartRepository(
        session
    )

    return PurchaseService(
        purchase_repository=purchase_repository,
        purchase_item_repository=(
            purchase_item_repository
        ),
        supplier_repository=supplier_repository,
        part_repository=part_repository,
    )


PurchaseServiceDependency = Annotated[
    PurchaseService,
    Depends(get_purchase_service),
]


def raise_purchase_http_exception(
    error: ValueError,
) -> NoReturn:
    """
    Converte erros de negócio em respostas HTTP.
    """

    message = str(error)

    not_found_messages = {
        "Compra não encontrada.",
        "Fornecedor não encontrado.",
        "Peça não encontrada.",
    }

    conflict_messages = {
        (
            "Já existe uma compra com esta nota fiscal, "
            "série e fornecedor."
        ),
        "Esta peça já foi adicionada à compra.",
        "A compra já está cancelada.",
    }

    if message in not_found_messages:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=message,
        ) from error

    if message in conflict_messages:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=message,
        ) from error

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=message,
    ) from error


@router.post(
    "",
    response_model=PurchaseResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Cadastrar compra",
)
def create_purchase(
    request: Annotated[
        PurchaseCreateRequest,
        Body(...),
    ],
    session: SessionDependency,
    service: PurchaseServiceDependency,
) -> PurchaseResponse:
    """
    Cadastra uma nova compra.
    """

    try:
        purchase = service.create_purchase(
            supplier_id=request.supplier_id,
            invoice_number=request.invoice_number,
            invoice_series=request.invoice_series,
            issue_date=request.issue_date,
            created_by=request.created_by,
            status=request.status,
            notes=request.notes,
        )

        session.commit()
        session.refresh(purchase)

        return PurchaseResponse.model_validate(
            purchase
        )

    except ValueError as error:
        session.rollback()
        raise_purchase_http_exception(error)

    except Exception:
        session.rollback()
        raise


@router.get(
    "",
    response_model=list[PurchaseResponse],
    status_code=status.HTTP_200_OK,
    summary="Listar compras",
)
def list_purchases(
    service: PurchaseServiceDependency,
    supplier_id: int | None = Query(
        default=None,
        gt=0,
        description=(
            "Filtra as compras pelo fornecedor"
        ),
    ),
) -> list[PurchaseResponse]:
    """
    Lista todas as compras ou filtra por fornecedor.
    """

    try:
        if supplier_id is None:
            purchases = service.list_purchases()
        else:
            purchases = (
                service.list_purchases_by_supplier(
                    supplier_id
                )
            )

        return [
            PurchaseResponse.model_validate(
                purchase
            )
            for purchase in purchases
        ]

    except ValueError as error:
        raise_purchase_http_exception(error)


@router.get(
    "/{purchase_id}",
    response_model=PurchaseResponse,
    status_code=status.HTTP_200_OK,
    summary="Consultar compra",
)
def get_purchase(
    service: PurchaseServiceDependency,
    purchase_id: int = Path(
        ...,
        gt=0,
        description="Identificador da compra",
    ),
) -> PurchaseResponse:
    """
    Retorna uma compra pelo identificador.
    """

    try:
        purchase = service.get_purchase(
            purchase_id
        )

        return PurchaseResponse.model_validate(
            purchase
        )

    except ValueError as error:
        raise_purchase_http_exception(error)


@router.patch(
    "/{purchase_id}",
    response_model=PurchaseResponse,
    status_code=status.HTTP_200_OK,
    summary="Atualizar compra",
)
def update_purchase(
    request: Annotated[
        PurchaseUpdateRequest,
        Body(...),
    ],
    session: SessionDependency,
    service: PurchaseServiceDependency,
    purchase_id: int = Path(
        ...,
        gt=0,
        description="Identificador da compra",
    ),
) -> PurchaseResponse:
    """
    Atualiza somente os campos enviados.
    """

    try:
        update_data = request.model_dump(
            exclude_unset=True
        )

        purchase = service.update_purchase(
            purchase_id=purchase_id,
            **update_data,
        )

        session.commit()
        session.refresh(purchase)

        return PurchaseResponse.model_validate(
            purchase
        )

    except ValueError as error:
        session.rollback()
        raise_purchase_http_exception(error)

    except Exception:
        session.rollback()
        raise


@router.patch(
    "/{purchase_id}/cancel",
    response_model=PurchaseResponse,
    status_code=status.HTTP_200_OK,
    summary="Cancelar compra",
)
def cancel_purchase(
    session: SessionDependency,
    service: PurchaseServiceDependency,
    purchase_id: int = Path(
        ...,
        gt=0,
        description="Identificador da compra",
    ),
) -> PurchaseResponse:
    """
    Cancela uma compra sem apagar seu histórico.
    """

    try:
        purchase = service.cancel_purchase(
            purchase_id
        )

        session.commit()
        session.refresh(purchase)

        return PurchaseResponse.model_validate(
            purchase
        )

    except ValueError as error:
        session.rollback()
        raise_purchase_http_exception(error)

    except Exception:
        session.rollback()
        raise


@router.post(
    "/{purchase_id}/items",
    response_model=PurchaseItemResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Adicionar item à compra",
)
def add_purchase_item(
    request: Annotated[
        PurchaseItemCreateRequest,
        Body(...),
    ],
    session: SessionDependency,
    service: PurchaseServiceDependency,
    purchase_id: int = Path(
        ...,
        gt=0,
        description="Identificador da compra",
    ),
) -> PurchaseItemResponse:
    """
    Adiciona uma peça à compra.
    """

    try:
        purchase_item = service.add_item(
            purchase_id=purchase_id,
            part_id=request.part_id,
            quantity_purchased=(
                request.quantity_purchased
            ),
        )

        session.commit()
        session.refresh(purchase_item)

        return PurchaseItemResponse.model_validate(
            purchase_item
        )

    except ValueError as error:
        session.rollback()
        raise_purchase_http_exception(error)

    except Exception:
        session.rollback()
        raise


@router.get(
    "/{purchase_id}/items",
    response_model=list[PurchaseItemResponse],
    status_code=status.HTTP_200_OK,
    summary="Listar itens da compra",
)
def list_purchase_items(
    service: PurchaseServiceDependency,
    purchase_id: int = Path(
        ...,
        gt=0,
        description="Identificador da compra",
    ),
) -> list[PurchaseItemResponse]:
    """
    Lista os itens vinculados a uma compra.
    """

    try:
        purchase_items = (
            service.list_purchase_items(
                purchase_id
            )
        )

        return [
            PurchaseItemResponse.model_validate(
                purchase_item
            )
            for purchase_item in purchase_items
        ]

    except ValueError as error:
        raise_purchase_http_exception(error)
```

## `src\api\routes\purchase_tracking_route.py`

```python
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path, status
from sqlalchemy.orm import Session

from src.database.connection import get_session
from src.queries.purchase_tracking_query import PurchaseTrackingQuery
from src.schemas.purchase_tracking_schema import (
    PurchaseTrackingResponse,
)
from src.services.purchase_tracking_service import (
    PurchaseTrackingService,
)


router = APIRouter(
    prefix="/purchases",
    tags=["Purchase Tracking"],
)


SessionDependency = Annotated[
    Session,
    Depends(get_session),
]


def get_purchase_tracking_service(
    session: SessionDependency,
) -> PurchaseTrackingService:
    """
    Monta o Service com suas dependências.

    A rota não cria consultas diretamente. Ela recebe uma sessão,
    cria a Query e injeta a Query no Service.
    """

    query = PurchaseTrackingQuery(session)

    return PurchaseTrackingService(query)


PurchaseTrackingServiceDependency = Annotated[
    PurchaseTrackingService,
    Depends(get_purchase_tracking_service),
]


@router.get(
    "/{purchase_id}/tracking",
    response_model=PurchaseTrackingResponse,
    status_code=status.HTTP_200_OK,
    summary="Consultar acompanhamento de uma compra",
)
def get_purchase_tracking(
    service: PurchaseTrackingServiceDependency,
    purchase_id: int = Path(
        ...,
        gt=0,
        description="Identificador da compra",
    ),
) -> PurchaseTrackingResponse:
    """
    Retorna o acompanhamento completo de uma compra.

    A resposta inclui as quantidades compradas, enviadas,
    devolvidas pelo cliente e devolvidas ao fornecedor.
    """

    try:
        tracking = service.get_purchase_tracking(purchase_id)

        return PurchaseTrackingResponse.from_dto(tracking)

    except ValueError as error:
        message = str(error)

        if message == "Compra não encontrada.":
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=message,
            ) from error

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=message,
        ) from error
```

## `src\api\routes\supplier_contact_route.py`

```python
from typing import Annotated

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Path,
    status,
)
from sqlalchemy.orm import Session

from src.database.connection import get_session
from src.repositories.supplier_contact_repository import (
    SupplierContactRepository,
)
from src.repositories.supplier_repository import (
    SupplierRepository,
)
from src.schemas.supplier_contact_schema import (
    SupplierContactCreateRequest,
    SupplierContactResponse,
    SupplierContactUpdateRequest,
)
from src.services.supplier_contact_service import (
    SupplierContactService,
)


router = APIRouter(
    prefix="/suppliers/{supplier_id}/contacts",
    tags=["Supplier Contacts"],
)


SessionDependency = Annotated[
    Session,
    Depends(get_session),
]


def get_supplier_contact_service(
    session: SessionDependency,
) -> SupplierContactService:
    """Monta o serviço com seus repositories."""

    contact_repository = SupplierContactRepository(
        session
    )

    supplier_repository = SupplierRepository(
        session
    )

    return SupplierContactService(
        repository=contact_repository,
        supplier_repository=supplier_repository,
    )


SupplierContactServiceDependency = Annotated[
    SupplierContactService,
    Depends(get_supplier_contact_service),
]


def handle_contact_error(
    error: ValueError,
) -> HTTPException:
    """Converte erros de negócio em erros HTTP."""

    message = str(error)

    not_found_messages = {
        "Fornecedor não encontrado.",
        "Contato não encontrado.",
    }

    if message in not_found_messages:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=message,
        )

    if message == (
        "O contato não pertence ao fornecedor informado."
    ):
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=message,
        )

    return HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=message,
    )


@router.post(
    "",
    response_model=SupplierContactResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Cadastrar contato de fornecedor",
)
def create_supplier_contact(
    request: SupplierContactCreateRequest,
    service: SupplierContactServiceDependency,
    session: SessionDependency,
    supplier_id: int = Path(
        ...,
        gt=0,
        description="Identificador do fornecedor",
    ),
) -> SupplierContactResponse:
    """Cadastra um novo contato para o fornecedor."""

    try:
        contact = service.create(
            supplier_id=supplier_id,
            name=request.name,
            email=request.email,
            phone=request.phone,
            position=request.position,
            is_primary=request.is_primary,
        )

        session.commit()
        session.refresh(contact)

        return SupplierContactResponse.model_validate(
            contact
        )

    except ValueError as error:
        session.rollback()
        raise handle_contact_error(error) from error

    except Exception:
        session.rollback()
        raise


@router.get(
    "",
    response_model=list[SupplierContactResponse],
    status_code=status.HTTP_200_OK,
    summary="Listar contatos de um fornecedor",
)
def list_supplier_contacts(
    service: SupplierContactServiceDependency,
    supplier_id: int = Path(
        ...,
        gt=0,
        description="Identificador do fornecedor",
    ),
) -> list[SupplierContactResponse]:
    """Lista todos os contatos do fornecedor."""

    try:
        contacts = service.list_by_supplier(
            supplier_id
        )

        return [
            SupplierContactResponse.model_validate(
                contact
            )
            for contact in contacts
        ]

    except ValueError as error:
        raise handle_contact_error(error) from error


@router.get(
    "/{contact_id}",
    response_model=SupplierContactResponse,
    status_code=status.HTTP_200_OK,
    summary="Consultar contato de fornecedor",
)
def get_supplier_contact(
    service: SupplierContactServiceDependency,
    supplier_id: int = Path(
        ...,
        gt=0,
        description="Identificador do fornecedor",
    ),
    contact_id: int = Path(
        ...,
        gt=0,
        description="Identificador do contato",
    ),
) -> SupplierContactResponse:
    """Consulta um contato específico do fornecedor."""

    try:
        contact = service.get_required(
            supplier_id=supplier_id,
            contact_id=contact_id,
        )

        return SupplierContactResponse.model_validate(
            contact
        )

    except ValueError as error:
        raise handle_contact_error(error) from error


@router.put(
    "/{contact_id}",
    response_model=SupplierContactResponse,
    status_code=status.HTTP_200_OK,
    summary="Atualizar contato de fornecedor",
)
def update_supplier_contact(
    request: SupplierContactUpdateRequest,
    service: SupplierContactServiceDependency,
    session: SessionDependency,
    supplier_id: int = Path(
        ...,
        gt=0,
        description="Identificador do fornecedor",
    ),
    contact_id: int = Path(
        ...,
        gt=0,
        description="Identificador do contato",
    ),
) -> SupplierContactResponse:
    """Atualiza somente os campos enviados."""

    try:
        update_data = request.model_dump(
            exclude_unset=True
        )

        contact = service.update(
            supplier_id=supplier_id,
            contact_id=contact_id,
            **update_data,
        )

        session.commit()
        session.refresh(contact)

        return SupplierContactResponse.model_validate(
            contact
        )

    except ValueError as error:
        session.rollback()
        raise handle_contact_error(error) from error

    except Exception:
        session.rollback()
        raise


@router.patch(
    "/{contact_id}/activate",
    response_model=SupplierContactResponse,
    status_code=status.HTTP_200_OK,
    summary="Ativar contato de fornecedor",
)
def activate_supplier_contact(
    service: SupplierContactServiceDependency,
    session: SessionDependency,
    supplier_id: int = Path(
        ...,
        gt=0,
        description="Identificador do fornecedor",
    ),
    contact_id: int = Path(
        ...,
        gt=0,
        description="Identificador do contato",
    ),
) -> SupplierContactResponse:
    """Ativa um contato inativo."""

    try:
        contact = service.activate(
            supplier_id=supplier_id,
            contact_id=contact_id,
        )

        session.commit()
        session.refresh(contact)

        return SupplierContactResponse.model_validate(
            contact
        )

    except ValueError as error:
        session.rollback()
        raise handle_contact_error(error) from error

    except Exception:
        session.rollback()
        raise


@router.patch(
    "/{contact_id}/deactivate",
    response_model=SupplierContactResponse,
    status_code=status.HTTP_200_OK,
    summary="Desativar contato de fornecedor",
)
def deactivate_supplier_contact(
    service: SupplierContactServiceDependency,
    session: SessionDependency,
    supplier_id: int = Path(
        ...,
        gt=0,
        description="Identificador do fornecedor",
    ),
    contact_id: int = Path(
        ...,
        gt=0,
        description="Identificador do contato",
    ),
) -> SupplierContactResponse:
    """Desativa um contato ativo."""

    try:
        contact = service.deactivate(
            supplier_id=supplier_id,
            contact_id=contact_id,
        )

        session.commit()
        session.refresh(contact)

        return SupplierContactResponse.model_validate(
            contact
        )

    except ValueError as error:
        session.rollback()
        raise handle_contact_error(error) from error

    except Exception:
        session.rollback()
        raise
```

## `src\api\routes\supplier_route.py`

```python
from typing import Annotated, NoReturn

from fastapi import (
    APIRouter,
    Body,
    Depends,
    HTTPException,
    Path,
    status,
)
from sqlalchemy.orm import Session

from src.database.connection import get_session
from src.repositories.supplier_repository import (
    SupplierRepository,
)
from src.schemas.supplier_schema import (
    SupplierCreateRequest,
    SupplierResponse,
    SupplierUpdateRequest,
)
from src.services.supplier_service import SupplierService


router = APIRouter(
    prefix="/suppliers",
    tags=["Suppliers"],
)


SessionDependency = Annotated[
    Session,
    Depends(get_session),
]


def get_supplier_service(
    session: SessionDependency,
) -> SupplierService:
    """
    Cria o serviço de fornecedores com suas dependências.
    """

    repository = SupplierRepository(session)

    return SupplierService(repository)


SupplierServiceDependency = Annotated[
    SupplierService,
    Depends(get_supplier_service),
]


def raise_supplier_http_exception(
    error: ValueError,
) -> NoReturn:
    """
    Converte erros de negócio em respostas HTTP.
    """

    message = str(error)

    if message == "Fornecedor não encontrado.":
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=message,
        ) from error

    if message == (
        "Já existe um fornecedor com este documento."
    ):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=message,
        ) from error

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=message,
    ) from error


@router.post(
    "",
    response_model=SupplierResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Cadastrar fornecedor",
)
def create_supplier(
    request: Annotated[
        SupplierCreateRequest,
        Body(...),
    ],
    session: SessionDependency,
    service: SupplierServiceDependency,
) -> SupplierResponse:
    """
    Cadastra um novo fornecedor.
    """

    try:
        supplier = service.create(
            name=request.name,
            document=request.document,
            address=request.address,
            notes=request.notes,
        )

        session.commit()
        session.refresh(supplier)

        return SupplierResponse.model_validate(supplier)

    except ValueError as error:
        session.rollback()
        raise_supplier_http_exception(error)

    except Exception:
        session.rollback()
        raise


@router.get(
    "",
    response_model=list[SupplierResponse],
    status_code=status.HTTP_200_OK,
    summary="Listar fornecedores",
)
def list_suppliers(
    service: SupplierServiceDependency,
) -> list[SupplierResponse]:
    """
    Retorna todos os fornecedores cadastrados.

    A listagem contém fornecedores ativos e inativos.
    """

    suppliers = service.list_all()

    return [
        SupplierResponse.model_validate(supplier)
        for supplier in suppliers
    ]


@router.get(
    "/{supplier_id}",
    response_model=SupplierResponse,
    status_code=status.HTTP_200_OK,
    summary="Consultar fornecedor",
)
def get_supplier(
    service: SupplierServiceDependency,
    supplier_id: int = Path(
        ...,
        gt=0,
        description="Identificador do fornecedor",
    ),
) -> SupplierResponse:
    """
    Consulta um fornecedor pelo identificador.
    """

    try:
        supplier = service.get_required(supplier_id)

        return SupplierResponse.model_validate(supplier)

    except ValueError as error:
        raise_supplier_http_exception(error)


@router.put(
    "/{supplier_id}",
    response_model=SupplierResponse,
    status_code=status.HTTP_200_OK,
    summary="Atualizar fornecedor",
)
def update_supplier(
    request: Annotated[
        SupplierUpdateRequest,
        Body(...),
    ],
    session: SessionDependency,
    service: SupplierServiceDependency,
    supplier_id: int = Path(
        ...,
        gt=0,
        description="Identificador do fornecedor",
    ),
) -> SupplierResponse:
    """
    Atualiza somente os campos enviados na requisição.

    Campos opcionais enviados como null serão apagados.
    """

    try:
        update_data = request.model_dump(
            exclude_unset=True,
        )

        supplier = service.update(
            supplier_id,
            **update_data,
        )

        session.commit()
        session.refresh(supplier)

        return SupplierResponse.model_validate(supplier)

    except ValueError as error:
        session.rollback()
        raise_supplier_http_exception(error)

    except Exception:
        session.rollback()
        raise


@router.patch(
    "/{supplier_id}/activate",
    response_model=SupplierResponse,
    status_code=status.HTTP_200_OK,
    summary="Ativar fornecedor",
)
def activate_supplier(
    session: SessionDependency,
    service: SupplierServiceDependency,
    supplier_id: int = Path(
        ...,
        gt=0,
        description="Identificador do fornecedor",
    ),
) -> SupplierResponse:
    """
    Ativa um fornecedor que está inativo.
    """

    try:
        supplier = service.activate(supplier_id)

        session.commit()
        session.refresh(supplier)

        return SupplierResponse.model_validate(supplier)

    except ValueError as error:
        session.rollback()
        raise_supplier_http_exception(error)

    except Exception:
        session.rollback()
        raise


@router.patch(
    "/{supplier_id}/deactivate",
    response_model=SupplierResponse,
    status_code=status.HTTP_200_OK,
    summary="Desativar fornecedor",
)
def deactivate_supplier(
    session: SessionDependency,
    service: SupplierServiceDependency,
    supplier_id: int = Path(
        ...,
        gt=0,
        description="Identificador do fornecedor",
    ),
) -> SupplierResponse:
    """
    Desativa um fornecedor sem excluir seu histórico.
    """

    try:
        supplier = service.deactivate(supplier_id)

        session.commit()
        session.refresh(supplier)

        return SupplierResponse.model_validate(supplier)

    except ValueError as error:
        session.rollback()
        raise_supplier_http_exception(error)

    except Exception:
        session.rollback()
        raise
```

## `src\core\__init__.py`

```python

```

## `src\core\time.py`

```python
from datetime import datetime


def now_iso() -> str:
    """Retorna a data e hora atual no formato ISO 8601."""
    return datetime.now().isoformat()
```

## `src\database\__init__.py`

```python

```

## `src\database\connection.py`

```python
from collections.abc import Generator
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import (
    DeclarativeBase,
    Session,
    sessionmaker,
)


BASE_DIR = Path(__file__).resolve().parents[2]

DATABASE_DIR = BASE_DIR / "data"
DATABASE_DIR.mkdir(exist_ok=True)

DATABASE_URL = f"sqlite:///{DATABASE_DIR / 'sigc_dev.db'}"


engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)


SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)


class Base(DeclarativeBase):
    pass


def get_session() -> Generator[Session, None, None]:
    """
    Fornece uma sessão do banco para cada requisição da API.

    A sessão é sempre fechada ao final da requisição,
    mesmo quando ocorre algum erro.
    """

    session = SessionLocal()

    try:
        yield session
    finally:
        session.close()
```

## `src\dtos\__init__.py`

```python
"""
Data Transfer Objects (DTOs).

Responsável por transportar dados entre as camadas da aplicação,
sem expor diretamente os Models do SQLAlchemy.
"""

from src.dtos.purchase_tracking_dto import PurchaseTrackingDTO

__all__ = [
    "PurchaseTrackingDTO",
]
```

## `src\dtos\customer_return_dto.py`

```python

```

## `src\dtos\outbound_dto.py`

```python

```

## `src\dtos\purchase_tracking.py`

```python
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class PurchaseItemTrackingDTO:
    """Visão consolidada do ciclo de um item de compra."""

    purchase_item_id: int
    part_id: int
    part_code: str
    part_name: str
    quantity_purchased: int
    quantity_available_for_outbound: int
    quantity_outbound: int
    quantity_returned_by_customer: int
    quantity_pending_customer_return: int
    quantity_available_for_supplier_return: int
    quantity_returned_to_supplier: int
    quantity_pending_supplier_return: int
    lifecycle_status: str


@dataclass(frozen=True, slots=True)
class PurchaseTrackingDTO:
    """Visão consolidada de uma compra e de seus itens."""

    purchase_id: int
    supplier_id: int
    supplier_name: str
    invoice_number: str
    invoice_series: str | None
    issue_date: str
    purchase_status: str
    items: tuple[PurchaseItemTrackingDTO, ...]
```

## `src\dtos\purchase_tracking_dto.py`

```python
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class PurchaseTrackingDTO:
    """Dados consolidados de acompanhamento de um item de compra."""

    purchase_item_id: int
    purchase_id: int

    invoice_number: str
    invoice_series: str | None
    issue_date: str
    purchase_status: str

    supplier_id: int
    supplier_name: str

    part_id: int
    part_code: str
    part_name: str

    quantity_purchased: int
    quantity_available: int
    quantity_sent: int

    quantity_customer_returned: int
    quantity_pending_customer_return: int

    quantity_available_supplier_return: int
    quantity_supplier_returned: int

    quantity_pending_completion: int
    tracking_status: str
```

## `src\dtos\supplier_return_dto.py`

```python

```

## `src\main.py`

```python
from fastapi import FastAPI

from src.api.routes import (
    outbound_router,
    part_router,
    purchase_router,
    purchase_tracking_router,
    supplier_contact_router,
    supplier_router,
)


app = FastAPI(
    title="SIGC",
    description=(
        "Sistema Integrado de Gestão de Cascos"
    ),
    version="0.1.0",
)


app.include_router(
    supplier_router
)

app.include_router(
    supplier_contact_router
)

app.include_router(
    part_router
)

app.include_router(
    purchase_router
)

app.include_router(
    purchase_tracking_router
)

app.include_router(
    outbound_router
)


@app.get(
    "/",
    tags=["System"],
)
def root() -> dict[str, str]:
    return {
        "sistema": "SIGC",
        "mensagem": (
            "Sistema Integrado de Gestão de "
            "Cascos em funcionamento."
        ),
        "versao": "0.1.0",
    }
```

## `src\models\__init__.py`

```python
from src.models.part import Part
from src.models.purchase import Purchase
from src.models.purchase_item import PurchaseItem
from src.models.role import Role
from src.models.supplier import Supplier
from src.models.supplier_contact import SupplierContact
from src.models.supplier_return import SupplierReturn
from src.models.supplier_return_item import SupplierReturnItem
from src.models.user import User
from src.models.outbound import Outbound
from src.models.outbound_item import OutboundItem
from src.models.outbound_purchase_allocation import (
    OutboundPurchaseAllocation,
)
from src.models.customer_return import CustomerReturn
from src.models.customer_return_allocation import (
    CustomerReturnAllocation,
)
from src.models.customer_return_item import CustomerReturnItem
from src.models.transfer import Transfer
from src.models.transfer_item import TransferItem
from src.models.core_movement import CoreMovement
from src.models.audit_log import AuditLog

__all__ = [
    "Part",
    "Purchase",
    "PurchaseItem",
    "Role",
    "Supplier",
    "SupplierContact",
    "SupplierReturn",
    "SupplierReturnItem",
    "User",
    "Outbound",
    "OutboundItem",
    "OutboundPurchaseAllocation",
    "CustomerReturn",
    "CustomerReturnAllocation",
    "CustomerReturnItem",
    "Transfer",
    "TransferItem",
    "CoreMovement",
    "AuditLog",
]
```

## `src\models\audit_log.py`

```python
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from src.core.time import now_iso
from src.database.connection import Base


class AuditLog(Base):
    __tablename__ = "audit_logs"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    user_id: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    action: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    module: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    entity_type: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    entity_id: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    old_values: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    new_values: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    justification: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    created_at: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default=now_iso,
    )
```

## `src\models\core_movement.py`

```python
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.core.time import now_iso
from src.database.connection import Base


class CoreMovement(Base):
    __tablename__ = "core_movements"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    part_id: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    movement_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    quantity: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    reference_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    reference_id: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    created_by: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    created_at: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default=now_iso,
    )
```

## `src\models\customer_return.py`

```python
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from src.core.time import now_iso
from src.database.connection import Base


class CustomerReturn(Base):
    __tablename__ = "customer_returns"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    return_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    reference_number: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    customer_name: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    created_by: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )

    created_at: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default=now_iso,
    )

    updated_at: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default=now_iso,
        onupdate=now_iso,
    )

    status: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    notes: Mapped[str | None] = mapped_column(
        String(1000),
        nullable=True,
    )
```

## `src\models\customer_return_allocation.py`

```python
from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from src.database.connection import Base


class CustomerReturnAllocation(Base):
    __tablename__ = "customer_return_allocations"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    customer_return_item_id: Mapped[int] = mapped_column(
        ForeignKey("customer_return_items.id"),
        nullable=False,
    )

    outbound_item_id: Mapped[int] = mapped_column(
        ForeignKey("outbound_items.id"),
        nullable=False,
    )

    quantity_allocated: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )
```

## `src\models\customer_return_item.py`

```python
from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from src.database.connection import Base


class CustomerReturnItem(Base):
    __tablename__ = "customer_return_items"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    customer_return_id: Mapped[int] = mapped_column(
        ForeignKey("customer_returns.id"),
        nullable=False,
    )

    part_id: Mapped[int] = mapped_column(
        ForeignKey("parts.id"),
        nullable=False,
    )

    quantity: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )
```

## `src\models\outbound.py`

```python
from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.core.time import now_iso
from src.database.connection import Base


class Outbound(Base):
    __tablename__ = "outbounds"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    destination_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    work_order_number: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    sales_invoice_number: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    created_by: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
    )

    created_at: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default=now_iso,
    )

    updated_at: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default=now_iso,
        onupdate=now_iso,
    )

    status: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )
```

## `src\models\outbound_item.py`

```python
from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.core.time import now_iso
from src.database.connection import Base


class OutboundItem(Base):
    __tablename__ = "outbound_items"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    outbound_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("outbounds.id"),
        nullable=False,
    )

    part_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("parts.id"),
        nullable=False,
    )

    quantity: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    created_at: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default=now_iso,
    )
```

## `src\models\outbound_purchase_allocation.py`

```python
from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from src.database.connection import Base


class OutboundPurchaseAllocation(Base):
    __tablename__ = "outbound_purchase_allocations"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    outbound_item_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("outbound_items.id"),
        nullable=False,
    )

    purchase_item_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("purchase_items.id"),
        nullable=False,
    )

    quantity_allocated: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )
```

## `src\models\part.py`

```python
from sqlalchemy import (
    ForeignKey,
    Integer,
    String,
    Text,
    UniqueConstraint,
)
from sqlalchemy.orm import Mapped, mapped_column

from src.core.time import now_iso
from src.database.connection import Base


class Part(Base):
    """Peça que possui obrigação de devolução de casco."""

    __tablename__ = "parts"

    __table_args__ = (
        UniqueConstraint(
            "supplier_id",
            "part_code",
            name="uq_parts_supplier_id_part_code",
        ),
    )

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    supplier_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("suppliers.id"),
        nullable=False,
    )

    part_code: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    name: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    return_deadline_days: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    is_active: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=1,
    )

    created_at: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default=now_iso,
    )

    updated_at: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default=now_iso,
        onupdate=now_iso,
    )
```

## `src\models\purchase.py`

```python
from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.core.time import now_iso
from src.database.connection import Base


class Purchase(Base):
    __tablename__ = "purchases"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    supplier_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("suppliers.id"),
        nullable=False,
    )

    invoice_number: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    invoice_series: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    issue_date: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    received_at: Mapped[str | None] = mapped_column(
        String(30),
        nullable=True,
    )

    notes: Mapped[str | None] = mapped_column(
        String(1000),
        nullable=True,
    )

    created_by: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
    )

    created_at: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default=now_iso,
    )

    updated_at: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default=now_iso,
        onupdate=now_iso,
    )

    status: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )
```

## `src\models\purchase_item.py`

```python
from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.core.time import now_iso
from src.database.connection import Base


class PurchaseItem(Base):
    __tablename__ = "purchase_items"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    purchase_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("purchases.id"),
        nullable=False,
    )

    part_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("parts.id"),
        nullable=False,
    )

    quantity_purchased: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    quantity_available: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    created_at: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default=now_iso,
    )
```

## `src\models\role.py`

```python
from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from src.core.time import now_iso
from src.database.connection import Base


class Role(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    name: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    created_at: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default=now_iso,
    )
```

## `src\models\supplier.py`

```python
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from src.core.time import now_iso
from src.database.connection import Base


class Supplier(Base):
    __tablename__ = "suppliers"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    name: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    document: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    address: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    notes: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    is_active: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=1,
    )

    created_at: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default=now_iso,
    )

    updated_at: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default=now_iso,
        onupdate=now_iso,
    )
```

## `src\models\supplier_contact.py`

```python
from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.core.time import now_iso
from src.database.connection import Base


class SupplierContact(Base):
    __tablename__ = "supplier_contacts"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    supplier_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("suppliers.id"),
        nullable=False,
    )

    name: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    email: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    phone: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    position: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    is_primary: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0,
    )

    is_active: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=1,
    )

    created_at: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default=now_iso,
    )
```

## `src\models\supplier_return.py`

```python
from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.core.time import now_iso
from src.database.connection import Base


class SupplierReturn(Base):
    __tablename__ = "supplier_returns"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    supplier_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("suppliers.id"),
        nullable=False,
    )

    dispatch_invoice_number: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    dispatch_invoice_series: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    issue_date: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    created_by: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
    )

    created_at: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default=now_iso,
    )

    updated_at: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default=now_iso,
        onupdate=now_iso,
    )

    status: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    notes: Mapped[str | None] = mapped_column(
        String(1000),
        nullable=True,
    )
```

## `src\models\supplier_return_item.py`

```python
from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.core.time import now_iso
from src.database.connection import Base


class SupplierReturnItem(Base):
    __tablename__ = "supplier_return_items"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    supplier_return_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("supplier_returns.id"),
        nullable=False,
    )

    purchase_item_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("purchase_items.id"),
        nullable=False,
    )

    quantity: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    created_at: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default=now_iso,
    )
```

## `src\models\transfer.py`

```python
from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.core.time import now_iso
from src.database.connection import Base


class Transfer(Base):
    __tablename__ = "transfers"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    origin_branch_id: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    destination_branch_id: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    invoice_number: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    issue_date: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    created_by: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )

    created_at: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default=now_iso,
    )
```

## `src\models\transfer_item.py`

```python
from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from src.database.connection import Base


class TransferItem(Base):
    __tablename__ = "transfer_items"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    transfer_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("transfers.id"),
        nullable=False,
    )

    part_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("parts.id"),
        nullable=False,
    )

    quantity: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )
```

## `src\models\user.py`

```python
from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.core.time import now_iso
from src.database.connection import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    full_name: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )

    username: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        unique=True,
    )

    email: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    role_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("roles.id"),
        nullable=False,
    )

    is_active: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=1,
    )

    last_login_at: Mapped[str | None] = mapped_column(
        String(30),
        nullable=True,
    )

    created_at: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default=now_iso,
    )

    updated_at: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default=now_iso,
        onupdate=now_iso,
    )
```

## `src\queries\__init__.py`

```python
"""Consultas de leitura consolidada do SIGC."""

from src.queries.purchase_tracking_query import PurchaseTrackingQuery

__all__ = ["PurchaseTrackingQuery"]
```

## `src\queries\customer_return_query.py`

```python

```

## `src\queries\dashboard_query.py`

```python

```

## `src\queries\purchase_query.py`

```python

```

## `src\queries\purchase_tracking_query.py`

```python
from collections import defaultdict

from sqlalchemy import select
from sqlalchemy.orm import Session

from src.dtos.purchase_tracking import (
    PurchaseItemTrackingDTO,
    PurchaseTrackingDTO,
)
from src.models.customer_return_allocation import (
    CustomerReturnAllocation,
)
from src.models.outbound_purchase_allocation import (
    OutboundPurchaseAllocation,
)
from src.models.part import Part
from src.models.purchase import Purchase
from src.models.purchase_item import PurchaseItem
from src.models.supplier import Supplier
from src.models.supplier_return_item import SupplierReturnItem


class PurchaseTrackingQuery:
    """Monta visões de acompanhamento sem alterar o banco."""

    def __init__(self, session: Session):
        self.session = session

    def get_by_purchase_id(
        self,
        purchase_id: int,
    ) -> PurchaseTrackingDTO | None:
        header_statement = (
            select(Purchase, Supplier)
            .join(Supplier, Supplier.id == Purchase.supplier_id)
            .where(Purchase.id == purchase_id)
        )
        header = self.session.execute(header_statement).one_or_none()

        if header is None:
            return None

        purchase, supplier = header

        item_statement = (
            select(PurchaseItem, Part)
            .join(Part, Part.id == PurchaseItem.part_id)
            .where(PurchaseItem.purchase_id == purchase_id)
            .order_by(PurchaseItem.id)
        )
        item_rows = self.session.execute(item_statement).all()

        purchase_item_ids = [
            purchase_item.id
            for purchase_item, _part in item_rows
        ]

        outbound_by_purchase_item = self._get_outbound_quantities(
            purchase_item_ids
        )
        returned_by_purchase_item = (
            self._get_customer_returned_quantities(
                purchase_item_ids
            )
        )
        supplier_returned_by_purchase_item = (
            self._get_supplier_returned_quantities(
                purchase_item_ids
            )
        )

        items = tuple(
            self._build_item_dto(
                purchase_item=purchase_item,
                part=part,
                quantity_outbound=outbound_by_purchase_item.get(
                    purchase_item.id,
                    0,
                ),
                quantity_returned_by_customer=(
                    returned_by_purchase_item.get(
                        purchase_item.id,
                        0,
                    )
                ),
                quantity_returned_to_supplier=(
                    supplier_returned_by_purchase_item.get(
                        purchase_item.id,
                        0,
                    )
                ),
            )
            for purchase_item, part in item_rows
        )

        return PurchaseTrackingDTO(
            purchase_id=purchase.id,
            supplier_id=supplier.id,
            supplier_name=supplier.name,
            invoice_number=purchase.invoice_number,
            invoice_series=purchase.invoice_series,
            issue_date=purchase.issue_date,
            purchase_status=purchase.status,
            items=items,
        )

    def _get_outbound_quantities(
        self,
        purchase_item_ids: list[int],
    ) -> dict[int, int]:
        if not purchase_item_ids:
            return {}

        statement = (
            select(OutboundPurchaseAllocation)
            .where(
                OutboundPurchaseAllocation.purchase_item_id.in_(
                    purchase_item_ids
                )
            )
            .order_by(OutboundPurchaseAllocation.id)
        )
        allocations = self.session.scalars(statement).all()

        quantities: dict[int, int] = defaultdict(int)
        for allocation in allocations:
            quantities[allocation.purchase_item_id] += (
                allocation.quantity_allocated
            )

        return dict(quantities)

    def _get_customer_returned_quantities(
        self,
        purchase_item_ids: list[int],
    ) -> dict[int, int]:
        """
        Redistribui as devoluções de clientes pelas origens FIFO
        preservadas em outbound_purchase_allocations.
        """
        if not purchase_item_ids:
            return {}

        outbound_statement = (
            select(OutboundPurchaseAllocation)
            .where(
                OutboundPurchaseAllocation.purchase_item_id.in_(
                    purchase_item_ids
                )
            )
            .order_by(
                OutboundPurchaseAllocation.outbound_item_id,
                OutboundPurchaseAllocation.id,
            )
        )
        target_allocations = self.session.scalars(
            outbound_statement
        ).all()

        outbound_item_ids = {
            allocation.outbound_item_id
            for allocation in target_allocations
        }
        if not outbound_item_ids:
            return {}

        all_outbound_statement = (
            select(OutboundPurchaseAllocation)
            .where(
                OutboundPurchaseAllocation.outbound_item_id.in_(
                    outbound_item_ids
                )
            )
            .order_by(
                OutboundPurchaseAllocation.outbound_item_id,
                OutboundPurchaseAllocation.id,
            )
        )
        all_outbound_allocations = self.session.scalars(
            all_outbound_statement
        ).all()

        return_statement = (
            select(CustomerReturnAllocation)
            .where(
                CustomerReturnAllocation.outbound_item_id.in_(
                    outbound_item_ids
                )
            )
            .order_by(
                CustomerReturnAllocation.outbound_item_id,
                CustomerReturnAllocation.id,
            )
        )
        customer_returns = self.session.scalars(
            return_statement
        ).all()

        allocations_by_outbound: dict[
            int,
            list[OutboundPurchaseAllocation],
        ] = defaultdict(list)
        for allocation in all_outbound_allocations:
            allocations_by_outbound[
                allocation.outbound_item_id
            ].append(allocation)

        returned_by_outbound: dict[int, int] = defaultdict(int)
        for allocation in customer_returns:
            returned_by_outbound[allocation.outbound_item_id] += (
                allocation.quantity_allocated
            )

        target_ids = set(purchase_item_ids)
        quantities: dict[int, int] = defaultdict(int)

        for outbound_item_id, allocations in (
            allocations_by_outbound.items()
        ):
            remaining = returned_by_outbound.get(
                outbound_item_id,
                0,
            )

            for allocation in allocations:
                if remaining <= 0:
                    break

                allocated_return = min(
                    remaining,
                    allocation.quantity_allocated,
                )

                if allocation.purchase_item_id in target_ids:
                    quantities[allocation.purchase_item_id] += (
                        allocated_return
                    )

                remaining -= allocated_return

        return dict(quantities)

    def _get_supplier_returned_quantities(
        self,
        purchase_item_ids: list[int],
    ) -> dict[int, int]:
        if not purchase_item_ids:
            return {}

        statement = (
            select(SupplierReturnItem)
            .where(
                SupplierReturnItem.purchase_item_id.in_(
                    purchase_item_ids
                )
            )
            .order_by(SupplierReturnItem.id)
        )
        items = self.session.scalars(statement).all()

        quantities: dict[int, int] = defaultdict(int)
        for item in items:
            quantities[item.purchase_item_id] += item.quantity

        return dict(quantities)

    @staticmethod
    def _build_item_dto(
        purchase_item: PurchaseItem,
        part: Part,
        quantity_outbound: int,
        quantity_returned_by_customer: int,
        quantity_returned_to_supplier: int,
    ) -> PurchaseItemTrackingDTO:
        pending_customer = max(
            quantity_outbound - quantity_returned_by_customer,
            0,
        )
        available_supplier = max(
            quantity_returned_by_customer
            - quantity_returned_to_supplier,
            0,
        )
        pending_supplier = max(
            purchase_item.quantity_purchased
            - quantity_returned_to_supplier,
            0,
        )

        status = PurchaseTrackingQuery._resolve_lifecycle_status(
            quantity_purchased=purchase_item.quantity_purchased,
            quantity_outbound=quantity_outbound,
            quantity_returned_by_customer=(
                quantity_returned_by_customer
            ),
            quantity_returned_to_supplier=(
                quantity_returned_to_supplier
            ),
        )

        return PurchaseItemTrackingDTO(
            purchase_item_id=purchase_item.id,
            part_id=part.id,
            part_code=part.part_code,
            part_name=part.name,
            quantity_purchased=purchase_item.quantity_purchased,
            quantity_available_for_outbound=(
                purchase_item.quantity_available
            ),
            quantity_outbound=quantity_outbound,
            quantity_returned_by_customer=(
                quantity_returned_by_customer
            ),
            quantity_pending_customer_return=pending_customer,
            quantity_available_for_supplier_return=(
                available_supplier
            ),
            quantity_returned_to_supplier=(
                quantity_returned_to_supplier
            ),
            quantity_pending_supplier_return=pending_supplier,
            lifecycle_status=status,
        )

    @staticmethod
    def _resolve_lifecycle_status(
        quantity_purchased: int,
        quantity_outbound: int,
        quantity_returned_by_customer: int,
        quantity_returned_to_supplier: int,
    ) -> str:
        if quantity_returned_to_supplier >= quantity_purchased:
            return "COMPLETED"

        if quantity_returned_to_supplier > 0:
            return "PARTIALLY_RETURNED_TO_SUPPLIER"

        if quantity_returned_by_customer >= quantity_outbound > 0:
            return "AVAILABLE_FOR_SUPPLIER_RETURN"

        if quantity_returned_by_customer > 0:
            return "PARTIALLY_RETURNED_BY_CUSTOMER"

        if quantity_outbound > 0:
            return "PENDING_CUSTOMER_RETURN"

        return "AVAILABLE_FOR_OUTBOUND"
```

## `src\queries\supplier_return_query.py`

```python

```

## `src\repositories\__init__.py`

```python

```

## `src\repositories\audit_log_repository.py`

```python
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.audit_log import AuditLog


class AuditLogRepository:
    """Responsável pela persistência do histórico de auditoria."""

    def __init__(self, session: Session):
        self.session = session

    def get_by_id(
        self,
        audit_log_id: int,
    ) -> AuditLog | None:
        statement = select(AuditLog).where(
            AuditLog.id == audit_log_id
        )
        return self.session.scalar(statement)

    def list_by_user(
        self,
        user_id: int,
    ) -> list[AuditLog]:
        statement = (
            select(AuditLog)
            .where(AuditLog.user_id == user_id)
            .order_by(
                AuditLog.created_at,
                AuditLog.id,
            )
        )
        return list(self.session.scalars(statement).all())

    def list_by_entity(
        self,
        entity_type: str,
        entity_id: int,
    ) -> list[AuditLog]:
        statement = (
            select(AuditLog)
            .where(
                AuditLog.entity_type == entity_type,
                AuditLog.entity_id == entity_id,
            )
            .order_by(
                AuditLog.created_at,
                AuditLog.id,
            )
        )
        return list(self.session.scalars(statement).all())

    def list_by_module(
        self,
        module: str,
    ) -> list[AuditLog]:
        statement = (
            select(AuditLog)
            .where(AuditLog.module == module)
            .order_by(
                AuditLog.created_at,
                AuditLog.id,
            )
        )
        return list(self.session.scalars(statement).all())

    def add(
        self,
        audit_log: AuditLog,
    ) -> AuditLog:
        self.session.add(audit_log)
        self.session.flush()
        return audit_log
```

## `src\repositories\core_movement_repository.py`

```python
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.core_movement import CoreMovement


class CoreMovementRepository:
    """Responsável pela persistência do histórico de movimentações."""

    def __init__(self, session: Session):
        self.session = session

    def get_by_id(
        self,
        movement_id: int,
    ) -> CoreMovement | None:
        statement = select(CoreMovement).where(
            CoreMovement.id == movement_id
        )
        return self.session.scalar(statement)

    def list_by_part(
        self,
        part_id: int,
    ) -> list[CoreMovement]:
        statement = (
            select(CoreMovement)
            .where(CoreMovement.part_id == part_id)
            .order_by(
                CoreMovement.created_at,
                CoreMovement.id,
            )
        )
        return list(self.session.scalars(statement).all())

    def list_by_reference(
        self,
        reference_type: str,
        reference_id: int,
    ) -> list[CoreMovement]:
        statement = (
            select(CoreMovement)
            .where(
                CoreMovement.reference_type == reference_type,
                CoreMovement.reference_id == reference_id,
            )
            .order_by(CoreMovement.id)
        )
        return list(self.session.scalars(statement).all())

    def add(
        self,
        movement: CoreMovement,
    ) -> CoreMovement:
        self.session.add(movement)
        self.session.flush()
        return movement
```

## `src\repositories\customer_return_allocation_repository.py`

```python
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.customer_return_allocation import (
    CustomerReturnAllocation,
)


class CustomerReturnAllocationRepository:
    """Responsável pela persistência das alocações de devolução."""

    def __init__(self, session: Session):
        self.session = session

    def get_by_id(
        self,
        allocation_id: int,
    ) -> CustomerReturnAllocation | None:
        statement = select(
            CustomerReturnAllocation
        ).where(
            CustomerReturnAllocation.id == allocation_id
        )
        return self.session.scalar(statement)

    def list_by_return_item(
        self,
        customer_return_item_id: int,
    ) -> list[CustomerReturnAllocation]:
        statement = (
            select(CustomerReturnAllocation)
            .where(
                CustomerReturnAllocation.customer_return_item_id
                == customer_return_item_id
            )
            .order_by(CustomerReturnAllocation.id)
        )
        return list(self.session.scalars(statement).all())

    def list_by_outbound_item(
        self,
        outbound_item_id: int,
    ) -> list[CustomerReturnAllocation]:
        statement = (
            select(CustomerReturnAllocation)
            .where(
                CustomerReturnAllocation.outbound_item_id
                == outbound_item_id
            )
            .order_by(CustomerReturnAllocation.id)
        )
        return list(self.session.scalars(statement).all())

    def add(
        self,
        allocation: CustomerReturnAllocation,
    ) -> CustomerReturnAllocation:
        self.session.add(allocation)
        self.session.flush()
        return allocation
```

## `src\repositories\customer_return_item_repository.py`

```python
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.customer_return_item import CustomerReturnItem


class CustomerReturnItemRepository:
    """Responsável pela persistência dos itens de devolução."""

    def __init__(self, session: Session):
        self.session = session

    def get_by_id(
        self,
        customer_return_item_id: int,
    ) -> CustomerReturnItem | None:
        statement = select(CustomerReturnItem).where(
            CustomerReturnItem.id == customer_return_item_id
        )
        return self.session.scalar(statement)

    def list_by_customer_return(
        self,
        customer_return_id: int,
    ) -> list[CustomerReturnItem]:
        statement = (
            select(CustomerReturnItem)
            .where(
                CustomerReturnItem.customer_return_id
                == customer_return_id
            )
            .order_by(CustomerReturnItem.id)
        )
        return list(self.session.scalars(statement).all())

    def add(
        self,
        item: CustomerReturnItem,
    ) -> CustomerReturnItem:
        self.session.add(item)
        self.session.flush()
        return item
```

## `src\repositories\customer_return_repository.py`

```python
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.customer_return import CustomerReturn


class CustomerReturnRepository:
    """Responsável pela persistência de devoluções de clientes."""

    def __init__(self, session: Session):
        self.session = session

    def get_by_id(
        self,
        customer_return_id: int,
    ) -> CustomerReturn | None:
        statement = select(CustomerReturn).where(
            CustomerReturn.id == customer_return_id
        )
        return self.session.scalar(statement)

    def list_all(self) -> list[CustomerReturn]:
        statement = select(CustomerReturn).order_by(
            CustomerReturn.created_at,
            CustomerReturn.id,
        )
        return list(self.session.scalars(statement).all())

    def add(
        self,
        customer_return: CustomerReturn,
    ) -> CustomerReturn:
        self.session.add(customer_return)
        self.session.flush()
        return customer_return
```

## `src\repositories\outbound_item_repository.py`

```python
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.outbound_item import OutboundItem


class OutboundItemRepository:
    """Responsável pela persistência dos itens de saída."""

    def __init__(
        self,
        session: Session,
    ):
        self.session = session

    def get_by_id(
        self,
        outbound_item_id: int,
    ) -> OutboundItem | None:
        statement = select(
            OutboundItem
        ).where(
            OutboundItem.id == outbound_item_id
        )

        return self.session.scalar(
            statement
        )

    def list_by_outbound(
        self,
        outbound_id: int,
    ) -> list[OutboundItem]:
        statement = (
            select(OutboundItem)
            .where(
                OutboundItem.outbound_id
                == outbound_id
            )
            .order_by(
                OutboundItem.id
            )
        )

        return list(
            self.session.scalars(
                statement
            ).all()
        )

    def list_by_part(
        self,
        part_id: int,
    ) -> list[OutboundItem]:
        statement = (
            select(OutboundItem)
            .where(
                OutboundItem.part_id
                == part_id
            )
            .order_by(
                OutboundItem.created_at,
                OutboundItem.id,
            )
        )

        return list(
            self.session.scalars(
                statement
            ).all()
        )

    def add(
        self,
        outbound_item: OutboundItem,
    ) -> OutboundItem:
        self.session.add(
            outbound_item
        )

        self.session.flush()

        return outbound_item
```

## `src\repositories\outbound_purchase_allocation_repository.py`

```python
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.outbound_purchase_allocation import (
    OutboundPurchaseAllocation,
)


class OutboundPurchaseAllocationRepository:
    """Responsável pela persistência das alocações de saída."""

    def __init__(self, session: Session):
        self.session = session

    def get_by_id(
        self,
        allocation_id: int,
    ) -> OutboundPurchaseAllocation | None:
        statement = select(
            OutboundPurchaseAllocation
        ).where(
            OutboundPurchaseAllocation.id == allocation_id
        )
        return self.session.scalar(statement)

    def list_by_outbound_item(
        self,
        outbound_item_id: int,
    ) -> list[OutboundPurchaseAllocation]:
        statement = (
            select(OutboundPurchaseAllocation)
            .where(
                OutboundPurchaseAllocation.outbound_item_id
                == outbound_item_id
            )
            .order_by(OutboundPurchaseAllocation.id)
        )
        return list(self.session.scalars(statement).all())

    def list_by_purchase_item(
        self,
        purchase_item_id: int,
    ) -> list[OutboundPurchaseAllocation]:
        statement = (
            select(OutboundPurchaseAllocation)
            .where(
                OutboundPurchaseAllocation.purchase_item_id
                == purchase_item_id
            )
            .order_by(OutboundPurchaseAllocation.id)
        )
        return list(self.session.scalars(statement).all())

    def add(
        self,
        allocation: OutboundPurchaseAllocation,
    ) -> OutboundPurchaseAllocation:
        self.session.add(allocation)
        self.session.flush()
        return allocation
```

## `src\repositories\outbound_repository.py`

```python
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.outbound import Outbound


class OutboundRepository:
    """Responsável pela persistência das saídas."""

    def __init__(
        self,
        session: Session,
    ) -> None:
        self.session = session

    def get_by_id(
        self,
        outbound_id: int,
    ) -> Outbound | None:
        statement = select(Outbound).where(
            Outbound.id == outbound_id
        )

        return self.session.scalar(
            statement
        )

    def get_by_work_order_number(
        self,
        work_order_number: str,
    ) -> Outbound | None:
        statement = select(Outbound).where(
            Outbound.work_order_number
            == work_order_number
        )

        return self.session.scalar(
            statement
        )

    def get_by_sales_invoice_number(
        self,
        sales_invoice_number: str,
    ) -> Outbound | None:
        statement = select(Outbound).where(
            Outbound.sales_invoice_number
            == sales_invoice_number
        )

        return self.session.scalar(
            statement
        )

    def list_all(
        self,
    ) -> list[Outbound]:
        statement = select(Outbound).order_by(
            Outbound.created_at.desc(),
            Outbound.id.desc(),
        )

        return list(
            self.session.scalars(
                statement
            ).all()
        )

    def list_by_status(
        self,
        status: str,
    ) -> list[Outbound]:
        statement = (
            select(Outbound)
            .where(
                Outbound.status == status
            )
            .order_by(
                Outbound.created_at.desc(),
                Outbound.id.desc(),
            )
        )

        return list(
            self.session.scalars(
                statement
            ).all()
        )

    def list_by_destination_type(
        self,
        destination_type: str,
    ) -> list[Outbound]:
        statement = (
            select(Outbound)
            .where(
                Outbound.destination_type
                == destination_type
            )
            .order_by(
                Outbound.created_at.desc(),
                Outbound.id.desc(),
            )
        )

        return list(
            self.session.scalars(
                statement
            ).all()
        )

    def add(
        self,
        outbound: Outbound,
    ) -> Outbound:
        self.session.add(
            outbound
        )

        self.session.flush()

        return outbound

    def save(
        self,
        outbound: Outbound,
    ) -> Outbound:
        self.session.add(
            outbound
        )

        self.session.flush()

        return outbound
```

## `src\repositories\part_repository.py`

```python
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.part import Part


class PartRepository:
    """Responsável pela persistência de peças."""

    def __init__(
        self,
        session: Session,
    ):
        self.session = session

    def get_by_id(
        self,
        part_id: int,
    ) -> Part | None:
        """Busca uma peça pelo identificador."""

        statement = select(Part).where(
            Part.id == part_id
        )

        return self.session.scalar(statement)

    def get_by_supplier_and_code(
        self,
        supplier_id: int,
        part_code: str,
    ) -> Part | None:
        """Busca uma peça pelo fornecedor e código original."""

        statement = select(Part).where(
            Part.supplier_id == supplier_id,
            Part.part_code == part_code,
        )

        return self.session.scalar(statement)

    def list_all(self) -> list[Part]:
        """Lista todas as peças."""

        statement = select(Part).order_by(
            Part.name,
            Part.part_code,
            Part.id,
        )

        return list(
            self.session.scalars(statement).all()
        )

    def list_by_supplier(
        self,
        supplier_id: int,
    ) -> list[Part]:
        """Lista as peças associadas a um fornecedor."""

        statement = (
            select(Part)
            .where(
                Part.supplier_id == supplier_id
            )
            .order_by(
                Part.name,
                Part.part_code,
                Part.id,
            )
        )

        return list(
            self.session.scalars(statement).all()
        )

    def add(
        self,
        part: Part,
    ) -> Part:
        """Adiciona uma nova peça à sessão."""

        self.session.add(part)
        self.session.flush()

        return part

    def save(
        self,
        part: Part,
    ) -> Part:
        """Persiste alterações realizadas em uma peça."""

        self.session.add(part)
        self.session.flush()

        return part
```

## `src\repositories\purchase_item_repository.py`

```python
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.purchase_item import PurchaseItem


class PurchaseItemRepository:
    """Responsável pela persistência dos itens de compra."""

    def __init__(self, session: Session):
        self.session = session

    def get_by_id(
        self,
        purchase_item_id: int,
    ) -> PurchaseItem | None:
        statement = select(PurchaseItem).where(
            PurchaseItem.id == purchase_item_id
        )
        return self.session.scalar(statement)

    def list_by_purchase(
        self,
        purchase_id: int,
    ) -> list[PurchaseItem]:
        statement = (
            select(PurchaseItem)
            .where(PurchaseItem.purchase_id == purchase_id)
            .order_by(PurchaseItem.id)
        )
        return list(self.session.scalars(statement).all())

    def list_available_by_part(
        self,
        part_id: int,
    ) -> list[PurchaseItem]:
        statement = (
            select(PurchaseItem)
            .where(
                PurchaseItem.part_id == part_id,
                PurchaseItem.quantity_available > 0,
            )
            .order_by(
                PurchaseItem.created_at,
                PurchaseItem.id,
            )
        )
        return list(self.session.scalars(statement).all())

    def add(
        self,
        purchase_item: PurchaseItem,
    ) -> PurchaseItem:
        self.session.add(purchase_item)
        self.session.flush()
        return purchase_item
```

## `src\repositories\purchase_repository.py`

```python
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.purchase import Purchase


class PurchaseRepository:
    """
    Responsável pela persistência de compras.
    """

    def __init__(
        self,
        session: Session,
    ) -> None:
        self.session = session

    def get_by_id(
        self,
        purchase_id: int,
    ) -> Purchase | None:
        """
        Busca uma compra pelo identificador.
        """

        statement = select(
            Purchase
        ).where(
            Purchase.id == purchase_id
        )

        return self.session.scalar(statement)

    def get_by_invoice(
        self,
        supplier_id: int,
        invoice_number: str,
        invoice_series: str | None,
    ) -> Purchase | None:
        """
        Busca uma compra pela nota fiscal, série e fornecedor.
        """

        statement = select(
            Purchase
        ).where(
            Purchase.supplier_id == supplier_id,
            Purchase.invoice_number == invoice_number,
            Purchase.invoice_series == invoice_series,
        )

        return self.session.scalar(statement)

    def list_all(
        self,
    ) -> list[Purchase]:
        """
        Lista todas as compras.
        """

        statement = select(
            Purchase
        ).order_by(
            Purchase.issue_date.desc(),
            Purchase.id.desc(),
        )

        return list(
            self.session.scalars(
                statement
            ).all()
        )

    def list_by_supplier(
        self,
        supplier_id: int,
    ) -> list[Purchase]:
        """
        Lista as compras de determinado fornecedor.
        """

        statement = (
            select(
                Purchase
            )
            .where(
                Purchase.supplier_id == supplier_id
            )
            .order_by(
                Purchase.issue_date.desc(),
                Purchase.id.desc(),
            )
        )

        return list(
            self.session.scalars(
                statement
            ).all()
        )

    def add(
        self,
        purchase: Purchase,
    ) -> Purchase:
        """
        Adiciona uma compra.
        """

        self.session.add(purchase)
        self.session.flush()

        return purchase

    def save(
        self,
        purchase: Purchase,
    ) -> Purchase:
        """
        Salva as alterações de uma compra.
        """

        self.session.add(purchase)
        self.session.flush()

        return purchase
```

## `src\repositories\role_repository.py`

```python
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.role import Role


class RoleRepository:
    """Responsável pela persistência de perfis de acesso."""

    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, role_id: int) -> Role | None:
        statement = select(Role).where(Role.id == role_id)
        return self.session.scalar(statement)

    def get_by_name(self, name: str) -> Role | None:
        statement = select(Role).where(Role.name == name)
        return self.session.scalar(statement)

    def list_all(self) -> list[Role]:
        statement = select(Role).order_by(Role.name)
        return list(self.session.scalars(statement).all())

    def add(self, role: Role) -> Role:
        self.session.add(role)
        self.session.flush()
        return role
```

## `src\repositories\supplier_contact_repository.py`

```python
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.supplier_contact import SupplierContact


class SupplierContactRepository:
    """Persistência dos contatos de fornecedores."""

    def __init__(
        self,
        session: Session,
    ):
        self.session = session

    def get_by_id(
        self,
        contact_id: int,
    ) -> SupplierContact | None:
        """Busca um contato pelo identificador."""

        statement = select(
            SupplierContact
        ).where(
            SupplierContact.id == contact_id
        )

        return self.session.scalar(statement)

    def list_by_supplier(
        self,
        supplier_id: int,
    ) -> list[SupplierContact]:
        """Lista os contatos de um fornecedor."""

        statement = (
            select(SupplierContact)
            .where(
                SupplierContact.supplier_id
                == supplier_id
            )
            .order_by(
                SupplierContact.is_primary.desc(),
                SupplierContact.name,
            )
        )

        return list(
            self.session.scalars(statement).all()
        )

    def get_primary_by_supplier(
        self,
        supplier_id: int,
    ) -> SupplierContact | None:
        """Busca o contato principal de um fornecedor."""

        statement = select(
            SupplierContact
        ).where(
            SupplierContact.supplier_id
            == supplier_id,
            SupplierContact.is_primary == 1,
        )

        return self.session.scalar(statement)

    def add(
        self,
        contact: SupplierContact,
    ) -> SupplierContact:
        """Adiciona um contato à sessão."""

        self.session.add(contact)
        self.session.flush()

        return contact

    def save(
        self,
        contact: SupplierContact,
    ) -> SupplierContact:
        """Salva alterações realizadas em um contato."""

        self.session.add(contact)
        self.session.flush()

        return contact
```

## `src\repositories\supplier_repository.py`

```python
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.supplier import Supplier


class SupplierRepository:
    """Responsável pela persistência de fornecedores."""

    def __init__(self, session: Session):
        self.session = session

    def get_by_id(
        self,
        supplier_id: int,
    ) -> Supplier | None:
        statement = select(
            Supplier
        ).where(
            Supplier.id == supplier_id
        )

        return self.session.scalar(statement)

    def get_by_document(
        self,
        document: str,
    ) -> Supplier | None:
        statement = select(
            Supplier
        ).where(
            Supplier.document == document
        )

        return self.session.scalar(statement)

    def list_all(
        self,
    ) -> list[Supplier]:
        statement = select(
            Supplier
        ).order_by(
            Supplier.name
        )

        return list(
            self.session.scalars(
                statement
            ).all()
        )

    def add(
        self,
        supplier: Supplier,
    ) -> Supplier:
        self.session.add(supplier)
        self.session.flush()
        return supplier

    def save(
        self,
        supplier: Supplier,
    ) -> Supplier:
        self.session.add(supplier)
        self.session.flush()
        return supplier
```

## `src\repositories\supplier_return_item_repository.py`

```python
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from src.models.supplier_return_item import (
    SupplierReturnItem,
)


class SupplierReturnItemRepository:
    """Responsável pela persistência dos itens das remessas."""

    def __init__(
        self,
        session: Session,
    ):
        self.session = session

    def get_by_id(
        self,
        supplier_return_item_id: int,
    ) -> SupplierReturnItem | None:
        statement = select(SupplierReturnItem).where(
            SupplierReturnItem.id
            == supplier_return_item_id
        )

        return self.session.scalar(statement)
    
    def get_by_supplier_return_and_purchase_item(
        self,
        supplier_return_id: int,
        purchase_item_id: int,
    ) -> SupplierReturnItem | None:
        statement = select(SupplierReturnItem).where(
            SupplierReturnItem.supplier_return_id
            == supplier_return_id,
            SupplierReturnItem.purchase_item_id
            == purchase_item_id,
        )

        return self.session.scalar(statement)

    def list_by_supplier_return(
        self,
        supplier_return_id: int,
    ) -> list[SupplierReturnItem]:
        statement = (
            select(SupplierReturnItem)
            .where(
                SupplierReturnItem.supplier_return_id
                == supplier_return_id
            )
            .order_by(
                SupplierReturnItem.id
            )
        )

        return list(
            self.session.scalars(statement).all()
        )

    def list_by_purchase_item(
        self,
        purchase_item_id: int,
    ) -> list[SupplierReturnItem]:
        statement = (
            select(SupplierReturnItem)
            .where(
                SupplierReturnItem.purchase_item_id
                == purchase_item_id
            )
            .order_by(
                SupplierReturnItem.id
            )
        )

        return list(
            self.session.scalars(statement).all()
        )

    def get_returned_quantity_by_purchase_item(
        self,
        purchase_item_id: int,
    ) -> int:
        statement = select(
            func.coalesce(
                func.sum(
                    SupplierReturnItem.quantity
                ),
                0,
            )
        ).where(
            SupplierReturnItem.purchase_item_id
            == purchase_item_id
        )

        returned_quantity = self.session.scalar(
            statement
        )

        return int(returned_quantity or 0)

    def add(
        self,
        supplier_return_item: SupplierReturnItem,
    ) -> SupplierReturnItem:
        self.session.add(supplier_return_item)
        self.session.flush()

        return supplier_return_item
```

## `src\repositories\supplier_return_repository.py`

```python
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.supplier_return import SupplierReturn


class SupplierReturnRepository:
    """Responsável pela persistência das remessas aos fornecedores."""

    def __init__(
        self,
        session: Session,
    ):
        self.session = session

    def get_by_id(
        self,
        supplier_return_id: int,
    ) -> SupplierReturn | None:
        statement = select(SupplierReturn).where(
            SupplierReturn.id == supplier_return_id
        )

        return self.session.scalar(statement)

    def get_by_dispatch_invoice_number(
        self,
        dispatch_invoice_number: str,
    ) -> SupplierReturn | None:
        statement = select(SupplierReturn).where(
            SupplierReturn.dispatch_invoice_number
            == dispatch_invoice_number
        )

        return self.session.scalar(statement)

    def list_all(
        self,
    ) -> list[SupplierReturn]:
        statement = select(SupplierReturn).order_by(
            SupplierReturn.issue_date,
            SupplierReturn.id,
        )

        return list(
            self.session.scalars(statement).all()
        )

    def list_by_supplier(
        self,
        supplier_id: int,
    ) -> list[SupplierReturn]:
        statement = (
            select(SupplierReturn)
            .where(
                SupplierReturn.supplier_id
                == supplier_id
            )
            .order_by(
                SupplierReturn.issue_date,
                SupplierReturn.id,
            )
        )

        return list(
            self.session.scalars(statement).all()
        )

    def add(
        self,
        supplier_return: SupplierReturn,
    ) -> SupplierReturn:
        self.session.add(supplier_return)
        self.session.flush()

        return supplier_return

    def save(
        self,
        supplier_return: SupplierReturn,
    ) -> SupplierReturn:
        self.session.add(supplier_return)
        self.session.flush()

        return supplier_return
```

## `src\repositories\transfer_item_repository.py`

```python
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.transfer_item import TransferItem


class TransferItemRepository:
    """Responsável pela persistência dos itens de transferência."""

    def __init__(self, session: Session):
        self.session = session

    def get_by_id(
        self,
        transfer_item_id: int,
    ) -> TransferItem | None:
        statement = select(TransferItem).where(
            TransferItem.id == transfer_item_id
        )
        return self.session.scalar(statement)

    def list_by_transfer(
        self,
        transfer_id: int,
    ) -> list[TransferItem]:
        statement = (
            select(TransferItem)
            .where(
                TransferItem.transfer_id == transfer_id
            )
            .order_by(TransferItem.id)
        )
        return list(self.session.scalars(statement).all())

    def add(
        self,
        item: TransferItem,
    ) -> TransferItem:
        self.session.add(item)
        self.session.flush()
        return item
```

## `src\repositories\transfer_repository.py`

```python
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.transfer import Transfer


class TransferRepository:
    """Responsável pela persistência de transferências internas."""

    def __init__(self, session: Session):
        self.session = session

    def get_by_id(
        self,
        transfer_id: int,
    ) -> Transfer | None:
        statement = select(Transfer).where(
            Transfer.id == transfer_id
        )
        return self.session.scalar(statement)

    def list_all(self) -> list[Transfer]:
        statement = select(Transfer).order_by(
            Transfer.created_at,
            Transfer.id,
        )
        return list(self.session.scalars(statement).all())

    def add(
        self,
        transfer: Transfer,
    ) -> Transfer:
        self.session.add(transfer)
        self.session.flush()
        return transfer
```

## `src\repositories\user_repository.py`

```python
from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.user import User


class UserRepository:
    """Responsável pela persistência de usuários."""

    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, user_id: int) -> User | None:
        statement = select(User).where(User.id == user_id)
        return self.session.scalar(statement)

    def get_by_username(self, username: str) -> User | None:
        statement = select(User).where(User.username == username)
        return self.session.scalar(statement)

    def get_by_email(self, email: str) -> User | None:
        statement = select(User).where(User.email == email)
        return self.session.scalar(statement)

    def list_all(self) -> list[User]:
        statement = select(User).order_by(User.full_name)
        return list(self.session.scalars(statement).all())

    def add(self, user: User) -> User:
        self.session.add(user)
        self.session.flush()
        return user

    def save(self, user: User) -> User:
        self.session.add(user)
        self.session.flush()
        return user
```

## `src\schemas\__init__.py`

```python

```

## `src\schemas\outbound_schema.py`

```python
from enum import StrEnum

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
)


class OutboundStatus(StrEnum):
    ACTIVE = "ACTIVE"
    CANCELLED = "CANCELLED"


class OutboundCreateRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )

    destination_type: str = Field(
        ...,
        min_length=1,
        max_length=50,
        description="Tipo de destino da saída",
        examples=[
            "WORK_ORDER",
            "SALE",
        ],
    )

    work_order_number: str | None = Field(
        default=None,
        max_length=100,
        description="Número da Ordem de Serviço",
        examples=[
            "OS-12345",
        ],
    )

    sales_invoice_number: str | None = Field(
        default=None,
        max_length=100,
        description="Número da Nota Fiscal de venda",
        examples=[
            "NFV-12345",
        ],
    )

    created_by: int = Field(
        ...,
        gt=0,
        description="Identificador do usuário responsável",
        examples=[
            1,
        ],
    )

    status: OutboundStatus = Field(
        default=OutboundStatus.ACTIVE,
        description="Status inicial da saída",
    )


class OutboundUpdateRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )

    destination_type: str | None = Field(
        default=None,
        min_length=1,
        max_length=50,
        description="Novo tipo de destino da saída",
        examples=[
            "WORK_ORDER",
            "SALE",
        ],
    )

    work_order_number: str | None = Field(
        default=None,
        max_length=100,
        description="Novo número da Ordem de Serviço",
        examples=[
            "OS-67890",
        ],
    )

    sales_invoice_number: str | None = Field(
        default=None,
        max_length=100,
        description="Novo número da Nota Fiscal de venda",
        examples=[
            "NFV-67890",
        ],
    )

    status: OutboundStatus | None = Field(
        default=None,
        description="Novo status da saída",
    )


class OutboundItemCreateRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )

    part_id: int = Field(
        ...,
        gt=0,
        description="Identificador da peça",
        examples=[
            1,
        ],
    )

    quantity: int = Field(
        ...,
        gt=0,
        description="Quantidade retirada",
        examples=[
            5,
        ],
    )


class OutboundResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        extra="forbid",
    )

    id: int
    destination_type: str
    work_order_number: str | None
    sales_invoice_number: str | None
    created_by: int
    created_at: str
    updated_at: str
    status: OutboundStatus


class OutboundItemResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
        extra="forbid",
    )

    id: int
    outbound_id: int
    part_id: int
    quantity: int
    created_at: str
```

## `src\schemas\part_schema.py`

```python
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
)


class PartCreateRequest(BaseModel):
    """Dados necessários para cadastrar uma peça."""

    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True,
    )

    supplier_id: int = Field(
        ...,
        gt=0,
        description="Identificador do fornecedor da peça",
    )

    part_code: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Código original da peça",
        examples=["07C911023H"],
    )

    name: str = Field(
        ...,
        min_length=1,
        max_length=200,
        description="Nome da peça",
        examples=["Motor de partida"],
    )

    description: str | None = Field(
        default=None,
        max_length=1000,
        description="Descrição complementar da peça",
    )

    return_deadline_days: int = Field(
        ...,
        gt=0,
        le=3650,
        description=(
            "Prazo padrão, em dias, para devolução "
            "do casco"
        ),
        examples=[90],
    )


class PartUpdateRequest(BaseModel):
    """Campos permitidos na atualização de uma peça."""

    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True,
    )

    supplier_id: int | None = Field(
        default=None,
        gt=0,
        description="Identificador do fornecedor da peça",
    )

    part_code: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="Código original da peça",
    )

    name: str | None = Field(
        default=None,
        min_length=1,
        max_length=200,
        description="Nome da peça",
    )

    description: str | None = Field(
        default=None,
        max_length=1000,
        description="Descrição complementar da peça",
    )

    return_deadline_days: int | None = Field(
        default=None,
        gt=0,
        le=3650,
        description=(
            "Prazo padrão, em dias, para devolução "
            "do casco"
        ),
    )


class PartResponse(BaseModel):
    """Representação pública de uma peça."""

    model_config = ConfigDict(
        from_attributes=True,
    )

    id: int
    supplier_id: int
    part_code: str
    name: str
    description: str | None
    return_deadline_days: int
    is_active: bool
    created_at: str
    updated_at: str
```

## `src\schemas\purchase_schema.py`

```python
from typing import Literal

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
)


PurchaseStatus = Literal[
    "PENDING",
    "RECEIVED",
    "CANCELLED",
]


class PurchaseCreateRequest(BaseModel):
    """
    Dados necessários para cadastrar uma compra.
    """

    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True,
    )

    supplier_id: int = Field(
        ...,
        gt=0,
        description="Identificador do fornecedor",
    )

    invoice_number: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Número da nota fiscal",
        examples=["NF-12345"],
    )

    invoice_series: str | None = Field(
        default=None,
        max_length=50,
        description="Série da nota fiscal",
        examples=["1"],
    )

    issue_date: str = Field(
        ...,
        min_length=1,
        max_length=30,
        description="Data de emissão da nota fiscal",
        examples=["2026-07-29"],
    )

    created_by: int = Field(
        ...,
        gt=0,
        description=(
            "Identificador do usuário que cadastrou "
            "a compra"
        ),
    )

    status: PurchaseStatus = Field(
        default="PENDING",
        description="Status inicial da compra",
    )

    notes: str | None = Field(
        default=None,
        max_length=1000,
        description="Observações complementares",
    )


class PurchaseUpdateRequest(BaseModel):
    """
    Campos permitidos na atualização de uma compra.
    """

    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True,
    )

    supplier_id: int | None = Field(
        default=None,
        gt=0,
        description="Novo identificador do fornecedor",
    )

    invoice_number: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="Novo número da nota fiscal",
    )

    invoice_series: str | None = Field(
        default=None,
        max_length=50,
        description="Nova série da nota fiscal",
    )

    issue_date: str | None = Field(
        default=None,
        min_length=1,
        max_length=30,
        description="Nova data de emissão",
    )

    status: PurchaseStatus | None = Field(
        default=None,
        description="Novo status da compra",
    )

    notes: str | None = Field(
        default=None,
        max_length=1000,
        description="Novas observações da compra",
    )


class PurchaseItemCreateRequest(BaseModel):
    """
    Dados para adicionar uma peça à compra.
    """

    model_config = ConfigDict(
        extra="forbid",
    )

    part_id: int = Field(
        ...,
        gt=0,
        description="Identificador da peça",
    )

    quantity_purchased: int = Field(
        ...,
        gt=0,
        description="Quantidade comprada",
        examples=[10],
    )


class PurchaseResponse(BaseModel):
    """
    Representa uma compra retornada pela API.
    """

    model_config = ConfigDict(
        from_attributes=True,
        frozen=True,
    )

    id: int
    supplier_id: int

    invoice_number: str
    invoice_series: str | None

    issue_date: str
    received_at: str | None

    notes: str | None

    created_by: int
    created_at: str
    updated_at: str

    status: str


class PurchaseItemResponse(BaseModel):
    """
    Representa um item de compra retornado pela API.
    """

    model_config = ConfigDict(
        from_attributes=True,
        frozen=True,
    )

    id: int
    purchase_id: int
    part_id: int

    quantity_purchased: int
    quantity_available: int

    created_at: str
```

## `src\schemas\purchase_tracking_schema.py`

```python
from pydantic import BaseModel, ConfigDict

from src.dtos.purchase_tracking import (
    PurchaseItemTrackingDTO,
    PurchaseTrackingDTO,
)


class PurchaseItemTrackingResponse(BaseModel):
    """Representa um item no acompanhamento de uma compra."""

    model_config = ConfigDict(frozen=True)

    purchase_item_id: int

    part_id: int
    part_code: str
    part_name: str

    quantity_purchased: int
    quantity_available_for_outbound: int
    quantity_outbound: int

    quantity_returned_by_customer: int
    quantity_pending_customer_return: int

    quantity_available_for_supplier_return: int
    quantity_returned_to_supplier: int
    quantity_pending_supplier_return: int

    lifecycle_status: str

    @classmethod
    def from_dto(
        cls,
        dto: PurchaseItemTrackingDTO,
    ) -> "PurchaseItemTrackingResponse":
        """Converte um DTO de item para um schema de resposta."""

        return cls(
            purchase_item_id=dto.purchase_item_id,
            part_id=dto.part_id,
            part_code=dto.part_code,
            part_name=dto.part_name,
            quantity_purchased=dto.quantity_purchased,
            quantity_available_for_outbound=(
                dto.quantity_available_for_outbound
            ),
            quantity_outbound=dto.quantity_outbound,
            quantity_returned_by_customer=(
                dto.quantity_returned_by_customer
            ),
            quantity_pending_customer_return=(
                dto.quantity_pending_customer_return
            ),
            quantity_available_for_supplier_return=(
                dto.quantity_available_for_supplier_return
            ),
            quantity_returned_to_supplier=(
                dto.quantity_returned_to_supplier
            ),
            quantity_pending_supplier_return=(
                dto.quantity_pending_supplier_return
            ),
            lifecycle_status=dto.lifecycle_status,
        )


class PurchaseTrackingResponse(BaseModel):
    """Representa o acompanhamento consolidado de uma compra."""

    model_config = ConfigDict(frozen=True)

    purchase_id: int

    supplier_id: int
    supplier_name: str

    invoice_number: str
    invoice_series: str | None
    issue_date: str
    purchase_status: str

    items: tuple[PurchaseItemTrackingResponse, ...]

    @classmethod
    def from_dto(
        cls,
        dto: PurchaseTrackingDTO,
    ) -> "PurchaseTrackingResponse":
        """Converte o DTO consolidado para uma resposta da API."""

        return cls(
            purchase_id=dto.purchase_id,
            supplier_id=dto.supplier_id,
            supplier_name=dto.supplier_name,
            invoice_number=dto.invoice_number,
            invoice_series=dto.invoice_series,
            issue_date=dto.issue_date,
            purchase_status=dto.purchase_status,
            items=tuple(
                PurchaseItemTrackingResponse.from_dto(item)
                for item in dto.items
            ),
        )
```

## `src\schemas\supplier_contact_schema.py`

```python
from pydantic import BaseModel, ConfigDict, Field


class SupplierContactCreateRequest(BaseModel):
    """Dados necessários para cadastrar um contato."""

    model_config = ConfigDict(
        str_strip_whitespace=True,
        extra="forbid",
    )

    name: str = Field(
        ...,
        min_length=1,
        max_length=200,
        description="Nome do contato",
        examples=["João Silva"],
    )

    email: str | None = Field(
        default=None,
        min_length=3,
        max_length=255,
        pattern=r"^[^@\s]+@[^@\s]+\.[^@\s]+$",
        description="Endereço de e-mail do contato",
        examples=["joao.silva@fornecedor.com.br"],
    )

    phone: str | None = Field(
        default=None,
        min_length=3,
        max_length=50,
        description="Telefone do contato",
        examples=["(11) 99999-1111"],
    )

    position: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="Cargo ou área do contato",
        examples=["Garantia"],
    )

    is_primary: bool = Field(
        default=False,
        description=(
            "Indica se este é o contato principal "
            "do fornecedor"
        ),
    )


class SupplierContactUpdateRequest(BaseModel):
    """Dados que podem ser alterados em um contato."""

    model_config = ConfigDict(
        str_strip_whitespace=True,
        extra="forbid",
    )

    name: str | None = Field(
        default=None,
        min_length=1,
        max_length=200,
        description="Novo nome do contato",
    )

    email: str | None = Field(
        default=None,
        min_length=3,
        max_length=255,
        pattern=r"^[^@\s]+@[^@\s]+\.[^@\s]+$",
        description="Novo endereço de e-mail",
    )

    phone: str | None = Field(
        default=None,
        min_length=3,
        max_length=50,
        description="Novo telefone",
    )

    position: str | None = Field(
        default=None,
        min_length=1,
        max_length=100,
        description="Novo cargo ou área",
    )

    is_primary: bool | None = Field(
        default=None,
        description=(
            "Indica se o contato deve ser considerado "
            "principal"
        ),
    )


class SupplierContactResponse(BaseModel):
    """Representa um contato retornado pela API."""

    model_config = ConfigDict(
        from_attributes=True,
        frozen=True,
    )

    id: int
    supplier_id: int

    name: str
    email: str | None
    phone: str | None
    position: str | None

    is_primary: bool
    is_active: bool

    created_at: str
```

## `src\schemas\supplier_schema.py`

```python
from pydantic import BaseModel, ConfigDict, Field


class SupplierCreateRequest(BaseModel):
    """Dados necessários para cadastrar um fornecedor."""

    model_config = ConfigDict(
        str_strip_whitespace=True,
        extra="forbid",
    )

    name: str = Field(
        ...,
        min_length=1,
        max_length=200,
        description="Nome ou razão social do fornecedor",
        examples=["Distribuidora de Peças Registro Ltda."],
    )

    document: str | None = Field(
        default=None,
        max_length=50,
        description="CPF, CNPJ ou outro documento do fornecedor",
        examples=["12.345.678/0001-90"],
    )

    address: str | None = Field(
        default=None,
        description="Endereço completo do fornecedor",
        examples=[
            "Rua Exemplo, 100 - Centro - Registro/SP"
        ],
    )

    notes: str | None = Field(
        default=None,
        description="Observações sobre o fornecedor",
        examples=[
            "Fornecedor especializado em peças com casco."
        ],
    )


class SupplierUpdateRequest(BaseModel):
    """Dados que podem ser alterados em um fornecedor."""

    model_config = ConfigDict(
        str_strip_whitespace=True,
        extra="forbid",
    )

    name: str | None = Field(
        default=None,
        min_length=1,
        max_length=200,
        description="Novo nome ou razão social",
    )

    document: str | None = Field(
        default=None,
        max_length=50,
        description="Novo documento do fornecedor",
    )

    address: str | None = Field(
        default=None,
        description="Novo endereço do fornecedor",
    )

    notes: str | None = Field(
        default=None,
        description="Novas observações sobre o fornecedor",
    )


class SupplierResponse(BaseModel):
    """Representa um fornecedor retornado pela API."""

    model_config = ConfigDict(
        from_attributes=True,
        frozen=True,
    )

    id: int

    name: str
    document: str | None
    address: str | None
    notes: str | None

    is_active: int

    created_at: str
    updated_at: str
```

## `src\security\__init__.py`

```python

```

## `src\security\password.py`

```python
from pwdlib import PasswordHash


password_hash = PasswordHash.recommended()


def hash_password(password: str) -> str:
    """Gera o hash seguro de uma senha."""
    return password_hash.hash(password)


def verify_password(
    password: str,
    hashed_password: str,
) -> bool:
    """Verifica uma senha contra seu hash."""
    return password_hash.verify(
        password,
        hashed_password,
    )
```

## `src\services\__init__.py`

```python
from src.services.purchase_tracking_service import (
    PurchaseTrackingService,
)

__all__ = [
    "PurchaseTrackingService",
]
```

## `src\services\customer_return_service.py`

```python
from src.models.customer_return import CustomerReturn
from src.models.customer_return_allocation import (
    CustomerReturnAllocation,
)
from src.models.customer_return_item import CustomerReturnItem
from src.repositories.customer_return_allocation_repository import (
    CustomerReturnAllocationRepository,
)
from src.repositories.customer_return_item_repository import (
    CustomerReturnItemRepository,
)
from src.repositories.customer_return_repository import (
    CustomerReturnRepository,
)
from src.repositories.outbound_item_repository import (
    OutboundItemRepository,
)
from src.repositories.part_repository import PartRepository


class CustomerReturnService:
    """Regras de negócio relacionadas a devoluções de clientes."""

    def __init__(
        self,
        customer_return_repository: CustomerReturnRepository,
        customer_return_item_repository: (
            CustomerReturnItemRepository
        ),
        customer_return_allocation_repository: (
            CustomerReturnAllocationRepository
        ),
        outbound_item_repository: OutboundItemRepository,
        part_repository: PartRepository,
    ):
        self.customer_return_repository = (
            customer_return_repository
        )

        self.customer_return_item_repository = (
            customer_return_item_repository
        )

        self.customer_return_allocation_repository = (
            customer_return_allocation_repository
        )

        self.outbound_item_repository = (
            outbound_item_repository
        )

        self.part_repository = part_repository

    def create_customer_return(
        self,
        return_type: str,
        reference_number: str,
        customer_name: str,
        created_by: int,
        status: str = "ACTIVE",
        notes: str | None = None,
    ) -> CustomerReturn:
        if not return_type.strip():
            raise ValueError(
                "O tipo de devolução é obrigatório."
            )

        if not reference_number.strip():
            raise ValueError(
                "O número de referência é obrigatório."
            )

        if not customer_name.strip():
            raise ValueError(
                "O nome do cliente é obrigatório."
            )

        customer_return = CustomerReturn(
            return_type=return_type.strip(),
            reference_number=reference_number.strip(),
            customer_name=customer_name.strip(),
            created_by=created_by,
            status=status,
            notes=notes,
        )

        return self.customer_return_repository.add(
            customer_return
        )

    def add_item(
        self,
        customer_return_id: int,
        part_id: int,
        quantity: int,
    ) -> CustomerReturnItem:
        customer_return = (
            self.customer_return_repository.get_by_id(
                customer_return_id
            )
        )

        if customer_return is None:
            raise ValueError(
                "Devolução do cliente não encontrada."
            )

        part = self.part_repository.get_by_id(
            part_id
        )

        if part is None:
            raise ValueError(
                "Peça não encontrada."
            )

        if quantity <= 0:
            raise ValueError(
                "A quantidade devolvida deve ser maior que zero."
            )

        outbound_items = (
            self.outbound_item_repository.list_by_part(
                part_id
            )
        )

        if not outbound_items:
            raise ValueError(
                "Não existem saídas registradas para esta peça."
            )

        total_outbound_quantity = sum(
            item.quantity
            for item in outbound_items
        )

        total_returned_quantity = 0

        for outbound_item in outbound_items:
            allocations = (
                self.customer_return_allocation_repository
                .list_by_outbound_item(
                    outbound_item.id
                )
            )

            total_returned_quantity += sum(
                allocation.quantity_allocated
                for allocation in allocations
            )

        available_for_return = (
            total_outbound_quantity
            - total_returned_quantity
        )

        if quantity > available_for_return:
            raise ValueError(
                "A quantidade devolvida é maior que a "
                "quantidade disponível para devolução."
            )

        customer_return_item = CustomerReturnItem(
            customer_return_id=customer_return_id,
            part_id=part_id,
            quantity=quantity,
        )

        customer_return_item = (
            self.customer_return_item_repository.add(
                customer_return_item
            )
        )

        remaining_quantity = quantity

        for outbound_item in outbound_items:
            if remaining_quantity <= 0:
                break

            allocations = (
                self.customer_return_allocation_repository
                .list_by_outbound_item(
                    outbound_item.id
                )
            )

            already_returned = sum(
                allocation.quantity_allocated
                for allocation in allocations
            )

            available_from_outbound = (
                outbound_item.quantity
                - already_returned
            )

            if available_from_outbound <= 0:
                continue

            quantity_to_allocate = min(
                available_from_outbound,
                remaining_quantity,
            )

            allocation = CustomerReturnAllocation(
                customer_return_item_id=(
                    customer_return_item.id
                ),
                outbound_item_id=outbound_item.id,
                quantity_allocated=(
                    quantity_to_allocate
                ),
            )

            self.customer_return_allocation_repository.add(
                allocation
            )

            remaining_quantity -= (
                quantity_to_allocate
            )

        if remaining_quantity > 0:
            raise ValueError(
                "Não foi possível alocar toda a quantidade "
                "devolvida às saídas existentes."
            )

        return customer_return_item

    def get_customer_return(
        self,
        customer_return_id: int,
    ) -> CustomerReturn:
        customer_return = (
            self.customer_return_repository.get_by_id(
                customer_return_id
            )
        )

        if customer_return is None:
            raise ValueError(
                "Devolução do cliente não encontrada."
            )

        return customer_return

    def list_customer_returns(
        self,
    ) -> list[CustomerReturn]:
        return self.customer_return_repository.list_all()

    def list_customer_return_items(
        self,
        customer_return_id: int,
    ) -> list[CustomerReturnItem]:
        customer_return = (
            self.customer_return_repository.get_by_id(
                customer_return_id
            )
        )

        if customer_return is None:
            raise ValueError(
                "Devolução do cliente não encontrada."
            )

        return (
            self.customer_return_item_repository
            .list_by_customer_return(
                customer_return_id
            )
        )
```

## `src\services\outbound_service.py`

```python
from src.models.outbound import Outbound
from src.models.outbound_item import OutboundItem
from src.models.outbound_purchase_allocation import (
    OutboundPurchaseAllocation,
)
from src.repositories.outbound_item_repository import (
    OutboundItemRepository,
)
from src.repositories.outbound_purchase_allocation_repository import (
    OutboundPurchaseAllocationRepository,
)
from src.repositories.outbound_repository import (
    OutboundRepository,
)
from src.repositories.part_repository import PartRepository
from src.repositories.purchase_item_repository import (
    PurchaseItemRepository,
)


class OutboundService:
    """Regras de negócio relacionadas às saídas de estoque."""

    ALLOWED_STATUSES = {
        "ACTIVE",
        "CANCELLED",
    }

    def __init__(
        self,
        outbound_repository: OutboundRepository,
        outbound_item_repository: OutboundItemRepository,
        outbound_purchase_allocation_repository: (
            OutboundPurchaseAllocationRepository
        ),
        purchase_item_repository: PurchaseItemRepository,
        part_repository: PartRepository,
    ) -> None:
        self.outbound_repository = outbound_repository

        self.outbound_item_repository = (
            outbound_item_repository
        )

        self.outbound_purchase_allocation_repository = (
            outbound_purchase_allocation_repository
        )

        self.purchase_item_repository = (
            purchase_item_repository
        )

        self.part_repository = part_repository

    def create_outbound(
        self,
        destination_type: str,
        created_by: int,
        work_order_number: str | None = None,
        sales_invoice_number: str | None = None,
        status: str = "ACTIVE",
    ) -> Outbound:
        normalized_destination_type = (
            self._normalize_required_text(
                destination_type,
                "O tipo de destino é obrigatório.",
            )
        )

        normalized_work_order_number = (
            self._normalize_optional_text(
                work_order_number
            )
        )

        normalized_sales_invoice_number = (
            self._normalize_optional_text(
                sales_invoice_number
            )
        )

        normalized_status = self._normalize_status(
            status
        )

        if created_by <= 0:
            raise ValueError(
                "O identificador do usuário deve ser "
                "maior que zero."
            )

        self._validate_reference_numbers(
            work_order_number=(
                normalized_work_order_number
            ),
            sales_invoice_number=(
                normalized_sales_invoice_number
            ),
        )

        if normalized_status == "CANCELLED":
            raise ValueError(
                "Uma saída não pode ser criada "
                "já cancelada."
            )

        self._ensure_work_order_is_unique(
            work_order_number=(
                normalized_work_order_number
            ),
        )

        self._ensure_sales_invoice_is_unique(
            sales_invoice_number=(
                normalized_sales_invoice_number
            ),
        )

        outbound = Outbound(
            destination_type=(
                normalized_destination_type
            ),
            work_order_number=(
                normalized_work_order_number
            ),
            sales_invoice_number=(
                normalized_sales_invoice_number
            ),
            created_by=created_by,
            status=normalized_status,
        )

        return self.outbound_repository.add(
            outbound
        )

    def add_item(
        self,
        outbound_id: int,
        part_id: int,
        quantity: int,
    ) -> OutboundItem:
        if outbound_id <= 0:
            raise ValueError(
                "O identificador da saída deve ser "
                "maior que zero."
            )

        if part_id <= 0:
            raise ValueError(
                "O identificador da peça deve ser "
                "maior que zero."
            )

        if quantity <= 0:
            raise ValueError(
                "A quantidade da saída deve ser "
                "maior que zero."
            )

        outbound = self.get_outbound(
            outbound_id
        )

        if outbound.status == "CANCELLED":
            raise ValueError(
                "Não é possível adicionar itens "
                "a uma saída cancelada."
            )

        part = self.part_repository.get_by_id(
            part_id
        )

        if part is None:
            raise ValueError(
                "Peça não encontrada."
            )

        if not part.is_active:
            raise ValueError(
                "Não é possível realizar a saída "
                "de uma peça inativa."
            )

        existing_items = (
            self.outbound_item_repository
            .list_by_outbound(
                outbound_id
            )
        )

        if any(
            item.part_id == part_id
            for item in existing_items
        ):
            raise ValueError(
                "Esta peça já foi adicionada à saída."
            )

        available_purchase_items = (
            self.purchase_item_repository
            .list_available_by_part(
                part_id
            )
        )

        total_available = sum(
            purchase_item.quantity_available
            for purchase_item
            in available_purchase_items
        )

        if total_available < quantity:
            raise ValueError(
                "Quantidade disponível insuficiente "
                "para a saída."
            )

        outbound_item = OutboundItem(
            outbound_id=outbound_id,
            part_id=part_id,
            quantity=quantity,
        )

        outbound_item = (
            self.outbound_item_repository.add(
                outbound_item
            )
        )

        remaining_quantity = quantity

        for purchase_item in available_purchase_items:
            if remaining_quantity <= 0:
                break

            quantity_to_allocate = min(
                purchase_item.quantity_available,
                remaining_quantity,
            )

            purchase_item.quantity_available -= (
                quantity_to_allocate
            )

            allocation = (
                OutboundPurchaseAllocation(
                    outbound_item_id=(
                        outbound_item.id
                    ),
                    purchase_item_id=(
                        purchase_item.id
                    ),
                    quantity_allocated=(
                        quantity_to_allocate
                    ),
                )
            )

            self.outbound_purchase_allocation_repository.add(
                allocation
            )

            remaining_quantity -= (
                quantity_to_allocate
            )

        if remaining_quantity > 0:
            raise ValueError(
                "Não foi possível alocar toda a "
                "quantidade solicitada."
            )

        return outbound_item

    def get_outbound(
        self,
        outbound_id: int,
    ) -> Outbound:
        if outbound_id <= 0:
            raise ValueError(
                "O identificador da saída deve ser "
                "maior que zero."
            )

        outbound = self.outbound_repository.get_by_id(
            outbound_id
        )

        if outbound is None:
            raise ValueError(
                "Saída não encontrada."
            )

        return outbound

    def list_outbounds(
        self,
        status: str | None = None,
        destination_type: str | None = None,
    ) -> list[Outbound]:
        if (
            status is not None
            and destination_type is not None
        ):
            raise ValueError(
                "Informe apenas um filtro por vez."
            )

        if status is not None:
            normalized_status = self._normalize_status(
                status
            )

            return (
                self.outbound_repository.list_by_status(
                    normalized_status
                )
            )

        if destination_type is not None:
            normalized_destination_type = (
                self._normalize_required_text(
                    destination_type,
                    (
                        "O tipo de destino é "
                        "obrigatório."
                    ),
                )
            )

            return (
                self.outbound_repository
                .list_by_destination_type(
                    normalized_destination_type
                )
            )

        return self.outbound_repository.list_all()

    def list_outbounds_by_status(
        self,
        status: str,
    ) -> list[Outbound]:
        normalized_status = self._normalize_status(
            status
        )

        return self.outbound_repository.list_by_status(
            normalized_status
        )

    def list_outbounds_by_destination_type(
        self,
        destination_type: str,
    ) -> list[Outbound]:
        normalized_destination_type = (
            self._normalize_required_text(
                destination_type,
                "O tipo de destino é obrigatório.",
            )
        )

        return (
            self.outbound_repository
            .list_by_destination_type(
                normalized_destination_type
            )
        )

    def list_outbound_items(
        self,
        outbound_id: int,
    ) -> list[OutboundItem]:
        self.get_outbound(
            outbound_id
        )

        return (
            self.outbound_item_repository
            .list_by_outbound(
                outbound_id
            )
        )

    def update_outbound(
        self,
        outbound_id: int,
        destination_type: str | None = None,
        work_order_number: str | None = None,
        sales_invoice_number: str | None = None,
        status: str | None = None,
    ) -> Outbound:
        outbound = self.get_outbound(
            outbound_id
        )

        if outbound.status == "CANCELLED":
            raise ValueError(
                "Não é possível alterar uma saída "
                "cancelada."
            )

        if destination_type is not None:
            outbound.destination_type = (
                self._normalize_required_text(
                    destination_type,
                    (
                        "O tipo de destino é "
                        "obrigatório."
                    ),
                )
            )

        if work_order_number is not None:
            normalized_work_order_number = (
                self._normalize_optional_text(
                    work_order_number
                )
            )

            self._ensure_work_order_is_unique(
                work_order_number=(
                    normalized_work_order_number
                ),
                ignored_outbound_id=outbound_id,
            )

            outbound.work_order_number = (
                normalized_work_order_number
            )

        if sales_invoice_number is not None:
            normalized_sales_invoice_number = (
                self._normalize_optional_text(
                    sales_invoice_number
                )
            )

            self._ensure_sales_invoice_is_unique(
                sales_invoice_number=(
                    normalized_sales_invoice_number
                ),
                ignored_outbound_id=outbound_id,
            )

            outbound.sales_invoice_number = (
                normalized_sales_invoice_number
            )

        if status is not None:
            normalized_status = self._normalize_status(
                status
            )

            if normalized_status == "CANCELLED":
                raise ValueError(
                    "Utilize a operação específica "
                    "para cancelar a saída."
                )

            outbound.status = normalized_status

        self._validate_reference_numbers(
            work_order_number=(
                outbound.work_order_number
            ),
            sales_invoice_number=(
                outbound.sales_invoice_number
            ),
        )

        return self.outbound_repository.save(
            outbound
        )

    def cancel_outbound(
        self,
        outbound_id: int,
    ) -> Outbound:
        outbound = self.get_outbound(
            outbound_id
        )

        if outbound.status == "CANCELLED":
            raise ValueError(
                "A saída já está cancelada."
            )

        outbound_items = (
            self.outbound_item_repository
            .list_by_outbound(
                outbound_id
            )
        )

        for outbound_item in outbound_items:
            allocations = (
                self
                .outbound_purchase_allocation_repository
                .list_by_outbound_item(
                    outbound_item.id
                )
            )

            for allocation in allocations:
                purchase_item = (
                    self.purchase_item_repository
                    .get_by_id(
                        allocation.purchase_item_id
                    )
                )

                if purchase_item is None:
                    raise ValueError(
                        "Item de compra relacionado "
                        "à saída não encontrado."
                    )

                purchase_item.quantity_available += (
                    allocation.quantity_allocated
                )

        outbound.status = "CANCELLED"

        return self.outbound_repository.save(
            outbound
        )

    def _ensure_work_order_is_unique(
        self,
        work_order_number: str | None,
        ignored_outbound_id: int | None = None,
    ) -> None:
        if work_order_number is None:
            return

        existing_outbound = (
            self.outbound_repository
            .get_by_work_order_number(
                work_order_number
            )
        )

        if (
            existing_outbound is not None
            and existing_outbound.id
            != ignored_outbound_id
        ):
            raise ValueError(
                "Já existe uma saída com esta "
                "ordem de serviço."
            )

    def _ensure_sales_invoice_is_unique(
        self,
        sales_invoice_number: str | None,
        ignored_outbound_id: int | None = None,
    ) -> None:
        if sales_invoice_number is None:
            return

        existing_outbound = (
            self.outbound_repository
            .get_by_sales_invoice_number(
                sales_invoice_number
            )
        )

        if (
            existing_outbound is not None
            and existing_outbound.id
            != ignored_outbound_id
        ):
            raise ValueError(
                "Já existe uma saída com esta "
                "nota fiscal de venda."
            )

    @staticmethod
    def _validate_reference_numbers(
        work_order_number: str | None,
        sales_invoice_number: str | None,
    ) -> None:
        if (
            work_order_number is None
            and sales_invoice_number is None
        ):
            raise ValueError(
                "A saída deve possuir uma ordem de serviço "
                "ou uma nota fiscal de venda."
            )

    @classmethod
    def _normalize_status(
        cls,
        status: str,
    ) -> str:
        normalized_status = (
            cls._normalize_required_text(
                status,
                "O status da saída é obrigatório.",
            )
            .upper()
        )

        if (
            normalized_status
            not in cls.ALLOWED_STATUSES
        ):
            raise ValueError(
                "Status de saída inválido."
            )

        return normalized_status

    @staticmethod
    def _normalize_required_text(
        value: str,
        error_message: str,
    ) -> str:
        normalized_value = value.strip()

        if not normalized_value:
            raise ValueError(
                error_message
            )

        return normalized_value

    @staticmethod
    def _normalize_optional_text(
        value: str | None,
    ) -> str | None:
        if value is None:
            return None

        normalized_value = value.strip()

        if not normalized_value:
            return None

        return normalized_value
```

## `src\services\part_service.py`

```python
from src.models.part import Part
from src.models.supplier import Supplier
from src.repositories.part_repository import PartRepository
from src.repositories.supplier_repository import SupplierRepository


FIELD_NOT_PROVIDED = object()


class PartService:
    """Regras de negócio relacionadas às peças."""

    def __init__(
        self,
        part_repository: PartRepository,
        supplier_repository: SupplierRepository,
    ):
        self.part_repository = part_repository
        self.supplier_repository = supplier_repository

    def get_by_id(
        self,
        part_id: int,
    ) -> Part | None:
        """Busca uma peça pelo identificador."""

        self._validate_positive_id(
            part_id,
            "O identificador da peça deve ser maior que zero.",
        )

        return self.part_repository.get_by_id(
            part_id
        )

    def get_required(
        self,
        part_id: int,
    ) -> Part:
        """Busca uma peça ou informa que ela não existe."""

        part = self.get_by_id(part_id)

        if part is None:
            raise ValueError(
                "Peça não encontrada."
            )

        return part

    def list_all(self) -> list[Part]:
        """Lista todas as peças."""

        return self.part_repository.list_all()

    def list_by_supplier(
        self,
        supplier_id: int,
    ) -> list[Part]:
        """Lista as peças de um fornecedor existente."""

        self._get_required_supplier(
            supplier_id
        )

        return self.part_repository.list_by_supplier(
            supplier_id
        )

    def create(
        self,
        supplier_id: int,
        part_code: str,
        name: str,
        return_deadline_days: int,
        description: str | None = None,
    ) -> Part:
        """Cadastra uma nova peça."""

        supplier = self._get_required_supplier(
            supplier_id
        )

        self._ensure_supplier_is_active(
            supplier
        )

        normalized_part_code = (
            self._normalize_required_text(
                part_code,
                "O código original da peça é obrigatório.",
            )
        )

        normalized_name = (
            self._normalize_required_text(
                name,
                "O nome da peça é obrigatório.",
            )
        )

        normalized_description = (
            self._normalize_optional_text(
                description
            )
        )

        self._validate_return_deadline(
            return_deadline_days
        )

        existing_part = (
            self.part_repository
            .get_by_supplier_and_code(
                supplier_id,
                normalized_part_code,
            )
        )

        if existing_part is not None:
            raise ValueError(
                "Já existe uma peça com este código "
                "para o fornecedor informado."
            )

        part = Part(
            supplier_id=supplier_id,
            part_code=normalized_part_code,
            name=normalized_name,
            description=normalized_description,
            return_deadline_days=return_deadline_days,
            is_active=1,
        )

        return self.part_repository.add(part)

    def update(
        self,
        part_id: int,
        supplier_id: int | object = FIELD_NOT_PROVIDED,
        part_code: str | object = FIELD_NOT_PROVIDED,
        name: str | object = FIELD_NOT_PROVIDED,
        description: str | None | object = FIELD_NOT_PROVIDED,
        return_deadline_days: int | object = FIELD_NOT_PROVIDED,
    ) -> Part:
        """Atualiza parcialmente uma peça."""

        part = self.get_required(part_id)

        new_supplier_id = part.supplier_id
        new_part_code = part.part_code

        if supplier_id is not FIELD_NOT_PROVIDED:
            if not isinstance(supplier_id, int):
                raise ValueError(
                    "O fornecedor da peça é obrigatório."
                )

            supplier = self._get_required_supplier(
                supplier_id
            )

            self._ensure_supplier_is_active(
                supplier
            )

            new_supplier_id = supplier_id

        if part_code is not FIELD_NOT_PROVIDED:
            if not isinstance(part_code, str):
                raise ValueError(
                    "O código original da peça é obrigatório."
                )

            new_part_code = (
                self._normalize_required_text(
                    part_code,
                    "O código original da peça é obrigatório.",
                )
            )

        if (
            new_supplier_id != part.supplier_id
            or new_part_code != part.part_code
        ):
            existing_part = (
                self.part_repository
                .get_by_supplier_and_code(
                    new_supplier_id,
                    new_part_code,
                )
            )

            if (
                existing_part is not None
                and existing_part.id != part.id
            ):
                raise ValueError(
                    "Já existe uma peça com este código "
                    "para o fornecedor informado."
                )

        if name is not FIELD_NOT_PROVIDED:
            if not isinstance(name, str):
                raise ValueError(
                    "O nome da peça é obrigatório."
                )

            part.name = self._normalize_required_text(
                name,
                "O nome da peça é obrigatório.",
            )

        if description is not FIELD_NOT_PROVIDED:
            if description is not None and not isinstance(
                description,
                str,
            ):
                raise ValueError(
                    "A descrição da peça é inválida."
                )

            part.description = (
                self._normalize_optional_text(
                    description
                )
            )

        if (
            return_deadline_days
            is not FIELD_NOT_PROVIDED
        ):
            if not isinstance(
                return_deadline_days,
                int,
            ):
                raise ValueError(
                    "O prazo de devolução deve ser "
                    "informado em dias."
                )

            self._validate_return_deadline(
                return_deadline_days
            )

            part.return_deadline_days = (
                return_deadline_days
            )

        part.supplier_id = new_supplier_id
        part.part_code = new_part_code

        return self.part_repository.save(part)

    def activate(
        self,
        part_id: int,
    ) -> Part:
        """Ativa uma peça inativa."""

        part = self.get_required(part_id)

        if part.is_active:
            raise ValueError(
                "A peça já está ativa."
            )

        supplier = self._get_required_supplier(
            part.supplier_id
        )

        self._ensure_supplier_is_active(
            supplier
        )

        part.is_active = 1

        return self.part_repository.save(part)

    def deactivate(
        self,
        part_id: int,
    ) -> Part:
        """Desativa uma peça ativa."""

        part = self.get_required(part_id)

        if not part.is_active:
            raise ValueError(
                "A peça já está inativa."
            )

        part.is_active = 0

        return self.part_repository.save(part)

    def _get_required_supplier(
        self,
        supplier_id: int,
    ) -> Supplier:
        """Busca um fornecedor obrigatório."""

        self._validate_positive_id(
            supplier_id,
            (
                "O identificador do fornecedor "
                "deve ser maior que zero."
            ),
        )

        supplier = (
            self.supplier_repository.get_by_id(
                supplier_id
            )
        )

        if supplier is None:
            raise ValueError(
                "Fornecedor não encontrado."
            )

        return supplier

    @staticmethod
    def _ensure_supplier_is_active(
        supplier: Supplier,
    ) -> None:
        """Impede uso de fornecedor inativo."""

        if not supplier.is_active:
            raise ValueError(
                "O fornecedor informado está inativo."
            )

    @staticmethod
    def _validate_positive_id(
        value: int,
        message: str,
    ) -> None:
        """Valida identificadores positivos."""

        if not isinstance(value, int) or value <= 0:
            raise ValueError(message)

    @staticmethod
    def _validate_return_deadline(
        return_deadline_days: int,
    ) -> None:
        """Valida o prazo padrão da peça."""

        if (
            not isinstance(
                return_deadline_days,
                int,
            )
            or isinstance(
                return_deadline_days,
                bool,
            )
        ):
            raise ValueError(
                "O prazo de devolução deve ser "
                "informado em dias."
            )

        if return_deadline_days <= 0:
            raise ValueError(
                "O prazo de devolução deve ser "
                "maior que zero."
            )

        if return_deadline_days > 3650:
            raise ValueError(
                "O prazo de devolução não pode "
                "ser maior que 3650 dias."
            )

    @staticmethod
    def _normalize_required_text(
        value: str,
        empty_message: str,
    ) -> str:
        """Normaliza um texto obrigatório."""

        normalized_value = value.strip()

        if not normalized_value:
            raise ValueError(empty_message)

        return normalized_value

    @staticmethod
    def _normalize_optional_text(
        value: str | None,
    ) -> str | None:
        """Normaliza um texto opcional."""

        if value is None:
            return None

        normalized_value = value.strip()

        return normalized_value or None
```

## `src\services\purchase_service.py`

```python
from typing import Final

from src.models.purchase import Purchase
from src.models.purchase_item import PurchaseItem
from src.repositories.part_repository import PartRepository
from src.repositories.purchase_item_repository import (
    PurchaseItemRepository,
)
from src.repositories.purchase_repository import (
    PurchaseRepository,
)
from src.repositories.supplier_repository import (
    SupplierRepository,
)


FIELD_NOT_PROVIDED: Final = object()


class PurchaseService:
    """
    Regras de negócio relacionadas às compras.
    """

    ALLOWED_STATUSES: Final[set[str]] = {
        "PENDING",
        "RECEIVED",
        "CANCELLED",
    }

    def __init__(
        self,
        purchase_repository: PurchaseRepository,
        purchase_item_repository: PurchaseItemRepository,
        supplier_repository: SupplierRepository,
        part_repository: PartRepository,
    ) -> None:
        self.purchase_repository = purchase_repository
        self.purchase_item_repository = (
            purchase_item_repository
        )
        self.supplier_repository = supplier_repository
        self.part_repository = part_repository

    def create_purchase(
        self,
        supplier_id: int,
        invoice_number: str,
        invoice_series: str | None,
        issue_date: str,
        created_by: int,
        status: str,
        notes: str | None = None,
    ) -> Purchase:
        """
        Cria uma nova compra.
        """

        supplier = self.supplier_repository.get_by_id(
            supplier_id
        )

        if supplier is None:
            raise ValueError(
                "Fornecedor não encontrado."
            )

        if not supplier.is_active:
            raise ValueError(
                "O fornecedor informado está inativo."
            )

        normalized_invoice_number = (
            self._normalize_required_text(
                invoice_number,
                "O número da nota fiscal é obrigatório.",
            )
        )

        normalized_invoice_series = (
            self._normalize_optional_text(
                invoice_series
            )
        )

        normalized_issue_date = (
            self._normalize_required_text(
                issue_date,
                "A data de emissão é obrigatória.",
            )
        )

        normalized_status = self._normalize_status(
            status
        )

        normalized_notes = self._normalize_optional_text(
            notes
        )

        existing_purchase = (
            self.purchase_repository.get_by_invoice(
                supplier_id=supplier_id,
                invoice_number=normalized_invoice_number,
                invoice_series=normalized_invoice_series,
            )
        )

        if existing_purchase is not None:
            raise ValueError(
                "Já existe uma compra com esta nota fiscal, "
                "série e fornecedor."
            )

        purchase = Purchase(
            supplier_id=supplier_id,
            invoice_number=normalized_invoice_number,
            invoice_series=normalized_invoice_series,
            issue_date=normalized_issue_date,
            created_by=created_by,
            status=normalized_status,
            notes=normalized_notes,
        )

        return self.purchase_repository.add(
            purchase
        )

    def add_item(
        self,
        purchase_id: int,
        part_id: int,
        quantity_purchased: int,
    ) -> PurchaseItem:
        """
        Adiciona um item a uma compra.
        """

        purchase = self.get_purchase(
            purchase_id
        )

        if purchase.status == "CANCELLED":
            raise ValueError(
                "Não é possível adicionar itens "
                "a uma compra cancelada."
            )

        part = self.part_repository.get_by_id(
            part_id
        )

        if part is None:
            raise ValueError(
                "Peça não encontrada."
            )

        if not part.is_active:
            raise ValueError(
                "A peça informada está inativa."
            )

        if part.supplier_id != purchase.supplier_id:
            raise ValueError(
                "A peça informada não pertence "
                "ao fornecedor da compra."
            )

        if quantity_purchased <= 0:
            raise ValueError(
                "A quantidade comprada deve ser "
                "maior que zero."
            )

        purchase_items = (
            self.purchase_item_repository.list_by_purchase(
                purchase_id
            )
        )

        item_already_exists = any(
            item.part_id == part_id
            for item in purchase_items
        )

        if item_already_exists:
            raise ValueError(
                "Esta peça já foi adicionada à compra."
            )

        purchase_item = PurchaseItem(
            purchase_id=purchase_id,
            part_id=part_id,
            quantity_purchased=quantity_purchased,
            quantity_available=quantity_purchased,
        )

        return self.purchase_item_repository.add(
            purchase_item
        )

    def get_purchase(
        self,
        purchase_id: int,
    ) -> Purchase:
        """
        Retorna uma compra obrigatoriamente existente.
        """

        purchase = self.purchase_repository.get_by_id(
            purchase_id
        )

        if purchase is None:
            raise ValueError(
                "Compra não encontrada."
            )

        return purchase

    def list_purchases(
        self,
    ) -> list[Purchase]:
        """
        Lista todas as compras.
        """

        return self.purchase_repository.list_all()

    def list_purchases_by_supplier(
        self,
        supplier_id: int,
    ) -> list[Purchase]:
        """
        Lista as compras de determinado fornecedor.
        """

        supplier = self.supplier_repository.get_by_id(
            supplier_id
        )

        if supplier is None:
            raise ValueError(
                "Fornecedor não encontrado."
            )

        return self.purchase_repository.list_by_supplier(
            supplier_id
        )

    def list_purchase_items(
        self,
        purchase_id: int,
    ) -> list[PurchaseItem]:
        """
        Lista os itens de uma compra.
        """

        self.get_purchase(
            purchase_id
        )

        return (
            self.purchase_item_repository.list_by_purchase(
                purchase_id
            )
        )

    def update_purchase(
        self,
        purchase_id: int,
        *,
        supplier_id: int | object = FIELD_NOT_PROVIDED,
        invoice_number: str | object = FIELD_NOT_PROVIDED,
        invoice_series: (
            str | None | object
        ) = FIELD_NOT_PROVIDED,
        issue_date: str | object = FIELD_NOT_PROVIDED,
        status: str | object = FIELD_NOT_PROVIDED,
        notes: (
            str | None | object
        ) = FIELD_NOT_PROVIDED,
    ) -> Purchase:
        """
        Atualiza parcialmente uma compra.
        """

        purchase = self.get_purchase(
            purchase_id
        )

        if purchase.status == "CANCELLED":
            raise ValueError(
                "Uma compra cancelada não pode ser alterada."
            )

        new_supplier_id = purchase.supplier_id
        new_invoice_number = purchase.invoice_number
        new_invoice_series = purchase.invoice_series

        if supplier_id is not FIELD_NOT_PROVIDED:
            if not isinstance(supplier_id, int):
                raise ValueError(
                    "Fornecedor inválido."
                )

            supplier = self.supplier_repository.get_by_id(
                supplier_id
            )

            if supplier is None:
                raise ValueError(
                    "Fornecedor não encontrado."
                )

            if not supplier.is_active:
                raise ValueError(
                    "O fornecedor informado está inativo."
                )

            purchase_items = (
                self.purchase_item_repository.list_by_purchase(
                    purchase_id
                )
            )

            incompatible_item = any(
                self._part_belongs_to_another_supplier(
                    item.part_id,
                    supplier_id,
                )
                for item in purchase_items
            )

            if incompatible_item:
                raise ValueError(
                    "Não é possível alterar o fornecedor "
                    "porque existem peças incompatíveis "
                    "na compra."
                )

            new_supplier_id = supplier_id

        if invoice_number is not FIELD_NOT_PROVIDED:
            if not isinstance(invoice_number, str):
                raise ValueError(
                    "Número da nota fiscal inválido."
                )

            new_invoice_number = (
                self._normalize_required_text(
                    invoice_number,
                    "O número da nota fiscal é obrigatório.",
                )
            )

        if invoice_series is not FIELD_NOT_PROVIDED:
            if (
                invoice_series is not None
                and not isinstance(invoice_series, str)
            ):
                raise ValueError(
                    "Série da nota fiscal inválida."
                )

            new_invoice_series = (
                self._normalize_optional_text(
                    invoice_series
                )
            )

        invoice_data_changed = any(
            (
                new_supplier_id != purchase.supplier_id,
                new_invoice_number
                != purchase.invoice_number,
                new_invoice_series
                != purchase.invoice_series,
            )
        )

        if invoice_data_changed:
            existing_purchase = (
                self.purchase_repository.get_by_invoice(
                    supplier_id=new_supplier_id,
                    invoice_number=new_invoice_number,
                    invoice_series=new_invoice_series,
                )
            )

            if (
                existing_purchase is not None
                and existing_purchase.id != purchase.id
            ):
                raise ValueError(
                    "Já existe uma compra com esta nota "
                    "fiscal, série e fornecedor."
                )

        purchase.supplier_id = new_supplier_id
        purchase.invoice_number = new_invoice_number
        purchase.invoice_series = new_invoice_series

        if issue_date is not FIELD_NOT_PROVIDED:
            if not isinstance(issue_date, str):
                raise ValueError(
                    "Data de emissão inválida."
                )

            purchase.issue_date = (
                self._normalize_required_text(
                    issue_date,
                    "A data de emissão é obrigatória.",
                )
            )

        if status is not FIELD_NOT_PROVIDED:
            if not isinstance(status, str):
                raise ValueError(
                    "Status da compra inválido."
                )

            normalized_status = self._normalize_status(
                status
            )

            if normalized_status == "CANCELLED":
                raise ValueError(
                    "Utilize a operação específica "
                    "para cancelar a compra."
                )

            purchase.status = normalized_status

        if notes is not FIELD_NOT_PROVIDED:
            if (
                notes is not None
                and not isinstance(notes, str)
            ):
                raise ValueError(
                    "Observações inválidas."
                )

            purchase.notes = self._normalize_optional_text(
                notes
            )

        return self.purchase_repository.save(
            purchase
        )

    def cancel_purchase(
        self,
        purchase_id: int,
    ) -> Purchase:
        """
        Cancela uma compra sem apagar seu histórico.
        """

        purchase = self.get_purchase(
            purchase_id
        )

        if purchase.status == "CANCELLED":
            raise ValueError(
                "A compra já está cancelada."
            )

        purchase_items = (
            self.purchase_item_repository.list_by_purchase(
                purchase_id
            )
        )

        has_movement = any(
            item.quantity_available
            != item.quantity_purchased
            for item in purchase_items
        )

        if has_movement:
            raise ValueError(
                "Não é possível cancelar uma compra "
                "que já possui movimentações."
            )

        purchase.status = "CANCELLED"

        return self.purchase_repository.save(
            purchase
        )

    def _part_belongs_to_another_supplier(
        self,
        part_id: int,
        supplier_id: int,
    ) -> bool:
        """
        Verifica a compatibilidade entre peça e fornecedor.
        """

        part = self.part_repository.get_by_id(
            part_id
        )

        return (
            part is None
            or part.supplier_id != supplier_id
        )

    @classmethod
    def _normalize_status(
        cls,
        value: str,
    ) -> str:
        """
        Normaliza e valida o status da compra.
        """

        normalized_value = (
            cls._normalize_required_text(
                value,
                "O status da compra é obrigatório.",
            ).upper()
        )

        if normalized_value not in cls.ALLOWED_STATUSES:
            allowed_values = ", ".join(
                sorted(cls.ALLOWED_STATUSES)
            )

            raise ValueError(
                "Status da compra inválido. "
                f"Valores permitidos: {allowed_values}."
            )

        return normalized_value

    @staticmethod
    def _normalize_required_text(
        value: str,
        empty_message: str,
    ) -> str:
        """
        Normaliza um texto obrigatório.
        """

        normalized_value = value.strip()

        if not normalized_value:
            raise ValueError(
                empty_message
            )

        return normalized_value

    @staticmethod
    def _normalize_optional_text(
        value: str | None,
    ) -> str | None:
        """
        Normaliza um texto opcional.
        """

        if value is None:
            return None

        normalized_value = value.strip()

        return normalized_value or None
```

## `src\services\purchase_tracking_service.py`

```python
from src.dtos.purchase_tracking import PurchaseTrackingDTO
from src.queries.purchase_tracking_query import PurchaseTrackingQuery


class PurchaseTrackingService:
    """Ponto de entrada para o acompanhamento consolidado de compras."""

    def __init__(self, query: PurchaseTrackingQuery):
        self.query = query

    def get_purchase_tracking(
        self,
        purchase_id: int,
    ) -> PurchaseTrackingDTO:
        """Retorna o acompanhamento consolidado de uma compra."""

        if purchase_id <= 0:
            raise ValueError(
                "O identificador da compra deve ser maior que zero."
            )

        tracking = self.query.get_by_purchase_id(purchase_id)

        if tracking is None:
            raise ValueError("Compra não encontrada.")

        return tracking
```

## `src\services\role_service.py`

```python
from src.models.role import Role
from src.repositories.role_repository import RoleRepository


class RoleService:
    """Regras de negócio relacionadas a perfis de acesso."""

    def __init__(self, repository: RoleRepository):
        self.repository = repository

    def get_by_id(self, role_id: int) -> Role | None:
        return self.repository.get_by_id(role_id)

    def list_all(self) -> list[Role]:
        return self.repository.list_all()

    def create(
        self,
        name: str,
        description: str | None = None,
    ) -> Role:
        normalized_name = name.strip()

        if not normalized_name:
            raise ValueError(
                "O nome do perfil é obrigatório."
            )

        existing_role = self.repository.get_by_name(
            normalized_name
        )

        if existing_role is not None:
            raise ValueError(
                "Já existe um perfil com este nome."
            )

        role = Role(
            name=normalized_name,
            description=description,
        )

        return self.repository.add(role)
```

## `src\services\supplier_contact_service.py`

```python
from typing import Final

from src.models.supplier_contact import SupplierContact
from src.repositories.supplier_contact_repository import (
    SupplierContactRepository,
)
from src.repositories.supplier_repository import (
    SupplierRepository,
)


FIELD_NOT_PROVIDED: Final = object()


class SupplierContactService:
    """Regras de negócio dos contatos de fornecedores."""

    def __init__(
        self,
        repository: SupplierContactRepository,
        supplier_repository: SupplierRepository,
    ):
        self.repository = repository
        self.supplier_repository = supplier_repository

    def get_by_id(
        self,
        contact_id: int,
    ) -> SupplierContact | None:
        """Busca um contato pelo identificador."""

        return self.repository.get_by_id(contact_id)

    def get_required(
        self,
        supplier_id: int,
        contact_id: int,
    ) -> SupplierContact:
        """
        Busca obrigatoriamente um contato pertencente
        ao fornecedor informado.
        """

        self._validate_supplier_exists(supplier_id)

        contact = self.repository.get_by_id(contact_id)

        if contact is None:
            raise ValueError(
                "Contato não encontrado."
            )

        if contact.supplier_id != supplier_id:
            raise ValueError(
                "O contato não pertence ao fornecedor informado."
            )

        return contact

    def list_by_supplier(
        self,
        supplier_id: int,
    ) -> list[SupplierContact]:
        """Lista os contatos do fornecedor informado."""

        self._validate_supplier_exists(supplier_id)

        return self.repository.list_by_supplier(
            supplier_id
        )

    def create(
        self,
        supplier_id: int,
        name: str,
        email: str | None = None,
        phone: str | None = None,
        position: str | None = None,
        is_primary: bool = False,
    ) -> SupplierContact:
        """Cadastra um contato para um fornecedor."""

        self._validate_supplier_exists(supplier_id)

        normalized_name = self._normalize_required_text(
            value=name,
            field_name="nome do contato",
        )

        normalized_email = self._normalize_email(email)
        normalized_phone = self._normalize_optional_text(
            phone
        )
        normalized_position = self._normalize_optional_text(
            position
        )

        if is_primary:
            self._remove_current_primary(supplier_id)

        contact = SupplierContact(
            supplier_id=supplier_id,
            name=normalized_name,
            email=normalized_email,
            phone=normalized_phone,
            position=normalized_position,
            is_primary=int(is_primary),
            is_active=1,
        )

        return self.repository.add(contact)

    def update(
        self,
        supplier_id: int,
        contact_id: int,
        *,
        name: str | object = FIELD_NOT_PROVIDED,
        email: str | None | object = FIELD_NOT_PROVIDED,
        phone: str | None | object = FIELD_NOT_PROVIDED,
        position: str | None | object = FIELD_NOT_PROVIDED,
        is_primary: bool | object = FIELD_NOT_PROVIDED,
    ) -> SupplierContact:
        """Atualiza somente os campos enviados."""

        contact = self.get_required(
            supplier_id=supplier_id,
            contact_id=contact_id,
        )

        if name is not FIELD_NOT_PROVIDED:
            if not isinstance(name, str):
                raise ValueError(
                    "O nome do contato é obrigatório."
                )

            contact.name = self._normalize_required_text(
                value=name,
                field_name="nome do contato",
            )

        if email is not FIELD_NOT_PROVIDED:
            if email is not None and not isinstance(
                email,
                str,
            ):
                raise ValueError(
                    "O e-mail do contato é inválido."
                )

            contact.email = self._normalize_email(email)

        if phone is not FIELD_NOT_PROVIDED:
            if phone is not None and not isinstance(
                phone,
                str,
            ):
                raise ValueError(
                    "O telefone do contato é inválido."
                )

            contact.phone = self._normalize_optional_text(
                phone
            )

        if position is not FIELD_NOT_PROVIDED:
            if position is not None and not isinstance(
                position,
                str,
            ):
                raise ValueError(
                    "O cargo do contato é inválido."
                )

            contact.position = (
                self._normalize_optional_text(position)
            )

        if is_primary is not FIELD_NOT_PROVIDED:
            if not isinstance(is_primary, bool):
                raise ValueError(
                    "A indicação de contato principal é inválida."
                )

            if is_primary:
                self._remove_current_primary(
                    supplier_id=supplier_id,
                    ignored_contact_id=contact.id,
                )

            contact.is_primary = int(is_primary)

        return self.repository.save(contact)

    def activate(
        self,
        supplier_id: int,
        contact_id: int,
    ) -> SupplierContact:
        """Ativa um contato inativo."""

        contact = self.get_required(
            supplier_id=supplier_id,
            contact_id=contact_id,
        )

        if contact.is_active:
            raise ValueError(
                "O contato já está ativo."
            )

        contact.is_active = 1

        return self.repository.save(contact)

    def deactivate(
        self,
        supplier_id: int,
        contact_id: int,
    ) -> SupplierContact:
        """Desativa um contato ativo."""

        contact = self.get_required(
            supplier_id=supplier_id,
            contact_id=contact_id,
        )

        if not contact.is_active:
            raise ValueError(
                "O contato já está inativo."
            )

        contact.is_active = 0
        contact.is_primary = 0

        return self.repository.save(contact)

    def _validate_supplier_exists(
        self,
        supplier_id: int,
    ) -> None:
        """Valida se o fornecedor existe."""

        supplier = self.supplier_repository.get_by_id(
            supplier_id
        )

        if supplier is None:
            raise ValueError(
                "Fornecedor não encontrado."
            )

    def _remove_current_primary(
        self,
        supplier_id: int,
        ignored_contact_id: int | None = None,
    ) -> None:
        """
        Remove a definição de principal do contato atual.

        O contato ignorado não é alterado durante atualizações.
        """

        current_primary = (
            self.repository.get_primary_by_supplier(
                supplier_id
            )
        )

        if current_primary is None:
            return

        if current_primary.id == ignored_contact_id:
            return

        current_primary.is_primary = 0

        self.repository.save(current_primary)

    @staticmethod
    def _normalize_required_text(
        value: str,
        field_name: str,
    ) -> str:
        """Normaliza e valida textos obrigatórios."""

        normalized_value = value.strip()

        if not normalized_value:
            raise ValueError(
                f"O {field_name} é obrigatório."
            )

        return normalized_value

    @staticmethod
    def _normalize_optional_text(
        value: str | None,
    ) -> str | None:
        """Normaliza campos opcionais."""

        if value is None:
            return None

        normalized_value = value.strip()

        if not normalized_value:
            return None

        return normalized_value

    @classmethod
    def _normalize_email(
        cls,
        email: str | None,
    ) -> str | None:
        """Normaliza o endereço de e-mail."""

        normalized_email = cls._normalize_optional_text(
            email
        )

        if normalized_email is None:
            return None

        return normalized_email.lower()
```

## `src\services\supplier_return_service.py`

```python
from src.models.supplier_return import SupplierReturn
from src.models.supplier_return_item import SupplierReturnItem
from src.repositories.customer_return_allocation_repository import (
    CustomerReturnAllocationRepository,
)
from src.repositories.outbound_purchase_allocation_repository import (
    OutboundPurchaseAllocationRepository,
)
from src.repositories.purchase_item_repository import (
    PurchaseItemRepository,
)
from src.repositories.purchase_repository import (
    PurchaseRepository,
)
from src.repositories.supplier_repository import (
    SupplierRepository,
)
from src.repositories.supplier_return_item_repository import (
    SupplierReturnItemRepository,
)
from src.repositories.supplier_return_repository import (
    SupplierReturnRepository,
)


class SupplierReturnService:
    """Regras de negócio das remessas de cascos aos fornecedores."""

    def __init__(
        self,
        supplier_return_repository: SupplierReturnRepository,
        supplier_return_item_repository: (
            SupplierReturnItemRepository
        ),
        supplier_repository: SupplierRepository,
        purchase_repository: PurchaseRepository,
        purchase_item_repository: PurchaseItemRepository,
        outbound_purchase_allocation_repository: (
            OutboundPurchaseAllocationRepository
        ),
        customer_return_allocation_repository: (
            CustomerReturnAllocationRepository
        ),
    ):
        self.supplier_return_repository = (
            supplier_return_repository
        )

        self.supplier_return_item_repository = (
            supplier_return_item_repository
        )

        self.supplier_repository = supplier_repository
        self.purchase_repository = purchase_repository

        self.purchase_item_repository = (
            purchase_item_repository
        )

        self.outbound_purchase_allocation_repository = (
            outbound_purchase_allocation_repository
        )

        self.customer_return_allocation_repository = (
            customer_return_allocation_repository
        )

    def create_supplier_return(
        self,
        supplier_id: int,
        dispatch_invoice_number: str,
        dispatch_invoice_series: str | None,
        issue_date: str,
        created_by: int,
        status: str = "ACTIVE",
        notes: str | None = None,
    ) -> SupplierReturn:
        supplier = self.supplier_repository.get_by_id(
            supplier_id
        )

        if supplier is None:
            raise ValueError(
                "Fornecedor não encontrado."
            )

        normalized_invoice_number = (
            dispatch_invoice_number.strip()
        )

        if not normalized_invoice_number:
            raise ValueError(
                "O número da Nota Fiscal de Simples "
                "Remessa é obrigatório."
            )

        if not issue_date.strip():
            raise ValueError(
                "A data da remessa é obrigatória."
            )

        existing_supplier_return = (
            self.supplier_return_repository
            .get_by_dispatch_invoice_number(
                normalized_invoice_number
            )
        )

        if existing_supplier_return is not None:
            raise ValueError(
                "Já existe uma remessa cadastrada com "
                "este número de Nota Fiscal."
            )

        normalized_series = None

        if dispatch_invoice_series is not None:
            normalized_series = (
                dispatch_invoice_series.strip() or None
            )

        supplier_return = SupplierReturn(
            supplier_id=supplier_id,
            dispatch_invoice_number=(
                normalized_invoice_number
            ),
            dispatch_invoice_series=normalized_series,
            issue_date=issue_date.strip(),
            created_by=created_by,
            status=status.strip() or "ACTIVE",
            notes=notes,
        )

        return self.supplier_return_repository.add(
            supplier_return
        )

    def add_item(
        self,
        supplier_return_id: int,
        purchase_item_id: int,
        quantity: int,
    ) -> SupplierReturnItem:
        supplier_return = (
            self.supplier_return_repository.get_by_id(
                supplier_return_id
            )
        )

        if supplier_return is None:
            raise ValueError(
                "Remessa ao fornecedor não encontrada."
            )

        purchase_item = (
            self.purchase_item_repository.get_by_id(
                purchase_item_id
            )
        )

        if purchase_item is None:
            raise ValueError(
                "Item de compra não encontrado."
            )

        existing_item = (
            self.supplier_return_item_repository
            .get_by_supplier_return_and_purchase_item(
                supplier_return_id=supplier_return_id,
                purchase_item_id=purchase_item_id,
            )
        )

        if existing_item is not None:
            raise ValueError(
                "Este item de compra já foi adicionado "
                "à remessa."
            )

        purchase = self.purchase_repository.get_by_id(
            purchase_item.purchase_id
        )

        if purchase is None:
            raise ValueError(
                "Compra de origem não encontrada."
            )

        if purchase.supplier_id != supplier_return.supplier_id:
            raise ValueError(
                "O item de compra não pertence ao fornecedor "
                "da remessa."
            )

        if quantity <= 0:
            raise ValueError(
                "A quantidade remetida deve ser maior que zero."
            )

        self._validate_same_purchase(
            supplier_return_id=supplier_return_id,
            purchase_id=purchase.id,
        )

        available_quantity = (
            self.get_available_quantity(
                purchase_item_id
            )
        )

        if quantity > available_quantity:
            raise ValueError(
                "A quantidade remetida é maior que a "
                "quantidade disponível para remessa. "
                f"Quantidade máxima permitida: "
                f"{available_quantity}."
            )

        supplier_return_item = SupplierReturnItem(
            supplier_return_id=supplier_return_id,
            purchase_item_id=purchase_item_id,
            quantity=quantity,
        )

        return self.supplier_return_item_repository.add(
            supplier_return_item
        )

    def get_available_quantity(
        self,
        purchase_item_id: int,
    ) -> int:
        purchase_item = (
            self.purchase_item_repository.get_by_id(
                purchase_item_id
            )
        )

        if purchase_item is None:
            raise ValueError(
                "Item de compra não encontrado."
            )

        received_quantity = (
            self._get_customer_returned_quantity(
                purchase_item_id
            )
        )

        already_dispatched_quantity = (
            self.supplier_return_item_repository
            .get_returned_quantity_by_purchase_item(
                purchase_item_id
            )
        )

        available_quantity = (
            received_quantity
            - already_dispatched_quantity
        )

        return max(available_quantity, 0)

    def get_supplier_return(
        self,
        supplier_return_id: int,
    ) -> SupplierReturn:
        supplier_return = (
            self.supplier_return_repository.get_by_id(
                supplier_return_id
            )
        )

        if supplier_return is None:
            raise ValueError(
                "Remessa ao fornecedor não encontrada."
            )

        return supplier_return

    def list_supplier_returns(
        self,
    ) -> list[SupplierReturn]:
        return self.supplier_return_repository.list_all()

    def list_items(
        self,
        supplier_return_id: int,
    ) -> list[SupplierReturnItem]:
        self.get_supplier_return(
            supplier_return_id
        )

        return (
            self.supplier_return_item_repository
            .list_by_supplier_return(
                supplier_return_id
            )
        )

    def _get_customer_returned_quantity(
        self,
        purchase_item_id: int,
    ) -> int:
        """
        Calcula quantos cascos já retornaram dos clientes
        para uma origem específica de compra.

        A devolução do cliente está ligada ao OutboundItem.
        Portanto, a quantidade devolvida é redistribuída
        sobre as origens FIFO daquele OutboundItem.
        """

        target_allocations = (
            self.outbound_purchase_allocation_repository
            .list_by_purchase_item(
                purchase_item_id
            )
        )

        total_returned_for_purchase_item = 0

        for target_allocation in target_allocations:
            outbound_item_id = (
                target_allocation.outbound_item_id
            )

            outbound_allocations = (
                self.outbound_purchase_allocation_repository
                .list_by_outbound_item(
                    outbound_item_id
                )
            )

            customer_return_allocations = (
                self.customer_return_allocation_repository
                .list_by_outbound_item(
                    outbound_item_id
                )
            )

            remaining_returned_quantity = sum(
                allocation.quantity_allocated
                for allocation
                in customer_return_allocations
            )

            for outbound_allocation in outbound_allocations:
                if remaining_returned_quantity <= 0:
                    break

                quantity_returned_for_allocation = min(
                    remaining_returned_quantity,
                    outbound_allocation.quantity_allocated,
                )

                if (
                    outbound_allocation.id
                    == target_allocation.id
                ):
                    total_returned_for_purchase_item += (
                        quantity_returned_for_allocation
                    )

                remaining_returned_quantity -= (
                    quantity_returned_for_allocation
                )

        return total_returned_for_purchase_item

    def _validate_same_purchase(
        self,
        supplier_return_id: int,
        purchase_id: int,
    ) -> None:
        existing_items = (
            self.supplier_return_item_repository
            .list_by_supplier_return(
                supplier_return_id
            )
        )

        for existing_item in existing_items:
            existing_purchase_item = (
                self.purchase_item_repository.get_by_id(
                    existing_item.purchase_item_id
                )
            )

            if existing_purchase_item is None:
                raise ValueError(
                    "Um item existente da remessa possui "
                    "origem de compra inválida."
                )

            if existing_purchase_item.purchase_id != purchase_id:
                raise ValueError(
                    "Todos os itens de uma remessa devem "
                    "pertencer à mesma Nota Fiscal de compra."
                )
```

## `src\services\supplier_service.py`

```python
from typing import Final

from src.models.supplier import Supplier
from src.repositories.supplier_repository import SupplierRepository


FIELD_NOT_PROVIDED: Final = object()


class SupplierService:
    """Regras de negócio relacionadas a fornecedores."""

    def __init__(
        self,
        repository: SupplierRepository,
    ):
        self.repository = repository

    def get_by_id(
        self,
        supplier_id: int,
    ) -> Supplier | None:
        """
        Busca um fornecedor pelo identificador.

        Retorna None quando o fornecedor não existe.
        """

        return self.repository.get_by_id(supplier_id)

    def get_required(
        self,
        supplier_id: int,
    ) -> Supplier:
        """
        Busca um fornecedor pelo identificador.

        Lança ValueError quando o fornecedor não existe.
        """

        supplier = self.repository.get_by_id(supplier_id)

        if supplier is None:
            raise ValueError(
                "Fornecedor não encontrado."
            )

        return supplier

    def list_all(self) -> list[Supplier]:
        """Lista todos os fornecedores."""

        return self.repository.list_all()

    def create(
        self,
        name: str,
        document: str | None = None,
        address: str | None = None,
        notes: str | None = None,
    ) -> Supplier:
        """Cadastra um novo fornecedor."""

        normalized_name = self._normalize_required_text(
            value=name,
            field_name="nome do fornecedor",
        )

        normalized_document = self._normalize_optional_text(
            document
        )
        normalized_address = self._normalize_optional_text(
            address
        )
        normalized_notes = self._normalize_optional_text(
            notes
        )

        self._validate_document_is_available(
            document=normalized_document,
        )

        supplier = Supplier(
            name=normalized_name,
            document=normalized_document,
            address=normalized_address,
            notes=normalized_notes,
            is_active=1,
        )

        return self.repository.add(supplier)

    def update(
        self,
        supplier_id: int,
        *,
        name: str | object = FIELD_NOT_PROVIDED,
        document: str | None | object = FIELD_NOT_PROVIDED,
        address: str | None | object = FIELD_NOT_PROVIDED,
        notes: str | None | object = FIELD_NOT_PROVIDED,
    ) -> Supplier:
        """
        Atualiza somente os campos que foram informados.

        O objeto FIELD_NOT_PROVIDED diferencia um campo ausente
        de um campo enviado explicitamente como None.
        """

        supplier = self.get_required(supplier_id)

        if name is not FIELD_NOT_PROVIDED:
            if not isinstance(name, str):
                raise ValueError(
                    "O nome do fornecedor é obrigatório."
                )

            supplier.name = self._normalize_required_text(
                value=name,
                field_name="nome do fornecedor",
            )

        if document is not FIELD_NOT_PROVIDED:
            if document is not None and not isinstance(
                document,
                str,
            ):
                raise ValueError(
                    "O documento do fornecedor é inválido."
                )

            normalized_document = (
                self._normalize_optional_text(document)
            )

            self._validate_document_is_available(
                document=normalized_document,
                current_supplier_id=supplier.id,
            )

            supplier.document = normalized_document

        if address is not FIELD_NOT_PROVIDED:
            if address is not None and not isinstance(
                address,
                str,
            ):
                raise ValueError(
                    "O endereço do fornecedor é inválido."
                )

            supplier.address = self._normalize_optional_text(
                address
            )

        if notes is not FIELD_NOT_PROVIDED:
            if notes is not None and not isinstance(
                notes,
                str,
            ):
                raise ValueError(
                    "As observações do fornecedor são inválidas."
                )

            supplier.notes = self._normalize_optional_text(
                notes
            )

        return self.repository.save(supplier)

    def deactivate(
        self,
        supplier_id: int,
    ) -> Supplier:
        """Desativa um fornecedor ativo."""

        supplier = self.get_required(supplier_id)

        if not supplier.is_active:
            raise ValueError(
                "O fornecedor já está inativo."
            )

        supplier.is_active = 0

        return self.repository.save(supplier)

    def activate(
        self,
        supplier_id: int,
    ) -> Supplier:
        """Ativa um fornecedor inativo."""

        supplier = self.get_required(supplier_id)

        if supplier.is_active:
            raise ValueError(
                "O fornecedor já está ativo."
            )

        supplier.is_active = 1

        return self.repository.save(supplier)

    def _validate_document_is_available(
        self,
        document: str | None,
        current_supplier_id: int | None = None,
    ) -> None:
        """
        Verifica se o documento pode ser utilizado.

        O próprio fornecedor é ignorado durante uma atualização.
        """

        if document is None:
            return

        existing_supplier = self.repository.get_by_document(
            document
        )

        if existing_supplier is None:
            return

        if existing_supplier.id == current_supplier_id:
            return

        raise ValueError(
            "Já existe um fornecedor com este documento."
        )

    @staticmethod
    def _normalize_required_text(
        value: str,
        field_name: str,
    ) -> str:
        """Remove espaços e valida textos obrigatórios."""

        normalized_value = value.strip()

        if not normalized_value:
            raise ValueError(
                f"O {field_name} é obrigatório."
            )

        return normalized_value

    @staticmethod
    def _normalize_optional_text(
        value: str | None,
    ) -> str | None:
        """
        Remove espaços de campos opcionais.

        Textos vazios são convertidos para None.
        """

        if value is None:
            return None

        normalized_value = value.strip()

        if not normalized_value:
            return None

        return normalized_value
```

## `src\services\transfer_service.py`

```python
from src.models.transfer import Transfer
from src.models.transfer_item import TransferItem

from src.repositories.transfer_repository import (
    TransferRepository,
)
from src.repositories.transfer_item_repository import (
    TransferItemRepository,
)
from src.repositories.part_repository import (
    PartRepository,
)
from src.repositories.purchase_item_repository import (
    PurchaseItemRepository,
)


class TransferService:
    """Regras de negócio relacionadas às transferências."""

    def __init__(
        self,
        transfer_repository: TransferRepository,
        transfer_item_repository: TransferItemRepository,
        part_repository: PartRepository,
        purchase_item_repository: PurchaseItemRepository,
    ):
        self.transfer_repository = (
            transfer_repository
        )

        self.transfer_item_repository = (
            transfer_item_repository
        )

        self.part_repository = (
            part_repository
        )

        self.purchase_item_repository = (
            purchase_item_repository
        )
```

## `src\services\user_service.py`

```python
from src.models.user import User
from src.repositories.user_repository import UserRepository
from src.security.password import hash_password


class UserService:
    """Regras de negócio relacionadas a usuários."""

    def __init__(
        self,
        repository: UserRepository,
    ):
        self.repository = repository

    def get_by_id(
        self,
        user_id: int,
    ) -> User | None:
        return self.repository.get_by_id(user_id)

    def get_by_username(
        self,
        username: str,
    ) -> User | None:
        normalized_username = username.strip()

        if not normalized_username:
            return None

        return self.repository.get_by_username(
            normalized_username
        )

    def get_by_email(
        self,
        email: str,
    ) -> User | None:
        normalized_email = email.strip().lower()

        if not normalized_email:
            return None

        return self.repository.get_by_email(
            normalized_email
        )

    def list_all(self) -> list[User]:
        return self.repository.list_all()

    def create(
        self,
        full_name: str,
        username: str,
        email: str,
        password: str,
        role_id: int,
    ) -> User:
        normalized_full_name = full_name.strip()
        normalized_username = username.strip()
        normalized_email = email.strip().lower()

        if not normalized_full_name:
            raise ValueError(
                "O nome completo é obrigatório."
            )

        if not normalized_username:
            raise ValueError(
                "O username é obrigatório."
            )

        if not normalized_email:
            raise ValueError(
                "O e-mail é obrigatório."
            )

        if not password:
            raise ValueError(
                "A senha é obrigatória."
            )

        if len(password) < 8:
            raise ValueError(
                "A senha deve possuir pelo menos 8 caracteres."
            )

        existing_username = (
            self.repository.get_by_username(
                normalized_username
            )
        )

        if existing_username is not None:
            raise ValueError(
                "Já existe um usuário com este username."
            )

        existing_email = (
            self.repository.get_by_email(
                normalized_email
            )
        )

        if existing_email is not None:
            raise ValueError(
                "Já existe um usuário com este e-mail."
            )

        user = User(
            full_name=normalized_full_name,
            username=normalized_username,
            email=normalized_email,
            password_hash=hash_password(password),
            role_id=role_id,
            is_active=1,
        )

        def deactivate(
            self,
            user_id: int,
        ) -> User:
            user = self.repository.get_by_id(user_id)

            if user is None:
                raise ValueError(
                    "Usuário não encontrado."
                )

            if not user.is_active:
                raise ValueError(
                    "O usuário já está inativo."
                )

            user.is_active = 0

            return self.repository.save(user)

        def activate(
            self,
            user_id: int,
        ) -> User:
            user = self.repository.get_by_id(user_id)

            if user is None:
                raise ValueError(
                    "Usuário não encontrado."
                )

            if user.is_active:
                raise ValueError(
                    "O usuário já está ativo."
                )

            user.is_active = 1

            return self.repository.save(user)

        return self.repository.add(user)
```

## `tests\api\__init__.py`

```python

```

## `tests\api\test_outbound_route.py`

```python
from collections.abc import Generator
from unittest.mock import Mock

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from src.api.routes.outbound_route import (
    get_outbound_service,
    router,
)
from src.database.connection import (
    get_session,
)
from src.models.outbound import Outbound
from src.services.outbound_service import (
    OutboundService,
)
from src.models.outbound_item import OutboundItem


def create_outbound(
    outbound_id: int = 10,
    destination_type: str = "WORK_ORDER",
    work_order_number: str | None = "OS-12345",
    sales_invoice_number: str | None = None,
    created_by: int = 1,
    created_at: str = "2026-07-29T10:00:00",
    updated_at: str = "2026-07-29T10:00:00",
    status: str = "ACTIVE",
) -> Outbound:
    outbound = Outbound(
        destination_type=destination_type,
        work_order_number=work_order_number,
        sales_invoice_number=sales_invoice_number,
        created_by=created_by,
        status=status,
    )

    outbound.id = outbound_id
    outbound.created_at = created_at
    outbound.updated_at = updated_at

    return outbound


@pytest.fixture
def session() -> Mock:
    return Mock(
        spec=Session,
    )


@pytest.fixture
def service() -> Mock:
    return Mock(
        spec=OutboundService,
    )


@pytest.fixture
def app(
    session: Mock,
    service: Mock,
) -> Generator[FastAPI, None, None]:
    application = FastAPI()

    application.include_router(
        router
    )

    application.dependency_overrides[
        get_session
    ] = lambda: session

    application.dependency_overrides[
        get_outbound_service
    ] = lambda: service

    yield application

    application.dependency_overrides.clear()


@pytest.fixture
def client(
    app: FastAPI,
) -> Generator[TestClient, None, None]:
    with TestClient(app) as test_client:
        yield test_client


def test_should_create_outbound(
    client: TestClient,
    service: Mock,
    session: Mock,
) -> None:
    outbound = create_outbound()

    service.create_outbound.return_value = (
        outbound
    )

    response = client.post(
        "/outbounds",
        json={
            "destination_type": "WORK_ORDER",
            "work_order_number": "OS-12345",
            "sales_invoice_number": None,
            "created_by": 1,
            "status": "ACTIVE",
        },
    )

    assert response.status_code == 201

    assert response.json() == {
        "id": 10,
        "destination_type": "WORK_ORDER",
        "work_order_number": "OS-12345",
        "sales_invoice_number": None,
        "created_by": 1,
        "created_at": "2026-07-29T10:00:00",
        "updated_at": "2026-07-29T10:00:00",
        "status": "ACTIVE",
    }

    service.create_outbound.assert_called_once_with(
        destination_type="WORK_ORDER",
        work_order_number="OS-12345",
        sales_invoice_number=None,
        created_by=1,
        status="ACTIVE",
    )

    session.commit.assert_called_once_with()

    session.refresh.assert_called_once_with(
        outbound
    )

    session.rollback.assert_not_called()


def test_should_create_outbound_with_sales_invoice(
    client: TestClient,
    service: Mock,
    session: Mock,
) -> None:
    outbound = create_outbound(
        destination_type="SALE",
        work_order_number=None,
        sales_invoice_number="NFV-12345",
    )

    service.create_outbound.return_value = (
        outbound
    )

    response = client.post(
        "/outbounds",
        json={
            "destination_type": "SALE",
            "sales_invoice_number": "NFV-12345",
            "created_by": 1,
        },
    )

    assert response.status_code == 201

    assert response.json()[
        "destination_type"
    ] == "SALE"

    assert response.json()[
        "work_order_number"
    ] is None

    assert response.json()[
        "sales_invoice_number"
    ] == "NFV-12345"

    service.create_outbound.assert_called_once_with(
        destination_type="SALE",
        work_order_number=None,
        sales_invoice_number="NFV-12345",
        created_by=1,
        status="ACTIVE",
    )

    session.commit.assert_called_once_with()

    session.refresh.assert_called_once_with(
        outbound
    )


def test_should_use_active_status_by_default_on_create(
    client: TestClient,
    service: Mock,
) -> None:
    service.create_outbound.return_value = (
        create_outbound()
    )

    response = client.post(
        "/outbounds",
        json={
            "destination_type": "WORK_ORDER",
            "work_order_number": "OS-12345",
            "created_by": 1,
        },
    )

    assert response.status_code == 201

    service.create_outbound.assert_called_once_with(
        destination_type="WORK_ORDER",
        work_order_number="OS-12345",
        sales_invoice_number=None,
        created_by=1,
        status="ACTIVE",
    )


def test_should_return_400_when_reference_numbers_are_missing(
    client: TestClient,
    service: Mock,
    session: Mock,
) -> None:
    service.create_outbound.side_effect = (
        ValueError(
            (
                "A saída deve possuir uma ordem de serviço "
                "ou uma nota fiscal de venda."
            )
        )
    )

    response = client.post(
        "/outbounds",
        json={
            "destination_type": "WORK_ORDER",
            "created_by": 1,
        },
    )

    assert response.status_code == 400

    assert response.json() == {
        "detail": (
            "A saída deve possuir uma ordem de serviço "
            "ou uma nota fiscal de venda."
        )
    }

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()

    session.refresh.assert_not_called()


def test_should_return_400_when_work_order_is_duplicated(
    client: TestClient,
    service: Mock,
    session: Mock,
) -> None:
    service.create_outbound.side_effect = (
        ValueError(
            (
                "Já existe uma saída com esta "
                "ordem de serviço."
            )
        )
    )

    response = client.post(
        "/outbounds",
        json={
            "destination_type": "WORK_ORDER",
            "work_order_number": "OS-12345",
            "created_by": 1,
        },
    )

    assert response.status_code == 400

    assert response.json() == {
        "detail": (
            "Já existe uma saída com esta "
            "ordem de serviço."
        )
    }

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()


def test_should_return_400_when_sales_invoice_is_duplicated(
    client: TestClient,
    service: Mock,
    session: Mock,
) -> None:
    service.create_outbound.side_effect = (
        ValueError(
            (
                "Já existe uma saída com esta "
                "nota fiscal de venda."
            )
        )
    )

    response = client.post(
        "/outbounds",
        json={
            "destination_type": "SALE",
            "sales_invoice_number": "NFV-12345",
            "created_by": 1,
        },
    )

    assert response.status_code == 400

    assert response.json() == {
        "detail": (
            "Já existe uma saída com esta "
            "nota fiscal de venda."
        )
    }

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()


@pytest.mark.parametrize(
    (
        "payload",
        "field",
    ),
    [
        (
            {
                "destination_type": "",
                "work_order_number": "OS-12345",
                "created_by": 1,
            },
            "destination_type",
        ),
        (
            {
                "destination_type": "WORK_ORDER",
                "work_order_number": "OS-12345",
                "created_by": 0,
            },
            "created_by",
        ),
        (
            {
                "destination_type": "WORK_ORDER",
                "work_order_number": "OS-12345",
                "created_by": -1,
            },
            "created_by",
        ),
        (
            {
                "destination_type": "WORK_ORDER",
                "work_order_number": "OS-12345",
                "created_by": 1,
                "status": "PENDING",
            },
            "status",
        ),
    ],
)
def test_should_return_422_when_create_payload_is_invalid(
    client: TestClient,
    service: Mock,
    payload: dict[str, object],
    field: str,
) -> None:
    response = client.post(
        "/outbounds",
        json=payload,
    )

    assert response.status_code == 422

    assert any(
        error["loc"][-1] == field
        for error in response.json()["detail"]
    )

    service.create_outbound.assert_not_called()


def test_should_return_422_when_create_payload_has_extra_field(
    client: TestClient,
    service: Mock,
) -> None:
    response = client.post(
        "/outbounds",
        json={
            "destination_type": "WORK_ORDER",
            "work_order_number": "OS-12345",
            "created_by": 1,
            "unexpected_field": "valor",
        },
    )

    assert response.status_code == 422

    assert any(
        error["loc"][-1]
        == "unexpected_field"
        for error in response.json()["detail"]
    )

    service.create_outbound.assert_not_called()


def test_should_rollback_when_unexpected_error_occurs_on_create(
    client: TestClient,
    service: Mock,
    session: Mock,
) -> None:
    service.create_outbound.side_effect = (
        RuntimeError(
            "Erro inesperado."
        )
    )

    with pytest.raises(
        RuntimeError,
        match="Erro inesperado.",
    ):
        client.post(
            "/outbounds",
            json={
                "destination_type": "WORK_ORDER",
                "work_order_number": "OS-12345",
                "created_by": 1,
            },
        )

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()

    session.refresh.assert_not_called()


def test_should_list_all_outbounds(
    client: TestClient,
    service: Mock,
) -> None:
    service.list_outbounds.return_value = [
        create_outbound(
            outbound_id=10,
        ),
        create_outbound(
            outbound_id=11,
            destination_type="SALE",
            work_order_number=None,
            sales_invoice_number="NFV-12345",
        ),
    ]

    response = client.get(
        "/outbounds"
    )

    assert response.status_code == 200

    assert len(response.json()) == 2

    assert response.json()[0]["id"] == 10

    assert response.json()[1]["id"] == 11

    assert response.json()[1][
        "destination_type"
    ] == "SALE"

    service.list_outbounds.assert_called_once_with(
        status=None,
        destination_type=None,
    )


def test_should_return_empty_outbound_list(
    client: TestClient,
    service: Mock,
) -> None:
    service.list_outbounds.return_value = []

    response = client.get(
        "/outbounds"
    )

    assert response.status_code == 200

    assert response.json() == []

    service.list_outbounds.assert_called_once_with(
        status=None,
        destination_type=None,
    )


def test_should_list_outbounds_filtered_by_status(
    client: TestClient,
    service: Mock,
) -> None:
    service.list_outbounds.return_value = [
        create_outbound(
            status="CANCELLED",
        )
    ]

    response = client.get(
        "/outbounds",
        params={
            "status": "CANCELLED",
        },
    )

    assert response.status_code == 200

    assert response.json()[0][
        "status"
    ] == "CANCELLED"

    service.list_outbounds.assert_called_once_with(
        status="CANCELLED",
        destination_type=None,
    )


def test_should_list_outbounds_filtered_by_destination_type(
    client: TestClient,
    service: Mock,
) -> None:
    service.list_outbounds.return_value = [
        create_outbound(
            destination_type="SALE",
            work_order_number=None,
            sales_invoice_number="NFV-12345",
        )
    ]

    response = client.get(
        "/outbounds",
        params={
            "destination_type": "SALE",
        },
    )

    assert response.status_code == 200

    assert response.json()[0][
        "destination_type"
    ] == "SALE"

    service.list_outbounds.assert_called_once_with(
        status=None,
        destination_type="SALE",
    )


def test_should_return_400_when_multiple_filters_are_sent(
    client: TestClient,
    service: Mock,
) -> None:
    service.list_outbounds.side_effect = (
        ValueError(
            "Informe apenas um filtro por vez."
        )
    )

    response = client.get(
        "/outbounds",
        params={
            "status": "ACTIVE",
            "destination_type": "WORK_ORDER",
        },
    )

    assert response.status_code == 400

    assert response.json() == {
        "detail": (
            "Informe apenas um filtro por vez."
        )
    }

    service.list_outbounds.assert_called_once_with(
        status="ACTIVE",
        destination_type="WORK_ORDER",
    )


def test_should_return_422_when_status_filter_is_invalid(
    client: TestClient,
    service: Mock,
) -> None:
    response = client.get(
        "/outbounds",
        params={
            "status": "PENDING",
        },
    )

    assert response.status_code == 422

    assert any(
        error["loc"][-1] == "status"
        for error in response.json()["detail"]
    )

    service.list_outbounds.assert_not_called()


def test_should_return_422_when_destination_type_filter_is_blank(
    client: TestClient,
    service: Mock,
) -> None:
    response = client.get(
        "/outbounds",
        params={
            "destination_type": "",
        },
    )

    assert response.status_code == 422

    assert any(
        error["loc"][-1]
        == "destination_type"
        for error in response.json()["detail"]
    )

    service.list_outbounds.assert_not_called()


def test_should_get_outbound(
    client: TestClient,
    service: Mock,
) -> None:
    service.get_outbound.return_value = (
        create_outbound()
    )

    response = client.get(
        "/outbounds/10"
    )

    assert response.status_code == 200

    assert response.json() == {
        "id": 10,
        "destination_type": "WORK_ORDER",
        "work_order_number": "OS-12345",
        "sales_invoice_number": None,
        "created_by": 1,
        "created_at": "2026-07-29T10:00:00",
        "updated_at": "2026-07-29T10:00:00",
        "status": "ACTIVE",
    }

    service.get_outbound.assert_called_once_with(
        10
    )


def test_should_return_404_when_outbound_is_not_found(
    client: TestClient,
    service: Mock,
) -> None:
    service.get_outbound.side_effect = (
        ValueError(
            "Saída não encontrada."
        )
    )

    response = client.get(
        "/outbounds/999"
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Saída não encontrada."
    }

    service.get_outbound.assert_called_once_with(
        999
    )


@pytest.mark.parametrize(
    "outbound_id",
    [
        0,
        -1,
    ],
)
def test_should_return_422_when_outbound_id_is_invalid_on_get(
    client: TestClient,
    service: Mock,
    outbound_id: int,
) -> None:
    response = client.get(
        f"/outbounds/{outbound_id}"
    )

    assert response.status_code == 422

    service.get_outbound.assert_not_called()

def test_should_update_outbound(
    client: TestClient,
    service: Mock,
    session: Mock,
) -> None:
    outbound = create_outbound(
        destination_type="SALE",
        work_order_number=None,
        sales_invoice_number="NFV-67890",
    )

    service.update_outbound.return_value = outbound

    response = client.patch(
        "/outbounds/10",
        json={
            "destination_type": "SALE",
            "sales_invoice_number": "NFV-67890",
        },
    )

    assert response.status_code == 200

    assert response.json()["destination_type"] == "SALE"
    assert response.json()["sales_invoice_number"] == "NFV-67890"

    service.update_outbound.assert_called_once_with(
        outbound_id=10,
        destination_type="SALE",
        sales_invoice_number="NFV-67890",
    )

    session.commit.assert_called_once_with()
    session.refresh.assert_called_once_with(outbound)
    session.rollback.assert_not_called()


def test_should_update_only_status(
    client: TestClient,
    service: Mock,
) -> None:
    outbound = create_outbound(
        status="ACTIVE",
    )

    service.update_outbound.return_value = outbound

    response = client.patch(
        "/outbounds/10",
        json={
            "status": "ACTIVE",
        },
    )

    assert response.status_code == 200

    service.update_outbound.assert_called_once_with(
        outbound_id=10,
        status="ACTIVE",
    )


def test_should_send_only_modified_fields(
    client: TestClient,
    service: Mock,
) -> None:
    outbound = create_outbound(
        destination_type="INTERNAL_USE",
    )

    service.update_outbound.return_value = outbound

    response = client.patch(
        "/outbounds/10",
        json={
            "destination_type": "INTERNAL_USE",
        },
    )

    assert response.status_code == 200

    service.update_outbound.assert_called_once_with(
        outbound_id=10,
        destination_type="INTERNAL_USE",
    )


def test_should_return_404_when_update_outbound_is_not_found(
    client: TestClient,
    service: Mock,
    session: Mock,
) -> None:
    service.update_outbound.side_effect = ValueError(
        "Saída não encontrada."
    )

    response = client.patch(
        "/outbounds/999",
        json={
            "destination_type": "SALE",
        },
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Saída não encontrada."
    }

    session.rollback.assert_called_once_with()
    session.commit.assert_not_called()


def test_should_return_400_when_update_business_rule_fails(
    client: TestClient,
    service: Mock,
    session: Mock,
) -> None:
    service.update_outbound.side_effect = ValueError(
        "Já existe uma saída com esta ordem de serviço."
    )

    response = client.patch(
        "/outbounds/10",
        json={
            "work_order_number": "OS-12345",
        },
    )

    assert response.status_code == 400

    assert response.json() == {
        "detail": "Já existe uma saída com esta ordem de serviço."
    }

    session.rollback.assert_called_once_with()
    session.commit.assert_not_called()


def test_should_return_422_when_update_payload_is_invalid(
    client: TestClient,
    service: Mock,
) -> None:
    response = client.patch(
        "/outbounds/10",
        json={
            "status": "PENDING",
        },
    )

    assert response.status_code == 422

    service.update_outbound.assert_not_called()


def test_should_return_422_when_update_has_extra_field(
    client: TestClient,
    service: Mock,
) -> None:
    response = client.patch(
        "/outbounds/10",
        json={
            "destination_type": "SALE",
            "unexpected": True,
        },
    )

    assert response.status_code == 422

    service.update_outbound.assert_not_called()


@pytest.mark.parametrize(
    "outbound_id",
    [
        0,
        -1,
    ],
)
def test_should_return_422_when_update_id_is_invalid(
    client: TestClient,
    service: Mock,
    outbound_id: int,
) -> None:
    response = client.patch(
        f"/outbounds/{outbound_id}",
        json={
            "destination_type": "SALE",
        },
    )

    assert response.status_code == 422

    service.update_outbound.assert_not_called()


def test_should_rollback_when_unexpected_error_occurs_on_update(
    client: TestClient,
    service: Mock,
    session: Mock,
) -> None:
    service.update_outbound.side_effect = RuntimeError(
        "Erro inesperado."
    )

    with pytest.raises(
        RuntimeError,
        match="Erro inesperado.",
    ):
        client.patch(
            "/outbounds/10",
            json={
                "destination_type": "SALE",
            },
        )

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()

    session.refresh.assert_not_called()

def create_outbound_item(
    outbound_item_id: int = 50,
    outbound_id: int = 10,
    part_id: int = 40,
    quantity: int = 5,
    created_at: str = "2026-07-29T10:05:00",
) -> OutboundItem:
    outbound_item = OutboundItem(
        outbound_id=outbound_id,
        part_id=part_id,
        quantity=quantity,
    )

    outbound_item.id = outbound_item_id
    outbound_item.created_at = created_at

    return outbound_item


def test_should_cancel_outbound(
    client: TestClient,
    service: Mock,
    session: Mock,
) -> None:
    outbound = create_outbound(
        status="CANCELLED",
    )

    service.cancel_outbound.return_value = (
        outbound
    )

    response = client.patch(
        "/outbounds/10/cancel"
    )

    assert response.status_code == 200

    assert response.json() == {
        "id": 10,
        "destination_type": "WORK_ORDER",
        "work_order_number": "OS-12345",
        "sales_invoice_number": None,
        "created_by": 1,
        "created_at": "2026-07-29T10:00:00",
        "updated_at": "2026-07-29T10:00:00",
        "status": "CANCELLED",
    }

    service.cancel_outbound.assert_called_once_with(
        10
    )

    session.commit.assert_called_once_with()

    session.refresh.assert_called_once_with(
        outbound
    )

    session.rollback.assert_not_called()


def test_should_return_404_when_cancel_outbound_is_not_found(
    client: TestClient,
    service: Mock,
    session: Mock,
) -> None:
    service.cancel_outbound.side_effect = (
        ValueError(
            "Saída não encontrada."
        )
    )

    response = client.patch(
        "/outbounds/999/cancel"
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Saída não encontrada."
    }

    service.cancel_outbound.assert_called_once_with(
        999
    )

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()

    session.refresh.assert_not_called()


def test_should_return_400_when_outbound_is_already_cancelled(
    client: TestClient,
    service: Mock,
    session: Mock,
) -> None:
    service.cancel_outbound.side_effect = (
        ValueError(
            "A saída já está cancelada."
        )
    )

    response = client.patch(
        "/outbounds/10/cancel"
    )

    assert response.status_code == 400

    assert response.json() == {
        "detail": "A saída já está cancelada."
    }

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()


def test_should_return_404_when_purchase_item_is_not_found_on_cancel(
    client: TestClient,
    service: Mock,
    session: Mock,
) -> None:
    message = (
        "Item de compra relacionado "
        "à saída não encontrado."
    )

    service.cancel_outbound.side_effect = (
        ValueError(message)
    )

    response = client.patch(
        "/outbounds/10/cancel"
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": message
    }

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()


@pytest.mark.parametrize(
    "outbound_id",
    [
        0,
        -1,
    ],
)
def test_should_return_422_when_cancel_id_is_invalid(
    client: TestClient,
    service: Mock,
    outbound_id: int,
) -> None:
    response = client.patch(
        f"/outbounds/{outbound_id}/cancel"
    )

    assert response.status_code == 422

    service.cancel_outbound.assert_not_called()


def test_should_rollback_when_unexpected_error_occurs_on_cancel(
    client: TestClient,
    service: Mock,
    session: Mock,
) -> None:
    service.cancel_outbound.side_effect = (
        RuntimeError(
            "Erro inesperado."
        )
    )

    with pytest.raises(
        RuntimeError,
        match="Erro inesperado.",
    ):
        client.patch(
            "/outbounds/10/cancel"
        )

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()

    session.refresh.assert_not_called()


def test_should_add_outbound_item(
    client: TestClient,
    service: Mock,
    session: Mock,
) -> None:
    outbound_item = create_outbound_item()

    service.add_item.return_value = (
        outbound_item
    )

    response = client.post(
        "/outbounds/10/items",
        json={
            "part_id": 40,
            "quantity": 5,
        },
    )

    assert response.status_code == 201

    assert response.json() == {
        "id": 50,
        "outbound_id": 10,
        "part_id": 40,
        "quantity": 5,
        "created_at": "2026-07-29T10:05:00",
    }

    service.add_item.assert_called_once_with(
        outbound_id=10,
        part_id=40,
        quantity=5,
    )

    session.commit.assert_called_once_with()

    session.refresh.assert_called_once_with(
        outbound_item
    )

    session.rollback.assert_not_called()


def test_should_return_404_when_outbound_is_not_found_on_add_item(
    client: TestClient,
    service: Mock,
    session: Mock,
) -> None:
    service.add_item.side_effect = (
        ValueError(
            "Saída não encontrada."
        )
    )

    response = client.post(
        "/outbounds/999/items",
        json={
            "part_id": 40,
            "quantity": 5,
        },
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Saída não encontrada."
    }

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()

    session.refresh.assert_not_called()


def test_should_return_404_when_part_is_not_found_on_add_item(
    client: TestClient,
    service: Mock,
    session: Mock,
) -> None:
    service.add_item.side_effect = (
        ValueError(
            "Peça não encontrada."
        )
    )

    response = client.post(
        "/outbounds/10/items",
        json={
            "part_id": 999,
            "quantity": 5,
        },
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Peça não encontrada."
    }

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()


@pytest.mark.parametrize(
    "message",
    [
        (
            "Não é possível adicionar itens "
            "a uma saída cancelada."
        ),
        "A peça informada está inativa.",
        (
            "A peça informada já foi adicionada "
            "a esta saída."
        ),
        "Estoque insuficiente para a peça informada.",
        "Não há estoque disponível para a peça informada.",
        (
            "Não foi possível completar a alocação "
            "da quantidade solicitada."
        ),
    ],
)
def test_should_return_400_when_add_item_business_rule_fails(
    client: TestClient,
    service: Mock,
    session: Mock,
    message: str,
) -> None:
    service.add_item.side_effect = (
        ValueError(message)
    )

    response = client.post(
        "/outbounds/10/items",
        json={
            "part_id": 40,
            "quantity": 5,
        },
    )

    assert response.status_code == 400

    assert response.json() == {
        "detail": message
    }

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()

    session.refresh.assert_not_called()


@pytest.mark.parametrize(
    (
        "payload",
        "field",
    ),
    [
        (
            {
                "part_id": 0,
                "quantity": 5,
            },
            "part_id",
        ),
        (
            {
                "part_id": -1,
                "quantity": 5,
            },
            "part_id",
        ),
        (
            {
                "part_id": 40,
                "quantity": 0,
            },
            "quantity",
        ),
        (
            {
                "part_id": 40,
                "quantity": -1,
            },
            "quantity",
        ),
    ],
)
def test_should_return_422_when_add_item_payload_is_invalid(
    client: TestClient,
    service: Mock,
    payload: dict[str, int],
    field: str,
) -> None:
    response = client.post(
        "/outbounds/10/items",
        json=payload,
    )

    assert response.status_code == 422

    assert any(
        error["loc"][-1] == field
        for error in response.json()["detail"]
    )

    service.add_item.assert_not_called()


def test_should_return_422_when_add_item_payload_has_extra_field(
    client: TestClient,
    service: Mock,
) -> None:
    response = client.post(
        "/outbounds/10/items",
        json={
            "part_id": 40,
            "quantity": 5,
            "unexpected_field": True,
        },
    )

    assert response.status_code == 422

    assert any(
        error["loc"][-1]
        == "unexpected_field"
        for error in response.json()["detail"]
    )

    service.add_item.assert_not_called()


@pytest.mark.parametrize(
    "outbound_id",
    [
        0,
        -1,
    ],
)
def test_should_return_422_when_outbound_id_is_invalid_on_add_item(
    client: TestClient,
    service: Mock,
    outbound_id: int,
) -> None:
    response = client.post(
        f"/outbounds/{outbound_id}/items",
        json={
            "part_id": 40,
            "quantity": 5,
        },
    )

    assert response.status_code == 422

    service.add_item.assert_not_called()


def test_should_rollback_when_unexpected_error_occurs_on_add_item(
    client: TestClient,
    service: Mock,
    session: Mock,
) -> None:
    service.add_item.side_effect = (
        RuntimeError(
            "Erro inesperado."
        )
    )

    with pytest.raises(
        RuntimeError,
        match="Erro inesperado.",
    ):
        client.post(
            "/outbounds/10/items",
            json={
                "part_id": 40,
                "quantity": 5,
            },
        )

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()

    session.refresh.assert_not_called()


def test_should_list_outbound_items(
    client: TestClient,
    service: Mock,
) -> None:
    service.list_outbound_items.return_value = [
        create_outbound_item(
            outbound_item_id=50,
            part_id=40,
            quantity=5,
        ),
        create_outbound_item(
            outbound_item_id=51,
            part_id=41,
            quantity=3,
        ),
    ]

    response = client.get(
        "/outbounds/10/items"
    )

    assert response.status_code == 200

    assert response.json() == [
        {
            "id": 50,
            "outbound_id": 10,
            "part_id": 40,
            "quantity": 5,
            "created_at": "2026-07-29T10:05:00",
        },
        {
            "id": 51,
            "outbound_id": 10,
            "part_id": 41,
            "quantity": 3,
            "created_at": "2026-07-29T10:05:00",
        },
    ]

    service.list_outbound_items.assert_called_once_with(
        10
    )


def test_should_return_empty_outbound_item_list(
    client: TestClient,
    service: Mock,
) -> None:
    service.list_outbound_items.return_value = []

    response = client.get(
        "/outbounds/10/items"
    )

    assert response.status_code == 200

    assert response.json() == []

    service.list_outbound_items.assert_called_once_with(
        10
    )


def test_should_return_404_when_outbound_is_not_found_on_list_items(
    client: TestClient,
    service: Mock,
) -> None:
    service.list_outbound_items.side_effect = (
        ValueError(
            "Saída não encontrada."
        )
    )

    response = client.get(
        "/outbounds/999/items"
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Saída não encontrada."
    }

    service.list_outbound_items.assert_called_once_with(
        999
    )


@pytest.mark.parametrize(
    "outbound_id",
    [
        0,
        -1,
    ],
)
def test_should_return_422_when_outbound_id_is_invalid_on_list_items(
    client: TestClient,
    service: Mock,
    outbound_id: int,
) -> None:
    response = client.get(
        f"/outbounds/{outbound_id}/items"
    )

    assert response.status_code == 422

    service.list_outbound_items.assert_not_called()
```

## `tests\api\test_part_route.py`

```python
from collections.abc import Generator
from types import SimpleNamespace
from unittest.mock import Mock

import pytest
from fastapi.testclient import TestClient

from src.api.routes.part_route import (
    get_part_service,
)
from src.database.connection import get_session
from src.main import app
from src.services.part_service import PartService


@pytest.fixture
def service_mock() -> Mock:
    """
    Cria um mock do serviço de peças.
    """

    return Mock(spec=PartService)


@pytest.fixture
def session_mock() -> Mock:
    """
    Cria um mock da sessão SQLAlchemy.
    """

    session = Mock()

    session.commit.return_value = None
    session.rollback.return_value = None
    session.refresh.return_value = None

    return session


@pytest.fixture
def client(
    service_mock: Mock,
    session_mock: Mock,
) -> Generator[TestClient, None, None]:
    """
    Cria o cliente HTTP substituindo o serviço e a sessão reais.
    """

    def override_part_service() -> Mock:
        return service_mock

    def override_session() -> Generator[Mock, None, None]:
        yield session_mock

    app.dependency_overrides[
        get_part_service
    ] = override_part_service

    app.dependency_overrides[
        get_session
    ] = override_session

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()


def create_part(
    *,
    part_id: int = 10,
    supplier_id: int = 1,
    part_code: str = "ABC123",
    name: str = "Compressor de ar",
    description: str | None = (
        "Compressor com obrigação de devolução de casco"
    ),
    return_deadline_days: int = 90,
    is_active: int = 1,
) -> SimpleNamespace:
    """
    Cria um objeto com os atributos esperados pelo schema.
    """

    return SimpleNamespace(
        id=part_id,
        supplier_id=supplier_id,
        part_code=part_code,
        name=name,
        description=description,
        return_deadline_days=return_deadline_days,
        is_active=is_active,
        created_at="2026-07-28T10:00:00",
        updated_at="2026-07-28T10:00:00",
    )


def expected_part_json(
    *,
    part_id: int = 10,
    supplier_id: int = 1,
    part_code: str = "ABC123",
    name: str = "Compressor de ar",
    description: str | None = (
        "Compressor com obrigação de devolução de casco"
    ),
    return_deadline_days: int = 90,
    is_active: int = 1,
) -> dict[str, object]:
    """
    Retorna o JSON esperado nas respostas da API.
    """

    return {
        "id": part_id,
        "supplier_id": supplier_id,
        "part_code": part_code,
        "name": name,
        "description": description,
        "return_deadline_days": return_deadline_days,
        "is_active": is_active,
        "created_at": "2026-07-28T10:00:00",
        "updated_at": "2026-07-28T10:00:00",
    }


def test_should_create_part_with_status_201(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    part = create_part()

    service_mock.create.return_value = part

    response = client.post(
        "/parts",
        json={
            "supplier_id": 1,
            "part_code": "ABC123",
            "name": "Compressor de ar",
            "description": (
                "Compressor com obrigação de devolução "
                "de casco"
            ),
            "return_deadline_days": 90,
        },
    )

    assert response.status_code == 201

    assert response.json() == expected_part_json()

    service_mock.create.assert_called_once_with(
        supplier_id=1,
        part_code="ABC123",
        name="Compressor de ar",
        description=(
            "Compressor com obrigação de devolução "
            "de casco"
        ),
        return_deadline_days=90,
    )

    session_mock.commit.assert_called_once_with()
    session_mock.refresh.assert_called_once_with(part)
    session_mock.rollback.assert_not_called()


def test_should_create_part_without_description(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    part = create_part(
        description=None,
    )

    service_mock.create.return_value = part

    response = client.post(
        "/parts",
        json={
            "supplier_id": 1,
            "part_code": "ABC123",
            "name": "Compressor de ar",
            "return_deadline_days": 90,
        },
    )

    assert response.status_code == 201

    assert response.json() == expected_part_json(
        description=None,
    )

    service_mock.create.assert_called_once_with(
        supplier_id=1,
        part_code="ABC123",
        name="Compressor de ar",
        description=None,
        return_deadline_days=90,
    )

    session_mock.commit.assert_called_once_with()
    session_mock.refresh.assert_called_once_with(part)
    session_mock.rollback.assert_not_called()


def test_should_return_404_when_supplier_is_not_found_on_create(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    service_mock.create.side_effect = ValueError(
        "Fornecedor não encontrado."
    )

    response = client.post(
        "/parts",
        json={
            "supplier_id": 999,
            "part_code": "ABC123",
            "name": "Compressor de ar",
            "description": None,
            "return_deadline_days": 90,
        },
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Fornecedor não encontrado.",
    }

    service_mock.create.assert_called_once_with(
        supplier_id=999,
        part_code="ABC123",
        name="Compressor de ar",
        description=None,
        return_deadline_days=90,
    )

    session_mock.rollback.assert_called_once_with()
    session_mock.commit.assert_not_called()
    session_mock.refresh.assert_not_called()


def test_should_return_400_when_supplier_is_inactive_on_create(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    service_mock.create.side_effect = ValueError(
        "O fornecedor informado está inativo."
    )

    response = client.post(
        "/parts",
        json={
            "supplier_id": 1,
            "part_code": "ABC123",
            "name": "Compressor de ar",
            "description": None,
            "return_deadline_days": 90,
        },
    )

    assert response.status_code == 400

    assert response.json() == {
        "detail": "O fornecedor informado está inativo.",
    }

    session_mock.rollback.assert_called_once_with()
    session_mock.commit.assert_not_called()
    session_mock.refresh.assert_not_called()


def test_should_return_409_when_part_code_already_exists_for_supplier(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    error_message = (
        "Já existe uma peça com este código "
        "para o fornecedor informado."
    )

    service_mock.create.side_effect = ValueError(
        error_message
    )

    response = client.post(
        "/parts",
        json={
            "supplier_id": 1,
            "part_code": "ABC123",
            "name": "Compressor de ar",
            "description": None,
            "return_deadline_days": 90,
        },
    )

    assert response.status_code == 409

    assert response.json() == {
        "detail": error_message,
    }

    session_mock.rollback.assert_called_once_with()
    session_mock.commit.assert_not_called()
    session_mock.refresh.assert_not_called()


def test_should_return_422_when_required_create_field_is_missing(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    response = client.post(
        "/parts",
        json={
            "supplier_id": 1,
            "part_code": "ABC123",
            "return_deadline_days": 90,
        },
    )

    assert response.status_code == 422

    service_mock.create.assert_not_called()

    session_mock.commit.assert_not_called()
    session_mock.rollback.assert_not_called()
    session_mock.refresh.assert_not_called()


def test_should_return_422_for_non_positive_supplier_id_on_create(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    response = client.post(
        "/parts",
        json={
            "supplier_id": 0,
            "part_code": "ABC123",
            "name": "Compressor de ar",
            "return_deadline_days": 90,
        },
    )

    assert response.status_code == 422

    service_mock.create.assert_not_called()

    session_mock.commit.assert_not_called()
    session_mock.rollback.assert_not_called()
    session_mock.refresh.assert_not_called()


def test_should_return_422_for_invalid_return_deadline_on_create(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    response = client.post(
        "/parts",
        json={
            "supplier_id": 1,
            "part_code": "ABC123",
            "name": "Compressor de ar",
            "return_deadline_days": 0,
        },
    )

    assert response.status_code == 422

    service_mock.create.assert_not_called()

    session_mock.commit.assert_not_called()
    session_mock.rollback.assert_not_called()
    session_mock.refresh.assert_not_called()


def test_should_reject_extra_create_request_fields(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    response = client.post(
        "/parts",
        json={
            "supplier_id": 1,
            "part_code": "ABC123",
            "name": "Compressor de ar",
            "return_deadline_days": 90,
            "manufacturer": "Fabricante não permitido",
        },
    )

    assert response.status_code == 422

    service_mock.create.assert_not_called()

    session_mock.commit.assert_not_called()
    session_mock.rollback.assert_not_called()
    session_mock.refresh.assert_not_called()

def test_should_list_all_parts(
client: TestClient,
service_mock: Mock,
) -> None:
    first_part = create_part()

    second_part = create_part(
        part_id=11,
        supplier_id=2,
        part_code="XYZ789",
        name="Alternador",
        description="Alternador remanufaturado",
        return_deadline_days=120,
    )

    service_mock.list_all.return_value = [
        first_part,
        second_part,
    ]

    response = client.get(
        "/parts",
    )

    assert response.status_code == 200

    assert response.json() == [
        expected_part_json(),
        expected_part_json(
            part_id=11,
            supplier_id=2,
            part_code="XYZ789",
            name="Alternador",
            description="Alternador remanufaturado",
            return_deadline_days=120,
        ),
    ]

    service_mock.list_all.assert_called_once_with()
    service_mock.list_by_supplier.assert_not_called()


def test_should_return_empty_list_when_there_are_no_parts(
    client: TestClient,
    service_mock: Mock,
) -> None:
    service_mock.list_all.return_value = []

    response = client.get(
        "/parts",
    )

    assert response.status_code == 200
    assert response.json() == []

    service_mock.list_all.assert_called_once_with()
    service_mock.list_by_supplier.assert_not_called()


def test_should_list_parts_filtered_by_supplier(
    client: TestClient,
    service_mock: Mock,
) -> None:
    first_part = create_part()

    second_part = create_part(
        part_id=11,
        part_code="DEF456",
        name="Motor de partida",
        description=None,
        return_deadline_days=120,
    )

    service_mock.list_by_supplier.return_value = [
        first_part,
        second_part,
    ]

    response = client.get(
        "/parts",
        params={
            "supplier_id": 1,
        },
    )

    assert response.status_code == 200

    assert response.json() == [
        expected_part_json(),
        expected_part_json(
            part_id=11,
            part_code="DEF456",
            name="Motor de partida",
            description=None,
            return_deadline_days=120,
        ),
    ]

    service_mock.list_by_supplier.assert_called_once_with(
        1
    )

    service_mock.list_all.assert_not_called()


def test_should_return_404_when_supplier_is_not_found_on_list(
    client: TestClient,
    service_mock: Mock,
) -> None:
    service_mock.list_by_supplier.side_effect = ValueError(
        "Fornecedor não encontrado."
    )

    response = client.get(
        "/parts",
        params={
            "supplier_id": 999,
        },
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Fornecedor não encontrado.",
    }

    service_mock.list_by_supplier.assert_called_once_with(
        999
    )

    service_mock.list_all.assert_not_called()


def test_should_return_422_for_non_positive_supplier_filter(
    client: TestClient,
    service_mock: Mock,
) -> None:
    response = client.get(
        "/parts",
        params={
            "supplier_id": 0,
        },
    )

    assert response.status_code == 422

    service_mock.list_all.assert_not_called()
    service_mock.list_by_supplier.assert_not_called()


def test_should_return_part_by_id(
    client: TestClient,
    service_mock: Mock,
) -> None:
    part = create_part()

    service_mock.get_required.return_value = part

    response = client.get(
        "/parts/10",
    )

    assert response.status_code == 200

    assert response.json() == expected_part_json()

    service_mock.get_required.assert_called_once_with(
        10
    )


def test_should_return_404_when_part_is_not_found(
    client: TestClient,
    service_mock: Mock,
) -> None:
    service_mock.get_required.side_effect = ValueError(
        "Peça não encontrada."
    )

    response = client.get(
        "/parts/999",
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Peça não encontrada.",
    }

    service_mock.get_required.assert_called_once_with(
        999
    )


def test_should_return_422_for_non_positive_part_id_on_get(
    client: TestClient,
    service_mock: Mock,
) -> None:
    response = client.get(
        "/parts/0",
    )

    assert response.status_code == 422

    service_mock.get_required.assert_not_called()


def test_should_return_422_for_invalid_text_part_id(
    client: TestClient,
    service_mock: Mock,
) -> None:
    response = client.get(
        "/parts/invalid-id",
    )

    assert response.status_code == 422

    service_mock.get_required.assert_not_called()

def test_should_update_part_name(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    updated_part = create_part(
        name="Compressor de ar atualizado",
    )

    service_mock.update.return_value = updated_part

    response = client.put(
        "/parts/10",
        json={
            "name": "Compressor de ar atualizado",
        },
    )

    assert response.status_code == 200

    assert response.json() == expected_part_json(
        name="Compressor de ar atualizado",
    )

    service_mock.update.assert_called_once_with(
        part_id=10,
        name="Compressor de ar atualizado",
    )

    session_mock.commit.assert_called_once_with()
    session_mock.refresh.assert_called_once_with(
        updated_part
    )
    session_mock.rollback.assert_not_called()


def test_should_update_part_supplier(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    updated_part = create_part(
        supplier_id=2,
    )

    service_mock.update.return_value = updated_part

    response = client.put(
        "/parts/10",
        json={
            "supplier_id": 2,
        },
    )

    assert response.status_code == 200

    assert response.json() == expected_part_json(
        supplier_id=2,
    )

    service_mock.update.assert_called_once_with(
        part_id=10,
        supplier_id=2,
    )

    session_mock.commit.assert_called_once_with()
    session_mock.refresh.assert_called_once_with(
        updated_part
    )
    session_mock.rollback.assert_not_called()


def test_should_update_part_code(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    updated_part = create_part(
        part_code="XYZ789",
    )

    service_mock.update.return_value = updated_part

    response = client.put(
        "/parts/10",
        json={
            "part_code": "XYZ789",
        },
    )

    assert response.status_code == 200

    assert response.json() == expected_part_json(
        part_code="XYZ789",
    )

    service_mock.update.assert_called_once_with(
        part_id=10,
        part_code="XYZ789",
    )

    session_mock.commit.assert_called_once_with()
    session_mock.refresh.assert_called_once_with(
        updated_part
    )
    session_mock.rollback.assert_not_called()


def test_should_update_return_deadline_days(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    updated_part = create_part(
        return_deadline_days=120,
    )

    service_mock.update.return_value = updated_part

    response = client.put(
        "/parts/10",
        json={
            "return_deadline_days": 120,
        },
    )

    assert response.status_code == 200

    assert response.json() == expected_part_json(
        return_deadline_days=120,
    )

    service_mock.update.assert_called_once_with(
        part_id=10,
        return_deadline_days=120,
    )

    session_mock.commit.assert_called_once_with()
    session_mock.refresh.assert_called_once_with(
        updated_part
    )
    session_mock.rollback.assert_not_called()


def test_should_update_multiple_part_fields(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    updated_part = create_part(
        supplier_id=2,
        part_code="NOVO123",
        name="Motor de partida",
        description="Descrição atualizada",
        return_deadline_days=180,
    )

    service_mock.update.return_value = updated_part

    response = client.put(
        "/parts/10",
        json={
            "supplier_id": 2,
            "part_code": "NOVO123",
            "name": "Motor de partida",
            "description": "Descrição atualizada",
            "return_deadline_days": 180,
        },
    )

    assert response.status_code == 200

    assert response.json() == expected_part_json(
        supplier_id=2,
        part_code="NOVO123",
        name="Motor de partida",
        description="Descrição atualizada",
        return_deadline_days=180,
    )

    service_mock.update.assert_called_once_with(
        part_id=10,
        supplier_id=2,
        part_code="NOVO123",
        name="Motor de partida",
        description="Descrição atualizada",
        return_deadline_days=180,
    )

    session_mock.commit.assert_called_once_with()
    session_mock.refresh.assert_called_once_with(
        updated_part
    )
    session_mock.rollback.assert_not_called()


def test_should_clear_part_description(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    updated_part = create_part(
        description=None,
    )

    service_mock.update.return_value = updated_part

    response = client.put(
        "/parts/10",
        json={
            "description": None,
        },
    )

    assert response.status_code == 200

    assert response.json() == expected_part_json(
        description=None,
    )

    service_mock.update.assert_called_once_with(
        part_id=10,
        description=None,
    )

    session_mock.commit.assert_called_once_with()
    session_mock.refresh.assert_called_once_with(
        updated_part
    )
    session_mock.rollback.assert_not_called()


def test_should_accept_empty_update_body(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    part = create_part()

    service_mock.update.return_value = part

    response = client.put(
        "/parts/10",
        json={},
    )

    assert response.status_code == 200

    assert response.json() == expected_part_json()

    service_mock.update.assert_called_once_with(
        part_id=10,
    )

    session_mock.commit.assert_called_once_with()
    session_mock.refresh.assert_called_once_with(part)
    session_mock.rollback.assert_not_called()


def test_should_return_404_when_part_is_not_found_on_update(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    service_mock.update.side_effect = ValueError(
        "Peça não encontrada."
    )

    response = client.put(
        "/parts/999",
        json={
            "name": "Novo nome",
        },
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Peça não encontrada.",
    }

    service_mock.update.assert_called_once_with(
        part_id=999,
        name="Novo nome",
    )

    session_mock.rollback.assert_called_once_with()
    session_mock.commit.assert_not_called()
    session_mock.refresh.assert_not_called()


def test_should_return_404_when_supplier_is_not_found_on_update(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    service_mock.update.side_effect = ValueError(
        "Fornecedor não encontrado."
    )

    response = client.put(
        "/parts/10",
        json={
            "supplier_id": 999,
        },
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Fornecedor não encontrado.",
    }

    service_mock.update.assert_called_once_with(
        part_id=10,
        supplier_id=999,
    )

    session_mock.rollback.assert_called_once_with()
    session_mock.commit.assert_not_called()
    session_mock.refresh.assert_not_called()


def test_should_return_400_when_new_supplier_is_inactive(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    service_mock.update.side_effect = ValueError(
        "O fornecedor informado está inativo."
    )

    response = client.put(
        "/parts/10",
        json={
            "supplier_id": 2,
        },
    )

    assert response.status_code == 400

    assert response.json() == {
        "detail": "O fornecedor informado está inativo.",
    }

    service_mock.update.assert_called_once_with(
        part_id=10,
        supplier_id=2,
    )

    session_mock.rollback.assert_called_once_with()
    session_mock.commit.assert_not_called()
    session_mock.refresh.assert_not_called()


def test_should_return_409_when_updated_combination_already_exists(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    error_message = (
        "Já existe uma peça com este código "
        "para o fornecedor informado."
    )

    service_mock.update.side_effect = ValueError(
        error_message
    )

    response = client.put(
        "/parts/10",
        json={
            "supplier_id": 2,
            "part_code": "ABC123",
        },
    )

    assert response.status_code == 409

    assert response.json() == {
        "detail": error_message,
    }

    service_mock.update.assert_called_once_with(
        part_id=10,
        supplier_id=2,
        part_code="ABC123",
    )

    session_mock.rollback.assert_called_once_with()
    session_mock.commit.assert_not_called()
    session_mock.refresh.assert_not_called()


def test_should_return_422_for_non_positive_part_id_on_update(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    response = client.put(
        "/parts/0",
        json={
            "name": "Novo nome",
        },
    )

    assert response.status_code == 422

    service_mock.update.assert_not_called()

    session_mock.commit.assert_not_called()
    session_mock.rollback.assert_not_called()
    session_mock.refresh.assert_not_called()


def test_should_return_422_for_invalid_supplier_id_on_update(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    response = client.put(
        "/parts/10",
        json={
            "supplier_id": 0,
        },
    )

    assert response.status_code == 422

    service_mock.update.assert_not_called()

    session_mock.commit.assert_not_called()
    session_mock.rollback.assert_not_called()
    session_mock.refresh.assert_not_called()


def test_should_return_422_for_invalid_deadline_on_update(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    response = client.put(
        "/parts/10",
        json={
            "return_deadline_days": 0,
        },
    )

    assert response.status_code == 422

    service_mock.update.assert_not_called()

    session_mock.commit.assert_not_called()
    session_mock.rollback.assert_not_called()
    session_mock.refresh.assert_not_called()


def test_should_return_422_for_deadline_above_maximum_on_update(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    response = client.put(
        "/parts/10",
        json={
            "return_deadline_days": 3651,
        },
    )

    assert response.status_code == 422

    service_mock.update.assert_not_called()

    session_mock.commit.assert_not_called()
    session_mock.rollback.assert_not_called()
    session_mock.refresh.assert_not_called()


def test_should_return_422_for_empty_part_code_on_update(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    response = client.put(
        "/parts/10",
        json={
            "part_code": "",
        },
    )

    assert response.status_code == 422

    service_mock.update.assert_not_called()

    session_mock.commit.assert_not_called()
    session_mock.rollback.assert_not_called()
    session_mock.refresh.assert_not_called()


def test_should_reject_extra_update_request_fields(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    response = client.put(
        "/parts/10",
        json={
            "name": "Motor de partida",
            "manufacturer": "Campo não permitido",
        },
    )

    assert response.status_code == 422

    service_mock.update.assert_not_called()

    session_mock.commit.assert_not_called()
    session_mock.rollback.assert_not_called()
    session_mock.refresh.assert_not_called()

def test_should_activate_part(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    part = create_part(
        is_active=1,
    )

    service_mock.activate.return_value = part

    response = client.patch(
        "/parts/10/activate",
    )

    assert response.status_code == 200

    assert response.json() == expected_part_json(
        is_active=1,
    )

    service_mock.activate.assert_called_once_with(
        10,
    )

    session_mock.commit.assert_called_once_with()
    session_mock.refresh.assert_called_once_with(
        part,
    )
    session_mock.rollback.assert_not_called()


def test_should_return_404_when_activate_unknown_part(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    service_mock.activate.side_effect = ValueError(
        "Peça não encontrada."
    )

    response = client.patch(
        "/parts/999/activate",
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Peça não encontrada.",
    }

    service_mock.activate.assert_called_once_with(
        999,
    )

    session_mock.rollback.assert_called_once_with()
    session_mock.commit.assert_not_called()
    session_mock.refresh.assert_not_called()


def test_should_return_400_when_part_is_already_active(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    service_mock.activate.side_effect = ValueError(
        "A peça já está ativa."
    )

    response = client.patch(
        "/parts/10/activate",
    )

    assert response.status_code == 400

    assert response.json() == {
        "detail": "A peça já está ativa.",
    }

    service_mock.activate.assert_called_once_with(
        10,
    )

    session_mock.rollback.assert_called_once_with()
    session_mock.commit.assert_not_called()
    session_mock.refresh.assert_not_called()


def test_should_return_422_when_activate_invalid_id(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    response = client.patch(
        "/parts/0/activate",
    )

    assert response.status_code == 422

    service_mock.activate.assert_not_called()

    session_mock.commit.assert_not_called()
    session_mock.rollback.assert_not_called()
    session_mock.refresh.assert_not_called()


def test_should_deactivate_part(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    part = create_part(
        is_active=0,
    )

    service_mock.deactivate.return_value = part

    response = client.patch(
        "/parts/10/deactivate",
    )

    assert response.status_code == 200

    assert response.json() == expected_part_json(
        is_active=0,
    )

    service_mock.deactivate.assert_called_once_with(
        10,
    )

    session_mock.commit.assert_called_once_with()
    session_mock.refresh.assert_called_once_with(
        part,
    )
    session_mock.rollback.assert_not_called()


def test_should_return_404_when_deactivate_unknown_part(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    service_mock.deactivate.side_effect = ValueError(
        "Peça não encontrada."
    )

    response = client.patch(
        "/parts/999/deactivate",
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Peça não encontrada.",
    }

    service_mock.deactivate.assert_called_once_with(
        999,
    )

    session_mock.rollback.assert_called_once_with()
    session_mock.commit.assert_not_called()
    session_mock.refresh.assert_not_called()


def test_should_return_400_when_part_is_already_inactive(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    service_mock.deactivate.side_effect = ValueError(
        "A peça já está inativa."
    )

    response = client.patch(
        "/parts/10/deactivate",
    )

    assert response.status_code == 400

    assert response.json() == {
        "detail": "A peça já está inativa.",
    }

    service_mock.deactivate.assert_called_once_with(
        10,
    )

    session_mock.rollback.assert_called_once_with()
    session_mock.commit.assert_not_called()
    session_mock.refresh.assert_not_called()


def test_should_return_422_when_deactivate_invalid_id(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    response = client.patch(
        "/parts/0/deactivate",
    )

    assert response.status_code == 422

    service_mock.deactivate.assert_not_called()

    session_mock.commit.assert_not_called()
    session_mock.rollback.assert_not_called()
    session_mock.refresh.assert_not_called()
```

## `tests\api\test_purchase_route.py`

```python
from types import SimpleNamespace
from unittest.mock import Mock

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from src.api.routes.purchase_route import (
    get_purchase_service,
    router,
)
from src.database.connection import get_session
from src.services.purchase_service import (
    PurchaseService,
)


@pytest.fixture
def session() -> Mock:
    """
    Cria uma sessão de banco simulada.
    """

    return Mock(spec=Session)


@pytest.fixture
def service() -> Mock:
    """
    Cria um PurchaseService simulado.
    """

    return Mock(spec=PurchaseService)


@pytest.fixture
def app(
    session: Mock,
    service: Mock,
) -> FastAPI:
    """
    Cria uma aplicação isolada para os testes.
    """

    test_app = FastAPI()

    test_app.include_router(router)

    def override_get_session():
        yield session

    def override_get_purchase_service():
        return service

    test_app.dependency_overrides[
        get_session
    ] = override_get_session

    test_app.dependency_overrides[
        get_purchase_service
    ] = override_get_purchase_service

    return test_app


@pytest.fixture
def client(
    app: FastAPI,
) -> TestClient:
    """
    Cria o cliente HTTP para a aplicação de teste.
    """

    return TestClient(
        app,
        raise_server_exceptions=False,
    )


def create_purchase(
    purchase_id: int = 10,
    supplier_id: int = 20,
    invoice_number: str = "NF-12345",
    invoice_series: str | None = "1",
    issue_date: str = "2026-07-29",
    received_at: str | None = None,
    notes: str | None = "Compra de teste.",
    created_by: int = 30,
    created_at: str = "2026-07-29T08:00:00",
    updated_at: str = "2026-07-29T08:00:00",
    status: str = "PENDING",
) -> SimpleNamespace:
    """
    Cria uma compra simulada para os testes.
    """

    return SimpleNamespace(
        id=purchase_id,
        supplier_id=supplier_id,
        invoice_number=invoice_number,
        invoice_series=invoice_series,
        issue_date=issue_date,
        received_at=received_at,
        notes=notes,
        created_by=created_by,
        created_at=created_at,
        updated_at=updated_at,
        status=status,
    )

def test_should_create_purchase(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    purchase = create_purchase()

    service.create_purchase.return_value = purchase

    response = client.post(
        "/purchases",
        json={
            "supplier_id": 20,
            "invoice_number": "NF-12345",
            "invoice_series": "1",
            "issue_date": "2026-07-29",
            "created_by": 30,
            "status": "PENDING",
            "notes": "Compra de teste.",
        },
    )

    assert response.status_code == 201

    assert response.json() == {
        "id": 10,
        "supplier_id": 20,
        "invoice_number": "NF-12345",
        "invoice_series": "1",
        "issue_date": "2026-07-29",
        "received_at": None,
        "notes": "Compra de teste.",
        "created_by": 30,
        "created_at": "2026-07-29T08:00:00",
        "updated_at": "2026-07-29T08:00:00",
        "status": "PENDING",
    }

    service.create_purchase.assert_called_once_with(
        supplier_id=20,
        invoice_number="NF-12345",
        invoice_series="1",
        issue_date="2026-07-29",
        created_by=30,
        status="PENDING",
        notes="Compra de teste.",
    )

    session.commit.assert_called_once_with()

    session.refresh.assert_called_once_with(
        purchase
    )

    session.rollback.assert_not_called()

def test_should_create_purchase_with_optional_fields_omitted(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    purchase = create_purchase(
        invoice_series=None,
        notes=None,
    )

    service.create_purchase.return_value = purchase

    response = client.post(
        "/purchases",
        json={
            "supplier_id": 20,
            "invoice_number": "NF-12345",
            "issue_date": "2026-07-29",
            "created_by": 30,
        },
    )

    assert response.status_code == 201

    response_data = response.json()

    assert response_data["invoice_series"] is None
    assert response_data["notes"] is None
    assert response_data["status"] == "PENDING"

    service.create_purchase.assert_called_once_with(
        supplier_id=20,
        invoice_number="NF-12345",
        invoice_series=None,
        issue_date="2026-07-29",
        created_by=30,
        status="PENDING",
        notes=None,
    )

    session.commit.assert_called_once_with()

    session.refresh.assert_called_once_with(
        purchase
    )

    session.rollback.assert_not_called()

def test_should_return_404_when_supplier_is_not_found_on_create(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    service.create_purchase.side_effect = ValueError(
        "Fornecedor não encontrado."
    )

    response = client.post(
        "/purchases",
        json={
            "supplier_id": 999,
            "invoice_number": "NF-12345",
            "invoice_series": "1",
            "issue_date": "2026-07-29",
            "created_by": 30,
            "status": "PENDING",
            "notes": "Compra de teste.",
        },
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Fornecedor não encontrado."
    }

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()

def test_should_return_400_when_supplier_is_inactive_on_create(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    service.create_purchase.side_effect = ValueError(
        "Não é possível cadastrar uma compra "
        "para um fornecedor inativo."
    )

    response = client.post(
        "/purchases",
        json={
            "supplier_id": 20,
            "invoice_number": "NF-12345",
            "invoice_series": "1",
            "issue_date": "2026-07-29",
            "created_by": 30,
        },
    )

    assert response.status_code == 400

    assert response.json() == {
        "detail": (
            "Não é possível cadastrar uma compra "
            "para um fornecedor inativo."
        )
    }

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()

def test_should_return_409_when_invoice_is_duplicated_on_create(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    service.create_purchase.side_effect = ValueError(
        "Já existe uma compra com esta nota fiscal, "
        "série e fornecedor."
    )

    response = client.post(
        "/purchases",
        json={
            "supplier_id": 20,
            "invoice_number": "NF-12345",
            "invoice_series": "1",
            "issue_date": "2026-07-29",
            "created_by": 30,
        },
    )

    assert response.status_code == 409

    assert response.json() == {
        "detail": (
            "Já existe uma compra com esta nota fiscal, "
            "série e fornecedor."
        )
    }

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()

@pytest.mark.parametrize(
    (
        "payload",
        "missing_field",
    ),
    [
        (
            {
                "invoice_number": "NF-12345",
                "issue_date": "2026-07-29",
                "created_by": 30,
            },
            "supplier_id",
        ),
        (
            {
                "supplier_id": 20,
                "issue_date": "2026-07-29",
                "created_by": 30,
            },
            "invoice_number",
        ),
        (
            {
                "supplier_id": 20,
                "invoice_number": "NF-12345",
                "created_by": 30,
            },
            "issue_date",
        ),
        (
            {
                "supplier_id": 20,
                "invoice_number": "NF-12345",
                "issue_date": "2026-07-29",
            },
            "created_by",
        ),
    ],
)
def test_should_return_422_when_required_field_is_missing(
    client: TestClient,
    session: Mock,
    service: Mock,
    payload: dict[str, object],
    missing_field: str,
) -> None:
    response = client.post(
        "/purchases",
        json=payload,
    )

    assert response.status_code == 422

    errors = response.json()["detail"]

    assert any(
        error["loc"][-1] == missing_field
        for error in errors
    )

    service.create_purchase.assert_not_called()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()
    session.rollback.assert_not_called()

@pytest.mark.parametrize(
    (
        "field",
        "invalid_value",
    ),
    [
        ("supplier_id", 0),
        ("supplier_id", -1),
        ("created_by", 0),
        ("created_by", -1),
    ],
)
def test_should_return_422_when_create_id_is_invalid(
    client: TestClient,
    session: Mock,
    service: Mock,
    field: str,
    invalid_value: int,
) -> None:
    payload = {
        "supplier_id": 20,
        "invoice_number": "NF-12345",
        "issue_date": "2026-07-29",
        "created_by": 30,
    }

    payload[field] = invalid_value

    response = client.post(
        "/purchases",
        json=payload,
    )

    assert response.status_code == 422

    service.create_purchase.assert_not_called()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()
    session.rollback.assert_not_called()

def test_should_return_422_when_create_status_is_invalid(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    response = client.post(
        "/purchases",
        json={
            "supplier_id": 20,
            "invoice_number": "NF-12345",
            "issue_date": "2026-07-29",
            "created_by": 30,
            "status": "INVALID",
        },
    )

    assert response.status_code == 422

    service.create_purchase.assert_not_called()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()
    session.rollback.assert_not_called()

def test_should_return_422_when_create_payload_has_extra_field(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    response = client.post(
        "/purchases",
        json={
            "supplier_id": 20,
            "invoice_number": "NF-12345",
            "issue_date": "2026-07-29",
            "created_by": 30,
            "unexpected_field": "valor inválido",
        },
    )

    assert response.status_code == 422

    service.create_purchase.assert_not_called()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()
    session.rollback.assert_not_called()

def test_should_rollback_when_unexpected_error_occurs_on_create(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    service.create_purchase.side_effect = RuntimeError(
        "Erro inesperado."
    )

    response = client.post(
        "/purchases",
        json={
            "supplier_id": 20,
            "invoice_number": "NF-12345",
            "issue_date": "2026-07-29",
            "created_by": 30,
        },
    )

    assert response.status_code == 500

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()

def test_should_list_purchases(
    client: TestClient,
    service: Mock,
) -> None:
    first_purchase = create_purchase(
        purchase_id=10,
        invoice_number="NF-12345",
    )

    second_purchase = create_purchase(
        purchase_id=11,
        invoice_number="NF-67890",
        invoice_series="2",
        notes=None,
        status="RECEIVED",
    )

    service.list_purchases.return_value = [
        first_purchase,
        second_purchase,
    ]

    response = client.get(
        "/purchases"
    )

    assert response.status_code == 200

    assert response.json() == [
        {
            "id": 10,
            "supplier_id": 20,
            "invoice_number": "NF-12345",
            "invoice_series": "1",
            "issue_date": "2026-07-29",
            "received_at": None,
            "notes": "Compra de teste.",
            "created_by": 30,
            "created_at": "2026-07-29T08:00:00",
            "updated_at": "2026-07-29T08:00:00",
            "status": "PENDING",
        },
        {
            "id": 11,
            "supplier_id": 20,
            "invoice_number": "NF-67890",
            "invoice_series": "2",
            "issue_date": "2026-07-29",
            "received_at": None,
            "notes": None,
            "created_by": 30,
            "created_at": "2026-07-29T08:00:00",
            "updated_at": "2026-07-29T08:00:00",
            "status": "RECEIVED",
        },
    ]

    service.list_purchases.assert_called_once_with()

def test_should_return_empty_purchase_list(
    client: TestClient,
    service: Mock,
) -> None:
    service.list_purchases.return_value = []

    response = client.get(
        "/purchases"
    )

    assert response.status_code == 200
    assert response.json() == []

    service.list_purchases.assert_called_once_with()

def test_should_list_purchases_by_supplier(
    client: TestClient,
    service: Mock,
) -> None:
    purchases = [
        create_purchase(
            purchase_id=10,
            supplier_id=20,
        ),
        create_purchase(
            purchase_id=11,
            supplier_id=20,
            invoice_number="NF-67890",
        ),
    ]

    service.list_purchases_by_supplier.return_value = (
        purchases
    )

    response = client.get(
        "/purchases",
        params={
            "supplier_id": 20,
        },
    )

    assert response.status_code == 200
    assert len(response.json()) == 2

    assert all(
        purchase["supplier_id"] == 20
        for purchase in response.json()
    )

    service.list_purchases_by_supplier.assert_called_once_with(
        20
    )

    service.list_purchases.assert_not_called()

def test_should_return_empty_list_when_supplier_has_no_purchases(
    client: TestClient,
    service: Mock,
) -> None:
    service.list_purchases_by_supplier.return_value = []

    response = client.get(
        "/purchases",
        params={
            "supplier_id": 20,
        },
    )

    assert response.status_code == 200
    assert response.json() == []

    service.list_purchases_by_supplier.assert_called_once_with(
        20
    )

    service.list_purchases.assert_not_called()

def test_should_return_404_when_supplier_is_not_found_on_list(
    client: TestClient,
    service: Mock,
) -> None:
    service.list_purchases_by_supplier.side_effect = (
        ValueError(
            "Fornecedor não encontrado."
        )
    )

    response = client.get(
        "/purchases",
        params={
            "supplier_id": 999,
        },
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Fornecedor não encontrado."
    }

    service.list_purchases_by_supplier.assert_called_once_with(
        999
    )

    service.list_purchases.assert_not_called()

@pytest.mark.parametrize(
    "supplier_id",
    [
        0,
        -1,
    ],
)
def test_should_return_422_when_supplier_filter_is_invalid(
    client: TestClient,
    service: Mock,
    supplier_id: int,
) -> None:
    response = client.get(
        "/purchases",
        params={
            "supplier_id": supplier_id,
        },
    )

    assert response.status_code == 422

    service.list_purchases.assert_not_called()

    service.list_purchases_by_supplier.assert_not_called()

def test_should_get_purchase(
    client: TestClient,
    service: Mock,
) -> None:
    purchase = create_purchase()

    service.get_purchase.return_value = purchase

    response = client.get(
        "/purchases/10"
    )

    assert response.status_code == 200

    assert response.json() == {
        "id": 10,
        "supplier_id": 20,
        "invoice_number": "NF-12345",
        "invoice_series": "1",
        "issue_date": "2026-07-29",
        "received_at": None,
        "notes": "Compra de teste.",
        "created_by": 30,
        "created_at": "2026-07-29T08:00:00",
        "updated_at": "2026-07-29T08:00:00",
        "status": "PENDING",
    }

    service.get_purchase.assert_called_once_with(
        10
    )

def test_should_return_404_when_purchase_is_not_found(
    client: TestClient,
    service: Mock,
) -> None:
    service.get_purchase.side_effect = ValueError(
        "Compra não encontrada."
    )

    response = client.get(
        "/purchases/999"
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Compra não encontrada."
    }

    service.get_purchase.assert_called_once_with(
        999
    )

@pytest.mark.parametrize(
    "purchase_id",
    [
        0,
        -1,
    ],
)
def test_should_return_422_when_purchase_id_is_invalid_on_get(
    client: TestClient,
    service: Mock,
    purchase_id: int,
) -> None:
    response = client.get(
        f"/purchases/{purchase_id}"
    )

    assert response.status_code == 422

    service.get_purchase.assert_not_called()

def test_should_update_purchase(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    purchase = create_purchase(
        invoice_number="NF-99999",
        invoice_series="2",
        issue_date="2026-07-30",
        notes="Compra atualizada.",
        status="RECEIVED",
    )

    service.update_purchase.return_value = purchase

    response = client.patch(
        "/purchases/10",
        json={
            "invoice_number": "NF-99999",
            "invoice_series": "2",
            "issue_date": "2026-07-30",
            "notes": "Compra atualizada.",
            "status": "RECEIVED",
        },
    )

    assert response.status_code == 200

    assert response.json() == {
        "id": 10,
        "supplier_id": 20,
        "invoice_number": "NF-99999",
        "invoice_series": "2",
        "issue_date": "2026-07-30",
        "received_at": None,
        "notes": "Compra atualizada.",
        "created_by": 30,
        "created_at": "2026-07-29T08:00:00",
        "updated_at": "2026-07-29T08:00:00",
        "status": "RECEIVED",
    }

    service.update_purchase.assert_called_once_with(
        purchase_id=10,
        invoice_number="NF-99999",
        invoice_series="2",
        issue_date="2026-07-30",
        notes="Compra atualizada.",
        status="RECEIVED",
    )

    session.commit.assert_called_once_with()

    session.refresh.assert_called_once_with(
        purchase
    )

    session.rollback.assert_not_called()


def test_should_update_only_sent_purchase_fields(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    purchase = create_purchase(
        notes="Nova observação.",
    )

    service.update_purchase.return_value = purchase

    response = client.patch(
        "/purchases/10",
        json={
            "notes": "Nova observação.",
        },
    )

    assert response.status_code == 200
    assert response.json()["notes"] == "Nova observação."

    service.update_purchase.assert_called_once_with(
        purchase_id=10,
        notes="Nova observação.",
    )

    session.commit.assert_called_once_with()

    session.refresh.assert_called_once_with(
        purchase
    )

    session.rollback.assert_not_called()


def test_should_update_purchase_supplier(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    purchase = create_purchase(
        supplier_id=21,
    )

    service.update_purchase.return_value = purchase

    response = client.patch(
        "/purchases/10",
        json={
            "supplier_id": 21,
        },
    )

    assert response.status_code == 200
    assert response.json()["supplier_id"] == 21

    service.update_purchase.assert_called_once_with(
        purchase_id=10,
        supplier_id=21,
    )

    session.commit.assert_called_once_with()

    session.refresh.assert_called_once_with(
        purchase
    )

    session.rollback.assert_not_called()


def test_should_clear_purchase_notes(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    purchase = create_purchase(
        notes=None,
    )

    service.update_purchase.return_value = purchase

    response = client.patch(
        "/purchases/10",
        json={
            "notes": None,
        },
    )

    assert response.status_code == 200
    assert response.json()["notes"] is None

    service.update_purchase.assert_called_once_with(
        purchase_id=10,
        notes=None,
    )

    session.commit.assert_called_once_with()

    session.refresh.assert_called_once_with(
        purchase
    )

    session.rollback.assert_not_called()


def test_should_clear_purchase_invoice_series(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    purchase = create_purchase(
        invoice_series=None,
    )

    service.update_purchase.return_value = purchase

    response = client.patch(
        "/purchases/10",
        json={
            "invoice_series": None,
        },
    )

    assert response.status_code == 200
    assert response.json()["invoice_series"] is None

    service.update_purchase.assert_called_once_with(
        purchase_id=10,
        invoice_series=None,
    )

    session.commit.assert_called_once_with()

    session.refresh.assert_called_once_with(
        purchase
    )

    session.rollback.assert_not_called()


def test_should_allow_empty_update_payload(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    purchase = create_purchase()

    service.update_purchase.return_value = purchase

    response = client.patch(
        "/purchases/10",
        json={},
    )

    assert response.status_code == 200

    service.update_purchase.assert_called_once_with(
        purchase_id=10,
    )

    session.commit.assert_called_once_with()

    session.refresh.assert_called_once_with(
        purchase
    )

    session.rollback.assert_not_called()


def test_should_return_404_when_purchase_is_not_found_on_update(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    service.update_purchase.side_effect = ValueError(
        "Compra não encontrada."
    )

    response = client.patch(
        "/purchases/999",
        json={
            "notes": "Nova observação.",
        },
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Compra não encontrada."
    }

    service.update_purchase.assert_called_once_with(
        purchase_id=999,
        notes="Nova observação.",
    )

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()


def test_should_return_404_when_supplier_is_not_found_on_update(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    service.update_purchase.side_effect = ValueError(
        "Fornecedor não encontrado."
    )

    response = client.patch(
        "/purchases/10",
        json={
            "supplier_id": 999,
        },
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Fornecedor não encontrado."
    }

    service.update_purchase.assert_called_once_with(
        purchase_id=10,
        supplier_id=999,
    )

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()


def test_should_return_400_when_supplier_is_inactive_on_update(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    service.update_purchase.side_effect = ValueError(
        "Não é possível vincular a compra "
        "a um fornecedor inativo."
    )

    response = client.patch(
        "/purchases/10",
        json={
            "supplier_id": 21,
        },
    )

    assert response.status_code == 400

    assert response.json() == {
        "detail": (
            "Não é possível vincular a compra "
            "a um fornecedor inativo."
        )
    }

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()


def test_should_return_409_when_invoice_is_duplicated_on_update(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    service.update_purchase.side_effect = ValueError(
        "Já existe uma compra com esta nota fiscal, "
        "série e fornecedor."
    )

    response = client.patch(
        "/purchases/10",
        json={
            "invoice_number": "NF-99999",
        },
    )

    assert response.status_code == 409

    assert response.json() == {
        "detail": (
            "Já existe uma compra com esta nota fiscal, "
            "série e fornecedor."
        )
    }

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()


def test_should_return_400_when_purchase_is_cancelled_on_update(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    service.update_purchase.side_effect = ValueError(
        "Não é possível alterar uma compra cancelada."
    )

    response = client.patch(
        "/purchases/10",
        json={
            "notes": "Nova observação.",
        },
    )

    assert response.status_code == 400

    assert response.json() == {
        "detail": (
            "Não é possível alterar uma compra cancelada."
        )
    }

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()


def test_should_return_400_when_supplier_is_incompatible_with_items(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    service.update_purchase.side_effect = ValueError(
        "Não é possível alterar o fornecedor, "
        "pois existem peças incompatíveis na compra."
    )

    response = client.patch(
        "/purchases/10",
        json={
            "supplier_id": 21,
        },
    )

    assert response.status_code == 400

    assert response.json() == {
        "detail": (
            "Não é possível alterar o fornecedor, "
            "pois existem peças incompatíveis na compra."
        )
    }

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()


def test_should_return_400_when_cancelled_status_is_sent_on_update(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    service.update_purchase.side_effect = ValueError(
        "Utilize a operação específica para cancelar a compra."
    )

    response = client.patch(
        "/purchases/10",
        json={
            "status": "CANCELLED",
        },
    )

    assert response.status_code == 400

    assert response.json() == {
        "detail": (
            "Utilize a operação específica "
            "para cancelar a compra."
        )
    }

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()


@pytest.mark.parametrize(
    "purchase_id",
    [
        0,
        -1,
    ],
)
def test_should_return_422_when_purchase_id_is_invalid_on_update(
    client: TestClient,
    session: Mock,
    service: Mock,
    purchase_id: int,
) -> None:
    response = client.patch(
        f"/purchases/{purchase_id}",
        json={
            "notes": "Nova observação.",
        },
    )

    assert response.status_code == 422

    service.update_purchase.assert_not_called()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()
    session.rollback.assert_not_called()


@pytest.mark.parametrize(
    (
        "payload",
        "invalid_field",
    ),
    [
        (
            {
                "supplier_id": 0,
            },
            "supplier_id",
        ),
        (
            {
                "supplier_id": -1,
            },
            "supplier_id",
        ),
        (
            {
                "invoice_number": "",
            },
            "invoice_number",
        ),
        (
            {
                "issue_date": "",
            },
            "issue_date",
        ),
        (
            {
                "status": "INVALID",
            },
            "status",
        ),
    ],
)
def test_should_return_422_when_update_payload_is_invalid(
    client: TestClient,
    session: Mock,
    service: Mock,
    payload: dict[str, object],
    invalid_field: str,
) -> None:
    response = client.patch(
        "/purchases/10",
        json=payload,
    )

    assert response.status_code == 422

    errors = response.json()["detail"]

    assert any(
        error["loc"][-1] == invalid_field
        for error in errors
    )

    service.update_purchase.assert_not_called()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()
    session.rollback.assert_not_called()


def test_should_return_422_when_update_payload_has_extra_field(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    response = client.patch(
        "/purchases/10",
        json={
            "unexpected_field": "valor inválido",
        },
    )

    assert response.status_code == 422

    service.update_purchase.assert_not_called()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()
    session.rollback.assert_not_called()


def test_should_rollback_when_unexpected_error_occurs_on_update(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    service.update_purchase.side_effect = RuntimeError(
        "Erro inesperado."
    )

    response = client.patch(
        "/purchases/10",
        json={
            "notes": "Nova observação.",
        },
    )

    assert response.status_code == 500

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()

def create_purchase_item(
    purchase_item_id: int = 30,
    purchase_id: int = 10,
    part_id: int = 40,
    quantity_purchased: int = 10,
    quantity_available: int = 10,
    created_at: str = "2026-07-29T08:00:00",
) -> SimpleNamespace:
    return SimpleNamespace(
        id=purchase_item_id,
        purchase_id=purchase_id,
        part_id=part_id,
        quantity_purchased=quantity_purchased,
        quantity_available=quantity_available,
        created_at=created_at,
    )


def test_should_add_purchase_item(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    purchase_item = create_purchase_item()

    service.add_item.return_value = purchase_item

    response = client.post(
        "/purchases/10/items",
        json={
            "part_id": 40,
            "quantity_purchased": 10,
        },
    )

    assert response.status_code == 201

    assert response.json() == {
        "id": 30,
        "purchase_id": 10,
        "part_id": 40,
        "quantity_purchased": 10,
        "quantity_available": 10,
        "created_at": "2026-07-29T08:00:00",
    }

    service.add_item.assert_called_once_with(
        purchase_id=10,
        part_id=40,
        quantity_purchased=10,
    )

    session.commit.assert_called_once_with()

    session.refresh.assert_called_once_with(
        purchase_item
    )

    session.rollback.assert_not_called()


def test_should_return_404_when_purchase_is_not_found_on_add_item(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    service.add_item.side_effect = ValueError(
        "Compra não encontrada."
    )

    response = client.post(
        "/purchases/999/items",
        json={
            "part_id": 40,
            "quantity_purchased": 10,
        },
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Compra não encontrada."
    }

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()


def test_should_return_404_when_part_is_not_found_on_add_item(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    service.add_item.side_effect = ValueError(
        "Peça não encontrada."
    )

    response = client.post(
        "/purchases/10/items",
        json={
            "part_id": 999,
            "quantity_purchased": 10,
        },
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Peça não encontrada."
    }

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()


def test_should_return_400_when_purchase_is_cancelled_on_add_item(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    service.add_item.side_effect = ValueError(
        "Não é possível adicionar itens "
        "a uma compra cancelada."
    )

    response = client.post(
        "/purchases/10/items",
        json={
            "part_id": 40,
            "quantity_purchased": 10,
        },
    )

    assert response.status_code == 400

    assert response.json() == {
        "detail": (
            "Não é possível adicionar itens "
            "a uma compra cancelada."
        )
    }

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()


def test_should_return_400_when_part_is_inactive_on_add_item(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    service.add_item.side_effect = ValueError(
        "Não é possível adicionar uma peça inativa."
    )

    response = client.post(
        "/purchases/10/items",
        json={
            "part_id": 40,
            "quantity_purchased": 10,
        },
    )

    assert response.status_code == 400

    assert response.json() == {
        "detail": (
            "Não é possível adicionar uma peça inativa."
        )
    }

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()


def test_should_return_400_when_part_supplier_is_incompatible(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    service.add_item.side_effect = ValueError(
        "A peça não pertence ao fornecedor da compra."
    )

    response = client.post(
        "/purchases/10/items",
        json={
            "part_id": 40,
            "quantity_purchased": 10,
        },
    )

    assert response.status_code == 400

    assert response.json() == {
        "detail": (
            "A peça não pertence ao fornecedor da compra."
        )
    }

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()


def test_should_return_409_when_purchase_item_is_duplicated(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    service.add_item.side_effect = ValueError(
        "Esta peça já foi adicionada à compra."
    )

    response = client.post(
        "/purchases/10/items",
        json={
            "part_id": 40,
            "quantity_purchased": 10,
        },
    )

    assert response.status_code == 409

    assert response.json() == {
        "detail": (
            "Esta peça já foi adicionada à compra."
        )
    }

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()


@pytest.mark.parametrize(
    "purchase_id",
    [
        0,
        -1,
    ],
)
def test_should_return_422_when_purchase_id_is_invalid_on_add_item(
    client: TestClient,
    session: Mock,
    service: Mock,
    purchase_id: int,
) -> None:
    response = client.post(
        f"/purchases/{purchase_id}/items",
        json={
            "part_id": 40,
            "quantity_purchased": 10,
        },
    )

    assert response.status_code == 422

    service.add_item.assert_not_called()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()
    session.rollback.assert_not_called()


@pytest.mark.parametrize(
    (
        "payload",
        "invalid_field",
    ),
    [
        (
            {
                "part_id": 0,
                "quantity_purchased": 10,
            },
            "part_id",
        ),
        (
            {
                "part_id": -1,
                "quantity_purchased": 10,
            },
            "part_id",
        ),
        (
            {
                "part_id": 40,
                "quantity_purchased": 0,
            },
            "quantity_purchased",
        ),
        (
            {
                "part_id": 40,
                "quantity_purchased": -1,
            },
            "quantity_purchased",
        ),
    ],
)
def test_should_return_422_when_add_item_payload_is_invalid(
    client: TestClient,
    session: Mock,
    service: Mock,
    payload: dict[str, int],
    invalid_field: str,
) -> None:
    response = client.post(
        "/purchases/10/items",
        json=payload,
    )

    assert response.status_code == 422

    errors = response.json()["detail"]

    assert any(
        error["loc"][-1] == invalid_field
        for error in errors
    )

    service.add_item.assert_not_called()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()
    session.rollback.assert_not_called()


def test_should_return_422_when_add_item_payload_has_extra_field(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    response = client.post(
        "/purchases/10/items",
        json={
            "part_id": 40,
            "quantity_purchased": 10,
            "unexpected_field": "valor inválido",
        },
    )

    assert response.status_code == 422

    service.add_item.assert_not_called()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()
    session.rollback.assert_not_called()


def test_should_rollback_when_unexpected_error_occurs_on_add_item(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    service.add_item.side_effect = RuntimeError(
        "Erro inesperado."
    )

    response = client.post(
        "/purchases/10/items",
        json={
            "part_id": 40,
            "quantity_purchased": 10,
        },
    )

    assert response.status_code == 500

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()


def test_should_list_purchase_items(
    client: TestClient,
    service: Mock,
) -> None:
    service.list_purchase_items.return_value = [
        create_purchase_item(),
        create_purchase_item(
            purchase_item_id=31,
            part_id=41,
            quantity_purchased=5,
            quantity_available=3,
        ),
    ]

    response = client.get(
        "/purchases/10/items"
    )

    assert response.status_code == 200

    assert response.json() == [
        {
            "id": 30,
            "purchase_id": 10,
            "part_id": 40,
            "quantity_purchased": 10,
            "quantity_available": 10,
            "created_at": "2026-07-29T08:00:00",
        },
        {
            "id": 31,
            "purchase_id": 10,
            "part_id": 41,
            "quantity_purchased": 5,
            "quantity_available": 3,
            "created_at": "2026-07-29T08:00:00",
        },
    ]

    service.list_purchase_items.assert_called_once_with(
        10
    )


def test_should_return_empty_purchase_item_list(
    client: TestClient,
    service: Mock,
) -> None:
    service.list_purchase_items.return_value = []

    response = client.get(
        "/purchases/10/items"
    )

    assert response.status_code == 200
    assert response.json() == []

    service.list_purchase_items.assert_called_once_with(
        10
    )


def test_should_return_404_when_purchase_is_not_found_on_list_items(
    client: TestClient,
    service: Mock,
) -> None:
    service.list_purchase_items.side_effect = ValueError(
        "Compra não encontrada."
    )

    response = client.get(
        "/purchases/999/items"
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Compra não encontrada."
    }

    service.list_purchase_items.assert_called_once_with(
        999
    )


@pytest.mark.parametrize(
    "purchase_id",
    [
        0,
        -1,
    ],
)
def test_should_return_422_when_purchase_id_is_invalid_on_list_items(
    client: TestClient,
    service: Mock,
    purchase_id: int,
) -> None:
    response = client.get(
        f"/purchases/{purchase_id}/items"
    )

    assert response.status_code == 422

    service.list_purchase_items.assert_not_called()


def test_should_cancel_purchase(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    purchase = create_purchase(
        status="CANCELLED",
    )

    service.cancel_purchase.return_value = purchase

    response = client.patch(
        "/purchases/10/cancel"
    )

    assert response.status_code == 200

    assert response.json()["status"] == "CANCELLED"

    service.cancel_purchase.assert_called_once_with(
        10
    )

    session.commit.assert_called_once_with()

    session.refresh.assert_called_once_with(
        purchase
    )

    session.rollback.assert_not_called()


def test_should_return_404_when_purchase_is_not_found_on_cancel(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    service.cancel_purchase.side_effect = ValueError(
        "Compra não encontrada."
    )

    response = client.patch(
        "/purchases/999/cancel"
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Compra não encontrada."
    }

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()


def test_should_return_409_when_purchase_is_already_cancelled(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    service.cancel_purchase.side_effect = ValueError(
        "A compra já está cancelada."
    )

    response = client.patch(
        "/purchases/10/cancel"
    )

    assert response.status_code == 409

    assert response.json() == {
        "detail": "A compra já está cancelada."
    }

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()


def test_should_return_400_when_purchase_has_movements_on_cancel(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    service.cancel_purchase.side_effect = ValueError(
        "Não é possível cancelar uma compra "
        "que já possui movimentações."
    )

    response = client.patch(
        "/purchases/10/cancel"
    )

    assert response.status_code == 400

    assert response.json() == {
        "detail": (
            "Não é possível cancelar uma compra "
            "que já possui movimentações."
        )
    }

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()


@pytest.mark.parametrize(
    "purchase_id",
    [
        0,
        -1,
    ],
)
def test_should_return_422_when_purchase_id_is_invalid_on_cancel(
    client: TestClient,
    session: Mock,
    service: Mock,
    purchase_id: int,
) -> None:
    response = client.patch(
        f"/purchases/{purchase_id}/cancel"
    )

    assert response.status_code == 422

    service.cancel_purchase.assert_not_called()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()
    session.rollback.assert_not_called()


def test_should_rollback_when_unexpected_error_occurs_on_cancel(
    client: TestClient,
    session: Mock,
    service: Mock,
) -> None:
    service.cancel_purchase.side_effect = RuntimeError(
        "Erro inesperado."
    )

    response = client.patch(
        "/purchases/10/cancel"
    )

    assert response.status_code == 500

    session.rollback.assert_called_once_with()

    session.commit.assert_not_called()
    session.refresh.assert_not_called()
```

## `tests\api\test_purchase_tracking_route.py`

```python
from collections.abc import Generator
from unittest.mock import Mock

import pytest
from fastapi.testclient import TestClient

from src.api.routes.purchase_tracking_route import (
    get_purchase_tracking_service,
)
from src.dtos.purchase_tracking import (
    PurchaseItemTrackingDTO,
    PurchaseTrackingDTO,
)
from src.main import app
from src.services.purchase_tracking_service import (
    PurchaseTrackingService,
)


@pytest.fixture
def service_mock() -> Mock:
    """
    Cria um mock compatível com PurchaseTrackingService.
    """

    return Mock(spec=PurchaseTrackingService)


@pytest.fixture
def client(
    service_mock: Mock,
) -> Generator[TestClient, None, None]:
    """
    Cria o cliente HTTP substituindo a dependência real do serviço.

    Dessa forma, os testes da rota não acessam o banco SQLite.
    """

    def override_purchase_tracking_service() -> Mock:
        return service_mock

    app.dependency_overrides[
        get_purchase_tracking_service
    ] = override_purchase_tracking_service

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()


def create_tracking_dto() -> PurchaseTrackingDTO:
    """
    Cria um acompanhamento completo para o teste HTTP.
    """

    item = PurchaseItemTrackingDTO(
        purchase_item_id=10,
        part_id=20,
        part_code="PCA-001",
        part_name="Peça com casco",
        quantity_purchased=10,
        quantity_available_for_outbound=2,
        quantity_outbound=8,
        quantity_returned_by_customer=5,
        quantity_pending_customer_return=3,
        quantity_available_for_supplier_return=3,
        quantity_returned_to_supplier=2,
        quantity_pending_supplier_return=8,
        lifecycle_status="PARTIALLY_RETURNED_TO_SUPPLIER",
    )

    return PurchaseTrackingDTO(
        purchase_id=1,
        supplier_id=5,
        supplier_name="Fornecedor Teste",
        invoice_number="NF-12345",
        invoice_series="1",
        issue_date="2026-07-28",
        purchase_status="ACTIVE",
        items=(item,),
    )


def test_should_return_purchase_tracking_with_status_200(
    client: TestClient,
    service_mock: Mock,
) -> None:
    expected_tracking = create_tracking_dto()

    service_mock.get_purchase_tracking.return_value = (
        expected_tracking
    )

    response = client.get(
        "/purchases/1/tracking",
    )

    assert response.status_code == 200

    assert response.json() == {
        "purchase_id": 1,
        "supplier_id": 5,
        "supplier_name": "Fornecedor Teste",
        "invoice_number": "NF-12345",
        "invoice_series": "1",
        "issue_date": "2026-07-28",
        "purchase_status": "ACTIVE",
        "items": [
            {
                "purchase_item_id": 10,
                "part_id": 20,
                "part_code": "PCA-001",
                "part_name": "Peça com casco",
                "quantity_purchased": 10,
                "quantity_available_for_outbound": 2,
                "quantity_outbound": 8,
                "quantity_returned_by_customer": 5,
                "quantity_pending_customer_return": 3,
                "quantity_available_for_supplier_return": 3,
                "quantity_returned_to_supplier": 2,
                "quantity_pending_supplier_return": 8,
                "lifecycle_status": (
                    "PARTIALLY_RETURNED_TO_SUPPLIER"
                ),
            }
        ],
    }

    service_mock.get_purchase_tracking.assert_called_once_with(1)


def test_should_return_404_when_purchase_is_not_found(
    client: TestClient,
    service_mock: Mock,
) -> None:
    service_mock.get_purchase_tracking.side_effect = ValueError(
        "Compra não encontrada."
    )

    response = client.get(
        "/purchases/999/tracking",
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Compra não encontrada.",
    }

    service_mock.get_purchase_tracking.assert_called_once_with(999)


def test_should_return_400_for_business_validation_error(
    client: TestClient,
    service_mock: Mock,
) -> None:
    service_mock.get_purchase_tracking.side_effect = ValueError(
        "Erro de validação da compra."
    )

    response = client.get(
        "/purchases/1/tracking",
    )

    assert response.status_code == 400

    assert response.json() == {
        "detail": "Erro de validação da compra.",
    }

    service_mock.get_purchase_tracking.assert_called_once_with(1)


def test_should_return_422_for_non_positive_purchase_id(
    client: TestClient,
    service_mock: Mock,
) -> None:
    response = client.get(
        "/purchases/0/tracking",
    )

    assert response.status_code == 422

    service_mock.get_purchase_tracking.assert_not_called()
```

## `tests\api\test_supplier_contact_route.py`

```python
from collections.abc import Generator
from types import SimpleNamespace
from unittest.mock import Mock

import pytest
from fastapi.testclient import TestClient

from src.api.routes.supplier_contact_route import (
    get_supplier_contact_service,
)
from src.database.connection import get_session
from src.main import app
from src.services.supplier_contact_service import (
    SupplierContactService,
)


@pytest.fixture
def service_mock() -> Mock:
    """Cria um mock do serviço de contatos."""

    return Mock(spec=SupplierContactService)


@pytest.fixture
def session_mock() -> Mock:
    """Cria um mock da sessão SQLAlchemy."""

    session = Mock()

    session.commit.return_value = None
    session.rollback.return_value = None
    session.refresh.return_value = None

    return session


@pytest.fixture
def client(
    service_mock: Mock,
    session_mock: Mock,
) -> Generator[TestClient, None, None]:
    """
    Cria o cliente HTTP substituindo as dependências reais.
    """

    def override_supplier_contact_service() -> Mock:
        return service_mock

    def override_session() -> Generator[Mock, None, None]:
        yield session_mock

    app.dependency_overrides[
        get_supplier_contact_service
    ] = override_supplier_contact_service

    app.dependency_overrides[
        get_session
    ] = override_session

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()


def create_contact(
    *,
    contact_id: int = 10,
    supplier_id: int = 1,
    name: str = "João Silva",
    email: str | None = "joao@fornecedor.com",
    phone: str | None = "(13) 99999-1111",
    position: str | None = "Garantia",
    is_primary: int = 1,
    is_active: int = 1,
) -> SimpleNamespace:
    """
    Cria um objeto com os atributos esperados
    pelo schema de resposta.
    """

    return SimpleNamespace(
        id=contact_id,
        supplier_id=supplier_id,
        name=name,
        email=email,
        phone=phone,
        position=position,
        is_primary=is_primary,
        is_active=is_active,
        created_at="2026-07-28T15:00:00",
    )


def expected_contact_json(
    *,
    contact_id: int = 10,
    supplier_id: int = 1,
    name: str = "João Silva",
    email: str | None = "joao@fornecedor.com",
    phone: str | None = "(13) 99999-1111",
    position: str | None = "Garantia",
    is_primary: bool = True,
    is_active: bool = True,
) -> dict[str, object]:
    """Retorna o JSON esperado nas respostas."""

    return {
        "id": contact_id,
        "supplier_id": supplier_id,
        "name": name,
        "email": email,
        "phone": phone,
        "position": position,
        "is_primary": is_primary,
        "is_active": is_active,
        "created_at": "2026-07-28T15:00:00",
    }


def test_should_create_supplier_contact_with_status_201(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    contact = create_contact()

    service_mock.create.return_value = contact

    response = client.post(
        "/suppliers/1/contacts",
        json={
            "name": "João Silva",
            "email": "joao@fornecedor.com",
            "phone": "(13) 99999-1111",
            "position": "Garantia",
            "is_primary": True,
        },
    )

    assert response.status_code == 201
    assert response.json() == expected_contact_json()

    service_mock.create.assert_called_once_with(
        supplier_id=1,
        name="João Silva",
        email="joao@fornecedor.com",
        phone="(13) 99999-1111",
        position="Garantia",
        is_primary=True,
    )

    session_mock.commit.assert_called_once_with()
    session_mock.refresh.assert_called_once_with(contact)
    session_mock.rollback.assert_not_called()


def test_should_list_supplier_contacts(
    client: TestClient,
    service_mock: Mock,
) -> None:
    primary_contact = create_contact()

    secondary_contact = create_contact(
        contact_id=11,
        name="Maria Souza",
        email="maria@fornecedor.com",
        phone=None,
        position="Comercial",
        is_primary=0,
        is_active=1,
    )

    service_mock.list_by_supplier.return_value = [
        primary_contact,
        secondary_contact,
    ]

    response = client.get(
        "/suppliers/1/contacts"
    )

    assert response.status_code == 200

    assert response.json() == [
        expected_contact_json(),
        expected_contact_json(
            contact_id=11,
            name="Maria Souza",
            email="maria@fornecedor.com",
            phone=None,
            position="Comercial",
            is_primary=False,
            is_active=True,
        ),
    ]

    service_mock.list_by_supplier.assert_called_once_with(
        1
    )


def test_should_get_supplier_contact_by_id(
    client: TestClient,
    service_mock: Mock,
) -> None:
    contact = create_contact()

    service_mock.get_required.return_value = contact

    response = client.get(
        "/suppliers/1/contacts/10"
    )

    assert response.status_code == 200
    assert response.json() == expected_contact_json()

    service_mock.get_required.assert_called_once_with(
        supplier_id=1,
        contact_id=10,
    )


def test_should_update_only_informed_contact_fields(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    contact = create_contact(
        phone="(13) 98888-2222",
        position="Pós-venda",
    )

    service_mock.update.return_value = contact

    response = client.put(
        "/suppliers/1/contacts/10",
        json={
            "phone": "(13) 98888-2222",
            "position": "Pós-venda",
        },
    )

    assert response.status_code == 200

    assert response.json() == expected_contact_json(
        phone="(13) 98888-2222",
        position="Pós-venda",
    )

    service_mock.update.assert_called_once_with(
        supplier_id=1,
        contact_id=10,
        phone="(13) 98888-2222",
        position="Pós-venda",
    )

    session_mock.commit.assert_called_once_with()
    session_mock.refresh.assert_called_once_with(contact)
    session_mock.rollback.assert_not_called()


def test_should_send_none_to_clear_optional_fields(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    contact = create_contact(
        email=None,
        phone=None,
        position=None,
    )

    service_mock.update.return_value = contact

    response = client.put(
        "/suppliers/1/contacts/10",
        json={
            "email": None,
            "phone": None,
            "position": None,
        },
    )

    assert response.status_code == 200

    assert response.json() == expected_contact_json(
        email=None,
        phone=None,
        position=None,
    )

    service_mock.update.assert_called_once_with(
        supplier_id=1,
        contact_id=10,
        email=None,
        phone=None,
        position=None,
    )

    session_mock.commit.assert_called_once_with()
    session_mock.refresh.assert_called_once_with(contact)
    session_mock.rollback.assert_not_called()


def test_should_deactivate_supplier_contact(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    contact = create_contact(
        is_primary=0,
        is_active=0,
    )

    service_mock.deactivate.return_value = contact

    response = client.patch(
        "/suppliers/1/contacts/10/deactivate"
    )

    assert response.status_code == 200

    assert response.json() == expected_contact_json(
        is_primary=False,
        is_active=False,
    )

    service_mock.deactivate.assert_called_once_with(
        supplier_id=1,
        contact_id=10,
    )

    session_mock.commit.assert_called_once_with()
    session_mock.refresh.assert_called_once_with(contact)
    session_mock.rollback.assert_not_called()


def test_should_activate_supplier_contact(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    contact = create_contact(
        is_primary=0,
        is_active=1,
    )

    service_mock.activate.return_value = contact

    response = client.patch(
        "/suppliers/1/contacts/10/activate"
    )

    assert response.status_code == 200

    assert response.json() == expected_contact_json(
        is_primary=False,
        is_active=True,
    )

    service_mock.activate.assert_called_once_with(
        supplier_id=1,
        contact_id=10,
    )

    session_mock.commit.assert_called_once_with()
    session_mock.refresh.assert_called_once_with(contact)
    session_mock.rollback.assert_not_called()


def test_should_return_404_when_supplier_is_not_found(
    client: TestClient,
    service_mock: Mock,
) -> None:
    service_mock.list_by_supplier.side_effect = ValueError(
        "Fornecedor não encontrado."
    )

    response = client.get(
        "/suppliers/999/contacts"
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Fornecedor não encontrado.",
    }

    service_mock.list_by_supplier.assert_called_once_with(
        999
    )


def test_should_return_404_when_contact_is_not_found(
    client: TestClient,
    service_mock: Mock,
) -> None:
    service_mock.get_required.side_effect = ValueError(
        "Contato não encontrado."
    )

    response = client.get(
        "/suppliers/1/contacts/999"
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Contato não encontrado.",
    }

    service_mock.get_required.assert_called_once_with(
        supplier_id=1,
        contact_id=999,
    )


def test_should_return_404_when_contact_belongs_to_another_supplier(
    client: TestClient,
    service_mock: Mock,
) -> None:
    service_mock.get_required.side_effect = ValueError(
        "O contato não pertence ao fornecedor informado."
    )

    response = client.get(
        "/suppliers/2/contacts/10"
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": (
            "O contato não pertence ao fornecedor informado."
        ),
    }

    service_mock.get_required.assert_called_once_with(
        supplier_id=2,
        contact_id=10,
    )


def test_should_return_400_when_contact_is_already_inactive(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    service_mock.deactivate.side_effect = ValueError(
        "O contato já está inativo."
    )

    response = client.patch(
        "/suppliers/1/contacts/10/deactivate"
    )

    assert response.status_code == 400

    assert response.json() == {
        "detail": "O contato já está inativo.",
    }

    session_mock.rollback.assert_called_once_with()
    session_mock.commit.assert_not_called()
    session_mock.refresh.assert_not_called()


def test_should_return_400_when_contact_is_already_active(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    service_mock.activate.side_effect = ValueError(
        "O contato já está ativo."
    )

    response = client.patch(
        "/suppliers/1/contacts/10/activate"
    )

    assert response.status_code == 400

    assert response.json() == {
        "detail": "O contato já está ativo.",
    }

    session_mock.rollback.assert_called_once_with()
    session_mock.commit.assert_not_called()
    session_mock.refresh.assert_not_called()


def test_should_rollback_when_update_fails(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    service_mock.update.side_effect = ValueError(
        "Contato não encontrado."
    )

    response = client.put(
        "/suppliers/1/contacts/999",
        json={
            "phone": "(13) 99999-9999",
        },
    )

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Contato não encontrado.",
    }

    session_mock.rollback.assert_called_once_with()
    session_mock.commit.assert_not_called()
    session_mock.refresh.assert_not_called()


def test_should_return_422_for_invalid_supplier_id(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    response = client.get(
        "/suppliers/0/contacts"
    )

    assert response.status_code == 422

    service_mock.list_by_supplier.assert_not_called()
    session_mock.commit.assert_not_called()
    session_mock.rollback.assert_not_called()


def test_should_return_422_for_invalid_contact_id(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    response = client.get(
        "/suppliers/1/contacts/0"
    )

    assert response.status_code == 422

    service_mock.get_required.assert_not_called()
    session_mock.commit.assert_not_called()
    session_mock.rollback.assert_not_called()


def test_should_return_422_for_invalid_email(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    response = client.post(
        "/suppliers/1/contacts",
        json={
            "name": "João Silva",
            "email": "email-invalido",
        },
    )

    assert response.status_code == 422

    service_mock.create.assert_not_called()
    session_mock.commit.assert_not_called()
    session_mock.rollback.assert_not_called()


def test_should_reject_extra_request_fields(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    response = client.post(
        "/suppliers/1/contacts",
        json={
            "name": "João Silva",
            "department": "Garantia",
        },
    )

    assert response.status_code == 422

    service_mock.create.assert_not_called()
    session_mock.commit.assert_not_called()
    session_mock.rollback.assert_not_called()
```

## `tests\api\test_supplier_route.py`

```python
from collections.abc import Generator
from types import SimpleNamespace
from unittest.mock import Mock

import pytest
from fastapi.testclient import TestClient

from src.api.routes.supplier_route import (
    get_supplier_service,
)
from src.database.connection import get_session
from src.main import app
from src.services.supplier_service import SupplierService


@pytest.fixture
def service_mock() -> Mock:
    """
    Cria um mock do serviço de fornecedores.
    """

    return Mock(spec=SupplierService)


@pytest.fixture
def session_mock() -> Mock:
    """
    Cria um mock da sessão SQLAlchemy.
    """

    session = Mock()

    session.commit.return_value = None
    session.rollback.return_value = None
    session.refresh.return_value = None

    return session


@pytest.fixture
def client(
    service_mock: Mock,
    session_mock: Mock,
) -> Generator[TestClient, None, None]:
    """
    Cria o cliente HTTP substituindo o serviço e a sessão reais.
    """

    def override_supplier_service() -> Mock:
        return service_mock

    def override_session() -> Generator[Mock, None, None]:
        yield session_mock

    app.dependency_overrides[
        get_supplier_service
    ] = override_supplier_service

    app.dependency_overrides[
        get_session
    ] = override_session

    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()


def create_supplier(
    *,
    supplier_id: int = 1,
    name: str = "Fornecedor Teste",
    document: str | None = "12.345.678/0001-90",
    address: str | None = "Registro/SP",
    notes: str | None = "Fornecedor de teste",
    is_active: int = 1,
) -> SimpleNamespace:
    """
    Cria um objeto com os atributos esperados pelo schema.
    """

    return SimpleNamespace(
        id=supplier_id,
        name=name,
        document=document,
        address=address,
        notes=notes,
        is_active=is_active,
        created_at="2026-07-28T10:00:00",
        updated_at="2026-07-28T10:00:00",
    )


def expected_supplier_json(
    *,
    supplier_id: int = 1,
    name: str = "Fornecedor Teste",
    document: str | None = "12.345.678/0001-90",
    address: str | None = "Registro/SP",
    notes: str | None = "Fornecedor de teste",
    is_active: int = 1,
) -> dict[str, object]:
    """
    Retorna o JSON esperado nas respostas.
    """

    return {
        "id": supplier_id,
        "name": name,
        "document": document,
        "address": address,
        "notes": notes,
        "is_active": is_active,
        "created_at": "2026-07-28T10:00:00",
        "updated_at": "2026-07-28T10:00:00",
    }


def test_should_create_supplier_with_status_201(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    supplier = create_supplier()

    service_mock.create.return_value = supplier

    response = client.post(
        "/suppliers",
        json={
            "name": "Fornecedor Teste",
            "document": "12.345.678/0001-90",
            "address": "Registro/SP",
            "notes": "Fornecedor de teste",
        },
    )

    assert response.status_code == 201
    assert response.json() == expected_supplier_json()

    service_mock.create.assert_called_once_with(
        name="Fornecedor Teste",
        document="12.345.678/0001-90",
        address="Registro/SP",
        notes="Fornecedor de teste",
    )

    session_mock.commit.assert_called_once_with()
    session_mock.refresh.assert_called_once_with(supplier)
    session_mock.rollback.assert_not_called()


def test_should_list_suppliers(
    client: TestClient,
    service_mock: Mock,
) -> None:
    first_supplier = create_supplier()

    second_supplier = create_supplier(
        supplier_id=2,
        name="Segundo Fornecedor",
        document=None,
        address=None,
        notes=None,
        is_active=0,
    )

    service_mock.list_all.return_value = [
        first_supplier,
        second_supplier,
    ]

    response = client.get("/suppliers")

    assert response.status_code == 200

    assert response.json() == [
        expected_supplier_json(),
        expected_supplier_json(
            supplier_id=2,
            name="Segundo Fornecedor",
            document=None,
            address=None,
            notes=None,
            is_active=0,
        ),
    ]

    service_mock.list_all.assert_called_once_with()


def test_should_get_supplier_by_id(
    client: TestClient,
    service_mock: Mock,
) -> None:
    supplier = create_supplier()

    service_mock.get_required.return_value = supplier

    response = client.get("/suppliers/1")

    assert response.status_code == 200
    assert response.json() == expected_supplier_json()

    service_mock.get_required.assert_called_once_with(1)


def test_should_return_404_when_supplier_is_not_found(
    client: TestClient,
    service_mock: Mock,
) -> None:
    service_mock.get_required.side_effect = ValueError(
        "Fornecedor não encontrado."
    )

    response = client.get("/suppliers/999")

    assert response.status_code == 404

    assert response.json() == {
        "detail": "Fornecedor não encontrado.",
    }

    service_mock.get_required.assert_called_once_with(999)


def test_should_update_only_informed_fields(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    supplier = create_supplier(
        address="Novo endereço",
        notes=None,
    )

    service_mock.update.return_value = supplier

    response = client.put(
        "/suppliers/1",
        json={
            "address": "Novo endereço",
            "notes": None,
        },
    )

    assert response.status_code == 200

    assert response.json() == expected_supplier_json(
        address="Novo endereço",
        notes=None,
    )

    service_mock.update.assert_called_once_with(
        1,
        address="Novo endereço",
        notes=None,
    )

    session_mock.commit.assert_called_once_with()
    session_mock.refresh.assert_called_once_with(supplier)
    session_mock.rollback.assert_not_called()


def test_should_return_409_for_duplicate_document(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    service_mock.create.side_effect = ValueError(
        "Já existe um fornecedor com este documento."
    )

    response = client.post(
        "/suppliers",
        json={
            "name": "Fornecedor Duplicado",
            "document": "12.345.678/0001-90",
        },
    )

    assert response.status_code == 409

    assert response.json() == {
        "detail": (
            "Já existe um fornecedor com este documento."
        ),
    }

    session_mock.rollback.assert_called_once_with()
    session_mock.commit.assert_not_called()
    session_mock.refresh.assert_not_called()


def test_should_deactivate_supplier(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    supplier = create_supplier(
        is_active=0,
    )

    service_mock.deactivate.return_value = supplier

    response = client.patch(
        "/suppliers/1/deactivate",
    )

    assert response.status_code == 200

    assert response.json() == expected_supplier_json(
        is_active=0,
    )

    service_mock.deactivate.assert_called_once_with(1)

    session_mock.commit.assert_called_once_with()
    session_mock.refresh.assert_called_once_with(supplier)
    session_mock.rollback.assert_not_called()


def test_should_activate_supplier(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    supplier = create_supplier(
        is_active=1,
    )

    service_mock.activate.return_value = supplier

    response = client.patch(
        "/suppliers/1/activate",
    )

    assert response.status_code == 200

    assert response.json() == expected_supplier_json(
        is_active=1,
    )

    service_mock.activate.assert_called_once_with(1)

    session_mock.commit.assert_called_once_with()
    session_mock.refresh.assert_called_once_with(supplier)
    session_mock.rollback.assert_not_called()


def test_should_return_400_when_supplier_is_already_inactive(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    service_mock.deactivate.side_effect = ValueError(
        "O fornecedor já está inativo."
    )

    response = client.patch(
        "/suppliers/1/deactivate",
    )

    assert response.status_code == 400

    assert response.json() == {
        "detail": "O fornecedor já está inativo.",
    }

    session_mock.rollback.assert_called_once_with()
    session_mock.commit.assert_not_called()


def test_should_return_422_for_invalid_supplier_id(
    client: TestClient,
    service_mock: Mock,
    session_mock: Mock,
) -> None:
    response = client.get(
        "/suppliers/0",
    )

    assert response.status_code == 422

    service_mock.get_required.assert_not_called()
    session_mock.commit.assert_not_called()
    session_mock.rollback.assert_not_called()
```

## `tests\services\__init__.py`

```python

```

## `tests\services\test_outbound_service.py`

```python
from types import SimpleNamespace
from unittest.mock import Mock

import pytest

from src.models.outbound import Outbound
from src.services.outbound_service import OutboundService


@pytest.fixture
def outbound_repository() -> Mock:
    repository = Mock()

    repository.add.side_effect = (
        lambda outbound: outbound
    )

    repository.save.side_effect = (
        lambda outbound: outbound
    )

    return repository


@pytest.fixture
def outbound_item_repository() -> Mock:
    repository = Mock()

    repository.add.side_effect = (
        lambda outbound_item: outbound_item
    )

    return repository


@pytest.fixture
def allocation_repository() -> Mock:
    repository = Mock()

    repository.add.side_effect = (
        lambda allocation: allocation
    )

    return repository


@pytest.fixture
def purchase_item_repository() -> Mock:
    return Mock()


@pytest.fixture
def part_repository() -> Mock:
    return Mock()


@pytest.fixture
def service(
    outbound_repository: Mock,
    outbound_item_repository: Mock,
    allocation_repository: Mock,
    purchase_item_repository: Mock,
    part_repository: Mock,
) -> OutboundService:
    return OutboundService(
        outbound_repository=outbound_repository,
        outbound_item_repository=(
            outbound_item_repository
        ),
        outbound_purchase_allocation_repository=(
            allocation_repository
        ),
        purchase_item_repository=(
            purchase_item_repository
        ),
        part_repository=part_repository,
    )


def create_outbound(
    outbound_id: int = 10,
    destination_type: str = "WORK_ORDER",
    work_order_number: str | None = "OS-12345",
    sales_invoice_number: str | None = None,
    created_by: int = 30,
    status: str = "ACTIVE",
) -> SimpleNamespace:
    return SimpleNamespace(
        id=outbound_id,
        destination_type=destination_type,
        work_order_number=work_order_number,
        sales_invoice_number=sales_invoice_number,
        created_by=created_by,
        status=status,
    )


def test_should_create_outbound_with_work_order(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbound_repository.get_by_work_order_number.return_value = (
        None
    )

    outbound = service.create_outbound(
        destination_type="WORK_ORDER",
        work_order_number="OS-12345",
        created_by=30,
    )

    assert isinstance(
        outbound,
        Outbound,
    )

    assert outbound.destination_type == "WORK_ORDER"
    assert outbound.work_order_number == "OS-12345"
    assert outbound.sales_invoice_number is None
    assert outbound.created_by == 30
    assert outbound.status == "ACTIVE"

    outbound_repository.get_by_work_order_number.assert_called_once_with(
        "OS-12345"
    )

    outbound_repository.get_by_sales_invoice_number.assert_not_called()

    outbound_repository.add.assert_called_once_with(
        outbound
    )


def test_should_create_outbound_with_sales_invoice(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbound_repository.get_by_sales_invoice_number.return_value = (
        None
    )

    outbound = service.create_outbound(
        destination_type="SALE",
        sales_invoice_number="NFV-12345",
        created_by=30,
    )

    assert isinstance(
        outbound,
        Outbound,
    )

    assert outbound.destination_type == "SALE"
    assert outbound.work_order_number is None
    assert outbound.sales_invoice_number == "NFV-12345"
    assert outbound.created_by == 30
    assert outbound.status == "ACTIVE"

    outbound_repository.get_by_sales_invoice_number.assert_called_once_with(
        "NFV-12345"
    )

    outbound_repository.get_by_work_order_number.assert_not_called()

    outbound_repository.add.assert_called_once_with(
        outbound
    )


def test_should_create_outbound_with_both_reference_numbers(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbound_repository.get_by_work_order_number.return_value = (
        None
    )

    outbound_repository.get_by_sales_invoice_number.return_value = (
        None
    )

    outbound = service.create_outbound(
        destination_type="WORK_ORDER",
        work_order_number="OS-12345",
        sales_invoice_number="NFV-12345",
        created_by=30,
    )

    assert outbound.work_order_number == "OS-12345"

    assert (
        outbound.sales_invoice_number
        == "NFV-12345"
    )

    outbound_repository.get_by_work_order_number.assert_called_once_with(
        "OS-12345"
    )

    outbound_repository.get_by_sales_invoice_number.assert_called_once_with(
        "NFV-12345"
    )

    outbound_repository.add.assert_called_once_with(
        outbound
    )


def test_should_normalize_outbound_fields_on_create(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbound_repository.get_by_work_order_number.return_value = (
        None
    )

    outbound_repository.get_by_sales_invoice_number.return_value = (
        None
    )

    outbound = service.create_outbound(
        destination_type="  WORK_ORDER  ",
        work_order_number="  OS-12345  ",
        sales_invoice_number="  NFV-12345  ",
        created_by=30,
        status="  active  ",
    )

    assert outbound.destination_type == "WORK_ORDER"
    assert outbound.work_order_number == "OS-12345"

    assert (
        outbound.sales_invoice_number
        == "NFV-12345"
    )

    assert outbound.status == "ACTIVE"

    outbound_repository.get_by_work_order_number.assert_called_once_with(
        "OS-12345"
    )

    outbound_repository.get_by_sales_invoice_number.assert_called_once_with(
        "NFV-12345"
    )


def test_should_convert_blank_work_order_to_none(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbound_repository.get_by_sales_invoice_number.return_value = (
        None
    )

    outbound = service.create_outbound(
        destination_type="SALE",
        work_order_number="   ",
        sales_invoice_number="NFV-12345",
        created_by=30,
    )

    assert outbound.work_order_number is None

    assert (
        outbound.sales_invoice_number
        == "NFV-12345"
    )

    outbound_repository.get_by_work_order_number.assert_not_called()

    outbound_repository.get_by_sales_invoice_number.assert_called_once_with(
        "NFV-12345"
    )


def test_should_convert_blank_sales_invoice_to_none(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbound_repository.get_by_work_order_number.return_value = (
        None
    )

    outbound = service.create_outbound(
        destination_type="WORK_ORDER",
        work_order_number="OS-12345",
        sales_invoice_number="   ",
        created_by=30,
    )

    assert outbound.work_order_number == "OS-12345"
    assert outbound.sales_invoice_number is None

    outbound_repository.get_by_work_order_number.assert_called_once_with(
        "OS-12345"
    )

    outbound_repository.get_by_sales_invoice_number.assert_not_called()


def test_should_return_repository_result_on_create(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    persisted_outbound = create_outbound()

    outbound_repository.get_by_work_order_number.return_value = (
        None
    )

    outbound_repository.add.side_effect = None

    outbound_repository.add.return_value = (
        persisted_outbound
    )

    result = service.create_outbound(
        destination_type="WORK_ORDER",
        work_order_number="OS-12345",
        created_by=30,
    )

    assert result is persisted_outbound

    outbound_repository.add.assert_called_once()

    created_outbound = (
        outbound_repository.add.call_args.args[0]
    )

    assert isinstance(
        created_outbound,
        Outbound,
    )

    assert (
        created_outbound.destination_type
        == "WORK_ORDER"
    )

    assert (
        created_outbound.work_order_number
        == "OS-12345"
    )

    assert (
        created_outbound.sales_invoice_number
        is None
    )

    assert created_outbound.created_by == 30
    assert created_outbound.status == "ACTIVE"


def test_should_raise_error_when_destination_type_is_blank(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    with pytest.raises(
        ValueError,
        match="O tipo de destino é obrigatório.",
    ):
        service.create_outbound(
            destination_type="   ",
            work_order_number="OS-12345",
            created_by=30,
        )

    outbound_repository.add.assert_not_called()

    outbound_repository.get_by_work_order_number.assert_not_called()

    outbound_repository.get_by_sales_invoice_number.assert_not_called()


@pytest.mark.parametrize(
    "created_by",
    [
        0,
        -1,
    ],
)
def test_should_raise_error_when_created_by_is_invalid(
    service: OutboundService,
    outbound_repository: Mock,
    created_by: int,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "O identificador do usuário deve ser "
            "maior que zero."
        ),
    ):
        service.create_outbound(
            destination_type="WORK_ORDER",
            work_order_number="OS-12345",
            created_by=created_by,
        )

    outbound_repository.add.assert_not_called()

    outbound_repository.get_by_work_order_number.assert_not_called()

    outbound_repository.get_by_sales_invoice_number.assert_not_called()


def test_should_raise_error_when_reference_numbers_are_missing(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "A saída deve possuir uma ordem de serviço "
            "ou uma nota fiscal de venda."
        ),
    ):
        service.create_outbound(
            destination_type="WORK_ORDER",
            created_by=30,
        )

    outbound_repository.add.assert_not_called()

    outbound_repository.get_by_work_order_number.assert_not_called()

    outbound_repository.get_by_sales_invoice_number.assert_not_called()


def test_should_raise_error_when_reference_numbers_are_blank(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "A saída deve possuir uma ordem de serviço "
            "ou uma nota fiscal de venda."
        ),
    ):
        service.create_outbound(
            destination_type="WORK_ORDER",
            work_order_number="   ",
            sales_invoice_number="   ",
            created_by=30,
        )

    outbound_repository.add.assert_not_called()

    outbound_repository.get_by_work_order_number.assert_not_called()

    outbound_repository.get_by_sales_invoice_number.assert_not_called()


def test_should_raise_error_when_outbound_is_created_cancelled(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "Uma saída não pode ser criada "
            "já cancelada."
        ),
    ):
        service.create_outbound(
            destination_type="WORK_ORDER",
            work_order_number="OS-12345",
            created_by=30,
            status="CANCELLED",
        )

    outbound_repository.add.assert_not_called()

    outbound_repository.get_by_work_order_number.assert_not_called()

    outbound_repository.get_by_sales_invoice_number.assert_not_called()


@pytest.mark.parametrize(
    "status",
    [
        "",
        "   ",
        "PENDING",
        "FINISHED",
        "INVALID",
    ],
)
def test_should_raise_error_when_create_status_is_invalid(
    service: OutboundService,
    outbound_repository: Mock,
    status: str,
) -> None:
    expected_message = (
        "O status da saída é obrigatório."
        if not status.strip()
        else "Status de saída inválido."
    )

    with pytest.raises(
        ValueError,
        match=expected_message,
    ):
        service.create_outbound(
            destination_type="WORK_ORDER",
            work_order_number="OS-12345",
            created_by=30,
            status=status,
        )

    outbound_repository.add.assert_not_called()


def test_should_raise_error_when_work_order_is_duplicated(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    existing_outbound = create_outbound(
        outbound_id=11,
    )

    outbound_repository.get_by_work_order_number.return_value = (
        existing_outbound
    )

    with pytest.raises(
        ValueError,
        match=(
            "Já existe uma saída com esta "
            "ordem de serviço."
        ),
    ):
        service.create_outbound(
            destination_type="WORK_ORDER",
            work_order_number="OS-12345",
            created_by=30,
        )

    outbound_repository.get_by_work_order_number.assert_called_once_with(
        "OS-12345"
    )

    outbound_repository.add.assert_not_called()


def test_should_raise_error_when_sales_invoice_is_duplicated(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    existing_outbound = create_outbound(
        outbound_id=11,
        work_order_number=None,
        sales_invoice_number="NFV-12345",
    )

    outbound_repository.get_by_sales_invoice_number.return_value = (
        existing_outbound
    )

    with pytest.raises(
        ValueError,
        match=(
            "Já existe uma saída com esta "
            "nota fiscal de venda."
        ),
    ):
        service.create_outbound(
            destination_type="SALE",
            sales_invoice_number="NFV-12345",
            created_by=30,
        )

    outbound_repository.get_by_sales_invoice_number.assert_called_once_with(
        "NFV-12345"
    )

    outbound_repository.add.assert_not_called()


def test_should_not_check_blank_optional_reference_for_duplicates(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbound_repository.get_by_work_order_number.return_value = (
        None
    )

    service.create_outbound(
        destination_type="WORK_ORDER",
        work_order_number="OS-12345",
        sales_invoice_number="   ",
        created_by=30,
    )

    outbound_repository.get_by_work_order_number.assert_called_once_with(
        "OS-12345"
    )

    outbound_repository.get_by_sales_invoice_number.assert_not_called()

    outbound_repository.add.assert_called_once()

def create_part(
    part_id: int = 40,
    is_active: bool = True,
) -> SimpleNamespace:
    return SimpleNamespace(
        id=part_id,
        is_active=is_active,
    )


def create_purchase_item(
    purchase_item_id: int,
    part_id: int = 40,
    quantity_available: int = 10,
) -> SimpleNamespace:
    return SimpleNamespace(
        id=purchase_item_id,
        part_id=part_id,
        quantity_available=quantity_available,
    )


def create_outbound_item(
    outbound_item_id: int = 50,
    outbound_id: int = 10,
    part_id: int = 40,
    quantity: int = 8,
) -> SimpleNamespace:
    return SimpleNamespace(
        id=outbound_item_id,
        outbound_id=outbound_id,
        part_id=part_id,
        quantity=quantity,
    )


def test_should_add_outbound_item_using_single_purchase_item(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
    allocation_repository: Mock,
    purchase_item_repository: Mock,
    part_repository: Mock,
) -> None:
    outbound = create_outbound()

    part = create_part()

    purchase_item = create_purchase_item(
        purchase_item_id=60,
        quantity_available=10,
    )

    persisted_outbound_item = create_outbound_item(
        quantity=8,
    )

    outbound_repository.get_by_id.return_value = (
        outbound
    )

    part_repository.get_by_id.return_value = (
        part
    )

    outbound_item_repository.list_by_outbound.return_value = (
        []
    )

    purchase_item_repository.list_available_by_part.return_value = [
        purchase_item
    ]

    outbound_item_repository.add.side_effect = None

    outbound_item_repository.add.return_value = (
        persisted_outbound_item
    )

    result = service.add_item(
        outbound_id=10,
        part_id=40,
        quantity=8,
    )

    assert result is persisted_outbound_item

    outbound_repository.get_by_id.assert_called_once_with(
        10
    )

    part_repository.get_by_id.assert_called_once_with(
        40
    )

    outbound_item_repository.list_by_outbound.assert_called_once_with(
        10
    )

    purchase_item_repository.list_available_by_part.assert_called_once_with(
        40
    )

    outbound_item_repository.add.assert_called_once()

    created_outbound_item = (
        outbound_item_repository.add.call_args.args[0]
    )

    assert created_outbound_item.outbound_id == 10
    assert created_outbound_item.part_id == 40
    assert created_outbound_item.quantity == 8

    assert purchase_item.quantity_available == 2

    allocation_repository.add.assert_called_once()

    allocation = (
        allocation_repository.add.call_args.args[0]
    )

    assert allocation.outbound_item_id == 50
    assert allocation.purchase_item_id == 60
    assert allocation.quantity_allocated == 8


def test_should_add_outbound_item_using_fifo_allocation(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
    allocation_repository: Mock,
    purchase_item_repository: Mock,
    part_repository: Mock,
) -> None:
    outbound_repository.get_by_id.return_value = (
        create_outbound()
    )

    part_repository.get_by_id.return_value = (
        create_part()
    )

    outbound_item_repository.list_by_outbound.return_value = (
        []
    )

    first_purchase_item = create_purchase_item(
        purchase_item_id=60,
        quantity_available=3,
    )

    second_purchase_item = create_purchase_item(
        purchase_item_id=61,
        quantity_available=5,
    )

    third_purchase_item = create_purchase_item(
        purchase_item_id=62,
        quantity_available=10,
    )

    purchase_item_repository.list_available_by_part.return_value = [
        first_purchase_item,
        second_purchase_item,
        third_purchase_item,
    ]

    persisted_outbound_item = create_outbound_item(
        outbound_item_id=50,
        quantity=12,
    )

    outbound_item_repository.add.side_effect = None

    outbound_item_repository.add.return_value = (
        persisted_outbound_item
    )

    result = service.add_item(
        outbound_id=10,
        part_id=40,
        quantity=12,
    )

    assert result is persisted_outbound_item

    assert first_purchase_item.quantity_available == 0
    assert second_purchase_item.quantity_available == 0
    assert third_purchase_item.quantity_available == 6

    assert allocation_repository.add.call_count == 3

    allocations = [
        call.args[0]
        for call in allocation_repository.add.call_args_list
    ]

    assert allocations[0].outbound_item_id == 50
    assert allocations[0].purchase_item_id == 60
    assert allocations[0].quantity_allocated == 3

    assert allocations[1].outbound_item_id == 50
    assert allocations[1].purchase_item_id == 61
    assert allocations[1].quantity_allocated == 5

    assert allocations[2].outbound_item_id == 50
    assert allocations[2].purchase_item_id == 62
    assert allocations[2].quantity_allocated == 4


def test_should_use_exact_available_quantity_on_add_item(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
    allocation_repository: Mock,
    purchase_item_repository: Mock,
    part_repository: Mock,
) -> None:
    outbound_repository.get_by_id.return_value = (
        create_outbound()
    )

    part_repository.get_by_id.return_value = (
        create_part()
    )

    outbound_item_repository.list_by_outbound.return_value = (
        []
    )

    first_purchase_item = create_purchase_item(
        purchase_item_id=60,
        quantity_available=3,
    )

    second_purchase_item = create_purchase_item(
        purchase_item_id=61,
        quantity_available=5,
    )

    purchase_item_repository.list_available_by_part.return_value = [
        first_purchase_item,
        second_purchase_item,
    ]

    persisted_outbound_item = create_outbound_item(
        quantity=8,
    )

    outbound_item_repository.add.side_effect = None

    outbound_item_repository.add.return_value = (
        persisted_outbound_item
    )

    service.add_item(
        outbound_id=10,
        part_id=40,
        quantity=8,
    )

    assert first_purchase_item.quantity_available == 0
    assert second_purchase_item.quantity_available == 0

    assert allocation_repository.add.call_count == 2


def test_should_stop_fifo_allocation_after_requested_quantity(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
    allocation_repository: Mock,
    purchase_item_repository: Mock,
    part_repository: Mock,
) -> None:
    outbound_repository.get_by_id.return_value = (
        create_outbound()
    )

    part_repository.get_by_id.return_value = (
        create_part()
    )

    outbound_item_repository.list_by_outbound.return_value = (
        []
    )

    first_purchase_item = create_purchase_item(
        purchase_item_id=60,
        quantity_available=10,
    )

    second_purchase_item = create_purchase_item(
        purchase_item_id=61,
        quantity_available=10,
    )

    purchase_item_repository.list_available_by_part.return_value = [
        first_purchase_item,
        second_purchase_item,
    ]

    outbound_item_repository.add.side_effect = None

    outbound_item_repository.add.return_value = (
        create_outbound_item(
            quantity=4,
        )
    )

    service.add_item(
        outbound_id=10,
        part_id=40,
        quantity=4,
    )

    assert first_purchase_item.quantity_available == 6
    assert second_purchase_item.quantity_available == 10

    allocation_repository.add.assert_called_once()

    allocation = (
        allocation_repository.add.call_args.args[0]
    )

    assert allocation.purchase_item_id == 60
    assert allocation.quantity_allocated == 4


@pytest.mark.parametrize(
    "outbound_id",
    [
        0,
        -1,
    ],
)
def test_should_raise_error_when_outbound_id_is_invalid_on_add_item(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
    allocation_repository: Mock,
    purchase_item_repository: Mock,
    part_repository: Mock,
    outbound_id: int,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "O identificador da saída deve ser "
            "maior que zero."
        ),
    ):
        service.add_item(
            outbound_id=outbound_id,
            part_id=40,
            quantity=5,
        )

    outbound_repository.get_by_id.assert_not_called()
    part_repository.get_by_id.assert_not_called()

    outbound_item_repository.add.assert_not_called()

    purchase_item_repository.list_available_by_part.assert_not_called()

    allocation_repository.add.assert_not_called()


@pytest.mark.parametrize(
    "part_id",
    [
        0,
        -1,
    ],
)
def test_should_raise_error_when_part_id_is_invalid_on_add_item(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
    allocation_repository: Mock,
    purchase_item_repository: Mock,
    part_repository: Mock,
    part_id: int,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "O identificador da peça deve ser "
            "maior que zero."
        ),
    ):
        service.add_item(
            outbound_id=10,
            part_id=part_id,
            quantity=5,
        )

    outbound_repository.get_by_id.assert_not_called()
    part_repository.get_by_id.assert_not_called()

    outbound_item_repository.add.assert_not_called()

    purchase_item_repository.list_available_by_part.assert_not_called()

    allocation_repository.add.assert_not_called()


@pytest.mark.parametrize(
    "quantity",
    [
        0,
        -1,
    ],
)
def test_should_raise_error_when_quantity_is_invalid_on_add_item(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
    allocation_repository: Mock,
    purchase_item_repository: Mock,
    part_repository: Mock,
    quantity: int,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "A quantidade da saída deve ser "
            "maior que zero."
        ),
    ):
        service.add_item(
            outbound_id=10,
            part_id=40,
            quantity=quantity,
        )

    outbound_repository.get_by_id.assert_not_called()
    part_repository.get_by_id.assert_not_called()

    outbound_item_repository.add.assert_not_called()

    purchase_item_repository.list_available_by_part.assert_not_called()

    allocation_repository.add.assert_not_called()


def test_should_raise_error_when_outbound_is_not_found_on_add_item(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
    allocation_repository: Mock,
    purchase_item_repository: Mock,
    part_repository: Mock,
) -> None:
    outbound_repository.get_by_id.return_value = (
        None
    )

    with pytest.raises(
        ValueError,
        match="Saída não encontrada.",
    ):
        service.add_item(
            outbound_id=999,
            part_id=40,
            quantity=5,
        )

    outbound_repository.get_by_id.assert_called_once_with(
        999
    )

    part_repository.get_by_id.assert_not_called()

    outbound_item_repository.add.assert_not_called()

    purchase_item_repository.list_available_by_part.assert_not_called()

    allocation_repository.add.assert_not_called()


def test_should_raise_error_when_outbound_is_cancelled_on_add_item(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
    allocation_repository: Mock,
    purchase_item_repository: Mock,
    part_repository: Mock,
) -> None:
    outbound_repository.get_by_id.return_value = (
        create_outbound(
            status="CANCELLED",
        )
    )

    with pytest.raises(
        ValueError,
        match=(
            "Não é possível adicionar itens "
            "a uma saída cancelada."
        ),
    ):
        service.add_item(
            outbound_id=10,
            part_id=40,
            quantity=5,
        )

    part_repository.get_by_id.assert_not_called()

    outbound_item_repository.add.assert_not_called()

    purchase_item_repository.list_available_by_part.assert_not_called()

    allocation_repository.add.assert_not_called()


def test_should_raise_error_when_part_is_not_found_on_add_item(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
    allocation_repository: Mock,
    purchase_item_repository: Mock,
    part_repository: Mock,
) -> None:
    outbound_repository.get_by_id.return_value = (
        create_outbound()
    )

    part_repository.get_by_id.return_value = (
        None
    )

    with pytest.raises(
        ValueError,
        match="Peça não encontrada.",
    ):
        service.add_item(
            outbound_id=10,
            part_id=999,
            quantity=5,
        )

    part_repository.get_by_id.assert_called_once_with(
        999
    )

    outbound_item_repository.add.assert_not_called()

    purchase_item_repository.list_available_by_part.assert_not_called()

    allocation_repository.add.assert_not_called()


def test_should_raise_error_when_part_is_inactive_on_add_item(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
    allocation_repository: Mock,
    purchase_item_repository: Mock,
    part_repository: Mock,
) -> None:
    outbound_repository.get_by_id.return_value = (
        create_outbound()
    )

    part_repository.get_by_id.return_value = (
        create_part(
            is_active=False,
        )
    )

    with pytest.raises(
        ValueError,
        match=(
            "Não é possível realizar a saída "
            "de uma peça inativa."
        ),
    ):
        service.add_item(
            outbound_id=10,
            part_id=40,
            quantity=5,
        )

    outbound_item_repository.add.assert_not_called()

    purchase_item_repository.list_available_by_part.assert_not_called()

    allocation_repository.add.assert_not_called()


def test_should_raise_error_when_part_is_already_in_outbound(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
    allocation_repository: Mock,
    purchase_item_repository: Mock,
    part_repository: Mock,
) -> None:
    outbound_repository.get_by_id.return_value = (
        create_outbound()
    )

    part_repository.get_by_id.return_value = (
        create_part()
    )

    outbound_item_repository.list_by_outbound.return_value = [
        create_outbound_item(
            part_id=40,
        )
    ]

    with pytest.raises(
        ValueError,
        match=(
            "Esta peça já foi adicionada à saída."
        ),
    ):
        service.add_item(
            outbound_id=10,
            part_id=40,
            quantity=5,
        )

    outbound_item_repository.list_by_outbound.assert_called_once_with(
        10
    )

    purchase_item_repository.list_available_by_part.assert_not_called()

    outbound_item_repository.add.assert_not_called()

    allocation_repository.add.assert_not_called()


def test_should_allow_different_part_in_same_outbound(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
    allocation_repository: Mock,
    purchase_item_repository: Mock,
    part_repository: Mock,
) -> None:
    outbound_repository.get_by_id.return_value = (
        create_outbound()
    )

    part_repository.get_by_id.return_value = (
        create_part(
            part_id=41,
        )
    )

    outbound_item_repository.list_by_outbound.return_value = [
        create_outbound_item(
            part_id=40,
        )
    ]

    purchase_item = create_purchase_item(
        purchase_item_id=60,
        part_id=41,
        quantity_available=10,
    )

    purchase_item_repository.list_available_by_part.return_value = [
        purchase_item
    ]

    outbound_item_repository.add.side_effect = None

    outbound_item_repository.add.return_value = (
        create_outbound_item(
            part_id=41,
            quantity=5,
        )
    )

    result = service.add_item(
        outbound_id=10,
        part_id=41,
        quantity=5,
    )

    assert result.part_id == 41
    assert purchase_item.quantity_available == 5

    outbound_item_repository.add.assert_called_once()
    allocation_repository.add.assert_called_once()


def test_should_raise_error_when_stock_is_insufficient(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
    allocation_repository: Mock,
    purchase_item_repository: Mock,
    part_repository: Mock,
) -> None:
    outbound_repository.get_by_id.return_value = (
        create_outbound()
    )

    part_repository.get_by_id.return_value = (
        create_part()
    )

    outbound_item_repository.list_by_outbound.return_value = (
        []
    )

    first_purchase_item = create_purchase_item(
        purchase_item_id=60,
        quantity_available=2,
    )

    second_purchase_item = create_purchase_item(
        purchase_item_id=61,
        quantity_available=3,
    )

    purchase_item_repository.list_available_by_part.return_value = [
        first_purchase_item,
        second_purchase_item,
    ]

    with pytest.raises(
        ValueError,
        match=(
            "Quantidade disponível insuficiente "
            "para a saída."
        ),
    ):
        service.add_item(
            outbound_id=10,
            part_id=40,
            quantity=6,
        )

    assert first_purchase_item.quantity_available == 2
    assert second_purchase_item.quantity_available == 3

    outbound_item_repository.add.assert_not_called()

    allocation_repository.add.assert_not_called()


def test_should_raise_error_when_no_stock_is_available(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
    allocation_repository: Mock,
    purchase_item_repository: Mock,
    part_repository: Mock,
) -> None:
    outbound_repository.get_by_id.return_value = (
        create_outbound()
    )

    part_repository.get_by_id.return_value = (
        create_part()
    )

    outbound_item_repository.list_by_outbound.return_value = (
        []
    )

    purchase_item_repository.list_available_by_part.return_value = (
        []
    )

    with pytest.raises(
        ValueError,
        match=(
            "Quantidade disponível insuficiente "
            "para a saída."
        ),
    ):
        service.add_item(
            outbound_id=10,
            part_id=40,
            quantity=1,
        )

    outbound_item_repository.add.assert_not_called()

    allocation_repository.add.assert_not_called()


def test_should_raise_error_when_fifo_allocation_is_incomplete(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
    allocation_repository: Mock,
    purchase_item_repository: Mock,
    part_repository: Mock,
) -> None:
    outbound_repository.get_by_id.return_value = (
        create_outbound()
    )

    part_repository.get_by_id.return_value = (
        create_part()
    )

    outbound_item_repository.list_by_outbound.return_value = (
        []
    )

    purchase_item = create_purchase_item(
        purchase_item_id=60,
        quantity_available=10,
    )

    purchase_item_repository.list_available_by_part.return_value = [
        purchase_item
    ]

    persisted_outbound_item = create_outbound_item(
        quantity=8,
    )

    outbound_item_repository.add.side_effect = None

    outbound_item_repository.add.return_value = (
        persisted_outbound_item
    )

    def prevent_quantity_reduction(
        allocation: object,
    ) -> object:
        purchase_item.quantity_available = 0
        return allocation

    allocation_repository.add.side_effect = (
        prevent_quantity_reduction
    )

    result = service.add_item(
        outbound_id=10,
        part_id=40,
        quantity=8,
    )

    assert result is persisted_outbound_item

    allocation_repository.add.assert_called_once()

def test_should_get_outbound(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbound = create_outbound()

    outbound_repository.get_by_id.return_value = (
        outbound
    )

    result = service.get_outbound(
        10
    )

    assert result is outbound

    outbound_repository.get_by_id.assert_called_once_with(
        10
    )


@pytest.mark.parametrize(
    "outbound_id",
    [
        0,
        -1,
    ],
)
def test_should_raise_error_when_outbound_id_is_invalid_on_get(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_id: int,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "O identificador da saída deve ser "
            "maior que zero."
        ),
    ):
        service.get_outbound(
            outbound_id
        )

    outbound_repository.get_by_id.assert_not_called()


def test_should_raise_error_when_outbound_is_not_found_on_get(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbound_repository.get_by_id.return_value = (
        None
    )

    with pytest.raises(
        ValueError,
        match="Saída não encontrada.",
    ):
        service.get_outbound(
            999
        )

    outbound_repository.get_by_id.assert_called_once_with(
        999
    )


def test_should_list_all_outbounds(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbounds = [
        create_outbound(
            outbound_id=10,
        ),
        create_outbound(
            outbound_id=11,
            work_order_number=None,
            sales_invoice_number="NFV-67890",
        ),
    ]

    outbound_repository.list_all.return_value = (
        outbounds
    )

    result = service.list_outbounds()

    assert result is outbounds

    outbound_repository.list_all.assert_called_once_with()

    outbound_repository.list_by_status.assert_not_called()

    outbound_repository.list_by_destination_type.assert_not_called()


def test_should_return_empty_outbound_list(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbound_repository.list_all.return_value = []

    result = service.list_outbounds()

    assert result == []

    outbound_repository.list_all.assert_called_once_with()


def test_should_list_outbounds_filtered_by_status(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbounds = [
        create_outbound(
            outbound_id=10,
            status="ACTIVE",
        ),
    ]

    outbound_repository.list_by_status.return_value = (
        outbounds
    )

    result = service.list_outbounds(
        status="  active  ",
    )

    assert result is outbounds

    outbound_repository.list_by_status.assert_called_once_with(
        "ACTIVE"
    )

    outbound_repository.list_all.assert_not_called()

    outbound_repository.list_by_destination_type.assert_not_called()


def test_should_list_outbounds_filtered_by_destination_type(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbounds = [
        create_outbound(
            outbound_id=10,
            destination_type="WORK_ORDER",
        ),
    ]

    outbound_repository.list_by_destination_type.return_value = (
        outbounds
    )

    result = service.list_outbounds(
        destination_type="  WORK_ORDER  ",
    )

    assert result is outbounds

    outbound_repository.list_by_destination_type.assert_called_once_with(
        "WORK_ORDER"
    )

    outbound_repository.list_all.assert_not_called()

    outbound_repository.list_by_status.assert_not_called()


def test_should_raise_error_when_multiple_filters_are_sent(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    with pytest.raises(
        ValueError,
        match="Informe apenas um filtro por vez.",
    ):
        service.list_outbounds(
            status="ACTIVE",
            destination_type="WORK_ORDER",
        )

    outbound_repository.list_all.assert_not_called()

    outbound_repository.list_by_status.assert_not_called()

    outbound_repository.list_by_destination_type.assert_not_called()


@pytest.mark.parametrize(
    "status",
    [
        "",
        "   ",
        "PENDING",
        "FINISHED",
        "INVALID",
    ],
)
def test_should_raise_error_when_status_filter_is_invalid(
    service: OutboundService,
    outbound_repository: Mock,
    status: str,
) -> None:
    expected_message = (
        "O status da saída é obrigatório."
        if not status.strip()
        else "Status de saída inválido."
    )

    with pytest.raises(
        ValueError,
        match=expected_message,
    ):
        service.list_outbounds(
            status=status,
        )

    outbound_repository.list_all.assert_not_called()

    outbound_repository.list_by_status.assert_not_called()

    outbound_repository.list_by_destination_type.assert_not_called()


@pytest.mark.parametrize(
    "destination_type",
    [
        "",
        "   ",
    ],
)
def test_should_raise_error_when_destination_type_filter_is_blank(
    service: OutboundService,
    outbound_repository: Mock,
    destination_type: str,
) -> None:
    with pytest.raises(
        ValueError,
        match="O tipo de destino é obrigatório.",
    ):
        service.list_outbounds(
            destination_type=destination_type,
        )

    outbound_repository.list_all.assert_not_called()

    outbound_repository.list_by_status.assert_not_called()

    outbound_repository.list_by_destination_type.assert_not_called()


def test_should_list_outbounds_by_status(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbounds = [
        create_outbound(
            outbound_id=10,
            status="CANCELLED",
        ),
    ]

    outbound_repository.list_by_status.return_value = (
        outbounds
    )

    result = service.list_outbounds_by_status(
        "  cancelled  "
    )

    assert result is outbounds

    outbound_repository.list_by_status.assert_called_once_with(
        "CANCELLED"
    )


@pytest.mark.parametrize(
    "status",
    [
        "",
        "   ",
        "PENDING",
        "FINISHED",
        "INVALID",
    ],
)
def test_should_raise_error_when_status_is_invalid_on_list_by_status(
    service: OutboundService,
    outbound_repository: Mock,
    status: str,
) -> None:
    expected_message = (
        "O status da saída é obrigatório."
        if not status.strip()
        else "Status de saída inválido."
    )

    with pytest.raises(
        ValueError,
        match=expected_message,
    ):
        service.list_outbounds_by_status(
            status
        )

    outbound_repository.list_by_status.assert_not_called()


def test_should_list_outbounds_by_destination_type(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbounds = [
        create_outbound(
            outbound_id=10,
            destination_type="SALE",
            work_order_number=None,
            sales_invoice_number="NFV-12345",
        ),
    ]

    outbound_repository.list_by_destination_type.return_value = (
        outbounds
    )

    result = service.list_outbounds_by_destination_type(
        "  SALE  "
    )

    assert result is outbounds

    outbound_repository.list_by_destination_type.assert_called_once_with(
        "SALE"
    )


@pytest.mark.parametrize(
    "destination_type",
    [
        "",
        "   ",
    ],
)
def test_should_raise_error_when_destination_type_is_blank_on_list(
    service: OutboundService,
    outbound_repository: Mock,
    destination_type: str,
) -> None:
    with pytest.raises(
        ValueError,
        match="O tipo de destino é obrigatório.",
    ):
        service.list_outbounds_by_destination_type(
            destination_type
        )

    outbound_repository.list_by_destination_type.assert_not_called()


def test_should_list_outbound_items(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
) -> None:
    outbound = create_outbound()

    items = [
        create_outbound_item(
            outbound_item_id=50,
            part_id=40,
            quantity=5,
        ),
        create_outbound_item(
            outbound_item_id=51,
            part_id=41,
            quantity=3,
        ),
    ]

    outbound_repository.get_by_id.return_value = (
        outbound
    )

    outbound_item_repository.list_by_outbound.return_value = (
        items
    )

    result = service.list_outbound_items(
        10
    )

    assert result is items

    outbound_repository.get_by_id.assert_called_once_with(
        10
    )

    outbound_item_repository.list_by_outbound.assert_called_once_with(
        10
    )


def test_should_return_empty_outbound_item_list(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
) -> None:
    outbound_repository.get_by_id.return_value = (
        create_outbound()
    )

    outbound_item_repository.list_by_outbound.return_value = (
        []
    )

    result = service.list_outbound_items(
        10
    )

    assert result == []

    outbound_item_repository.list_by_outbound.assert_called_once_with(
        10
    )


@pytest.mark.parametrize(
    "outbound_id",
    [
        0,
        -1,
    ],
)
def test_should_raise_error_when_outbound_id_is_invalid_on_list_items(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
    outbound_id: int,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "O identificador da saída deve ser "
            "maior que zero."
        ),
    ):
        service.list_outbound_items(
            outbound_id
        )

    outbound_repository.get_by_id.assert_not_called()

    outbound_item_repository.list_by_outbound.assert_not_called()


def test_should_raise_error_when_outbound_is_not_found_on_list_items(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
) -> None:
    outbound_repository.get_by_id.return_value = (
        None
    )

    with pytest.raises(
        ValueError,
        match="Saída não encontrada.",
    ):
        service.list_outbound_items(
            999
        )

    outbound_repository.get_by_id.assert_called_once_with(
        999
    )

    outbound_item_repository.list_by_outbound.assert_not_called()

def create_allocation(
    allocation_id: int = 70,
    outbound_item_id: int = 50,
    purchase_item_id: int = 60,
    quantity_allocated: int = 5,
) -> SimpleNamespace:
    return SimpleNamespace(
        id=allocation_id,
        outbound_item_id=outbound_item_id,
        purchase_item_id=purchase_item_id,
        quantity_allocated=quantity_allocated,
    )


def test_should_update_outbound_destination_type(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbound = create_outbound()

    outbound_repository.get_by_id.return_value = (
        outbound
    )

    result = service.update_outbound(
        outbound_id=10,
        destination_type="  INTERNAL_USE  ",
    )

    assert result is outbound
    assert outbound.destination_type == "INTERNAL_USE"

    outbound_repository.get_by_id.assert_called_once_with(
        10
    )

    outbound_repository.save.assert_called_once_with(
        outbound
    )

    outbound_repository.get_by_work_order_number.assert_not_called()

    outbound_repository.get_by_sales_invoice_number.assert_not_called()


def test_should_update_outbound_work_order_number(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbound = create_outbound(
        work_order_number="OS-12345",
    )

    outbound_repository.get_by_id.return_value = (
        outbound
    )

    outbound_repository.get_by_work_order_number.return_value = (
        None
    )

    result = service.update_outbound(
        outbound_id=10,
        work_order_number="  OS-67890  ",
    )

    assert result is outbound

    assert (
        outbound.work_order_number
        == "OS-67890"
    )

    outbound_repository.get_by_work_order_number.assert_called_once_with(
        "OS-67890"
    )

    outbound_repository.save.assert_called_once_with(
        outbound
    )


def test_should_update_outbound_sales_invoice_number(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbound = create_outbound(
        work_order_number=None,
        sales_invoice_number="NFV-12345",
        destination_type="SALE",
    )

    outbound_repository.get_by_id.return_value = (
        outbound
    )

    outbound_repository.get_by_sales_invoice_number.return_value = (
        None
    )

    result = service.update_outbound(
        outbound_id=10,
        sales_invoice_number="  NFV-67890  ",
    )

    assert result is outbound

    assert (
        outbound.sales_invoice_number
        == "NFV-67890"
    )

    outbound_repository.get_by_sales_invoice_number.assert_called_once_with(
        "NFV-67890"
    )

    outbound_repository.save.assert_called_once_with(
        outbound
    )


def test_should_update_all_outbound_fields(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbound = create_outbound(
        destination_type="WORK_ORDER",
        work_order_number="OS-12345",
        sales_invoice_number=None,
    )

    outbound_repository.get_by_id.return_value = (
        outbound
    )

    outbound_repository.get_by_work_order_number.return_value = (
        None
    )

    outbound_repository.get_by_sales_invoice_number.return_value = (
        None
    )

    result = service.update_outbound(
        outbound_id=10,
        destination_type="  SALE  ",
        work_order_number="  OS-67890  ",
        sales_invoice_number="  NFV-67890  ",
        status="  active  ",
    )

    assert result is outbound

    assert outbound.destination_type == "SALE"

    assert (
        outbound.work_order_number
        == "OS-67890"
    )

    assert (
        outbound.sales_invoice_number
        == "NFV-67890"
    )

    assert outbound.status == "ACTIVE"

    outbound_repository.get_by_work_order_number.assert_called_once_with(
        "OS-67890"
    )

    outbound_repository.get_by_sales_invoice_number.assert_called_once_with(
        "NFV-67890"
    )

    outbound_repository.save.assert_called_once_with(
        outbound
    )


def test_should_return_repository_result_on_update(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbound = create_outbound()

    persisted_outbound = create_outbound(
        outbound_id=10,
        destination_type="INTERNAL_USE",
    )

    outbound_repository.get_by_id.return_value = (
        outbound
    )

    outbound_repository.save.side_effect = None

    outbound_repository.save.return_value = (
        persisted_outbound
    )

    result = service.update_outbound(
        outbound_id=10,
        destination_type="INTERNAL_USE",
    )

    assert result is persisted_outbound

    outbound_repository.save.assert_called_once_with(
        outbound
    )


def test_should_save_outbound_when_no_update_field_is_sent(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbound = create_outbound()

    outbound_repository.get_by_id.return_value = (
        outbound
    )

    result = service.update_outbound(
        outbound_id=10,
    )

    assert result is outbound

    assert outbound.destination_type == "WORK_ORDER"
    assert outbound.work_order_number == "OS-12345"
    assert outbound.sales_invoice_number is None
    assert outbound.status == "ACTIVE"

    outbound_repository.save.assert_called_once_with(
        outbound
    )


@pytest.mark.parametrize(
    "outbound_id",
    [
        0,
        -1,
    ],
)
def test_should_raise_error_when_outbound_id_is_invalid_on_update(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_id: int,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "O identificador da saída deve ser "
            "maior que zero."
        ),
    ):
        service.update_outbound(
            outbound_id=outbound_id,
            destination_type="SALE",
        )

    outbound_repository.get_by_id.assert_not_called()

    outbound_repository.save.assert_not_called()


def test_should_raise_error_when_outbound_is_not_found_on_update(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbound_repository.get_by_id.return_value = (
        None
    )

    with pytest.raises(
        ValueError,
        match="Saída não encontrada.",
    ):
        service.update_outbound(
            outbound_id=999,
            destination_type="SALE",
        )

    outbound_repository.get_by_id.assert_called_once_with(
        999
    )

    outbound_repository.save.assert_not_called()


def test_should_raise_error_when_outbound_is_cancelled_on_update(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbound_repository.get_by_id.return_value = (
        create_outbound(
            status="CANCELLED",
        )
    )

    with pytest.raises(
        ValueError,
        match=(
            "Não é possível alterar uma saída "
            "cancelada."
        ),
    ):
        service.update_outbound(
            outbound_id=10,
            destination_type="SALE",
        )

    outbound_repository.save.assert_not_called()

    outbound_repository.get_by_work_order_number.assert_not_called()

    outbound_repository.get_by_sales_invoice_number.assert_not_called()


def test_should_raise_error_when_destination_type_is_blank_on_update(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbound_repository.get_by_id.return_value = (
        create_outbound()
    )

    with pytest.raises(
        ValueError,
        match="O tipo de destino é obrigatório.",
    ):
        service.update_outbound(
            outbound_id=10,
            destination_type="   ",
        )

    outbound_repository.save.assert_not_called()


def test_should_convert_blank_work_order_to_none_on_update(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbound = create_outbound(
        work_order_number="OS-12345",
        sales_invoice_number="NFV-12345",
    )

    outbound_repository.get_by_id.return_value = (
        outbound
    )

    result = service.update_outbound(
        outbound_id=10,
        work_order_number="   ",
    )

    assert result is outbound
    assert outbound.work_order_number is None

    assert (
        outbound.sales_invoice_number
        == "NFV-12345"
    )

    outbound_repository.get_by_work_order_number.assert_not_called()

    outbound_repository.save.assert_called_once_with(
        outbound
    )


def test_should_convert_blank_sales_invoice_to_none_on_update(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbound = create_outbound(
        work_order_number="OS-12345",
        sales_invoice_number="NFV-12345",
    )

    outbound_repository.get_by_id.return_value = (
        outbound
    )

    result = service.update_outbound(
        outbound_id=10,
        sales_invoice_number="   ",
    )

    assert result is outbound

    assert outbound.work_order_number == "OS-12345"
    assert outbound.sales_invoice_number is None

    outbound_repository.get_by_sales_invoice_number.assert_not_called()

    outbound_repository.save.assert_called_once_with(
        outbound
    )


def test_should_raise_error_when_update_removes_all_reference_numbers(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbound = create_outbound(
        work_order_number="OS-12345",
        sales_invoice_number=None,
    )

    outbound_repository.get_by_id.return_value = (
        outbound
    )

    with pytest.raises(
        ValueError,
        match=(
            "A saída deve possuir uma ordem de serviço "
            "ou uma nota fiscal de venda."
        ),
    ):
        service.update_outbound(
            outbound_id=10,
            work_order_number="   ",
        )

    assert outbound.work_order_number is None
    assert outbound.sales_invoice_number is None

    outbound_repository.save.assert_not_called()


def test_should_raise_error_when_updated_work_order_is_duplicated(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbound = create_outbound(
        outbound_id=10,
        work_order_number="OS-12345",
    )

    duplicated_outbound = create_outbound(
        outbound_id=11,
        work_order_number="OS-67890",
    )

    outbound_repository.get_by_id.return_value = (
        outbound
    )

    outbound_repository.get_by_work_order_number.return_value = (
        duplicated_outbound
    )

    with pytest.raises(
        ValueError,
        match=(
            "Já existe uma saída com esta "
            "ordem de serviço."
        ),
    ):
        service.update_outbound(
            outbound_id=10,
            work_order_number="OS-67890",
        )

    outbound_repository.get_by_work_order_number.assert_called_once_with(
        "OS-67890"
    )

    outbound_repository.save.assert_not_called()


def test_should_allow_same_work_order_on_same_outbound(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbound = create_outbound(
        outbound_id=10,
        work_order_number="OS-12345",
    )

    outbound_repository.get_by_id.return_value = (
        outbound
    )

    outbound_repository.get_by_work_order_number.return_value = (
        outbound
    )

    result = service.update_outbound(
        outbound_id=10,
        work_order_number="OS-12345",
    )

    assert result is outbound

    outbound_repository.get_by_work_order_number.assert_called_once_with(
        "OS-12345"
    )

    outbound_repository.save.assert_called_once_with(
        outbound
    )


def test_should_raise_error_when_updated_sales_invoice_is_duplicated(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbound = create_outbound(
        outbound_id=10,
        sales_invoice_number=None,
    )

    duplicated_outbound = create_outbound(
        outbound_id=11,
        work_order_number=None,
        sales_invoice_number="NFV-67890",
        destination_type="SALE",
    )

    outbound_repository.get_by_id.return_value = (
        outbound
    )

    outbound_repository.get_by_sales_invoice_number.return_value = (
        duplicated_outbound
    )

    with pytest.raises(
        ValueError,
        match=(
            "Já existe uma saída com esta "
            "nota fiscal de venda."
        ),
    ):
        service.update_outbound(
            outbound_id=10,
            sales_invoice_number="NFV-67890",
        )

    outbound_repository.get_by_sales_invoice_number.assert_called_once_with(
        "NFV-67890"
    )

    outbound_repository.save.assert_not_called()


def test_should_allow_same_sales_invoice_on_same_outbound(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbound = create_outbound(
        outbound_id=10,
        work_order_number=None,
        sales_invoice_number="NFV-12345",
        destination_type="SALE",
    )

    outbound_repository.get_by_id.return_value = (
        outbound
    )

    outbound_repository.get_by_sales_invoice_number.return_value = (
        outbound
    )

    result = service.update_outbound(
        outbound_id=10,
        sales_invoice_number="NFV-12345",
    )

    assert result is outbound

    outbound_repository.get_by_sales_invoice_number.assert_called_once_with(
        "NFV-12345"
    )

    outbound_repository.save.assert_called_once_with(
        outbound
    )


@pytest.mark.parametrize(
    "status",
    [
        "",
        "   ",
        "PENDING",
        "FINISHED",
        "INVALID",
    ],
)
def test_should_raise_error_when_status_is_invalid_on_update(
    service: OutboundService,
    outbound_repository: Mock,
    status: str,
) -> None:
    outbound_repository.get_by_id.return_value = (
        create_outbound()
    )

    expected_message = (
        "O status da saída é obrigatório."
        if not status.strip()
        else "Status de saída inválido."
    )

    with pytest.raises(
        ValueError,
        match=expected_message,
    ):
        service.update_outbound(
            outbound_id=10,
            status=status,
        )

    outbound_repository.save.assert_not_called()


def test_should_raise_error_when_status_cancelled_is_used_on_update(
    service: OutboundService,
    outbound_repository: Mock,
) -> None:
    outbound_repository.get_by_id.return_value = (
        create_outbound()
    )

    with pytest.raises(
        ValueError,
        match=(
            "Utilize a operação específica "
            "para cancelar a saída."
        ),
    ):
        service.update_outbound(
            outbound_id=10,
            status="CANCELLED",
        )

    outbound_repository.save.assert_not_called()


def test_should_cancel_outbound_without_items(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
    allocation_repository: Mock,
    purchase_item_repository: Mock,
) -> None:
    outbound = create_outbound()

    outbound_repository.get_by_id.return_value = (
        outbound
    )

    outbound_item_repository.list_by_outbound.return_value = (
        []
    )

    result = service.cancel_outbound(
        10
    )

    assert result is outbound
    assert outbound.status == "CANCELLED"

    outbound_repository.get_by_id.assert_called_once_with(
        10
    )

    outbound_item_repository.list_by_outbound.assert_called_once_with(
        10
    )

    allocation_repository.list_by_outbound_item.assert_not_called()

    purchase_item_repository.get_by_id.assert_not_called()

    outbound_repository.save.assert_called_once_with(
        outbound
    )


def test_should_cancel_outbound_and_restore_single_allocation(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
    allocation_repository: Mock,
    purchase_item_repository: Mock,
) -> None:
    outbound = create_outbound()

    outbound_item = create_outbound_item(
        outbound_item_id=50,
        quantity=5,
    )

    allocation = create_allocation(
        outbound_item_id=50,
        purchase_item_id=60,
        quantity_allocated=5,
    )

    purchase_item = create_purchase_item(
        purchase_item_id=60,
        quantity_available=2,
    )

    outbound_repository.get_by_id.return_value = (
        outbound
    )

    outbound_item_repository.list_by_outbound.return_value = [
        outbound_item
    ]

    allocation_repository.list_by_outbound_item.return_value = [
        allocation
    ]

    purchase_item_repository.get_by_id.return_value = (
        purchase_item
    )

    result = service.cancel_outbound(
        10
    )

    assert result is outbound
    assert outbound.status == "CANCELLED"

    assert purchase_item.quantity_available == 7

    allocation_repository.list_by_outbound_item.assert_called_once_with(
        50
    )

    purchase_item_repository.get_by_id.assert_called_once_with(
        60
    )

    outbound_repository.save.assert_called_once_with(
        outbound
    )


def test_should_cancel_outbound_and_restore_multiple_allocations(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
    allocation_repository: Mock,
    purchase_item_repository: Mock,
) -> None:
    outbound = create_outbound()

    first_outbound_item = create_outbound_item(
        outbound_item_id=50,
        part_id=40,
        quantity=8,
    )

    second_outbound_item = create_outbound_item(
        outbound_item_id=51,
        part_id=41,
        quantity=4,
    )

    first_allocation = create_allocation(
        allocation_id=70,
        outbound_item_id=50,
        purchase_item_id=60,
        quantity_allocated=3,
    )

    second_allocation = create_allocation(
        allocation_id=71,
        outbound_item_id=50,
        purchase_item_id=61,
        quantity_allocated=5,
    )

    third_allocation = create_allocation(
        allocation_id=72,
        outbound_item_id=51,
        purchase_item_id=62,
        quantity_allocated=4,
    )

    first_purchase_item = create_purchase_item(
        purchase_item_id=60,
        part_id=40,
        quantity_available=0,
    )

    second_purchase_item = create_purchase_item(
        purchase_item_id=61,
        part_id=40,
        quantity_available=2,
    )

    third_purchase_item = create_purchase_item(
        purchase_item_id=62,
        part_id=41,
        quantity_available=1,
    )

    outbound_repository.get_by_id.return_value = (
        outbound
    )

    outbound_item_repository.list_by_outbound.return_value = [
        first_outbound_item,
        second_outbound_item,
    ]

    allocation_repository.list_by_outbound_item.side_effect = [
        [
            first_allocation,
            second_allocation,
        ],
        [
            third_allocation,
        ],
    ]

    purchase_items_by_id = {
        60: first_purchase_item,
        61: second_purchase_item,
        62: third_purchase_item,
    }

    purchase_item_repository.get_by_id.side_effect = (
        lambda purchase_item_id: purchase_items_by_id[
            purchase_item_id
        ]
    )

    result = service.cancel_outbound(
        10
    )

    assert result is outbound
    assert outbound.status == "CANCELLED"

    assert first_purchase_item.quantity_available == 3
    assert second_purchase_item.quantity_available == 7
    assert third_purchase_item.quantity_available == 5

    assert (
        allocation_repository
        .list_by_outbound_item.call_count
        == 2
    )

    allocation_repository.list_by_outbound_item.assert_any_call(
        50
    )

    allocation_repository.list_by_outbound_item.assert_any_call(
        51
    )

    assert purchase_item_repository.get_by_id.call_count == 3

    purchase_item_repository.get_by_id.assert_any_call(
        60
    )

    purchase_item_repository.get_by_id.assert_any_call(
        61
    )

    purchase_item_repository.get_by_id.assert_any_call(
        62
    )

    outbound_repository.save.assert_called_once_with(
        outbound
    )


def test_should_cancel_outbound_item_without_allocations(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
    allocation_repository: Mock,
    purchase_item_repository: Mock,
) -> None:
    outbound = create_outbound()

    outbound_item = create_outbound_item()

    outbound_repository.get_by_id.return_value = (
        outbound
    )

    outbound_item_repository.list_by_outbound.return_value = [
        outbound_item
    ]

    allocation_repository.list_by_outbound_item.return_value = (
        []
    )

    result = service.cancel_outbound(
        10
    )

    assert result is outbound
    assert outbound.status == "CANCELLED"

    allocation_repository.list_by_outbound_item.assert_called_once_with(
        50
    )

    purchase_item_repository.get_by_id.assert_not_called()

    outbound_repository.save.assert_called_once_with(
        outbound
    )


def test_should_return_repository_result_on_cancel(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
) -> None:
    outbound = create_outbound()

    persisted_outbound = create_outbound(
        status="CANCELLED",
    )

    outbound_repository.get_by_id.return_value = (
        outbound
    )

    outbound_item_repository.list_by_outbound.return_value = (
        []
    )

    outbound_repository.save.side_effect = None

    outbound_repository.save.return_value = (
        persisted_outbound
    )

    result = service.cancel_outbound(
        10
    )

    assert result is persisted_outbound
    assert outbound.status == "CANCELLED"

    outbound_repository.save.assert_called_once_with(
        outbound
    )


@pytest.mark.parametrize(
    "outbound_id",
    [
        0,
        -1,
    ],
)
def test_should_raise_error_when_outbound_id_is_invalid_on_cancel(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
    outbound_id: int,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "O identificador da saída deve ser "
            "maior que zero."
        ),
    ):
        service.cancel_outbound(
            outbound_id
        )

    outbound_repository.get_by_id.assert_not_called()

    outbound_item_repository.list_by_outbound.assert_not_called()

    outbound_repository.save.assert_not_called()


def test_should_raise_error_when_outbound_is_not_found_on_cancel(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
) -> None:
    outbound_repository.get_by_id.return_value = (
        None
    )

    with pytest.raises(
        ValueError,
        match="Saída não encontrada.",
    ):
        service.cancel_outbound(
            999
        )

    outbound_repository.get_by_id.assert_called_once_with(
        999
    )

    outbound_item_repository.list_by_outbound.assert_not_called()

    outbound_repository.save.assert_not_called()


def test_should_raise_error_when_outbound_is_already_cancelled(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
) -> None:
    outbound_repository.get_by_id.return_value = (
        create_outbound(
            status="CANCELLED",
        )
    )

    with pytest.raises(
        ValueError,
        match="A saída já está cancelada.",
    ):
        service.cancel_outbound(
            10
        )

    outbound_item_repository.list_by_outbound.assert_not_called()

    outbound_repository.save.assert_not_called()


def test_should_raise_error_when_purchase_item_is_not_found_on_cancel(
    service: OutboundService,
    outbound_repository: Mock,
    outbound_item_repository: Mock,
    allocation_repository: Mock,
    purchase_item_repository: Mock,
) -> None:
    outbound = create_outbound()

    outbound_item = create_outbound_item(
        outbound_item_id=50,
    )

    allocation = create_allocation(
        outbound_item_id=50,
        purchase_item_id=999,
        quantity_allocated=5,
    )

    outbound_repository.get_by_id.return_value = (
        outbound
    )

    outbound_item_repository.list_by_outbound.return_value = [
        outbound_item
    ]

    allocation_repository.list_by_outbound_item.return_value = [
        allocation
    ]

    purchase_item_repository.get_by_id.return_value = (
        None
    )

    with pytest.raises(
        ValueError,
        match=(
            "Item de compra relacionado "
            "à saída não encontrado."
        ),
    ):
        service.cancel_outbound(
            10
        )

    purchase_item_repository.get_by_id.assert_called_once_with(
        999
    )

    assert outbound.status == "ACTIVE"

    outbound_repository.save.assert_not_called()
```

## `tests\services\test_part_service.py`

```python
from unittest.mock import Mock

import pytest

from src.models.part import Part
from src.models.supplier import Supplier
from src.services.part_service import PartService


@pytest.fixture
def part_repository() -> Mock:
    """Repository de peças simulado."""

    return Mock()


@pytest.fixture
def supplier_repository() -> Mock:
    """Repository de fornecedores simulado."""

    return Mock()


@pytest.fixture
def service(
    part_repository: Mock,
    supplier_repository: Mock,
) -> PartService:
    """Service de peças com dependências simuladas."""

    return PartService(
        part_repository=part_repository,
        supplier_repository=supplier_repository,
    )


def create_supplier(
    supplier_id: int = 1,
    name: str = "Fornecedor Teste",
    is_active: int = 1,
) -> Supplier:
    """Cria um fornecedor para utilização nos testes."""

    return Supplier(
        id=supplier_id,
        name=name,
        document="12345678000199",
        address="Registro/SP",
        notes=None,
        is_active=is_active,
    )


def create_part(
    part_id: int = 10,
    supplier_id: int = 1,
    part_code: str = "ABC123",
    name: str = "Motor de partida",
    description: str | None = "Peça remanufaturada",
    return_deadline_days: int = 90,
    is_active: int = 1,
) -> Part:
    """Cria uma peça para utilização nos testes."""

    return Part(
        id=part_id,
        supplier_id=supplier_id,
        part_code=part_code,
        name=name,
        description=description,
        return_deadline_days=return_deadline_days,
        is_active=is_active,
    )


def test_should_create_part(
    service: PartService,
    part_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )

    part_repository.get_by_supplier_and_code.return_value = (
        None
    )

    part_repository.add.side_effect = (
        lambda part: part
    )

    part = service.create(
        supplier_id=1,
        part_code="ABC123",
        name="Motor de partida",
        description="Peça remanufaturada",
        return_deadline_days=90,
    )

    assert part.supplier_id == 1
    assert part.part_code == "ABC123"
    assert part.name == "Motor de partida"
    assert part.description == "Peça remanufaturada"
    assert part.return_deadline_days == 90
    assert part.is_active == 1

    supplier_repository.get_by_id.assert_called_once_with(
        1
    )

    (
        part_repository
        .get_by_supplier_and_code
        .assert_called_once_with(
            1,
            "ABC123",
        )
    )

    part_repository.add.assert_called_once_with(
        part
    )


def test_should_normalize_fields_when_creating_part(
    service: PartService,
    part_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )

    part_repository.get_by_supplier_and_code.return_value = (
        None
    )

    part_repository.add.side_effect = (
        lambda part: part
    )

    part = service.create(
        supplier_id=1,
        part_code="  ABC123  ",
        name="  Motor de partida  ",
        description="  Peça remanufaturada  ",
        return_deadline_days=90,
    )

    assert part.part_code == "ABC123"
    assert part.name == "Motor de partida"
    assert part.description == "Peça remanufaturada"

    (
        part_repository
        .get_by_supplier_and_code
        .assert_called_once_with(
            1,
            "ABC123",
        )
    )


def test_should_convert_empty_description_to_none(
    service: PartService,
    part_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )

    part_repository.get_by_supplier_and_code.return_value = (
        None
    )

    part_repository.add.side_effect = (
        lambda part: part
    )

    part = service.create(
        supplier_id=1,
        part_code="ABC123",
        name="Motor de partida",
        description="   ",
        return_deadline_days=90,
    )

    assert part.description is None


def test_should_raise_when_supplier_does_not_exist(
    service: PartService,
    part_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier_repository.get_by_id.return_value = None

    with pytest.raises(
        ValueError,
        match="Fornecedor não encontrado.",
    ):
        service.create(
            supplier_id=1,
            part_code="ABC123",
            name="Motor de partida",
            return_deadline_days=90,
        )

    part_repository.add.assert_not_called()


def test_should_raise_when_supplier_is_inactive(
    service: PartService,
    part_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier_repository.get_by_id.return_value = (
        create_supplier(
            is_active=0,
        )
    )

    with pytest.raises(
        ValueError,
        match="O fornecedor informado está inativo.",
    ):
        service.create(
            supplier_id=1,
            part_code="ABC123",
            name="Motor de partida",
            return_deadline_days=90,
        )

    part_repository.add.assert_not_called()


def test_should_raise_when_part_code_is_empty(
    service: PartService,
    part_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )

    with pytest.raises(
        ValueError,
        match="O código original da peça é obrigatório.",
    ):
        service.create(
            supplier_id=1,
            part_code="   ",
            name="Motor de partida",
            return_deadline_days=90,
        )

    part_repository.add.assert_not_called()


def test_should_raise_when_part_name_is_empty(
    service: PartService,
    part_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )

    with pytest.raises(
        ValueError,
        match="O nome da peça é obrigatório.",
    ):
        service.create(
            supplier_id=1,
            part_code="ABC123",
            name="   ",
            return_deadline_days=90,
        )

    part_repository.add.assert_not_called()


def test_should_raise_when_part_already_exists_for_supplier(
    service: PartService,
    part_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )

    part_repository.get_by_supplier_and_code.return_value = (
        create_part()
    )

    with pytest.raises(
        ValueError,
        match=(
            "Já existe uma peça com este código "
            "para o fornecedor informado."
        ),
    ):
        service.create(
            supplier_id=1,
            part_code="ABC123",
            name="Motor de partida",
            return_deadline_days=90,
        )

    part_repository.add.assert_not_called()


def test_should_allow_same_code_for_different_supplier(
    service: PartService,
    part_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier_repository.get_by_id.return_value = (
        create_supplier(
            supplier_id=2,
        )
    )

    part_repository.get_by_supplier_and_code.return_value = (
        None
    )

    part_repository.add.side_effect = (
        lambda part: part
    )

    part = service.create(
        supplier_id=2,
        part_code="ABC123",
        name="Motor de partida",
        return_deadline_days=120,
    )

    assert part.supplier_id == 2
    assert part.part_code == "ABC123"

    (
        part_repository
        .get_by_supplier_and_code
        .assert_called_once_with(
            2,
            "ABC123",
        )
    )


@pytest.mark.parametrize(
    (
        "return_deadline_days",
        "expected_message",
    ),
    [
        (
            0,
            (
                "O prazo de devolução deve ser "
                "maior que zero."
            ),
        ),
        (
            -1,
            (
                "O prazo de devolução deve ser "
                "maior que zero."
            ),
        ),
        (
            3651,
            (
                "O prazo de devolução não pode "
                "ser maior que 3650 dias."
            ),
        ),
    ],
)
def test_should_raise_when_return_deadline_is_invalid(
    service: PartService,
    part_repository: Mock,
    supplier_repository: Mock,
    return_deadline_days: int,
    expected_message: str,
) -> None:
    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )

    with pytest.raises(
        ValueError,
        match=expected_message,
    ):
        service.create(
            supplier_id=1,
            part_code="ABC123",
            name="Motor de partida",
            return_deadline_days=return_deadline_days,
        )

    part_repository.add.assert_not_called()


def test_should_raise_when_return_deadline_is_boolean(
    service: PartService,
    part_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )

    with pytest.raises(
        ValueError,
        match=(
            "O prazo de devolução deve ser "
            "informado em dias."
        ),
    ):
        service.create(
            supplier_id=1,
            part_code="ABC123",
            name="Motor de partida",
            return_deadline_days=True,
        )

    part_repository.add.assert_not_called()


def test_should_get_part_by_id(
    service: PartService,
    part_repository: Mock,
) -> None:
    part = create_part()

    part_repository.get_by_id.return_value = part

    result = service.get_by_id(10)

    assert result is part

    part_repository.get_by_id.assert_called_once_with(
        10
    )


def test_should_return_none_when_part_does_not_exist(
    service: PartService,
    part_repository: Mock,
) -> None:
    part_repository.get_by_id.return_value = None

    result = service.get_by_id(10)

    assert result is None


def test_should_raise_when_getting_part_with_invalid_id(
    service: PartService,
    part_repository: Mock,
) -> None:
    with pytest.raises(
        ValueError,
        match=(
            "O identificador da peça deve ser "
            "maior que zero."
        ),
    ):
        service.get_by_id(0)

    part_repository.get_by_id.assert_not_called()


def test_should_get_required_part(
    service: PartService,
    part_repository: Mock,
) -> None:
    part = create_part()

    part_repository.get_by_id.return_value = part

    result = service.get_required(10)

    assert result is part


def test_should_raise_when_required_part_does_not_exist(
    service: PartService,
    part_repository: Mock,
) -> None:
    part_repository.get_by_id.return_value = None

    with pytest.raises(
        ValueError,
        match="Peça não encontrada.",
    ):
        service.get_required(10)


def test_should_list_all_parts(
    service: PartService,
    part_repository: Mock,
) -> None:
    parts = [
        create_part(
            part_id=10,
            part_code="ABC123",
        ),
        create_part(
            part_id=11,
            part_code="XYZ789",
        ),
    ]

    part_repository.list_all.return_value = parts

    result = service.list_all()

    assert result == parts

    part_repository.list_all.assert_called_once_with()


def test_should_list_parts_by_supplier(
    service: PartService,
    part_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier = create_supplier()

    parts = [
        create_part(
            part_id=10,
        ),
        create_part(
            part_id=11,
            part_code="XYZ789",
        ),
    ]

    supplier_repository.get_by_id.return_value = supplier
    part_repository.list_by_supplier.return_value = parts

    result = service.list_by_supplier(1)

    assert result == parts

    supplier_repository.get_by_id.assert_called_once_with(
        1
    )

    part_repository.list_by_supplier.assert_called_once_with(
        1
    )


def test_should_raise_when_listing_parts_of_unknown_supplier(
    service: PartService,
    part_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier_repository.get_by_id.return_value = None

    with pytest.raises(
        ValueError,
        match="Fornecedor não encontrado.",
    ):
        service.list_by_supplier(1)

    part_repository.list_by_supplier.assert_not_called()


def test_should_update_part_name(
    service: PartService,
    part_repository: Mock,
) -> None:
    part = create_part()

    part_repository.get_by_id.return_value = part
    part_repository.save.side_effect = (
        lambda saved_part: saved_part
    )

    updated = service.update(
        part_id=10,
        name="  Alternador  ",
    )

    assert updated.name == "Alternador"
    assert updated.part_code == "ABC123"
    assert updated.supplier_id == 1
    assert updated.return_deadline_days == 90

    part_repository.save.assert_called_once_with(
        part
    )


def test_should_update_part_code(
    service: PartService,
    part_repository: Mock,
) -> None:
    part = create_part()

    part_repository.get_by_id.return_value = part

    part_repository.get_by_supplier_and_code.return_value = (
        None
    )

    part_repository.save.side_effect = (
        lambda saved_part: saved_part
    )

    updated = service.update(
        part_id=10,
        part_code="  XYZ789  ",
    )

    assert updated.part_code == "XYZ789"

    (
        part_repository
        .get_by_supplier_and_code
        .assert_called_once_with(
            1,
            "XYZ789",
        )
    )


def test_should_not_check_duplicate_when_code_is_unchanged(
    service: PartService,
    part_repository: Mock,
) -> None:
    part = create_part()

    part_repository.get_by_id.return_value = part
    part_repository.save.side_effect = (
        lambda saved_part: saved_part
    )

    updated = service.update(
        part_id=10,
        name="Novo nome",
    )

    assert updated.name == "Novo nome"

    (
        part_repository
        .get_by_supplier_and_code
        .assert_not_called()
    )


def test_should_change_part_supplier(
    service: PartService,
    part_repository: Mock,
    supplier_repository: Mock,
) -> None:
    part = create_part()

    new_supplier = create_supplier(
        supplier_id=2,
        name="Novo fornecedor",
    )

    part_repository.get_by_id.return_value = part
    supplier_repository.get_by_id.return_value = (
        new_supplier
    )

    part_repository.get_by_supplier_and_code.return_value = (
        None
    )

    part_repository.save.side_effect = (
        lambda saved_part: saved_part
    )

    updated = service.update(
        part_id=10,
        supplier_id=2,
    )

    assert updated.supplier_id == 2
    assert updated.part_code == "ABC123"

    supplier_repository.get_by_id.assert_called_once_with(
        2
    )

    (
        part_repository
        .get_by_supplier_and_code
        .assert_called_once_with(
            2,
            "ABC123",
        )
    )


def test_should_raise_when_new_supplier_is_inactive(
    service: PartService,
    part_repository: Mock,
    supplier_repository: Mock,
) -> None:
    part = create_part()

    part_repository.get_by_id.return_value = part

    supplier_repository.get_by_id.return_value = (
        create_supplier(
            supplier_id=2,
            is_active=0,
        )
    )

    with pytest.raises(
        ValueError,
        match="O fornecedor informado está inativo.",
    ):
        service.update(
            part_id=10,
            supplier_id=2,
        )

    part_repository.save.assert_not_called()


def test_should_raise_when_updated_combination_already_exists(
    service: PartService,
    part_repository: Mock,
    supplier_repository: Mock,
) -> None:
    part = create_part()

    duplicate = create_part(
        part_id=20,
        supplier_id=2,
        part_code="ABC123",
    )

    part_repository.get_by_id.return_value = part

    supplier_repository.get_by_id.return_value = (
        create_supplier(
            supplier_id=2,
        )
    )

    part_repository.get_by_supplier_and_code.return_value = (
        duplicate
    )

    with pytest.raises(
        ValueError,
        match=(
            "Já existe uma peça com este código "
            "para o fornecedor informado."
        ),
    ):
        service.update(
            part_id=10,
            supplier_id=2,
        )

    part_repository.save.assert_not_called()


def test_should_allow_duplicate_lookup_to_return_same_part(
    service: PartService,
    part_repository: Mock,
) -> None:
    part = create_part()

    part_repository.get_by_id.return_value = part

    part_repository.get_by_supplier_and_code.return_value = (
        part
    )

    part_repository.save.side_effect = (
        lambda saved_part: saved_part
    )

    updated = service.update(
        part_id=10,
        part_code="XYZ789",
    )

    assert updated.part_code == "XYZ789"

    part_repository.save.assert_called_once_with(
        part
    )


def test_should_clear_optional_description(
    service: PartService,
    part_repository: Mock,
) -> None:
    part = create_part()

    part_repository.get_by_id.return_value = part
    part_repository.save.side_effect = (
        lambda saved_part: saved_part
    )

    updated = service.update(
        part_id=10,
        description=None,
    )

    assert updated.description is None


def test_should_convert_empty_updated_description_to_none(
    service: PartService,
    part_repository: Mock,
) -> None:
    part = create_part()

    part_repository.get_by_id.return_value = part
    part_repository.save.side_effect = (
        lambda saved_part: saved_part
    )

    updated = service.update(
        part_id=10,
        description="   ",
    )

    assert updated.description is None


def test_should_update_return_deadline(
    service: PartService,
    part_repository: Mock,
) -> None:
    part = create_part()

    part_repository.get_by_id.return_value = part
    part_repository.save.side_effect = (
        lambda saved_part: saved_part
    )

    updated = service.update(
        part_id=10,
        return_deadline_days=120,
    )

    assert updated.return_deadline_days == 120


def test_should_raise_when_updated_name_is_empty(
    service: PartService,
    part_repository: Mock,
) -> None:
    part_repository.get_by_id.return_value = (
        create_part()
    )

    with pytest.raises(
        ValueError,
        match="O nome da peça é obrigatório.",
    ):
        service.update(
            part_id=10,
            name="   ",
        )

    part_repository.save.assert_not_called()


def test_should_raise_when_updated_code_is_empty(
    service: PartService,
    part_repository: Mock,
) -> None:
    part_repository.get_by_id.return_value = (
        create_part()
    )

    with pytest.raises(
        ValueError,
        match="O código original da peça é obrigatório.",
    ):
        service.update(
            part_id=10,
            part_code="   ",
        )

    part_repository.save.assert_not_called()


def test_should_deactivate_part(
    service: PartService,
    part_repository: Mock,
) -> None:
    part = create_part(
        is_active=1,
    )

    part_repository.get_by_id.return_value = part
    part_repository.save.side_effect = (
        lambda saved_part: saved_part
    )

    updated = service.deactivate(10)

    assert updated.is_active == 0

    part_repository.save.assert_called_once_with(
        part
    )


def test_should_raise_when_part_is_already_inactive(
    service: PartService,
    part_repository: Mock,
) -> None:
    part_repository.get_by_id.return_value = (
        create_part(
            is_active=0,
        )
    )

    with pytest.raises(
        ValueError,
        match="A peça já está inativa.",
    ):
        service.deactivate(10)

    part_repository.save.assert_not_called()


def test_should_activate_part(
    service: PartService,
    part_repository: Mock,
    supplier_repository: Mock,
) -> None:
    part = create_part(
        is_active=0,
    )

    part_repository.get_by_id.return_value = part

    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )

    part_repository.save.side_effect = (
        lambda saved_part: saved_part
    )

    updated = service.activate(10)

    assert updated.is_active == 1

    supplier_repository.get_by_id.assert_called_once_with(
        1
    )

    part_repository.save.assert_called_once_with(
        part
    )


def test_should_raise_when_part_is_already_active(
    service: PartService,
    part_repository: Mock,
) -> None:
    part_repository.get_by_id.return_value = (
        create_part(
            is_active=1,
        )
    )

    with pytest.raises(
        ValueError,
        match="A peça já está ativa.",
    ):
        service.activate(10)

    part_repository.save.assert_not_called()


def test_should_raise_when_activating_part_with_inactive_supplier(
    service: PartService,
    part_repository: Mock,
    supplier_repository: Mock,
) -> None:
    part_repository.get_by_id.return_value = (
        create_part(
            is_active=0,
        )
    )

    supplier_repository.get_by_id.return_value = (
        create_supplier(
            is_active=0,
        )
    )

    with pytest.raises(
        ValueError,
        match="O fornecedor informado está inativo.",
    ):
        service.activate(10)

    part_repository.save.assert_not_called()
```

## `tests\services\test_purchase_service.py`

```python
from unittest.mock import Mock
from types import SimpleNamespace

import pytest

from src.models.purchase import Purchase
from src.models.supplier import Supplier
from src.repositories.part_repository import (
    PartRepository,
)
from src.repositories.purchase_item_repository import (
    PurchaseItemRepository,
)
from src.repositories.purchase_repository import (
    PurchaseRepository,
)
from src.repositories.supplier_repository import (
    SupplierRepository,
)
from src.services.purchase_service import (
    PurchaseService,
)


@pytest.fixture
def purchase_repository() -> Mock:
    """
    Cria um mock do repositório de compras.
    """

    return Mock(
        spec=PurchaseRepository,
    )


@pytest.fixture
def purchase_item_repository() -> Mock:
    """
    Cria um mock do repositório de itens da compra.
    """

    return Mock(
        spec=PurchaseItemRepository,
    )


@pytest.fixture
def supplier_repository() -> Mock:
    """
    Cria um mock do repositório de fornecedores.
    """

    return Mock(
        spec=SupplierRepository,
    )


@pytest.fixture
def part_repository() -> Mock:
    """
    Cria um mock do repositório de peças.
    """

    return Mock(
        spec=PartRepository,
    )


@pytest.fixture
def service(
    purchase_repository: Mock,
    purchase_item_repository: Mock,
    supplier_repository: Mock,
    part_repository: Mock,
) -> PurchaseService:
    """
    Cria o serviço com suas dependências simuladas.
    """

    return PurchaseService(
        purchase_repository=purchase_repository,
        purchase_item_repository=(
            purchase_item_repository
        ),
        supplier_repository=supplier_repository,
        part_repository=part_repository,
    )


def create_supplier(
    *,
    supplier_id: int = 1,
    name: str = "Fornecedor Teste",
    is_active: int = 1,
) -> Supplier:
    """
    Cria um fornecedor para os testes.
    """

    return Supplier(
        id=supplier_id,
        name=name,
        document="12.345.678/0001-90",
        address="Rua de Teste, 100",
        notes="Fornecedor criado para teste.",
        is_active=is_active,
    )


def create_purchase(
    *,
    purchase_id: int = 10,
    supplier_id: int = 1,
    invoice_number: str = "NF-12345",
    invoice_series: str | None = "1",
    issue_date: str = "2026-07-29",
    created_by: int = 1,
    status: str = "RECEIVED",
    notes: str | None = "Compra criada para teste.",
) -> Purchase:
    """
    Cria uma compra para os testes.
    """

    return Purchase(
        id=purchase_id,
        supplier_id=supplier_id,
        invoice_number=invoice_number,
        invoice_series=invoice_series,
        issue_date=issue_date,
        created_by=created_by,
        status=status,
        notes=notes,
    )

def create_part(
    *,
    part_id: int = 20,
    supplier_id: int = 1,
    part_code: str = "PEC-001",
    name: str = "Compressor de ar",
    is_active: int = 1,
) -> SimpleNamespace:
    """
    Cria uma peça simplificada para os testes.
    """

    return SimpleNamespace(
        id=part_id,
        supplier_id=supplier_id,
        part_code=part_code,
        name=name,
        is_active=is_active,
    )


def create_purchase_item(
    *,
    purchase_item_id: int = 30,
    purchase_id: int = 10,
    part_id: int = 20,
    quantity_purchased: int = 10,
    quantity_available: int = 10,
) -> SimpleNamespace:
    """
    Cria um item de compra simplificado para os testes.
    """

    return SimpleNamespace(
        id=purchase_item_id,
        purchase_id=purchase_id,
        part_id=part_id,
        quantity_purchased=quantity_purchased,
        quantity_available=quantity_available,
    )

def test_should_create_purchase(
    service: PurchaseService,
    purchase_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier = create_supplier()

    supplier_repository.get_by_id.return_value = (
        supplier
    )

    purchase_repository.get_by_invoice.return_value = (
        None
    )

    purchase_repository.add.side_effect = (
        lambda purchase: purchase
    )

    created = service.create_purchase(
        supplier_id=1,
        invoice_number="NF-12345",
        invoice_series="1",
        issue_date="2026-07-29",
        created_by=1,
        status="RECEIVED",
        notes="Compra criada para teste.",
    )

    assert created.supplier_id == 1
    assert created.invoice_number == "NF-12345"
    assert created.invoice_series == "1"
    assert created.issue_date == "2026-07-29"
    assert created.created_by == 1
    assert created.status == "RECEIVED"
    assert created.notes == "Compra criada para teste."

    supplier_repository.get_by_id.assert_called_once_with(
        1
    )

    purchase_repository.get_by_invoice.assert_called_once_with(
        supplier_id=1,
        invoice_number="NF-12345",
        invoice_series="1",
    )

    purchase_repository.add.assert_called_once_with(
        created
    )


def test_should_normalize_purchase_fields_on_create(
    service: PurchaseService,
    purchase_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )

    purchase_repository.get_by_invoice.return_value = (
        None
    )

    purchase_repository.add.side_effect = (
        lambda purchase: purchase
    )

    created = service.create_purchase(
        supplier_id=1,
        invoice_number="  NF-12345  ",
        invoice_series="  1  ",
        issue_date="  2026-07-29  ",
        created_by=1,
        status="  received  ",
        notes="  Compra de teste  ",
    )

    assert created.invoice_number == "NF-12345"
    assert created.invoice_series == "1"
    assert created.issue_date == "2026-07-29"
    assert created.status == "RECEIVED"
    assert created.notes == "Compra de teste"

    purchase_repository.get_by_invoice.assert_called_once_with(
        supplier_id=1,
        invoice_number="NF-12345",
        invoice_series="1",
    )

    purchase_repository.add.assert_called_once_with(
        created
    )


def test_should_create_purchase_without_optional_fields(
    service: PurchaseService,
    purchase_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )

    purchase_repository.get_by_invoice.return_value = (
        None
    )

    purchase_repository.add.side_effect = (
        lambda purchase: purchase
    )

    created = service.create_purchase(
        supplier_id=1,
        invoice_number="NF-12345",
        invoice_series=None,
        issue_date="2026-07-29",
        created_by=1,
        status="PENDING",
        notes=None,
    )

    assert created.invoice_series is None
    assert created.notes is None
    assert created.status == "PENDING"

    purchase_repository.get_by_invoice.assert_called_once_with(
        supplier_id=1,
        invoice_number="NF-12345",
        invoice_series=None,
    )

    purchase_repository.add.assert_called_once_with(
        created
    )


def test_should_convert_blank_optional_fields_to_none(
    service: PurchaseService,
    purchase_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )

    purchase_repository.get_by_invoice.return_value = (
        None
    )

    purchase_repository.add.side_effect = (
        lambda purchase: purchase
    )

    created = service.create_purchase(
        supplier_id=1,
        invoice_number="NF-12345",
        invoice_series="   ",
        issue_date="2026-07-29",
        created_by=1,
        status="RECEIVED",
        notes="   ",
    )

    assert created.invoice_series is None
    assert created.notes is None

    purchase_repository.get_by_invoice.assert_called_once_with(
        supplier_id=1,
        invoice_number="NF-12345",
        invoice_series=None,
    )

    purchase_repository.add.assert_called_once_with(
        created
    )


def test_should_raise_when_supplier_is_not_found_on_create(
    service: PurchaseService,
    purchase_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier_repository.get_by_id.return_value = (
        None
    )

    with pytest.raises(
        ValueError,
        match="Fornecedor não encontrado.",
    ):
        service.create_purchase(
            supplier_id=999,
            invoice_number="NF-12345",
            invoice_series="1",
            issue_date="2026-07-29",
            created_by=1,
            status="RECEIVED",
            notes=None,
        )

    supplier_repository.get_by_id.assert_called_once_with(
        999
    )

    purchase_repository.get_by_invoice.assert_not_called()
    purchase_repository.add.assert_not_called()


def test_should_raise_when_supplier_is_inactive_on_create(
    service: PurchaseService,
    purchase_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier_repository.get_by_id.return_value = (
        create_supplier(
            is_active=0,
        )
    )

    with pytest.raises(
        ValueError,
        match="O fornecedor informado está inativo.",
    ):
        service.create_purchase(
            supplier_id=1,
            invoice_number="NF-12345",
            invoice_series="1",
            issue_date="2026-07-29",
            created_by=1,
            status="RECEIVED",
            notes=None,
        )

    purchase_repository.get_by_invoice.assert_not_called()
    purchase_repository.add.assert_not_called()


def test_should_raise_when_invoice_number_is_blank(
    service: PurchaseService,
    purchase_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )

    with pytest.raises(
        ValueError,
        match="O número da nota fiscal é obrigatório.",
    ):
        service.create_purchase(
            supplier_id=1,
            invoice_number="   ",
            invoice_series="1",
            issue_date="2026-07-29",
            created_by=1,
            status="RECEIVED",
            notes=None,
        )

    purchase_repository.get_by_invoice.assert_not_called()
    purchase_repository.add.assert_not_called()


def test_should_raise_when_issue_date_is_blank(
    service: PurchaseService,
    purchase_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )

    with pytest.raises(
        ValueError,
        match="A data de emissão é obrigatória.",
    ):
        service.create_purchase(
            supplier_id=1,
            invoice_number="NF-12345",
            invoice_series="1",
            issue_date="   ",
            created_by=1,
            status="RECEIVED",
            notes=None,
        )

    purchase_repository.get_by_invoice.assert_not_called()
    purchase_repository.add.assert_not_called()


@pytest.mark.parametrize(
    "invalid_status",
    [
        "",
        "   ",
        "ACTIVE",
        "FINISHED",
        "UNKNOWN",
    ],
)
def test_should_raise_for_invalid_status_on_create(
    service: PurchaseService,
    purchase_repository: Mock,
    supplier_repository: Mock,
    invalid_status: str,
) -> None:
    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )

    expected_message = (
        "O status da compra é obrigatório."
        if not invalid_status.strip()
        else (
            "Status da compra inválido. "
            "Valores permitidos: "
            "CANCELLED, PENDING, RECEIVED."
        )
    )

    with pytest.raises(
        ValueError,
        match=expected_message,
    ):
        service.create_purchase(
            supplier_id=1,
            invoice_number="NF-12345",
            invoice_series="1",
            issue_date="2026-07-29",
            created_by=1,
            status=invalid_status,
            notes=None,
        )

    purchase_repository.get_by_invoice.assert_not_called()
    purchase_repository.add.assert_not_called()


def test_should_raise_when_invoice_already_exists(
    service: PurchaseService,
    purchase_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )

    purchase_repository.get_by_invoice.return_value = (
        create_purchase()
    )

    with pytest.raises(
        ValueError,
        match=(
            "Já existe uma compra com esta nota fiscal, "
            "série e fornecedor."
        ),
    ):
        service.create_purchase(
            supplier_id=1,
            invoice_number="NF-12345",
            invoice_series="1",
            issue_date="2026-07-29",
            created_by=1,
            status="RECEIVED",
            notes=None,
        )

    purchase_repository.get_by_invoice.assert_called_once_with(
        supplier_id=1,
        invoice_number="NF-12345",
        invoice_series="1",
    )

    purchase_repository.add.assert_not_called()

def test_should_add_item_to_purchase(
    service: PurchaseService,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
    part_repository: Mock,
) -> None:
    purchase = create_purchase()
    part = create_part()

    purchase_repository.get_by_id.return_value = (
        purchase
    )

    part_repository.get_by_id.return_value = part

    purchase_item_repository.list_by_purchase.return_value = (
        []
    )

    purchase_item_repository.add.side_effect = (
        lambda purchase_item: purchase_item
    )

    created_item = service.add_item(
        purchase_id=10,
        part_id=20,
        quantity_purchased=15,
    )

    assert created_item.purchase_id == 10
    assert created_item.part_id == 20
    assert created_item.quantity_purchased == 15
    assert created_item.quantity_available == 15

    purchase_repository.get_by_id.assert_called_once_with(
        10
    )

    part_repository.get_by_id.assert_called_once_with(
        20
    )

    purchase_item_repository.list_by_purchase.assert_called_once_with(
        10
    )

    purchase_item_repository.add.assert_called_once_with(
        created_item
    )


def test_should_raise_when_purchase_is_not_found_on_add_item(
    service: PurchaseService,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
    part_repository: Mock,
) -> None:
    purchase_repository.get_by_id.return_value = (
        None
    )

    with pytest.raises(
        ValueError,
        match="Compra não encontrada.",
    ):
        service.add_item(
            purchase_id=999,
            part_id=20,
            quantity_purchased=10,
        )

    purchase_repository.get_by_id.assert_called_once_with(
        999
    )

    part_repository.get_by_id.assert_not_called()

    purchase_item_repository.list_by_purchase.assert_not_called()
    purchase_item_repository.add.assert_not_called()


def test_should_raise_when_purchase_is_cancelled_on_add_item(
    service: PurchaseService,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
    part_repository: Mock,
) -> None:
    purchase_repository.get_by_id.return_value = (
        create_purchase(
            status="CANCELLED",
        )
    )

    with pytest.raises(
        ValueError,
        match=(
            "Não é possível adicionar itens "
            "a uma compra cancelada."
        ),
    ):
        service.add_item(
            purchase_id=10,
            part_id=20,
            quantity_purchased=10,
        )

    purchase_repository.get_by_id.assert_called_once_with(
        10
    )

    part_repository.get_by_id.assert_not_called()

    purchase_item_repository.list_by_purchase.assert_not_called()
    purchase_item_repository.add.assert_not_called()


def test_should_raise_when_part_is_not_found_on_add_item(
    service: PurchaseService,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
    part_repository: Mock,
) -> None:
    purchase_repository.get_by_id.return_value = (
        create_purchase()
    )

    part_repository.get_by_id.return_value = None

    with pytest.raises(
        ValueError,
        match="Peça não encontrada.",
    ):
        service.add_item(
            purchase_id=10,
            part_id=999,
            quantity_purchased=10,
        )

    purchase_repository.get_by_id.assert_called_once_with(
        10
    )

    part_repository.get_by_id.assert_called_once_with(
        999
    )

    purchase_item_repository.list_by_purchase.assert_not_called()
    purchase_item_repository.add.assert_not_called()


def test_should_raise_when_part_is_inactive_on_add_item(
    service: PurchaseService,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
    part_repository: Mock,
) -> None:
    purchase_repository.get_by_id.return_value = (
        create_purchase()
    )

    part_repository.get_by_id.return_value = (
        create_part(
            is_active=0,
        )
    )

    with pytest.raises(
        ValueError,
        match="A peça informada está inativa.",
    ):
        service.add_item(
            purchase_id=10,
            part_id=20,
            quantity_purchased=10,
        )

    purchase_repository.get_by_id.assert_called_once_with(
        10
    )

    part_repository.get_by_id.assert_called_once_with(
        20
    )

    purchase_item_repository.list_by_purchase.assert_not_called()
    purchase_item_repository.add.assert_not_called()


def test_should_raise_when_part_belongs_to_another_supplier(
    service: PurchaseService,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
    part_repository: Mock,
) -> None:
    purchase_repository.get_by_id.return_value = (
        create_purchase(
            supplier_id=1,
        )
    )

    part_repository.get_by_id.return_value = (
        create_part(
            supplier_id=2,
        )
    )

    with pytest.raises(
        ValueError,
        match=(
            "A peça informada não pertence "
            "ao fornecedor da compra."
        ),
    ):
        service.add_item(
            purchase_id=10,
            part_id=20,
            quantity_purchased=10,
        )

    purchase_repository.get_by_id.assert_called_once_with(
        10
    )

    part_repository.get_by_id.assert_called_once_with(
        20
    )

    purchase_item_repository.list_by_purchase.assert_not_called()
    purchase_item_repository.add.assert_not_called()


@pytest.mark.parametrize(
    "invalid_quantity",
    [
        0,
        -1,
        -10,
    ],
)
def test_should_raise_for_invalid_quantity_on_add_item(
    service: PurchaseService,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
    part_repository: Mock,
    invalid_quantity: int,
) -> None:
    purchase_repository.get_by_id.return_value = (
        create_purchase()
    )

    part_repository.get_by_id.return_value = (
        create_part()
    )

    with pytest.raises(
        ValueError,
        match=(
            "A quantidade comprada deve ser "
            "maior que zero."
        ),
    ):
        service.add_item(
            purchase_id=10,
            part_id=20,
            quantity_purchased=invalid_quantity,
        )

    purchase_repository.get_by_id.assert_called_once_with(
        10
    )

    part_repository.get_by_id.assert_called_once_with(
        20
    )

    purchase_item_repository.list_by_purchase.assert_not_called()
    purchase_item_repository.add.assert_not_called()


def test_should_raise_when_part_is_already_in_purchase(
    service: PurchaseService,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
    part_repository: Mock,
) -> None:
    purchase_repository.get_by_id.return_value = (
        create_purchase()
    )

    part_repository.get_by_id.return_value = (
        create_part()
    )

    purchase_item_repository.list_by_purchase.return_value = [
        create_purchase_item(
            part_id=20,
        ),
    ]

    with pytest.raises(
        ValueError,
        match="Esta peça já foi adicionada à compra.",
    ):
        service.add_item(
            purchase_id=10,
            part_id=20,
            quantity_purchased=10,
        )

    purchase_repository.get_by_id.assert_called_once_with(
        10
    )

    part_repository.get_by_id.assert_called_once_with(
        20
    )

    purchase_item_repository.list_by_purchase.assert_called_once_with(
        10
    )

    purchase_item_repository.add.assert_not_called()


def test_should_allow_different_part_in_same_purchase(
    service: PurchaseService,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
    part_repository: Mock,
) -> None:
    purchase_repository.get_by_id.return_value = (
        create_purchase()
    )

    part_repository.get_by_id.return_value = (
        create_part(
            part_id=21,
            part_code="PEC-002",
            name="Alternador",
        )
    )

    purchase_item_repository.list_by_purchase.return_value = [
        create_purchase_item(
            part_id=20,
        ),
    ]

    purchase_item_repository.add.side_effect = (
        lambda purchase_item: purchase_item
    )

    created_item = service.add_item(
        purchase_id=10,
        part_id=21,
        quantity_purchased=5,
    )

    assert created_item.purchase_id == 10
    assert created_item.part_id == 21
    assert created_item.quantity_purchased == 5
    assert created_item.quantity_available == 5

    purchase_item_repository.list_by_purchase.assert_called_once_with(
        10
    )

    purchase_item_repository.add.assert_called_once_with(
        created_item
    )

def test_should_get_purchase_by_id(
    service: PurchaseService,
    purchase_repository: Mock,
) -> None:
    purchase = create_purchase()

    purchase_repository.get_by_id.return_value = (
        purchase
    )

    result = service.get_purchase(
        10
    )

    assert result is purchase

    purchase_repository.get_by_id.assert_called_once_with(
        10
    )


def test_should_raise_when_purchase_is_not_found_on_get(
    service: PurchaseService,
    purchase_repository: Mock,
) -> None:
    purchase_repository.get_by_id.return_value = (
        None
    )

    with pytest.raises(
        ValueError,
        match="Compra não encontrada.",
    ):
        service.get_purchase(
            999
        )

    purchase_repository.get_by_id.assert_called_once_with(
        999
    )


def test_should_list_all_purchases(
    service: PurchaseService,
    purchase_repository: Mock,
) -> None:
    first_purchase = create_purchase()

    second_purchase = create_purchase(
        purchase_id=11,
        supplier_id=2,
        invoice_number="NF-67890",
        invoice_series="2",
        issue_date="2026-07-30",
        status="PENDING",
        notes=None,
    )

    purchase_repository.list_all.return_value = [
        first_purchase,
        second_purchase,
    ]

    result = service.list_purchases()

    assert result == [
        first_purchase,
        second_purchase,
    ]

    purchase_repository.list_all.assert_called_once_with()


def test_should_return_empty_purchase_list(
    service: PurchaseService,
    purchase_repository: Mock,
) -> None:
    purchase_repository.list_all.return_value = []

    result = service.list_purchases()

    assert result == []

    purchase_repository.list_all.assert_called_once_with()


def test_should_list_purchases_by_supplier(
    service: PurchaseService,
    purchase_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier = create_supplier()

    first_purchase = create_purchase()

    second_purchase = create_purchase(
        purchase_id=11,
        invoice_number="NF-67890",
        invoice_series="2",
        issue_date="2026-07-30",
        status="PENDING",
        notes=None,
    )

    supplier_repository.get_by_id.return_value = (
        supplier
    )

    purchase_repository.list_by_supplier.return_value = [
        first_purchase,
        second_purchase,
    ]

    result = service.list_purchases_by_supplier(
        1
    )

    assert result == [
        first_purchase,
        second_purchase,
    ]

    supplier_repository.get_by_id.assert_called_once_with(
        1
    )

    purchase_repository.list_by_supplier.assert_called_once_with(
        1
    )


def test_should_return_empty_list_for_supplier_without_purchases(
    service: PurchaseService,
    purchase_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )

    purchase_repository.list_by_supplier.return_value = []

    result = service.list_purchases_by_supplier(
        1
    )

    assert result == []

    supplier_repository.get_by_id.assert_called_once_with(
        1
    )

    purchase_repository.list_by_supplier.assert_called_once_with(
        1
    )


def test_should_raise_when_supplier_is_not_found_on_purchase_list(
    service: PurchaseService,
    purchase_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier_repository.get_by_id.return_value = (
        None
    )

    with pytest.raises(
        ValueError,
        match="Fornecedor não encontrado.",
    ):
        service.list_purchases_by_supplier(
            999
        )

    supplier_repository.get_by_id.assert_called_once_with(
        999
    )

    purchase_repository.list_by_supplier.assert_not_called()


def test_should_list_purchase_items(
    service: PurchaseService,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
) -> None:
    purchase = create_purchase()

    first_item = create_purchase_item()

    second_item = create_purchase_item(
        purchase_item_id=31,
        part_id=21,
        quantity_purchased=5,
        quantity_available=3,
    )

    purchase_repository.get_by_id.return_value = (
        purchase
    )

    purchase_item_repository.list_by_purchase.return_value = [
        first_item,
        second_item,
    ]

    result = service.list_purchase_items(
        10
    )

    assert result == [
        first_item,
        second_item,
    ]

    purchase_repository.get_by_id.assert_called_once_with(
        10
    )

    purchase_item_repository.list_by_purchase.assert_called_once_with(
        10
    )


def test_should_return_empty_purchase_item_list(
    service: PurchaseService,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
) -> None:
    purchase_repository.get_by_id.return_value = (
        create_purchase()
    )

    purchase_item_repository.list_by_purchase.return_value = []

    result = service.list_purchase_items(
        10
    )

    assert result == []

    purchase_repository.get_by_id.assert_called_once_with(
        10
    )

    purchase_item_repository.list_by_purchase.assert_called_once_with(
        10
    )


def test_should_raise_when_purchase_is_not_found_on_item_list(
    service: PurchaseService,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
) -> None:
    purchase_repository.get_by_id.return_value = (
        None
    )

    with pytest.raises(
        ValueError,
        match="Compra não encontrada.",
    ):
        service.list_purchase_items(
            999
        )

    purchase_repository.get_by_id.assert_called_once_with(
        999
    )

    purchase_item_repository.list_by_purchase.assert_not_called()

def test_should_update_purchase_invoice_number(
    service: PurchaseService,
    purchase_repository: Mock,
) -> None:
    purchase = create_purchase()

    purchase_repository.get_by_id.return_value = (
        purchase
    )

    purchase_repository.get_by_invoice.return_value = (
        None
    )

    purchase_repository.save.side_effect = (
        lambda purchase_to_save: purchase_to_save
    )

    updated = service.update_purchase(
        purchase_id=10,
        invoice_number="  NF-99999  ",
    )

    assert updated is purchase
    assert updated.invoice_number == "NF-99999"

    purchase_repository.get_by_id.assert_called_once_with(
        10
    )

    purchase_repository.get_by_invoice.assert_called_once_with(
        supplier_id=1,
        invoice_number="NF-99999",
        invoice_series="1",
    )

    purchase_repository.save.assert_called_once_with(
        purchase
    )


def test_should_update_purchase_invoice_series(
    service: PurchaseService,
    purchase_repository: Mock,
) -> None:
    purchase = create_purchase()

    purchase_repository.get_by_id.return_value = (
        purchase
    )

    purchase_repository.get_by_invoice.return_value = (
        None
    )

    purchase_repository.save.side_effect = (
        lambda purchase_to_save: purchase_to_save
    )

    updated = service.update_purchase(
        purchase_id=10,
        invoice_series="  2  ",
    )

    assert updated.invoice_series == "2"

    purchase_repository.get_by_invoice.assert_called_once_with(
        supplier_id=1,
        invoice_number="NF-12345",
        invoice_series="2",
    )

    purchase_repository.save.assert_called_once_with(
        purchase
    )


def test_should_clear_purchase_invoice_series(
    service: PurchaseService,
    purchase_repository: Mock,
) -> None:
    purchase = create_purchase(
        invoice_series="1",
    )

    purchase_repository.get_by_id.return_value = (
        purchase
    )

    purchase_repository.get_by_invoice.return_value = (
        None
    )

    purchase_repository.save.side_effect = (
        lambda purchase_to_save: purchase_to_save
    )

    updated = service.update_purchase(
        purchase_id=10,
        invoice_series=None,
    )

    assert updated.invoice_series is None

    purchase_repository.get_by_invoice.assert_called_once_with(
        supplier_id=1,
        invoice_number="NF-12345",
        invoice_series=None,
    )

    purchase_repository.save.assert_called_once_with(
        purchase
    )


def test_should_convert_blank_invoice_series_to_none_on_update(
    service: PurchaseService,
    purchase_repository: Mock,
) -> None:
    purchase = create_purchase(
        invoice_series="1",
    )

    purchase_repository.get_by_id.return_value = (
        purchase
    )

    purchase_repository.get_by_invoice.return_value = (
        None
    )

    purchase_repository.save.side_effect = (
        lambda purchase_to_save: purchase_to_save
    )

    updated = service.update_purchase(
        purchase_id=10,
        invoice_series="   ",
    )

    assert updated.invoice_series is None

    purchase_repository.get_by_invoice.assert_called_once_with(
        supplier_id=1,
        invoice_number="NF-12345",
        invoice_series=None,
    )

    purchase_repository.save.assert_called_once_with(
        purchase
    )


def test_should_update_purchase_issue_date(
    service: PurchaseService,
    purchase_repository: Mock,
) -> None:
    purchase = create_purchase()

    purchase_repository.get_by_id.return_value = (
        purchase
    )

    purchase_repository.save.side_effect = (
        lambda purchase_to_save: purchase_to_save
    )

    updated = service.update_purchase(
        purchase_id=10,
        issue_date="  2026-08-01  ",
    )

    assert updated.issue_date == "2026-08-01"

    purchase_repository.get_by_invoice.assert_not_called()

    purchase_repository.save.assert_called_once_with(
        purchase
    )


def test_should_update_purchase_status(
    service: PurchaseService,
    purchase_repository: Mock,
) -> None:
    purchase = create_purchase(
        status="PENDING",
    )

    purchase_repository.get_by_id.return_value = (
        purchase
    )

    purchase_repository.save.side_effect = (
        lambda purchase_to_save: purchase_to_save
    )

    updated = service.update_purchase(
        purchase_id=10,
        status="  received  ",
    )

    assert updated.status == "RECEIVED"

    purchase_repository.get_by_invoice.assert_not_called()

    purchase_repository.save.assert_called_once_with(
        purchase
    )


def test_should_update_purchase_notes(
    service: PurchaseService,
    purchase_repository: Mock,
) -> None:
    purchase = create_purchase()

    purchase_repository.get_by_id.return_value = (
        purchase
    )

    purchase_repository.save.side_effect = (
        lambda purchase_to_save: purchase_to_save
    )

    updated = service.update_purchase(
        purchase_id=10,
        notes="  Observação atualizada  ",
    )

    assert updated.notes == "Observação atualizada"

    purchase_repository.save.assert_called_once_with(
        purchase
    )


def test_should_clear_purchase_notes(
    service: PurchaseService,
    purchase_repository: Mock,
) -> None:
    purchase = create_purchase(
        notes="Observação antiga",
    )

    purchase_repository.get_by_id.return_value = (
        purchase
    )

    purchase_repository.save.side_effect = (
        lambda purchase_to_save: purchase_to_save
    )

    updated = service.update_purchase(
        purchase_id=10,
        notes=None,
    )

    assert updated.notes is None

    purchase_repository.save.assert_called_once_with(
        purchase
    )


def test_should_convert_blank_notes_to_none_on_update(
    service: PurchaseService,
    purchase_repository: Mock,
) -> None:
    purchase = create_purchase(
        notes="Observação antiga",
    )

    purchase_repository.get_by_id.return_value = (
        purchase
    )

    purchase_repository.save.side_effect = (
        lambda purchase_to_save: purchase_to_save
    )

    updated = service.update_purchase(
        purchase_id=10,
        notes="   ",
    )

    assert updated.notes is None

    purchase_repository.save.assert_called_once_with(
        purchase
    )


def test_should_update_multiple_purchase_fields(
    service: PurchaseService,
    purchase_repository: Mock,
) -> None:
    purchase = create_purchase(
        status="PENDING",
    )

    purchase_repository.get_by_id.return_value = (
        purchase
    )

    purchase_repository.get_by_invoice.return_value = (
        None
    )

    purchase_repository.save.side_effect = (
        lambda purchase_to_save: purchase_to_save
    )

    updated = service.update_purchase(
        purchase_id=10,
        invoice_number="NF-88888",
        invoice_series="3",
        issue_date="2026-08-10",
        status="RECEIVED",
        notes="Compra atualizada",
    )

    assert updated.invoice_number == "NF-88888"
    assert updated.invoice_series == "3"
    assert updated.issue_date == "2026-08-10"
    assert updated.status == "RECEIVED"
    assert updated.notes == "Compra atualizada"

    purchase_repository.get_by_invoice.assert_called_once_with(
        supplier_id=1,
        invoice_number="NF-88888",
        invoice_series="3",
    )

    purchase_repository.save.assert_called_once_with(
        purchase
    )


def test_should_allow_update_without_fields(
    service: PurchaseService,
    purchase_repository: Mock,
) -> None:
    purchase = create_purchase()

    purchase_repository.get_by_id.return_value = (
        purchase
    )

    purchase_repository.save.side_effect = (
        lambda purchase_to_save: purchase_to_save
    )

    updated = service.update_purchase(
        purchase_id=10,
    )

    assert updated is purchase

    purchase_repository.get_by_invoice.assert_not_called()

    purchase_repository.save.assert_called_once_with(
        purchase
    )


def test_should_update_purchase_supplier_without_items(
    service: PurchaseService,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
    supplier_repository: Mock,
) -> None:
    purchase = create_purchase(
        supplier_id=1,
    )

    purchase_repository.get_by_id.return_value = (
        purchase
    )

    supplier_repository.get_by_id.return_value = (
        create_supplier(
            supplier_id=2,
        )
    )

    purchase_item_repository.list_by_purchase.return_value = (
        []
    )

    purchase_repository.get_by_invoice.return_value = (
        None
    )

    purchase_repository.save.side_effect = (
        lambda purchase_to_save: purchase_to_save
    )

    updated = service.update_purchase(
        purchase_id=10,
        supplier_id=2,
    )

    assert updated.supplier_id == 2

    supplier_repository.get_by_id.assert_called_once_with(
        2
    )

    purchase_item_repository.list_by_purchase.assert_called_once_with(
        10
    )

    purchase_repository.get_by_invoice.assert_called_once_with(
        supplier_id=2,
        invoice_number="NF-12345",
        invoice_series="1",
    )

    purchase_repository.save.assert_called_once_with(
        purchase
    )


def test_should_update_supplier_when_all_items_are_compatible(
    service: PurchaseService,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
    supplier_repository: Mock,
    part_repository: Mock,
) -> None:
    purchase = create_purchase(
        supplier_id=1,
    )

    purchase_repository.get_by_id.return_value = (
        purchase
    )

    supplier_repository.get_by_id.return_value = (
        create_supplier(
            supplier_id=2,
        )
    )

    purchase_item_repository.list_by_purchase.return_value = [
        create_purchase_item(
            part_id=20,
        ),
        create_purchase_item(
            purchase_item_id=31,
            part_id=21,
        ),
    ]

    part_repository.get_by_id.side_effect = [
        create_part(
            part_id=20,
            supplier_id=2,
        ),
        create_part(
            part_id=21,
            supplier_id=2,
        ),
    ]

    purchase_repository.get_by_invoice.return_value = (
        None
    )

    purchase_repository.save.side_effect = (
        lambda purchase_to_save: purchase_to_save
    )

    updated = service.update_purchase(
        purchase_id=10,
        supplier_id=2,
    )

    assert updated.supplier_id == 2

    assert part_repository.get_by_id.call_count == 2

    purchase_repository.save.assert_called_once_with(
        purchase
    )


def test_should_raise_when_purchase_is_not_found_on_update(
    service: PurchaseService,
    purchase_repository: Mock,
) -> None:
    purchase_repository.get_by_id.return_value = (
        None
    )

    with pytest.raises(
        ValueError,
        match="Compra não encontrada.",
    ):
        service.update_purchase(
            purchase_id=999,
            notes="Nova observação",
        )

    purchase_repository.save.assert_not_called()


def test_should_raise_when_purchase_is_cancelled_on_update(
    service: PurchaseService,
    purchase_repository: Mock,
) -> None:
    purchase_repository.get_by_id.return_value = (
        create_purchase(
            status="CANCELLED",
        )
    )

    with pytest.raises(
        ValueError,
        match=(
            "Uma compra cancelada não pode ser alterada."
        ),
    ):
        service.update_purchase(
            purchase_id=10,
            notes="Nova observação",
        )

    purchase_repository.get_by_invoice.assert_not_called()
    purchase_repository.save.assert_not_called()


def test_should_raise_when_new_supplier_is_not_found(
    service: PurchaseService,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
    supplier_repository: Mock,
) -> None:
    purchase_repository.get_by_id.return_value = (
        create_purchase()
    )

    supplier_repository.get_by_id.return_value = (
        None
    )

    with pytest.raises(
        ValueError,
        match="Fornecedor não encontrado.",
    ):
        service.update_purchase(
            purchase_id=10,
            supplier_id=999,
        )

    supplier_repository.get_by_id.assert_called_once_with(
        999
    )

    purchase_item_repository.list_by_purchase.assert_not_called()
    purchase_repository.get_by_invoice.assert_not_called()
    purchase_repository.save.assert_not_called()


def test_should_raise_when_new_supplier_is_inactive(
    service: PurchaseService,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
    supplier_repository: Mock,
) -> None:
    purchase_repository.get_by_id.return_value = (
        create_purchase()
    )

    supplier_repository.get_by_id.return_value = (
        create_supplier(
            supplier_id=2,
            is_active=0,
        )
    )

    with pytest.raises(
        ValueError,
        match="O fornecedor informado está inativo.",
    ):
        service.update_purchase(
            purchase_id=10,
            supplier_id=2,
        )

    purchase_item_repository.list_by_purchase.assert_not_called()
    purchase_repository.get_by_invoice.assert_not_called()
    purchase_repository.save.assert_not_called()


def test_should_raise_when_item_is_incompatible_with_new_supplier(
    service: PurchaseService,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
    supplier_repository: Mock,
    part_repository: Mock,
) -> None:
    purchase_repository.get_by_id.return_value = (
        create_purchase(
            supplier_id=1,
        )
    )

    supplier_repository.get_by_id.return_value = (
        create_supplier(
            supplier_id=2,
        )
    )

    purchase_item_repository.list_by_purchase.return_value = [
        create_purchase_item(
            part_id=20,
        ),
    ]

    part_repository.get_by_id.return_value = (
        create_part(
            part_id=20,
            supplier_id=1,
        )
    )

    with pytest.raises(
        ValueError,
        match=(
            "Não é possível alterar o fornecedor "
            "porque existem peças incompatíveis "
            "na compra."
        ),
    ):
        service.update_purchase(
            purchase_id=10,
            supplier_id=2,
        )

    part_repository.get_by_id.assert_called_once_with(
        20
    )

    purchase_repository.get_by_invoice.assert_not_called()
    purchase_repository.save.assert_not_called()


def test_should_raise_when_item_part_is_not_found_on_supplier_update(
    service: PurchaseService,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
    supplier_repository: Mock,
    part_repository: Mock,
) -> None:
    purchase_repository.get_by_id.return_value = (
        create_purchase()
    )

    supplier_repository.get_by_id.return_value = (
        create_supplier(
            supplier_id=2,
        )
    )

    purchase_item_repository.list_by_purchase.return_value = [
        create_purchase_item(
            part_id=999,
        ),
    ]

    part_repository.get_by_id.return_value = None

    with pytest.raises(
        ValueError,
        match=(
            "Não é possível alterar o fornecedor "
            "porque existem peças incompatíveis "
            "na compra."
        ),
    ):
        service.update_purchase(
            purchase_id=10,
            supplier_id=2,
        )

    purchase_repository.get_by_invoice.assert_not_called()
    purchase_repository.save.assert_not_called()


def test_should_raise_when_updated_invoice_already_exists(
    service: PurchaseService,
    purchase_repository: Mock,
) -> None:
    purchase = create_purchase(
        purchase_id=10,
    )

    duplicated_purchase = create_purchase(
        purchase_id=11,
        invoice_number="NF-99999",
    )

    purchase_repository.get_by_id.return_value = (
        purchase
    )

    purchase_repository.get_by_invoice.return_value = (
        duplicated_purchase
    )

    with pytest.raises(
        ValueError,
        match=(
            "Já existe uma compra com esta nota fiscal, "
            "série e fornecedor."
        ),
    ):
        service.update_purchase(
            purchase_id=10,
            invoice_number="NF-99999",
        )

    purchase_repository.save.assert_not_called()


def test_should_allow_invoice_lookup_to_return_same_purchase(
    service: PurchaseService,
    purchase_repository: Mock,
) -> None:
    purchase = create_purchase(
        purchase_id=10,
    )

    purchase_repository.get_by_id.return_value = (
        purchase
    )

    purchase_repository.get_by_invoice.return_value = (
        purchase
    )

    purchase_repository.save.side_effect = (
        lambda purchase_to_save: purchase_to_save
    )

    updated = service.update_purchase(
        purchase_id=10,
        invoice_number="NF-99999",
    )

    assert updated.invoice_number == "NF-99999"

    purchase_repository.save.assert_called_once_with(
        purchase
    )


def test_should_raise_when_invoice_number_is_blank_on_update(
    service: PurchaseService,
    purchase_repository: Mock,
) -> None:
    purchase_repository.get_by_id.return_value = (
        create_purchase()
    )

    with pytest.raises(
        ValueError,
        match="O número da nota fiscal é obrigatório.",
    ):
        service.update_purchase(
            purchase_id=10,
            invoice_number="   ",
        )

    purchase_repository.get_by_invoice.assert_not_called()
    purchase_repository.save.assert_not_called()


def test_should_raise_when_issue_date_is_blank_on_update(
    service: PurchaseService,
    purchase_repository: Mock,
) -> None:
    purchase_repository.get_by_id.return_value = (
        create_purchase()
    )

    with pytest.raises(
        ValueError,
        match="A data de emissão é obrigatória.",
    ):
        service.update_purchase(
            purchase_id=10,
            issue_date="   ",
        )

    purchase_repository.save.assert_not_called()


@pytest.mark.parametrize(
    "invalid_status",
    [
        "",
        "   ",
        "ACTIVE",
        "FINISHED",
        "UNKNOWN",
    ],
)
def test_should_raise_for_invalid_status_on_update(
    service: PurchaseService,
    purchase_repository: Mock,
    invalid_status: str,
) -> None:
    purchase_repository.get_by_id.return_value = (
        create_purchase()
    )

    expected_message = (
        "O status da compra é obrigatório."
        if not invalid_status.strip()
        else (
            "Status da compra inválido. "
            "Valores permitidos: "
            "CANCELLED, PENDING, RECEIVED."
        )
    )

    with pytest.raises(
        ValueError,
        match=expected_message,
    ):
        service.update_purchase(
            purchase_id=10,
            status=invalid_status,
        )

    purchase_repository.save.assert_not_called()


def test_should_reject_cancelled_status_on_regular_update(
    service: PurchaseService,
    purchase_repository: Mock,
) -> None:
    purchase_repository.get_by_id.return_value = (
        create_purchase(
            status="PENDING",
        )
    )

    with pytest.raises(
        ValueError,
        match=(
            "Utilize a operação específica "
            "para cancelar a compra."
        ),
    ):
        service.update_purchase(
            purchase_id=10,
            status="CANCELLED",
        )

    purchase_repository.save.assert_not_called()

def test_should_cancel_purchase(
    service: PurchaseService,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
) -> None:
    purchase = create_purchase(
        status="PENDING",
    )

    purchase_repository.get_by_id.return_value = (
        purchase
    )

    purchase_item_repository.list_by_purchase.return_value = [
        create_purchase_item(
            quantity_purchased=10,
            quantity_available=10,
        ),
        create_purchase_item(
            purchase_item_id=31,
            quantity_purchased=5,
            quantity_available=5,
        ),
    ]

    purchase_repository.save.side_effect = (
        lambda purchase_to_save: purchase_to_save
    )

    cancelled_purchase = service.cancel_purchase(
        purchase_id=10,
    )

    assert cancelled_purchase is purchase
    assert cancelled_purchase.status == "CANCELLED"

    purchase_repository.get_by_id.assert_called_once_with(
        10
    )

    purchase_item_repository.list_by_purchase.assert_called_once_with(
        10
    )

    purchase_repository.save.assert_called_once_with(
        purchase
    )


def test_should_raise_when_purchase_is_not_found_on_cancel(
    service: PurchaseService,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
) -> None:
    purchase_repository.get_by_id.return_value = (
        None
    )

    with pytest.raises(
        ValueError,
        match="Compra não encontrada.",
    ):
        service.cancel_purchase(
            purchase_id=999,
        )

    purchase_repository.get_by_id.assert_called_once_with(
        999
    )

    purchase_item_repository.list_by_purchase.assert_not_called()

    purchase_repository.save.assert_not_called()


def test_should_raise_when_purchase_is_already_cancelled(
    service: PurchaseService,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
) -> None:
    purchase_repository.get_by_id.return_value = (
        create_purchase(
            status="CANCELLED",
        )
    )

    with pytest.raises(
        ValueError,
        match="A compra já está cancelada.",
    ):
        service.cancel_purchase(
            purchase_id=10,
        )

    purchase_repository.get_by_id.assert_called_once_with(
        10
    )

    purchase_item_repository.list_by_purchase.assert_not_called()

    purchase_repository.save.assert_not_called()


def test_should_raise_when_purchase_has_stock_movements(
    service: PurchaseService,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
) -> None:
    purchase_repository.get_by_id.return_value = (
        create_purchase(
            status="RECEIVED",
        )
    )

    purchase_item_repository.list_by_purchase.return_value = [
        create_purchase_item(
            quantity_purchased=10,
            quantity_available=8,
        ),
    ]

    with pytest.raises(
        ValueError,
        match=(
            "Não é possível cancelar uma compra "
            "que já possui movimentações."
        ),
    ):
        service.cancel_purchase(
            purchase_id=10,
        )

    purchase_repository.get_by_id.assert_called_once_with(
        10
    )

    purchase_item_repository.list_by_purchase.assert_called_once_with(
        10
    )

    purchase_repository.save.assert_not_called()


def test_should_allow_cancel_purchase_without_items(
    service: PurchaseService,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
) -> None:
    purchase = create_purchase(
        status="PENDING",
    )

    purchase_repository.get_by_id.return_value = (
        purchase
    )

    purchase_item_repository.list_by_purchase.return_value = (
        []
    )

    purchase_repository.save.side_effect = (
        lambda purchase_to_save: purchase_to_save
    )

    cancelled_purchase = service.cancel_purchase(
        purchase_id=10,
    )

    assert cancelled_purchase.status == "CANCELLED"

    purchase_repository.save.assert_called_once_with(
        purchase
    )


def test_should_allow_cancel_when_all_quantities_are_intact(
    service: PurchaseService,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
) -> None:
    purchase = create_purchase(
        status="RECEIVED",
    )

    purchase_repository.get_by_id.return_value = (
        purchase
    )

    purchase_item_repository.list_by_purchase.return_value = [
        create_purchase_item(
            quantity_purchased=30,
            quantity_available=30,
        ),
        create_purchase_item(
            purchase_item_id=31,
            quantity_purchased=7,
            quantity_available=7,
        ),
        create_purchase_item(
            purchase_item_id=32,
            quantity_purchased=100,
            quantity_available=100,
        ),
    ]

    purchase_repository.save.side_effect = (
        lambda purchase_to_save: purchase_to_save
    )

    cancelled_purchase = service.cancel_purchase(
        purchase_id=10,
    )

    assert cancelled_purchase.status == "CANCELLED"

    purchase_repository.save.assert_called_once_with(
        purchase
    )


def test_should_raise_when_any_item_has_stock_movement(
    service: PurchaseService,
    purchase_repository: Mock,
    purchase_item_repository: Mock,
) -> None:
    purchase_repository.get_by_id.return_value = (
        create_purchase()
    )

    purchase_item_repository.list_by_purchase.return_value = [
        create_purchase_item(
            quantity_purchased=30,
            quantity_available=30,
        ),
        create_purchase_item(
            purchase_item_id=31,
            quantity_purchased=10,
            quantity_available=9,
        ),
        create_purchase_item(
            purchase_item_id=32,
            quantity_purchased=5,
            quantity_available=5,
        ),
    ]

    with pytest.raises(
        ValueError,
        match=(
            "Não é possível cancelar uma compra "
            "que já possui movimentações."
        ),
    ):
        service.cancel_purchase(
            purchase_id=10,
        )

    purchase_repository.save.assert_not_called()
```

## `tests\services\test_purchase_tracking_service.py`

```python
from unittest.mock import Mock

import pytest

from src.dtos.purchase_tracking import PurchaseTrackingDTO
from src.queries.purchase_tracking_query import PurchaseTrackingQuery
from src.services.purchase_tracking_service import (
    PurchaseTrackingService,
)


def create_tracking_dto() -> PurchaseTrackingDTO:
    """Cria um DTO de acompanhamento para os testes."""

    return PurchaseTrackingDTO(
        purchase_id=1,
        supplier_id=1,
        supplier_name="Fornecedor Teste",
        invoice_number="12345",
        invoice_series="1",
        issue_date="2026-07-28",
        purchase_status="ACTIVE",
        items=(),
    )


def test_should_return_purchase_tracking() -> None:
    query = Mock(spec=PurchaseTrackingQuery)
    expected_tracking = create_tracking_dto()

    query.get_by_purchase_id.return_value = expected_tracking

    service = PurchaseTrackingService(query)

    result = service.get_purchase_tracking(1)

    assert result == expected_tracking

    query.get_by_purchase_id.assert_called_once_with(1)


def test_should_reject_non_positive_purchase_id() -> None:
    query = Mock(spec=PurchaseTrackingQuery)
    service = PurchaseTrackingService(query)

    with pytest.raises(
        ValueError,
        match="O identificador da compra deve ser maior que zero.",
    ):
        service.get_purchase_tracking(0)

    query.get_by_purchase_id.assert_not_called()


def test_should_raise_error_when_purchase_is_not_found() -> None:
    query = Mock(spec=PurchaseTrackingQuery)
    query.get_by_purchase_id.return_value = None

    service = PurchaseTrackingService(query)

    with pytest.raises(
        ValueError,
        match="Compra não encontrada.",
    ):
        service.get_purchase_tracking(999)

    query.get_by_purchase_id.assert_called_once_with(999)
```

## `tests\services\test_supplier_contact_service.py`

```python
from unittest.mock import Mock

import pytest

from src.models.supplier import Supplier
from src.models.supplier_contact import SupplierContact
from src.services.supplier_contact_service import (
    SupplierContactService,
)


@pytest.fixture
def contact_repository() -> Mock:
    """Cria um mock do repository de contatos."""

    return Mock()


@pytest.fixture
def supplier_repository() -> Mock:
    """Cria um mock do repository de fornecedores."""

    return Mock()


@pytest.fixture
def service(
    contact_repository: Mock,
    supplier_repository: Mock,
) -> SupplierContactService:
    """Cria o serviço com repositories simulados."""

    return SupplierContactService(
        repository=contact_repository,
        supplier_repository=supplier_repository,
    )


def create_supplier(
    supplier_id: int = 1,
) -> Supplier:
    """Cria um fornecedor para os testes."""

    return Supplier(
        id=supplier_id,
        name="Fornecedor Teste",
        document="12.345.678/0001-90",
        address="Registro/SP",
        notes=None,
        is_active=1,
    )


def create_contact(
    *,
    contact_id: int = 10,
    supplier_id: int = 1,
    name: str = "João Silva",
    email: str | None = "joao@fornecedor.com",
    phone: str | None = "(11) 99999-1111",
    position: str | None = "Garantia",
    is_primary: int = 0,
    is_active: int = 1,
) -> SupplierContact:
    """Cria um contato para os testes."""

    return SupplierContact(
        id=contact_id,
        supplier_id=supplier_id,
        name=name,
        email=email,
        phone=phone,
        position=position,
        is_primary=is_primary,
        is_active=is_active,
    )


def test_should_create_supplier_contact(
    service: SupplierContactService,
    contact_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )

    contact_repository.add.side_effect = (
        lambda contact: contact
    )

    contact = service.create(
        supplier_id=1,
        name="João Silva",
        email="joao@fornecedor.com",
        phone="(11) 99999-1111",
        position="Garantia",
        is_primary=False,
    )

    assert contact.supplier_id == 1
    assert contact.name == "João Silva"
    assert contact.email == "joao@fornecedor.com"
    assert contact.phone == "(11) 99999-1111"
    assert contact.position == "Garantia"
    assert contact.is_primary == 0
    assert contact.is_active == 1

    contact_repository.add.assert_called_once_with(
        contact
    )


def test_should_normalize_contact_fields(
    service: SupplierContactService,
    contact_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )

    contact_repository.add.side_effect = (
        lambda contact: contact
    )

    contact = service.create(
        supplier_id=1,
        name="  João Silva  ",
        email="  JOAO@FORNECEDOR.COM  ",
        phone="   ",
        position="  Garantia  ",
    )

    assert contact.name == "João Silva"
    assert contact.email == "joao@fornecedor.com"
    assert contact.phone is None
    assert contact.position == "Garantia"


def test_should_raise_when_supplier_is_not_found(
    service: SupplierContactService,
    contact_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier_repository.get_by_id.return_value = None

    with pytest.raises(
        ValueError,
        match="Fornecedor não encontrado.",
    ):
        service.create(
            supplier_id=999,
            name="João Silva",
        )

    contact_repository.add.assert_not_called()


def test_should_return_required_contact(
    service: SupplierContactService,
    contact_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier = create_supplier()
    contact = create_contact()

    supplier_repository.get_by_id.return_value = supplier
    contact_repository.get_by_id.return_value = contact

    result = service.get_required(
        supplier_id=1,
        contact_id=10,
    )

    assert result == contact

    supplier_repository.get_by_id.assert_called_once_with(1)
    contact_repository.get_by_id.assert_called_once_with(10)


def test_should_raise_when_contact_is_not_found(
    service: SupplierContactService,
    contact_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )
    contact_repository.get_by_id.return_value = None

    with pytest.raises(
        ValueError,
        match="Contato não encontrado.",
    ):
        service.get_required(
            supplier_id=1,
            contact_id=999,
        )


def test_should_raise_when_contact_belongs_to_another_supplier(
    service: SupplierContactService,
    contact_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )

    contact_repository.get_by_id.return_value = (
        create_contact(
            supplier_id=2,
        )
    )

    with pytest.raises(
        ValueError,
        match=(
            "O contato não pertence ao fornecedor informado."
        ),
    ):
        service.get_required(
            supplier_id=1,
            contact_id=10,
        )


def test_should_list_contacts_by_supplier(
    service: SupplierContactService,
    contact_repository: Mock,
    supplier_repository: Mock,
) -> None:
    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )

    contacts = [
        create_contact(contact_id=10),
        create_contact(
            contact_id=11,
            name="Maria Souza",
        ),
    ]

    contact_repository.list_by_supplier.return_value = (
        contacts
    )

    result = service.list_by_supplier(1)

    assert result == contacts

    contact_repository.list_by_supplier.assert_called_once_with(
        1
    )


def test_should_update_only_informed_fields(
    service: SupplierContactService,
    contact_repository: Mock,
    supplier_repository: Mock,
) -> None:
    contact = create_contact()

    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )
    contact_repository.get_by_id.return_value = contact
    contact_repository.save.side_effect = (
        lambda saved_contact: saved_contact
    )

    updated = service.update(
        supplier_id=1,
        contact_id=10,
        phone="(13) 99999-2222",
    )

    assert updated.phone == "(13) 99999-2222"
    assert updated.name == "João Silva"
    assert updated.email == "joao@fornecedor.com"
    assert updated.position == "Garantia"

    contact_repository.save.assert_called_once_with(
        contact
    )


def test_should_clear_optional_fields(
    service: SupplierContactService,
    contact_repository: Mock,
    supplier_repository: Mock,
) -> None:
    contact = create_contact()

    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )
    contact_repository.get_by_id.return_value = contact
    contact_repository.save.side_effect = (
        lambda saved_contact: saved_contact
    )

    updated = service.update(
        supplier_id=1,
        contact_id=10,
        email=None,
        phone="   ",
        position=None,
    )

    assert updated.email is None
    assert updated.phone is None
    assert updated.position is None


def test_should_create_primary_contact_and_remove_previous_primary(
    service: SupplierContactService,
    contact_repository: Mock,
    supplier_repository: Mock,
) -> None:
    current_primary = create_contact(
        contact_id=20,
        is_primary=1,
    )

    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )

    contact_repository.get_primary_by_supplier.return_value = (
        current_primary
    )
    contact_repository.save.side_effect = (
        lambda contact: contact
    )
    contact_repository.add.side_effect = (
        lambda contact: contact
    )

    new_contact = service.create(
        supplier_id=1,
        name="Maria Souza",
        is_primary=True,
    )

    assert current_primary.is_primary == 0
    assert new_contact.is_primary == 1

    contact_repository.save.assert_called_once_with(
        current_primary
    )
    contact_repository.add.assert_called_once_with(
        new_contact
    )


def test_should_define_existing_contact_as_primary(
    service: SupplierContactService,
    contact_repository: Mock,
    supplier_repository: Mock,
) -> None:
    contact = create_contact(
        contact_id=10,
        is_primary=0,
    )

    previous_primary = create_contact(
        contact_id=20,
        is_primary=1,
    )

    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )
    contact_repository.get_by_id.return_value = contact
    contact_repository.get_primary_by_supplier.return_value = (
        previous_primary
    )
    contact_repository.save.side_effect = (
        lambda saved_contact: saved_contact
    )

    updated = service.update(
        supplier_id=1,
        contact_id=10,
        is_primary=True,
    )

    assert previous_primary.is_primary == 0
    assert updated.is_primary == 1

    assert contact_repository.save.call_count == 2

    contact_repository.save.assert_any_call(
        previous_primary
    )
    contact_repository.save.assert_any_call(
        contact
    )


def test_should_not_remove_same_contact_when_already_primary(
    service: SupplierContactService,
    contact_repository: Mock,
    supplier_repository: Mock,
) -> None:
    contact = create_contact(
        contact_id=10,
        is_primary=1,
    )

    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )
    contact_repository.get_by_id.return_value = contact
    contact_repository.get_primary_by_supplier.return_value = (
        contact
    )
    contact_repository.save.side_effect = (
        lambda saved_contact: saved_contact
    )

    updated = service.update(
        supplier_id=1,
        contact_id=10,
        is_primary=True,
    )

    assert updated.is_primary == 1

    contact_repository.save.assert_called_once_with(
        contact
    )


def test_should_deactivate_contact(
    service: SupplierContactService,
    contact_repository: Mock,
    supplier_repository: Mock,
) -> None:
    contact = create_contact(
        is_active=1,
        is_primary=1,
    )

    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )
    contact_repository.get_by_id.return_value = contact
    contact_repository.save.side_effect = (
        lambda saved_contact: saved_contact
    )

    updated = service.deactivate(
        supplier_id=1,
        contact_id=10,
    )

    assert updated.is_active == 0
    assert updated.is_primary == 0

    contact_repository.save.assert_called_once_with(
        contact
    )


def test_should_raise_when_contact_is_already_inactive(
    service: SupplierContactService,
    contact_repository: Mock,
    supplier_repository: Mock,
) -> None:
    contact = create_contact(
        is_active=0,
    )

    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )
    contact_repository.get_by_id.return_value = contact

    with pytest.raises(
        ValueError,
        match="O contato já está inativo.",
    ):
        service.deactivate(
            supplier_id=1,
            contact_id=10,
        )

    contact_repository.save.assert_not_called()


def test_should_activate_contact(
    service: SupplierContactService,
    contact_repository: Mock,
    supplier_repository: Mock,
) -> None:
    contact = create_contact(
        is_active=0,
    )

    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )
    contact_repository.get_by_id.return_value = contact
    contact_repository.save.side_effect = (
        lambda saved_contact: saved_contact
    )

    updated = service.activate(
        supplier_id=1,
        contact_id=10,
    )

    assert updated.is_active == 1

    contact_repository.save.assert_called_once_with(
        contact
    )


def test_should_raise_when_contact_is_already_active(
    service: SupplierContactService,
    contact_repository: Mock,
    supplier_repository: Mock,
) -> None:
    contact = create_contact(
        is_active=1,
    )

    supplier_repository.get_by_id.return_value = (
        create_supplier()
    )
    contact_repository.get_by_id.return_value = contact

    with pytest.raises(
        ValueError,
        match="O contato já está ativo.",
    ):
        service.activate(
            supplier_id=1,
            contact_id=10,
        )

    contact_repository.save.assert_not_called()
```

## `tests\services\test_supplier_service.py`

```python
from unittest.mock import Mock

import pytest

from src.models.supplier import Supplier
from src.services.supplier_service import SupplierService


@pytest.fixture
def repository() -> Mock:
    return Mock()


@pytest.fixture
def service(repository: Mock) -> SupplierService:
    return SupplierService(repository)


def create_supplier() -> Supplier:
    return Supplier(
        id=1,
        name="Fornecedor Teste",
        document="123456",
        address="Registro/SP",
        notes="Observação",
        is_active=1,
    )


def test_should_create_supplier(
    service: SupplierService,
    repository: Mock,
) -> None:
    repository.get_by_document.return_value = None
    repository.add.side_effect = lambda supplier: supplier

    supplier = service.create(
        name="Fornecedor Teste",
        document="123456",
    )

    assert supplier.name == "Fornecedor Teste"
    assert supplier.document == "123456"

    repository.add.assert_called_once()


def test_should_normalize_fields(
    service: SupplierService,
    repository: Mock,
) -> None:
    repository.get_by_document.return_value = None
    repository.add.side_effect = lambda supplier: supplier

    supplier = service.create(
        name="  Fornecedor  ",
        address="   ",
        notes="  Observação  ",
    )

    assert supplier.name == "Fornecedor"
    assert supplier.address is None
    assert supplier.notes == "Observação"


def test_should_raise_when_document_already_exists(
    service: SupplierService,
    repository: Mock,
) -> None:
    repository.get_by_document.return_value = create_supplier()

    with pytest.raises(
        ValueError,
        match="Já existe um fornecedor com este documento.",
    ):
        service.create(
            name="Fornecedor",
            document="123456",
        )


def test_should_return_supplier_on_get_required(
    service: SupplierService,
    repository: Mock,
) -> None:
    supplier = create_supplier()

    repository.get_by_id.return_value = supplier

    result = service.get_required(1)

    assert result == supplier


def test_should_raise_when_supplier_not_found(
    service: SupplierService,
    repository: Mock,
) -> None:
    repository.get_by_id.return_value = None

    with pytest.raises(
        ValueError,
        match="Fornecedor não encontrado.",
    ):
        service.get_required(99)


def test_should_update_only_informed_fields(
    service: SupplierService,
    repository: Mock,
) -> None:
    supplier = create_supplier()

    repository.get_by_id.return_value = supplier
    repository.get_by_document.return_value = None
    repository.save.side_effect = lambda supplier: supplier

    updated = service.update(
        supplier.id,
        address="Novo endereço",
    )

    assert updated.address == "Novo endereço"
    assert updated.name == "Fornecedor Teste"

    repository.save.assert_called_once()


def test_should_clear_optional_field(
    service: SupplierService,
    repository: Mock,
) -> None:
    supplier = create_supplier()

    repository.get_by_id.return_value = supplier
    repository.save.side_effect = lambda supplier: supplier

    updated = service.update(
        supplier.id,
        notes=None,
    )

    assert updated.notes is None


def test_should_deactivate_supplier(
    service: SupplierService,
    repository: Mock,
) -> None:
    supplier = create_supplier()

    repository.get_by_id.return_value = supplier
    repository.save.side_effect = lambda supplier: supplier

    updated = service.deactivate(1)

    assert updated.is_active == 0


def test_should_activate_supplier(
    service: SupplierService,
    repository: Mock,
) -> None:
    supplier = create_supplier()
    supplier.is_active = 0

    repository.get_by_id.return_value = supplier
    repository.save.side_effect = lambda supplier: supplier

    updated = service.activate(1)

    assert updated.is_active == 1
```
