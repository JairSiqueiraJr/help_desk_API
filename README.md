<h1>🚀 ClickTech HelpDesk </h1>
Sistema de gerenciamento de chamados de suporte técnico desenvolvido para simular um ambiente corporativo real de Help Desk.

O projeto está sendo desenvolvido de forma incremental, começando pela modelagem do banco de dados e gerenciamento do ciclo de vida dos chamados, com evolução planejada para uma arquitetura completa baseada em API REST, autenticação, containers, dashboards e cloud.

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

<h1>📌 Status atual</h1>

Em desenvolvimento 🚧

✅ Implementado
Modelagem inicial do banco de dados
Cadastro e gerenciamento de chamados
Controle de status
Histórico de alterações de status
Trigger para registro automático das mudanças
Consultas SQL para acompanhamento dos chamados
Estruturação inicial pensando em métricas e BI
🔨 Em desenvolvimento
Usuários e técnicos
Atribuição de chamados
API REST com FastAPI
SQLAlchemy
Pydantic
Organização em camadas
Testes automatizados
🔮 Roadmap
JWT e controle de permissões
Docker e Docker Compose
React
Dashboard operacional
Indicadores de SLA
Power BI
CI/CD
GitHub Actions
Deploy em Cloud/AWS
Monitoramento e observabilidade
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
Isso cria uma base para, futuramente, calcular tempo por status, tempo de resolução e indicadores de SLA.

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
| Tecnologia | Status                        |
| ---------- | ----------------------------- |
| SQL        | ✅ Utilizado                   |
| PostgreSQL | 🔨 Em desenvolvimento         |
| Python     | 🔨 Em desenvolvimento         |
| FastAPI    | 🔨 Planejado/Em implementação |
| SQLAlchemy | 🔨 Planejado/Em implementação |
| Docker     | 🔮 Roadmap                    |
| React      | 🔮 Roadmap                    |
| Power BI   | 🔮 Roadmap                    |
| AWS        | 🔮 Roadmap                    |
| Git/GitHub | ✅ Utilizado                   |


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

<h1>🚧 Tecnologias e funcionalidades futuras</h1>

O projeto está planejado para evoluir gradualmente.

<h2>Backend</h2>
 FastAPI
 SQLAlchemy
 Pydantic
 Alembic
 JWT
 Pytest
<h2>Banco de dados</h2>
 SQL
 Modelagem relacional



 
 Histórico de alterações
 PostgreSQL em ambiente containerizado
 Índices e otimização de consultas
 Views para relatórios
<h2>Infraestrutura</h2>
 Docker
 Docker Compose
 Linux
 CI/CD
 GitHub Actions
 Deploy em Cloud
<h2>Frontend</h2>
 React
 Interface responsiva
 Dashboard
 Tela de chamados
 Tela de usuários
 Tela de técnicos
<h2>Dados / BI</h2>
 Power BI
 Indicadores de SLA
 Tempo médio de resolução
 Análise de produtividade
 Dashboard operacional
Cloud

<h2>Possíveis tecnologias futuras:</h2>

 AWS
 Serviços gerenciados de banco de dados
 Deploy de API
 Monitoramento
 Storage
 CI/CD em ambiente cloud


<h1>📋 Requisitos</h1>

Para executar o projeto futuramente em ambiente local, serão necessários:

<h1>Obrigatórios</h1>
Python 3.11+
PostgreSQL
Git
<h1>Recomendados</h1>
Docker
Docker Compose
Visual Studio Code
Postman ou Insomnia

<h1>🚀 Instalação</h1>

Clone o repositório:
git clone https://github.com/JairSiqueiraJr/clicktech-helpdesk.git

Entre no diretório:
cd clicktech-helpdesk

Crie um ambiente virtual:
python -m venv .venv

Ative o ambiente virtual no Windows:
.venv\Scripts\activate

Instale as dependências:
pip install -r requirements.txt

Configure as variáveis de ambiente no arquivo:
.env

Execute a aplicação:
uvicorn app.main:app --reload

A documentação da API poderá ser acessada através do Swagger:
/docs

<h1>🧪 Testes</h1>

O projeto será estruturado para utilizar testes automatizados.

Tecnologia planejada:
Pytest

<h1>Os testes deverão contemplar:</h1>

Endpoints;
Regras de negócio;
Autenticação;
CRUD;
Alterações de status;
Histórico;
Consultas.


<h1>📈 Roadmap</h1>
<h2>Fase 1 — Banco de dados</h2>
 Estrutura inicial de chamados
 Status
 Histórico de status
 Trigger para alterações de status
 Usuários
 Técnicos
 Relacionamentos
<h2>Fase 2 — Backend</h2>
 Estrutura FastAPI
 Models
 Schemas
 CRUD
 Services
 Endpoints
 Tratamento de erros
<h2>Fase 3 — Segurança</h2>
 Cadastro
 Login
 JWT
 Controle de permissões
<h2>Fase 4 — Interface</h2>
 Frontend
 Dashboard
 Gestão de chamados
 Gestão de usuários
<h2>Fase 5 — Dados</h2>
 Consultas analíticas
 Indicadores
 SLA
 Power BI
<h2>Fase 6 — Infraestrutura</h2>
 Docker
 CI/CD
 GitHub Actions
 Deploy
 Cloud


 <h1>🎓 Objetivo profissional do projeto</h1>

O ClickTech HelpDesk também representa um projeto de aprendizado prático em engenharia de software.

Através dele são aplicados conceitos relacionados a:

Desenvolvimento Backend;
APIs REST;
Banco de dados;
SQL;
Modelagem de dados;
Arquitetura de software;
Controle de versão;
Containers;
Segurança;
Análise de dados;
Business Intelligence;
Cloud Computing.

O objetivo é evoluir continuamente a aplicação, aproximando sua arquitetura e funcionalidades de um sistema utilizado em um ambiente corporativo real.


<h1>👨‍💻 Autor
Jair Siqueira Junior</h1>

Estudante de Análise e Desenvolvimento de Sistemas e profissional com experiência em suporte técnico, atualmente direcionando sua carreira para desenvolvimento de software, backend, dados e cloud.

Contatos

💼 LinkedIn:
Jair Siqueira | LinkedIn

💻 GitHub:
JairSiqueiraJr — GitHub

<h1>📄 Licença</h1>

Este projeto está em desenvolvimento para fins de aprendizado, portfólio e demonstração técnica.

A licença definitiva será definida conforme a evolução do projeto.

⭐ Se este projeto for útil para você, considere deixar uma estrela no repositório!

