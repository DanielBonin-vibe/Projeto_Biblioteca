📚 Sistema de Gerenciamento de Biblioteca

Sistema desenvolvido em Python para gerenciamento de uma biblioteca, utilizando SQLite3 como banco de dados e FastAPI para criação de uma API REST.

Este projeto faz parte dos estudos práticos de Python, SQL, Banco de Dados e APIs, evoluindo progressivamente conforme novos conceitos são aprendidos.

✨ Funcionalidades

👤 Usuários

Cadastro de usuários
Listagem de usuários
Remoção de usuários
Consulta de usuários através da API
Relatórios de usuários
Ordenação por nome
Ordenação por ID
Relatório de usuários com empréstimos
Relatório de usuários sem empréstimos-

📚 Livros

Cadastro de livros
Listagem de livros
Remoção de livros
Controle de disponibilidade
Filtro por ano
Pesquisa por nome
Ordenação alfabética
Ordenação por ID
Ordenação por autor
Relatórios de livros disponíveis
Relatórios de livros indisponíveis
Relatório do total de livros

🔄 Empréstimos

Cadastro de empréstimos
Relacionamento entre usuários e livros
Controle automático da disponibilidade do livro
Listagem de empréstimos
Devolução de livros
Atualização da disponibilidade após a devolução

📊 Relatórios
O sistema possui um menu próprio para geração de relatórios, permitindo analisar informações dos livros e usuários.

Entre os conceitos utilizados estão:

COUNT()
GROUP BY
ORDER BY
WHERE
INNER JOIN
LEFT JOIN

🛠️ Tecnologias utilizadas

  🐍 Python
  ⚡ FastAPI
  🗄️ SQLite3
  📦 Pydantic
  📄 SQL
  🔗 Git / GitHub
  📁 Estrutura do projeto

  
Projeto_Biblioteca/
│
├── main.py
├── menu.py
├── banco_de_dados.py
│
├── database/
│   └── biblioteca.db
│
└── README.md
Responsabilidade dos arquivos

# main.py

Inicialização da aplicação FastAPI
Definição das rotas
Modelos utilizados pela API

# banco_de_dados.py

Conexão com SQLite
Operações no banco de dados
Consultas SQL
Cadastro, alteração e remoção de registros
Funções de relatórios

# menu.py

Menus do sistema
Navegação pelas funcionalidades
Menu de relatórios

# database/biblioteca.db
Banco de dados SQLite utilizado pelo projeto.

▶️ Como executar

1. Clone o repositório
  git clone <URL_DO_REPOSITORIO>
2. Entre na pasta do projeto
  cd Projeto_Biblioteca
3. Instale as dependências
  pip install fastapi uvicorn
4. Execute a API
  uvicorn main:app --reload

A API estará disponível localmente.

📖 Documentação da API

Com o servidor executando, acesse a documentação automática do FastAPI:

/docs

Exemplo:

http://127.0.0.1:8000/docs
🗃️ Banco de Dados

O projeto utiliza SQLite3 e possui relacionamento entre as principais entidades:

USUÁRIOS
   │
   │ id_usuario
   ▼
EMPRÉSTIMOS
   ▲
   │ id_livro
   │
   ▼
LIVROS
Tabelas principais

usuarios

id_usuario
nome
idade
cpf
numero

livros

id_livro
titulo
autor
ano
disponivel

emprestimos

id_emprestimo
id_usuario
id_livro

As relações entre as tabelas são realizadas através de chaves estrangeiras (Foreign Keys).

🧠 Conceitos aplicados

Durante o desenvolvimento deste projeto foram praticados:

Programação Orientada a Objetos
Funções
Modularização
Tratamento de dados
SQLite3
SQL
CRUD
Primary Key
Foreign Key
Relacionamentos entre tabelas
INNER JOIN
LEFT JOIN
SELECT
INSERT
UPDATE
DELETE
WHERE
ORDER BY
COUNT
GROUP BY
APIs REST
FastAPI
Pydantic
Métodos HTTP
Git e GitHub

📈 Evolução do projeto

🟢 Versão 1.0
Sistema básico de biblioteca
Cadastro e gerenciamento de livros
Primeiros contatos com SQLite3 e SQL

🔵 Versão 2.0
Implementação do banco de dados relacional
Cadastro e gerenciamento de usuários
Sistema de empréstimos
Sistema de devolução
Controle de disponibilidade dos livros
Relacionamentos com Foreign Keys
Consultas utilizando JOIN
Criação de API com FastAPI
Documentação automática da API
Sistema de relatórios
Relatórios utilizando COUNT, GROUP BY, INNER JOIN e LEFT JOIN

🎯 Objetivo do projeto

O objetivo principal deste projeto é consolidar, através da prática, conhecimentos de Python, bancos de dados relacionais, SQL e desenvolvimento de APIs.

O projeto também serve como base para a criação de sistemas mais completos e para a evolução gradual da complexidade dos próximos projetos.

👨‍💻 Desenvolvimento

Projeto desenvolvido durante os estudos práticos de Python, SQL, SQLite3, FastAPI e desenvolvimento de APIs.

Biblioteca — Versão 2.0 🚀
