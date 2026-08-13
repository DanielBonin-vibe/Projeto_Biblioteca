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

cursor.execute("""
CREATE TABLE IF NOT EXISTS emprestimos(
    id_emprestimo INTERGER PRIMARY KEY AUTOINCREMENT,
    id_usuario INTERGER NOT NULL,
    id_livro INTERGER NOT NULL):
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
    VALUES(?, ?, ?, ?) 
    """,(usuario.nome, usuario.idade, usuario.cpf, usuario.numero))

    conexao.commit()
    conexao.close()

def remover_usuario(usuario):
    conexao = sqlite3.connect('database/biblioteca.db')
    cursor = conexao.cursor()

    cursor.execute("""
    DELETE FROM usuarios
    WHERE id_usuario = ?
    """,(usuario,))

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
    """, (livro.titulo, livro.autor, livro.ano, livro.disponivel))

    conexao.commit()
    conexao.close()

def apagar_livro(livro):
    conexao = sqlite3.connect('database/biblioteca.db')
    cursor = conexao.cursor()

    cursor.execute(
        """
        DELETE FROM livros
        WHERE id_livro = ?
        """,(livro,))

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

##################################################################################
# Filtros:

def filtrar__livro_ano():
    conexao = sqlite3.connect('database/biblioteca.db')
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT ano, COUNT(*) FROM livros
        GROUP BY ano
        ORDER BY ano;
    """)

    filtro = cursor.fetchall()

    for ano, quantidade in filtro:
        print(f'{ano} -> {quantidade} livros(s)')


    conexao.commit()
    conexao.close()

def filtrar_livro_ordem_alfabetica():
    conexao = sqlite3.connect('database/biblioteca.db')
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM livros 
    ORDER BY nome ASC
    """)

    filtro = cursor.fetchall()

    for livro in filtro:
        print(f"""
            ID: {livro[0]}
            Nome: {livro[1]}
            Autor: {livro[2]}
            Ano: {livro[3]}
            Disponibilidade: {livro[4]}
            """)

    conexao.commit()
    conexao.close()


def filtrar_encontrar_livro_nome(nome_pesquisado):
    conexao = sqlite3.connect('database/biblioteca.db')
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM livros
    WHERE nome LIKE  ?
    """, (f'%{nome_pesquisado}%',)
    )

    filtro = cursor.fetchall()

    for livro in filtro:
        print(f"""
            ID: {livro[0]}
            Nome: {livro[1]}
            Autor: {livro[2]}
            Ano: {livro[3]}
            Disponibilidade: {livro[4]}
            """)

    conexao.commit()
    conexao.close()

####################################################################################
def cadastrar_emprestimo(id_usuario, id_livro):
    conexao = sqlite3.connect('database/biblioteca.db')
    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO emprestimos (id_usuario, id_livro)
    VALUES (?, ?)
    """, (id_usuario, id_livro))

    cursor.execute("""
        UPDATE livros
        SET disponivel = 0
        WHERE id_livro = ?
    """, (id_livro,))
    # Aqui fazemos que ao ser emprestado, o valor se torne 0

    conexao.commit()
    conexao.close()

def listar_emprestimos():
    conexao = sqlite3.connect('database/biblioteca.db')
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT usuarios.nome, livros.titulo FROM emprestimos 
    INNER JOIN usuarios
        ON emprestimos.id_usuario = usuarios.id_usuario 
        ON emprestimos.id_livro = livros.id_livro
    """)

    emprestimos = cursor.fetchall()

    for emprestimo in emprestimos:
        print(f'Usuário: {emprestimo[0]}')
        print(f'Livro: {emprestimo[1]}')
        print('----------------')

    conexao.commit()
    conexao.close()

def devolver_emprestimo(id_emprestimo):
    conexao = sqlite3.connect('database/biblioteca.db')
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT id_livro FROM emprestimos
    WHERE id_emprestimo = ?
    """, (id_emprestimo,))
    # Estamos descobrindo qual livro pertence áqeuele empréstimo

    emprestimo = cursor.fetchall()

    if emprestimo:
        id_livro = emprestimo[0]

    cursor.execute("""
    UPDATE livros
    SET disponivel = 1
    WHERE id_livro = ?
    """, (id_livro,))
    # Marcamos o livro como disponível

    cursor.execute("""
        DELETE FROM emprestimos
        WHERE id_emprestimo = ?
    """, (id_emprestimo))
    # retiramos o empréstimo da tabela

    conexao.commit()
    conexao.close()