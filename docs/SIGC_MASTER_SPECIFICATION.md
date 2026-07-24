# SIGC — Sistema Integrado de Gestão de Cascos

**Sistema Integrado de Gestão de Cascos**

---

## Informações do Projeto

| Informação              | Valor                                 |
| ----------------------- | ------------------------------------- |
| Nome do sistema         | SIGC                                  |
| Nome completo           | Sistema Integrado de Gestão de Cascos |
| Autor                   | Lucas do Nascimento Miura             |
| Status                  | Em fase de especificação              |
| Versão da especificação | 1.0.0                                 |
| Data de criação         | 23/07/2026                            |
| Plataforma inicial      | Aplicação Desktop                     |
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

O SIGC é um sistema desktop desenvolvido para controlar o ciclo de vida de cascos relacionados a peças de veículos pesados, especialmente caminhões, desde a aquisição da peça junto ao fornecedor até a devolução do casco ao fornecedor.

O sistema será utilizado inicialmente por uma única filial de uma concessionária Volkswagen e funcionará de forma independente do sistema principal da empresa.

---

# 2. Visão Geral

O SIGC — Sistema Integrado de Gestão de Cascos é uma aplicação desktop desenvolvida para auxiliar no controle, rastreamento e gerenciamento do ciclo de vida de cascos relacionados a peças de veículos pesados, especialmente caminhões.

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

A primeira versão do SIGC será desenvolvida como uma aplicação desktop.

Aplicações para dispositivos móveis não fazem parte do escopo inicial.

Essa possibilidade poderá ser avaliada futuramente caso exista necessidade operacional.

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
| `unit_price`         | NUMERIC | Valor unitário        |
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

---

# 16.20 Tabela `supplier_return_items`

Representa os itens enviados ao fornecedor.

| Campo                | Tipo    | Descrição             |
| -------------------- | ------- | --------------------- |
| `id`                 | INTEGER | Identificador         |
| `supplier_return_id` | INTEGER | Devolução             |
| `part_id`            | INTEGER | Peça                  |
| `purchase_id`        | INTEGER | Nota Fiscal de origem |
| `quantity`           | INTEGER | Quantidade devolvida  |

O sistema não deverá permitir uma quantidade superior à quantidade disponível para devolução.

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