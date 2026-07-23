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

[Esta seção será preenchida na próxima etapa.]

---

# 4. Objetivos

[Esta seção será preenchida na próxima etapa.]

---

# 5. Escopo do Sistema

[Esta seção será preenchida na próxima etapa.]

---

# 6. Fora do Escopo

[Esta seção será preenchida na próxima etapa.]

---

# 7. Usuários e Perfis

[Esta seção será preenchida na próxima etapa.]

---

# 8. Regras de Negócio

[Esta seção será preenchida após a definição completa dos fluxos.]

---

# 9. Fluxos Operacionais

[Esta seção será preenchida após a definição dos fluxos completos.]

---

# 10. Requisitos Funcionais

[Esta seção será preenchida após a consolidação das regras de negócio.]

---

# 11. Requisitos Não Funcionais

[Esta seção será preenchida após a definição da arquitetura técnica.]

---

# 12. Segurança e Autenticação

[Esta seção será preenchida após a definição completa da autenticação.]

---

# 13. Auditoria e Histórico

[Esta seção será preenchida após a definição completa das operações auditáveis.]

---

# 14. Backup e Recuperação de Dados

[Esta seção será preenchida após a definição da estratégia de backup.]

---

# 15. Arquitetura Técnica

[Esta seção será preenchida antes do início da implementação.]

---

# 16. Banco de Dados

[Esta seção será preenchida após a definição dos requisitos e fluxos.]

---

# 17. Interface e Design System

[Esta seção será preenchida antes da implementação da interface.]

---

# 18. GitHub e Controle de Versão

[Esta seção será preenchida durante a configuração do projeto.]

---

# 19. Decisões Técnicas

[Esta seção registrará as decisões técnicas importantes do projeto.]

---

# 20. Decisões Pendentes

[Esta seção será utilizada para registrar decisões ainda não definidas.]

---

# 21. Histórico de Alterações

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
