<h1>🚀 ClickTech HelpDesk </h1>
Sistema de gerenciamento de chamados de suporte técnico desenvolvido com foco em simular um ambiente real de Help Desk corporativo.

O projeto tem como objetivo aplicar, na prática, conceitos de desenvolvimento de software, APIs, bancos de dados, gerenciamento de chamados, rastreamento de eventos e análise de dados.

> 📌 Projeto em desenvolvimento contínuo, com novas funcionalidades e tecnologias planejadas para as próximas etapas.

---

<h1>📋 Sobre o projeto</h1>

O **ClickTech HelpDesk** é uma aplicação voltada para gerenciamento do ciclo de vida de chamados de suporte técnico.

A proposta é criar uma solução capaz de centralizar solicitações de usuários, permitindo que equipes de suporte possam registrar, acompanhar, atualizar e analisar chamados de forma organizada.

O projeto também foi desenvolvido com uma visão de evolução para uma arquitetura mais completa, incorporando futuramente recursos de autenticação, APIs REST, dashboards, métricas operacionais, containers e integração com serviços em nuvem.

A construção do sistema busca aproximar o projeto de um cenário encontrado em ambientes corporativos reais, utilizando boas práticas de desenvolvimento e organização de software.

---

<h1>🎯 Objetivo</h1>

O principal objetivo do ClickTech HelpDesk é desenvolver uma plataforma de gerenciamento de chamados que permita:

- Registrar solicitações de suporte;
- Organizar chamados por status e prioridade;
- Acompanhar o ciclo de vida de cada chamado;
- Associar chamados a usuários e técnicos;
- Registrar alterações realizadas durante o atendimento;
- Manter histórico das mudanças de status;
- Gerar informações para análise operacional;
- Criar uma base para indicadores de SLA e desempenho;
- Aplicar conceitos de engenharia de software em um projeto prático.

Além do objetivo funcional, o projeto também possui finalidade de **estudo, desenvolvimento profissional e construção de portfólio**.

---

<h1> 👥 Público-alvo</h1>

O sistema é destinado principalmente a:

- Empresas que possuem equipes de suporte técnico;
- Service Desks;
- Help Desks;
- Equipes de TI;
- Técnicos de suporte;
- Analistas de infraestrutura;
- Administradores de sistemas;
- Usuários que necessitam solicitar suporte técnico.

O projeto também foi pensado como uma aplicação demonstrativa para estudantes e profissionais que desejam estudar desenvolvimento backend, bancos de dados, APIs e análise de dados.

---

<h1>⚙️ Funcionalidades</h1>

## 🔹 Gerenciamento de chamados

- [x] Cadastro de chamados
- [x] Consulta de chamados
- [x] Atualização de chamados
- [x] Controle de status
- [x] Controle de prioridade
- [ ] Atribuição de técnico
- [ ] Associação de solicitante
- [ ] Categorias de atendimento
- [ ] Filtros avançados
- [ ] Paginação

---

<h1>🔹 Controle de status</h1>

O sistema trabalha com o ciclo de vida dos chamados através de diferentes estados.

Exemplo:

```text
Aberto
   ↓
Em andamento
   ↓
Aguardando cliente
   ↓
Resolvido
   ↓
Fechado
```
O sistema possui estrutura para registrar as alterações realizadas nos status dos chamados.

<h1>🔹 Histórico de alterações</h1>

Uma das funcionalidades importantes do projeto é o rastreamento das mudanças de status.

Exemplo:

Chamado #1

Aberto
  ↓
Em andamento
  ↓
Aguardando cliente
  ↓
Resolvido

Essas alterações são armazenadas em uma estrutura de histórico, permitindo posteriormente analisar o comportamento e o tempo de permanência dos chamados em cada etapa.

<h1>🔹 Métricas e indicadores</h1>

O projeto está sendo estruturado para futuramente disponibilizar indicadores como:

Total de chamados;
Chamados abertos;
Chamados em andamento;
Chamados resolvidos;
Chamados por prioridade;
Chamados por técnico;
Tempo médio de atendimento;
Tempo médio de resolução;
Tempo de permanência por status;
Cumprimento de SLA;
Volume de chamados por período.

<h1>🧠 Arquitetura planejada</h1>

A evolução do projeto está planejada para utilizar uma arquitetura baseada em API REST.

                    ┌─────────────────────┐
                    │      Frontend       │
                    │   React / Web App    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │       FastAPI       │
                    │      REST API       │
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │      Services       │
                    │    Business Logic   │
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │     PostgreSQL      │
                    │      Database       │
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │     Analytics       │
                    │  BI / Dashboards    │
                    └─────────────────────┘

<h1>🛠️ Tecnologias utilizadas</h1>
Backend
Python

Linguagem principal planejada para desenvolvimento do backend.

Utilizada pela flexibilidade, produtividade e amplo ecossistema para desenvolvimento de APIs, automações e soluções orientadas a dados.

FastAPI

Framework planejado para construção da API REST do sistema.

Principais objetivos:

Criação de endpoints;
Validação de dados;
Documentação automática;
Integração com banco de dados;
Desenvolvimento de serviços backend.

<h1>Banco de dados</h1>
<h1>MySql</h1>

Banco de dados relacional planejado como principal banco da aplicação.

Será utilizado para armazenar:

Usuários;
Técnicos;
Chamados;
Status;
Histórico;
Categorias;
Informações relacionadas ao atendimento.
SQL

Utilizado para:

Consultas;
Inserções;
Atualizações;
Relacionamentos;
Análises;
Criação de estruturas;
Desenvolvimento de consultas para indicadores.

<h1>ORM
SQLAlchemy</h1>

Planejado para realizar a comunicação entre a aplicação Python e o banco de dados.

Será utilizado para trabalhar com:

Models;
Relacionamentos;
Consultas;
Persistência de dados.

Migrações
Alembic

Tecnologia planejada para controle de alterações do schema do banco de dados.

Permitirá versionar mudanças como:

CREATE TABLE
ALTER TABLE
ADD COLUMN
CREATE INDEX
sem depender de alterações manuais no banco de produção.

<h1>🐳 Infraestrutura
Docker</h1>

O projeto será containerizado utilizando Docker.

Objetivos:

Padronizar o ambiente;
Facilitar instalação;
Isolar serviços;
Facilitar desenvolvimento;
Preparar o projeto para deploy.

<h1>Docker Compose</h1>

Planejado para orquestrar inicialmente:

ClickTech HelpDesk
│
├── Backend
│   └── FastAPI
│
└── Database
    └── PostgreSQL
Posteriormente poderão ser adicionados outros serviços.

<h1>🔐 Segurança</h1>

Funcionalidades de segurança planejadas:

Autenticação de usuários;
JWT;
Controle de acesso baseado em função;
Hash de senhas;
Proteção de endpoints;
Validação de dados;
Controle de permissões.

Perfis planejados:
ADMIN
  │
  ├── Gerenciamento do sistema
  ├── Usuários
  └── Relatórios

TÉCNICO
  │
  ├── Visualizar chamados
  ├── Atender chamados
  └── Atualizar status

USUÁRIO
  │
  ├── Criar chamados
  ├── Consultar chamados
  └── Acompanhar atendimento

<h1>📊 Dados e Business Intelligence</h1>

Uma das evoluções planejadas para o ClickTech HelpDesk é transformar os dados operacionais em informações para tomada de decisão.

A aplicação poderá fornecer dados para ferramentas como:

Power BI;
Python;
SQL;
Ferramentas de visualização de dados.

Exemplos de indicadores:  
                    CHAMADOS
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
       Status      Prioridade    Técnico
          │            │            │
          └────────────┼────────────┘
                       ▼
                    Métricas
                       │
                       ▼
                    Dashboard

🚧 Tecnologias e funcionalidades futuras

O projeto está planejado para evoluir gradualmente.

Backend
 FastAPI
 SQLAlchemy
 Pydantic
 Alembic
 JWT
 Pytest
Banco de dados
 SQL
 Modelagem relacional
 Histórico de alterações
 PostgreSQL em ambiente containerizado
 Índices e otimização de consultas
 Views para relatórios
Infraestrutura
 Docker
 Docker Compose
 Linux
 CI/CD
 GitHub Actions
 Deploy em Cloud
Frontend
 React
 Interface responsiva
 Dashboard
 Tela de chamados
 Tela de usuários
 Tela de técnicos
Dados / BI
 Power BI
 Indicadores de SLA
 Tempo médio de resolução
 Análise de produtividade
 Dashboard operacional
Cloud

Possíveis tecnologias futuras:

 AWS
 Serviços gerenciados de banco de dados
 Deploy de API
 Monitoramento
 Storage
 CI/CD em ambiente cloud
