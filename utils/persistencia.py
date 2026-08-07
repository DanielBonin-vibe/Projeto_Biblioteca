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

def remover_usuario(usuario):
    conexao = sqlite3.connect('database/biblioteca.db')
    cursor = conexao.cursor()

    cursor.execute("""
    DELETE FROM usuarios
    WHERE id_usuario = ?
    """,
    (usuario,)
    )

    conexao.commit()
    conexao.close()

def listar_usuarios():
    conexao = sqlite3.connect('database/biblioteca.db')
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM usuarios
    """)

    usuarios = cursor.fetchall()

    for usuario in usuarios:
        print(f"""
        ID: {usuario[0]}
        Nome: {usuario[1]}
        Idade: {usuario[2]}
        CPF: {usuario[3]}
        Telefone: {usuario[4]}
        ----------------------
              """)

    conexao.close()

def cadastrar_livro(livro):
    conexao = sqlite3.connect('database/biblioteca.db')
    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO livros(titulo, autor, ano, disponivel)
    VALUES(?, ?, ?, ?)
    """, (livro.titulo, livro.autor, livro.ano, livro.disponivel)
    )

    conexao.commit()
    conexao.close()

def apagar_livro(livro):
    conexao = sqlite3.connect('database/biblioteca.db')
    cursor = conexao.cursor()

    cursor.execute(
        """
        DELETE FROM livros
        WHERE id_livro = ?
        """,
        (livro,) 
        )

    conexao.commit()
    conexao.close()

def pecorrer_livros():
    conexao = sqlite3.connect('database/biblioteca.db')
    cursor = conexao.cursor()

    cursor.execute(""" SELECT * FROM livros""")

    livros = cursor.fetchall()

    for livro in livros:
        print(f"""
        ID: {livro[0]}
        Título: {livro[1]}
        Autor: {livro[2]}
        Ano: {livro[3]}
        Disponibilidade: {livro[4]}
        """)

    conexao.commit()
    conexao.close()

def contar_livros():
    conexao = sqlite3.connect('database/biblioteca.db')
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT COUNT(*) FROM livros
    """)

    quantidade = cursor.fetchall()[0]   # O COUNT retorna apenas uma linha, é vital colcoar o fetchall()[0]
    print(f'A quantidade de livros em nossa biblioteca é {quantidade}')

    conexao.commit()
    conexao.close()


