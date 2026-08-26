# 📚 Sistema de Gerenciamento de Biblioteca

Sistema de gerenciamento de biblioteca desenvolvido em **Python**, utilizando **PostgreSQL** como banco de dados e seguindo uma arquitetura progressivamente organizada em camadas.

O projeto foi criado com objetivo educacional para aplicar, na prática, conhecimentos de **Python, Programação Orientada a Objetos, SQL, PostgreSQL, APIs REST e desenvolvimento backend**.

Atualmente, o projeto encontra-se na **Versão 4.0**, marcada principalmente pela evolução da arquitetura, segurança, regras de negócio e persistência dos dados.

---

# 🎯 Objetivo do projeto

O principal objetivo do Projeto Biblioteca é consolidar conhecimentos de desenvolvimento backend através da construção e evolução contínua de um sistema real.

Durante o desenvolvimento são trabalhados conceitos como:

* Python
* Programação Orientada a Objetos
* PostgreSQL
* SQL
* CRUD
* Chaves primárias e estrangeiras
* Relacionamentos entre tabelas
* Consultas parametrizadas
* Transações
* Arquitetura em camadas
* Repository Pattern
* Service Layer
* Variáveis de ambiente
* FastAPI
* Pydantic
* APIs REST
* Git
* GitHub

---

# ✨ Funcionalidades

## 👤 Usuários

O sistema permite:

* Cadastrar usuários
* Listar usuários
* Atualizar informações
* Remover usuários
* Ordenar usuários por nome
* Ordenar usuários por ID
* Gerar relatórios
* Identificar usuários com empréstimos
* Identificar usuários sem empréstimos

### CRUD de usuários

```text
Create ✅
Read   ✅
Update ✅
Delete ✅
```

---

# 📚 Livros

O sistema permite:

* Cadastrar livros
* Listar livros
* Atualizar informações
* Remover livros
* Pesquisar livros pelo título
* Ordenar livros por ano
* Ordenar livros alfabeticamente
* Ordenar livros por ID
* Ordenar por autor
* Controlar disponibilidade
* Listar livros disponíveis
* Listar livros indisponíveis
* Consultar quantidade total de livros

### CRUD de livros

```text
Create ✅
Read   ✅
Update ✅
Delete ✅
```

A disponibilidade não é alterada manualmente durante uma edição.

Ela é controlada automaticamente pelas regras de empréstimo:

```text
Livro cadastrado
      ↓
disponivel = TRUE

Livro emprestado
      ↓
disponivel = FALSE

Livro devolvido
      ↓
disponivel = TRUE
```

---

# 🔄 Empréstimos

O módulo de empréstimos relaciona usuários e livros através de chaves estrangeiras.

O sistema permite:

* Realizar empréstimos
* Verificar existência do livro
* Verificar disponibilidade
* Registrar automaticamente a data do empréstimo
* Tornar o livro indisponível
* Listar empréstimos ativos
* Realizar devoluções
* Registrar a data da devolução
* Alterar o status do empréstimo
* Restaurar a disponibilidade do livro
* Preservar o histórico das operações

---

# 🕒 Histórico de empréstimos

A partir da versão 4.0, os empréstimos deixaram de ser apagados após uma devolução.

Anteriormente:

```text
Empréstimo
    ↓
Devolução
    ↓
DELETE
```

Agora:

```text
Empréstimo
    ↓
status = ativo
    ↓
Devolução
    ↓
status = devolvido
data_devolucao = data atual
    ↓
Registro permanece no banco
```

Isso permite preservar todo o histórico da biblioteca.

A tabela de empréstimos possui:

```text
id_emprestimo
id_usuario
id_livro
data_emprestimo
data_devolucao
status
```

---

# 🗄️ PostgreSQL

O projeto utiliza **PostgreSQL** como sistema gerenciador de banco de dados.

A comunicação entre Python e PostgreSQL é realizada através do:

```text
Psycopg
```

O PostgreSQL substituiu completamente o SQLite utilizado nas primeiras versões do projeto.

---

# 🧱 Modelagem do banco

As principais entidades são:

```text
USUÁRIOS
    │
    │ id_usuario
    ▼
EMPRÉSTIMOS
    ▲
    │ id_livro
    │
LIVROS
```

## Tabela `usuarios`

```text
id_usuario
nome
idade
cpf
numero
```

## Tabela `livros`

```text
id_livro
titulo
autor
ano
disponivel
```

## Tabela `emprestimos`

```text
id_emprestimo
id_usuario
id_livro
data_emprestimo
data_devolucao
status
```

---

# 🔗 Relacionamentos

A tabela `emprestimos` relaciona usuários e livros através de Foreign Keys.

```sql
FOREIGN KEY (id_usuario)
REFERENCES usuarios(id_usuario)
```

```sql
FOREIGN KEY (id_livro)
REFERENCES livros(id_livro)
```

Isso garante integridade entre os registros do sistema.

---

# 🔑 IDs automáticos

As chaves primárias utilizam `IDENTITY` do PostgreSQL.

Exemplo:

```sql
id_livro INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY
```

Dessa forma, os IDs são gerados automaticamente pelo próprio banco.

---

# 📅 Datas automáticas

Ao realizar um empréstimo, o PostgreSQL registra automaticamente sua data e horário:

```sql
data_emprestimo TIMESTAMP
NOT NULL
DEFAULT CURRENT_TIMESTAMP
```

Enquanto o livro não for devolvido:

```text
data_devolucao = NULL
status = ativo
```

Na devolução:

```text
data_devolucao = CURRENT_TIMESTAMP
status = devolvido
```

---

# 🔐 Variáveis de ambiente

A partir da versão 4.0, as credenciais do PostgreSQL não ficam mais armazenadas diretamente no código-fonte.

O projeto utiliza:

```text
python-dotenv
```

e um arquivo:

```text
.env
```

Exemplo:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=projeto_biblioteca
DB_USER=postgres
DB_PASSWORD=sua_senha
```

O arquivo `.env` está incluído no `.gitignore` e **não deve ser enviado para o GitHub**.

---

# 🔌 Conexão com PostgreSQL

A conexão utiliza as variáveis carregadas do ambiente:

```python
import os

import psycopg
from dotenv import load_dotenv


load_dotenv()


def conectar():
    return psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )
```

---

# 🔄 Transações

Operações importantes utilizam transações para garantir consistência dos dados.

Um empréstimo envolve:

```text
INSERT empréstimo
+
UPDATE disponibilidade do livro
```

Uma devolução envolve:

```text
UPDATE disponibilidade do livro
+
UPDATE empréstimo
```

Se todas as operações funcionarem:

```python
conexao.commit()
```

Se algum erro ocorrer:

```python
conexao.rollback()
```

Isso impede que apenas parte de uma operação seja gravada.

---

# 🏗️ Arquitetura

A versão 4.0 introduziu uma divisão mais clara de responsabilidades.

O fluxo principal da aplicação é:

```text
main.py
   ↓
Biblioteca
   ↓
Services
   ↓
Repositories
   ↓
PostgreSQL
```

---

# 🧠 Service Layer

Os **services** concentram regras de negócio e interpretam os resultados recebidos dos repositories.

Exemplos:

```text
emprestimos_service
livros_service
usuarios_service
```

Responsabilidades:

```text
Service
→ valida regras
→ interpreta resultados
→ decide se uma operação pode continuar
```

Exemplo:

```text
O livro existe?
      ↓
Está disponível?
      ↓
Pode ser emprestado?
```

---

# 🗃️ Repository Layer

Os repositories são responsáveis pelo acesso ao PostgreSQL.

Eles concentram operações como:

```text
SELECT
INSERT
UPDATE
DELETE
COMMIT
ROLLBACK
```

A estrutura utiliza repositories separados para cada domínio:

```text
usuarios_repository
livros_repository
emprestimos_repository
relatorios_repository
```

Responsabilidade:

```text
Repository
→ acessar e modificar dados
```

---

# 🧩 Separação de responsabilidades

A arquitetura segue a ideia:

```text
Interface
   ↓
Regra de negócio
   ↓
Persistência
```

Ou:

```text
Biblioteca
→ interação e apresentação

Services
→ regras de negócio

Repositories
→ SQL e PostgreSQL
```

Essa separação reduz o acoplamento e facilita futuras expansões da aplicação.

---

# 📁 Estrutura do projeto

A estrutura atual é organizada aproximadamente da seguinte forma:

```text
Projeto_Biblioteca/
│
├── database/
│   ├── __init__.py
│   ├── conexao_postgre.py
│   ├── usuarios_repository.py
│   ├── livros_repository.py
│   ├── emprestimos_repository.py
│   └── schema.sql
│
├── models/
│   ├── __init__.py
│   ├── biblioteca.py
│   ├── livro.py
│   └── usuario.py
│
├── services/
│   ├── __init__.py
│   ├── usuarios_service.py
│   ├── livros_service.py
│   └── emprestimos_service.py
│
├── relatorios/
│   ├── __init__.py
│   ├── relatorios.py
│   └── relatorios_repository.py
│
├── utils/
│   ├── __init__.py
│   └── menu.py
│
├── app/
│   └── api.py
│
├── .env
├── .gitignore
├── requirements.txt
├── main.py
└── README.md
```

---

# 📊 Relatórios

O projeto possui relatórios baseados em consultas SQL.

São utilizados conceitos como:

```sql
SELECT
WHERE
ORDER BY
COUNT
GROUP BY
INNER JOIN
LEFT JOIN
```

## Relatórios de livros

* Total de livros
* Listagem completa
* Ordenação por título
* Ordenação por ID
* Ordenação por autor
* Livros disponíveis
* Livros indisponíveis

## Relatórios de usuários

* Listagem completa
* Ordenação alfabética
* Ordenação por ID
* Usuários com empréstimos
* Usuários sem empréstimos

---

# 📄 Schema SQL

A estrutura necessária para criação das tabelas está armazenada em:

```text
database/schema.sql
```

Isso permite recriar o banco de dados em outra máquina sem depender de arquivos locais de banco.

---

# 📦 Dependências

As dependências utilizadas pelo projeto estão registradas em:

```text
requirements.txt
```

Para instalar:

```bash
pip install -r requirements.txt
```

---

# 🐍 Ambiente virtual

É recomendado utilizar um ambiente virtual.

Criando:

```bash
python -m venv venv
```

No Windows:

```bash
venv\Scripts\activate
```

Depois:

```bash
pip install -r requirements.txt
```

---

# ▶️ Executando a aplicação

Com o ambiente virtual ativado:

```bash
python main.py
```

---

# ⚡ FastAPI

O projeto possui uma implementação inicial utilizando **FastAPI** e **Pydantic**.

A API foi introduzida em versões anteriores e será o principal foco da próxima grande evolução do projeto.

A arquitetura construída na versão 4.0 prepara a aplicação para que tanto o terminal quanto a API possam reutilizar os mesmos services e regras de negócio.

---

# 🚀 Roadmap — Versão 5.0

A versão 5.0 terá foco principal na evolução da **API REST**.

Entre os objetivos planejados estão:

* [ ] Reorganizar a estrutura da FastAPI
* [ ] Separar rotas com routers
* [ ] Criar rotas completas de usuários
* [ ] Criar rotas completas de livros
* [ ] Criar rotas de empréstimos
* [ ] Criar rota de devolução
* [ ] Disponibilizar histórico de empréstimos
* [ ] Integrar a API aos services
* [ ] Criar schemas Pydantic de entrada e saída
* [ ] Utilizar códigos HTTP adequados
* [ ] Melhorar tratamento de erros
* [ ] Implementar testes automatizados
* [ ] Testar endpoints
* [ ] Melhorar documentação automática
* [ ] Revisar e expandir relatórios

---

# 🧪 Testes

Até a versão 4.0, os principais fluxos foram validados através de testes manuais.

Foram testados:

* Conexão com PostgreSQL
* Cadastro de usuários
* Atualização de usuários
* Remoção de usuários
* Listagem de usuários
* Cadastro de livros
* Atualização de livros
* Remoção de livros
* Listagem de livros
* Filtros
* Empréstimos
* Disponibilidade
* Devoluções
* Histórico
* Menus
* Relatórios
* Services
* Repositories

A implementação de testes automatizados está planejada para uma próxima etapa do projeto.

---

# 🛠️ Tecnologias utilizadas

* 🐍 Python
* 🐘 PostgreSQL
* 🔌 Psycopg
* ⚡ FastAPI
* 📦 Pydantic
* 🔐 python-dotenv
* 📄 SQL
* 🔗 Git
* 🐙 GitHub

---

# 🧠 Conceitos aplicados

Durante o desenvolvimento foram utilizados:

* Programação Orientada a Objetos
* Classes
* Objetos
* Métodos
* Funções
* Modularização
* Arquitetura em camadas
* Repository Pattern
* Service Layer
* PostgreSQL
* Psycopg
* SQL
* CRUD completo
* Primary Key
* Foreign Key
* `IDENTITY`
* `BOOLEAN`
* `TIMESTAMP`
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
* `commit`
* `rollback`
* Variáveis de ambiente
* FastAPI
* Pydantic
* APIs REST
* Git
* GitHub

---

# 📈 Evolução do projeto

## 🟢 Versão 1.0

Primeira versão do sistema.

Principais características:

* Python
* Programação Orientada a Objetos
* Cadastro básico de livros
* Classes e objetos
* Estrutura inicial da biblioteca

---

## 🔵 Versão 2.0

Expansão para banco de dados e API.

Principais evoluções:

* SQLite3
* SQL
* Usuários
* Empréstimos
* Devoluções
* Controle de disponibilidade
* Foreign Keys
* Relacionamentos
* JOIN
* Relatórios
* FastAPI
* Pydantic
* API REST inicial

---

## 🟣 Versão 3.0

Migração da infraestrutura de dados.

Principais evoluções:

* Migração de SQLite3 para PostgreSQL
* Integração com Psycopg
* Criação de `schema.sql`
* Uso de `IDENTITY`
* Uso de `BOOLEAN`
* Reorganização da estrutura
* Separação inicial dos módulos
* Criação de `.gitignore`
* Criação de `requirements.txt`
* Adaptação das consultas para PostgreSQL
* Correções nos fluxos
* Estabilização da aplicação

---

## 🟠 Versão 4.0

Refatoração estrutural e evolução das regras de negócio.

Principais mudanças:

* Credenciais protegidas através de `.env`
* Integração com `python-dotenv`
* Uso de variáveis de ambiente
* Implementação de transações
* Uso de `commit()` e `rollback()`
* Histórico permanente de empréstimos
* Registro automático de data de empréstimo
* Registro de data de devolução
* Status de empréstimos
* Fim da exclusão do histórico durante devoluções
* CRUD completo de usuários
* CRUD completo de livros
* Separação do acesso ao banco através de repositories
* Criação da camada de services
* Separação entre regras de negócio e persistência
* Services de livros
* Services de usuários
* Services de empréstimos
* Reorganização das responsabilidades internas
* Correção e padronização dos fluxos
* Testes manuais das principais funcionalidades

### Resumo da versão 4.0

> **Refatoração estrutural do sistema com `.env`, transações e `rollback`, histórico de empréstimos, CRUD completo, separação em repositories e criação da camada de services para centralizar as regras de negócio.**

---

# 🎯 Próxima etapa

A arquitetura atual prepara o projeto para a versão 5.0.

O próximo grande objetivo será evoluir a API para aproveitar:

```text
FastAPI
   ↓
Services
   ↓
Repositories
   ↓
PostgreSQL
```

Permitindo que terminal e API utilizem as mesmas regras de negócio.

---

# 👨‍💻 Desenvolvimento

Projeto desenvolvido como parte dos estudos práticos de:

**Python • PostgreSQL • SQL • Programação Orientada a Objetos • Arquitetura Backend • FastAPI • APIs REST**

---

**📚 Projeto Biblioteca — Versão 4.0**

