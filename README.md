# 📚 Sistema de Gerenciamento de Biblioteca

Sistema de gerenciamento de biblioteca desenvolvido em **Python**, utilizando **PostgreSQL** como banco de dados e **FastAPI** para disponibilização de uma API REST.

O projeto foi criado com objetivo educacional e evolui progressivamente conforme novos conceitos de programação, banco de dados, desenvolvimento backend e arquitetura de software são estudados e aplicados.

A **versão 4.0** representa uma nova etapa do projeto, com foco não apenas na adição de funcionalidades, mas também em **experiência de uso, regras de negócio, organização, segurança, manutenção e qualidade do código**.

---

# 🎯 Objetivo do projeto

O principal objetivo do Projeto Biblioteca é consolidar, através da prática, conhecimentos relacionados a:

* Python
* Programação Orientada a Objetos
* PostgreSQL
* SQL
* Bancos de dados relacionais
* CRUD
* Relacionamentos entre tabelas
* APIs REST
* FastAPI
* Pydantic
* Arquitetura de software
* Regras de negócio
* Git e GitHub

O projeto também funciona como uma base de estudos para evolução gradual em desenvolvimento backend.

---

# ✨ Funcionalidades

## 👤 Usuários

O sistema permite atualmente:

* Cadastro de usuários
* Listagem de usuários
* Remoção de usuários
* Consulta de usuários
* Ordenação por nome
* Ordenação por ID
* Relatórios de usuários
* Relatório de usuários com empréstimos
* Relatório de usuários sem empréstimos

### Planejado para a versão 4.0

* Edição de usuários
* CRUD completo
* Pesquisa de usuários para operações
* Redução da necessidade de informar IDs manualmente
* Melhor tratamento para usuários inexistentes
* Regras para remoção de usuários relacionados a empréstimos

---

# 📚 Livros

O sistema permite:

* Cadastro de livros
* Listagem de livros
* Remoção de livros
* Pesquisa por título
* Ordenação por ano
* Ordenação alfabética
* Ordenação por ID
* Ordenação por autor
* Controle de disponibilidade
* Relatório de livros disponíveis
* Relatório de livros indisponíveis
* Relatório da quantidade total de livros

Cada livro possui:

* ID
* Título
* Autor
* Ano
* Disponibilidade

### Planejado para a versão 4.0

* Edição de livros
* CRUD completo
* Pesquisa antes de operações de alteração e remoção
* Seleção de livros por informações legíveis
* Redução da dependência de IDs na interface
* Regras adicionais para remoção de livros emprestados

---

# 🔄 Empréstimos

O sistema possui relacionamento entre usuários e livros através da tabela de empréstimos.

Atualmente é possível:

* Registrar empréstimos
* Relacionar um usuário a um livro
* Verificar a existência do livro
* Verificar automaticamente a disponibilidade
* Tornar o livro indisponível após o empréstimo
* Listar empréstimos
* Realizar devoluções
* Restaurar automaticamente a disponibilidade após a devolução

O fluxo atual funciona da seguinte forma:

```text
Usuário
   │
   ▼
Empréstimo
   │
   ▼
Livro
```

Quando um livro é emprestado:

```text
Livro disponível
      ↓
Registro do empréstimo
      ↓
disponivel = FALSE
```

Quando é devolvido:

```text
Devolução
    ↓
disponivel = TRUE
    ↓
Empréstimo removido
```

---

# 🚀 Evolução dos empréstimos na versão 4.0

Uma das principais modificações planejadas para a versão 4.0 é transformar os empréstimos em registros históricos.

Atualmente, um empréstimo é removido do banco após a devolução.

Na nova implementação, o registro deverá ser preservado.

A tabela deverá evoluir conceitualmente para:

```text
emprestimos
│
├── id_emprestimo
├── id_usuario
├── id_livro
├── data_emprestimo
├── data_prevista_devolucao
├── data_devolucao
└── status
```

O novo fluxo será:

```text
EMPRÉSTIMO

Livro disponível
      ↓
Registro do empréstimo
      ↓
Data do empréstimo
      ↓
Prazo de devolução
      ↓
Status = ativo
      ↓
Livro indisponível
```

Na devolução:

```text
DEVOLUÇÃO

Empréstimo ativo
      ↓
Registrar data da devolução
      ↓
Status = devolvido
      ↓
Livro disponível
      ↓
Registro permanece no histórico
```

Dessa forma, os empréstimos não precisarão mais ser apagados após a devolução.

---

# 🕒 Histórico de empréstimos

Com a nova modelagem será possível implementar:

* Histórico completo de empréstimos
* Histórico por usuário
* Histórico por livro
* Empréstimos ativos
* Empréstimos devolvidos
* Empréstimos atrasados
* Data de realização do empréstimo
* Prazo previsto para devolução
* Data efetiva da devolução

---

# 🔎 Experiência de uso

Uma das melhorias planejadas para a versão 4.0 é reduzir a dependência de IDs na interface.

Os IDs continuarão sendo utilizados internamente pelo PostgreSQL como chaves primárias e estrangeiras.

Porém, o usuário do sistema não deverá precisar conhecê-los previamente para realizar operações.

Em vez de:

```text
Digite o ID do usuário: 7
Digite o ID do livro: 14
```

o sistema deverá permitir pesquisas e seleções mais legíveis:

```text
Digite o nome do usuário: Maria

1 - Maria Oliveira
2 - Maria Santos

Escolha: 1
```

Para livros:

```text
Digite o título: Dom

1 - Dom Casmurro — Machado de Assis
2 - Dom Quixote — Miguel de Cervantes
```

Internamente, o sistema continuará utilizando:

```text
id_usuario
id_livro
id_emprestimo
```

para garantir os relacionamentos do banco de dados.

---

# 📊 Relatórios

O projeto já possui um sistema próprio de relatórios.

São utilizadas consultas SQL envolvendo:

* `SELECT`
* `WHERE`
* `ORDER BY`
* `COUNT`
* `GROUP BY`
* `INNER JOIN`
* `LEFT JOIN`

## 📚 Relatórios de livros

Atualmente estão disponíveis:

* Total de livros
* Listagem completa
* Ordem alfabética
* Ordenação por ID
* Ordenação por autor
* Livros disponíveis
* Livros indisponíveis

## 👤 Relatórios de usuários

Atualmente estão disponíveis:

* Listagem de usuários
* Ordem alfabética
* Ordenação por ID
* Usuários com empréstimos
* Usuários sem empréstimos

## 📈 Novos relatórios planejados

Com a implementação do histórico de empréstimos, a versão 4.0 poderá incluir:

* Empréstimos ativos
* Empréstimos devolvidos
* Empréstimos atrasados
* Livros mais emprestados
* Usuários que mais realizam empréstimos
* Histórico de determinado usuário
* Histórico de determinado livro
* Quantidade de empréstimos por período

---

# 🗄️ Banco de dados

A partir da versão 3.0, o projeto utiliza **PostgreSQL** como sistema gerenciador de banco de dados.

A comunicação entre Python e PostgreSQL é realizada através do **Psycopg**.

O projeto deixou de utilizar SQLite3 como banco principal.

---

# 🧱 Modelagem atual

As principais entidades são:

```text
USUÁRIOS
   │
   │ id_usuario
   │
   ▼
EMPRÉSTIMOS
   ▲
   │
   │ id_livro
   │
LIVROS
```

## usuarios

```text
id_usuario
nome
idade
cpf
numero
```

## livros

```text
id_livro
titulo
autor
ano
disponivel
```

## emprestimos

```text
id_emprestimo
id_usuario
id_livro
```

Os relacionamentos são garantidos através de **Foreign Keys**.

---

# 🔑 Chaves primárias

O PostgreSQL utiliza colunas `IDENTITY` para geração automática dos identificadores.

Exemplo:

```sql
id_livro INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY
```

Isso permite que o próprio PostgreSQL controle a geração dos IDs.

---

# 🔗 Chaves estrangeiras

A tabela `emprestimos` relaciona usuários e livros:

```sql
FOREIGN KEY (id_usuario)
REFERENCES usuarios(id_usuario)
```

e:

```sql
FOREIGN KEY (id_livro)
REFERENCES livros(id_livro)
```

Isso garante integridade entre os registros relacionados.

---

# 📖 Schema SQL

A estrutura do banco é armazenada em:

```text
database/schema.sql
```

O arquivo permite recriar a estrutura do banco PostgreSQL em outras máquinas sem depender de um arquivo de banco local.

---

# 🏗️ Estrutura do projeto

A organização atual segue uma divisão modular:

```text
Projeto_Biblioteca/
│
├── app/
│   └── api.py
│
├── database/
│   ├── __init__.py
│   ├── conexao_postgre.py
│   └── schema.sql
│
├── models/
│   ├── __init__.py
│   ├── biblioteca.py
│   ├── livro.py
│   └── usuario.py
│
├── relatorios/
│   ├── __init__.py
│   └── relatorios.py
│
├── utils/
│   ├── __init__.py
│   ├── banco_de_dados.py
│   └── menu.py
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 📁 Responsabilidade atual dos módulos

## `main.py`

Responsável pelo fluxo principal da aplicação em terminal.

Realiza a integração entre:

* menus
* biblioteca
* usuários
* livros
* empréstimos
* relatórios

---

## `models/`

Contém os modelos principais do sistema.

### `livro.py`

Representação dos livros.

### `usuario.py`

Representação dos usuários.

### `biblioteca.py`

Intermedia várias operações entre o fluxo principal e a camada de persistência.

---

## `database/`

Responsável pela infraestrutura relacionada ao PostgreSQL.

### `conexao_postgre.py`

Criação da conexão entre Python e PostgreSQL utilizando Psycopg.

### `schema.sql`

Definição das tabelas e relacionamentos do banco.

---

## `utils/banco_de_dados.py`

Atualmente concentra:

* consultas SQL
* INSERT
* SELECT
* UPDATE
* DELETE
* empréstimos
* devoluções
* filtros
* relatórios

Uma das metas arquiteturais da versão 4.0 é reduzir essa concentração de responsabilidades.

---

## `utils/menu.py`

Contém os menus utilizados pela aplicação em terminal.

---

## `relatorios/relatorios.py`

Controla o fluxo dos menus relacionados aos relatórios.

Os relatórios deixaram de ser executados automaticamente durante a importação do módulo e agora são chamados explicitamente pelo fluxo principal.

---

# 🧠 Arquitetura planejada para a versão 4.0

A versão 4.0 pretende separar melhor três responsabilidades:

```text
Persistência
     ↓
Regras de negócio
     ↓
Apresentação
```

O banco de dados deverá ser responsável por buscar e persistir informações.

As regras de negócio deverão decidir o que pode ou não acontecer.

A camada de apresentação poderá utilizar os mesmos dados tanto no terminal quanto na API.

Conceitualmente:

```text
             ┌── Terminal
             │
PostgreSQL → Aplicação
             │
             └── FastAPI
```

Isso permitirá reutilizar as mesmas regras de negócio em diferentes interfaces.

---

# ⚙️ Transações

Operações que modificam mais de uma informação deverão ser tratadas como uma única transação.

Um empréstimo, por exemplo, envolve:

```text
INSERT empréstimo
+
UPDATE disponibilidade do livro
```

As duas operações deverão funcionar juntas.

Caso uma delas falhe, a operação inteira deverá ser revertida através de `rollback`.

---

# 🔐 Configuração e segurança

Outra evolução planejada para a versão 4.0 é retirar credenciais do código-fonte.

Informações como:

```text
host
porta
nome do banco
usuário
senha
```

deverão ser armazenadas através de variáveis de ambiente.

Será utilizado um arquivo:

```text
.env
```

que não deverá ser enviado ao GitHub.

O `.gitignore` deverá conter:

```gitignore
.env
venv/
.venv/
__pycache__/
*.pyc
*.db
*.sqlite
*.sqlite3
.vscode/
```

---

# 🌐 API REST

O projeto utiliza **FastAPI** para desenvolvimento da API.

A versão 4.0 pretende aproximar as funcionalidades disponíveis pela API das funcionalidades disponíveis no sistema principal.

Entre as melhorias planejadas:

* Rotas de usuários
* Rotas de livros
* Rotas de empréstimos
* Edição de registros
* Validação de entrada com Pydantic
* Respostas HTTP adequadas
* Tratamento de registros inexistentes
* Tratamento de conflitos
* Reutilização das regras de negócio do sistema

---

# 🧪 Testes

A versão atual foi validada através de testes manuais das principais funcionalidades.

Foram testados fluxos envolvendo:

* Conexão com PostgreSQL
* Cadastro de livros
* Listagem de livros
* Remoção
* Cadastro de usuários
* Empréstimos
* Disponibilidade
* Devoluções
* Relatórios
* Menus

A versão 4.0 pretende iniciar a implementação de **testes automatizados**, principalmente para regras de negócio críticas.

---

# 🛠️ Tecnologias utilizadas

* 🐍 Python
* 🐘 PostgreSQL
* 🔌 Psycopg
* ⚡ FastAPI
* 📦 Pydantic
* 📄 SQL
* 🔗 Git
* 🐙 GitHub

---

# 📦 Dependências

As dependências do projeto estão registradas em:

```text
requirements.txt
```

Para instalá-las:

```bash
pip install -r requirements.txt
```

É recomendado utilizar um ambiente virtual.

No Windows:

```bash
python -m venv venv
```

Ativação:

```bash
venv\Scripts\activate
```

Depois:

```bash
pip install -r requirements.txt
```

---

# ▶️ Executando o sistema

Com o ambiente virtual ativado:

```bash
python main.py
```

---

# 🌐 Executando a API

Com as dependências instaladas:

```bash
uvicorn app.api:app --reload
```

A documentação automática poderá ser acessada através de:

```text
http://127.0.0.1:8000/docs
```

---

# 📈 Evolução do projeto

## 🟢 Versão 1.0

Primeira implementação do sistema.

Principais características:

* Cadastro de livros
* Gerenciamento básico da biblioteca
* Programação Orientada a Objetos
* Primeiros contatos com persistência

---

## 🔵 Versão 2.0

Expansão do sistema e utilização de banco de dados relacional.

Principais evoluções:

* SQLite3
* Cadastro de usuários
* Sistema de empréstimos
* Sistema de devoluções
* Controle de disponibilidade
* Foreign Keys
* Relacionamentos entre tabelas
* Consultas com JOIN
* Sistema de relatórios
* FastAPI
* Pydantic
* API REST

---

## 🟣 Versão 3.0

Migração e reorganização da aplicação.

Principais evoluções:

* Migração de SQLite3 para PostgreSQL
* Integração com Psycopg
* Criação de `schema.sql`
* Utilização de `IDENTITY`
* Utilização do tipo `BOOLEAN` do PostgreSQL
* Manutenção dos relacionamentos através de Foreign Keys
* Reorganização da estrutura de diretórios
* Separação do fluxo de relatórios
* Correção dos imports após reorganização
* Criação do `.gitignore`
* Criação do `requirements.txt`
* Remoção da dependência do arquivo SQLite
* Adaptação das queries para PostgreSQL
* Correções nos fluxos de empréstimos e devoluções
* Testes funcionais após a migração

---

## 🚀 Versão 4.0 — Em desenvolvimento

A versão 4.0 tem como objetivo transformar o projeto em uma aplicação backend mais estruturada, segura, amigável e próxima de um sistema real.

### Experiência de uso

* [ ] Reduzir dependência de IDs
* [ ] Implementar pesquisa e seleção de usuários
* [ ] Implementar pesquisa e seleção de livros
* [ ] Melhorar seleção de empréstimos para devolução

### CRUD

* [ ] Implementar edição de usuários
* [ ] Implementar edição de livros
* [ ] Completar CRUD das principais entidades

### Empréstimos

* [ ] Adicionar data do empréstimo
* [ ] Adicionar prazo de devolução
* [ ] Adicionar data efetiva de devolução
* [ ] Implementar status
* [ ] Manter histórico
* [ ] Remover `DELETE` da operação de devolução
* [ ] Identificar empréstimos atrasados

### Banco de dados

* [ ] Evoluir `schema.sql`
* [ ] Melhorar transações
* [ ] Implementar rollback
* [ ] Melhorar tratamento de erros PostgreSQL

### Arquitetura

* [ ] Separar persistência e apresentação
* [ ] Reduzir responsabilidades de `banco_de_dados.py`
* [ ] Centralizar regras de negócio
* [ ] Reutilizar regras entre terminal e API
* [ ] Padronizar nomes e retornos das funções

### Segurança

* [ ] Criar `.env`
* [ ] Remover credenciais do código
* [ ] Adicionar `.env` ao `.gitignore`
* [ ] Configurar variáveis de ambiente

### API

* [ ] Revisar endpoints
* [ ] Expandir CRUD pela API
* [ ] Criar endpoints de empréstimos
* [ ] Melhorar schemas Pydantic
* [ ] Utilizar códigos HTTP adequados
* [ ] Melhorar tratamento de erros

### Relatórios

* [ ] Histórico de empréstimos
* [ ] Empréstimos ativos
* [ ] Empréstimos atrasados
* [ ] Livros mais emprestados
* [ ] Usuários com mais empréstimos
* [ ] Histórico por usuário
* [ ] Histórico por livro

### Qualidade

* [ ] Implementar testes automatizados
* [ ] Revisar duplicações
* [ ] Melhorar tratamento de exceções
* [ ] Atualizar documentação
* [ ] Realizar bateria final de testes

---

# 🧹 Refatorações identificadas

Algumas melhorias já foram identificadas para a versão 4.0.

Entre elas:

```text
pecorrer_livros()
```

deverá ser padronizado para um nome mais descritivo, como:

```text
listar_livros()
```

A função de devolução também poderá deixar de receber `id_livro`, pois o próprio empréstimo permite identificar o livro relacionado.

As funções de acesso ao banco deverão gradualmente deixar de realizar `print()` diretamente.

O objetivo é chegar ao fluxo:

```text
PostgreSQL
    ↓
Consulta
    ↓
Dados
    ↓
Regra de negócio
    ↓
Terminal ou API
```

---

# 🧠 Conceitos aplicados

Durante o desenvolvimento do projeto foram aplicados:

* Programação Orientada a Objetos
* Classes
* Objetos
* Métodos
* Funções
* Modularização
* PostgreSQL
* Psycopg
* SQL
* CRUD
* Primary Key
* Foreign Key
* `IDENTITY`
* `BOOLEAN`
* Relacionamentos
* `INNER JOIN`
* `LEFT JOIN`
* `SELECT`
* `INSERT`
* `UPDATE`
* `DELETE`
* `WHERE`
* `ORDER BY`
* `COUNT`
* `GROUP BY`
* Consultas parametrizadas
* Transações
* FastAPI
* Pydantic
* APIs REST
* Git
* GitHub

---

# 🎯 Objetivo da versão 4.0

A versão 4.0 não tem como objetivo apenas adicionar mais funcionalidades.

O principal objetivo é evoluir o projeto de um sistema funcional de estudos para uma aplicação backend mais organizada e preparada para crescimento.

A evolução será baseada em quatro princípios:

```text
Funcionalidade
+
Usabilidade
+
Organização
+
Confiabilidade
```

O PostgreSQL continuará sendo utilizado diretamente através do Psycopg, permitindo aprofundar os conhecimentos de SQL antes da adoção futura de uma ORM.

---

# 👨‍💻 Desenvolvimento

Projeto desenvolvido como parte dos estudos práticos de **Python, PostgreSQL, SQL, Programação Orientada a Objetos, FastAPI, APIs REST e desenvolvimento backend**.

**Projeto Biblioteca — Versão 4.0 em desenvolvimento 🚀**
