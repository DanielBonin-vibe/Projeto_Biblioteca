"""
import json
from models import Usuario, Livro
def salvar_usuarios(usuarios):

    dados = []

    for usuario in usuarios:
        dados.append(usuario.to_dict())

    with open('dados/usuarios.json', 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

def salvar_livros(livros):

    dados = []

    for livro in livros:
        dados.append(livro.to_dict())

    with open('dados/livros.json', 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)


def carregar_usuarios():
    with open('dados/usuarios.json', 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)

    usuarios = []

    for usuario in dados:
        usuarios.append(Usuario.from_dict(usuario))
        return usuarios


def carregar_livros():
    with open('dados/livros.json', 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)

        livros = []

    for livro in dados:
        livros.append(Livro.from_dict(livro))
        return livros
"""
############################################################
# Criação das tabelas
import sqlite3

conexao = sqlite3.connect('database/biblioteca.db')
print('Conectado')

cursor = conexao.cursor()

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS usuarios(
    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    cpf TEXT NOT NULL,
    numero TEXT NOT NULL)
    """)

cursor.execute(
    """
CREATE TABLE IF NOT EXISTS livros(
    id_livro INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano INTERGER NOT NULL,
     disponivel INTERGER NOT NULL DEFAULT 1)
    """) 

conexao.commit()
conexao.close()
######################################################

# Salvar usuários:
def salvar_usuario(usuario):
    conexao = sqlite3.connect('database/biblioteca.db')
    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO usuarios(nome, idade, cpf, numero)
    VALUES(?, ?, ?, ?) """,
    (
        usuario.nome,
        usuario.idade,
        usuario.cpf,
        usuario.numero
    )
    )

    conexao.commit()
    conexao.close()