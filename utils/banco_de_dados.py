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
    id_emprestimo INTERGER PRIMARY KEY,
    id_usuario INTERGER NOT NULL,
    id_livro INTERGER NOT NULL,

    FOREIGN KEY(id_usuario) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (id_livro) REFERENCES livros(id_livro))
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
    
    conexao.close()

    return usuarios

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

    return livros

    conexao.close()

def contar_livros():
    conexao = sqlite3.connect('database/biblioteca.db')
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT COUNT(*) FROM livros
    """)

    quantidade = cursor.fetchall()[0]   # O COUNT retorna apenas uma linha, é vital colcoar o fetchall()[0]

    conexao.close()

    return {'Quantidade': quantidade}

##################################################################################
# Filtros:

def filtrar_livro_ano():
    conexao = sqlite3.connect('database/biblioteca.db')
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT ano, COUNT(*) FROM livros
        GROUP BY ano
        ORDER BY ano;
    """)

    filtro = cursor.fetchall()

    conexao.close()

    return filtro 

def filtrar_livro_ordem_alfabetica():
    conexao = sqlite3.connect('database/biblioteca.db')
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM livros 
    ORDER BY nome ASC
    """)

    filtro = cursor.fetchall()

    conexao.close()

    return filtro

def filtrar_encontrar_livro_nome(nome_pesquisado):
    conexao = sqlite3.connect('database/biblioteca.db')
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM livros
    WHERE nome LIKE  ?
    """, (f'%{nome_pesquisado}%',)
    )

    filtro = cursor.fetchall()

    conexao.close()

    return filtro

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

    conexao.close()

    return emprestimos



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

#####################################################################
# Relatórios livro:

def relatorio_livro_total():
    conexao = sqlite3.connect('database/biblioteca.db')
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT COUNT(*) FROM livro
    """)

    contagem = cursor.fetchone()
    print(f'O total de livros cadastrados é: {contagem}')

    cursor.execute("""
    SELECT * FROM livro
    """)

    resultado = cursor.fetchall()

    for livro in resultado:
        print(f'ID: {livro[0]}')
        print(f'Título: {livro[1]}')
        print(f'Autor: {livro[2]}')
        print(f'Ano: {livro[3]}')
        print(f'Disponível: {livro[4]}')

    conexao.close()

def relatorio_livro_ordem_alfabetica():
    conexao = sqlite3.connect('database/biblioteca.db')
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM livro
    ORDER BY titulo ASC
    """)

    resultado = cursor.fetchall()

    for livro in resultado:
        print(f'ID: {livro[0]}')
        print(f'Título: {livro[1]}')
        print(f'Autor: {livro[2]}')
        print(f'Ano: {livro[3]}')
        print(f'Disponível: {livro[4]}')

    conexao.close()

def relatorio_id_livro():
    conexao = sqlite3.connect('database/biblioteca')
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM livro
    ORDER BY id_livro ASC
    """)

    resultado = cursor.fetchall()

    for livro in resultado:
        print(f'ID: {livro[0]}')
        print(f'Título: {livro[1]}')
        print(f'Autor: {livro[2]}')
        print(f'Ano: {livro[3]}')
        print(f'Disponível: {livro[4]}')

    conexao.close()

def relatorio_autor_livro():
    conexao = sqlite3.connect('database/biblioteca')
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM livros
    ORDER BY autor ASC
    """)

    resultado = cursor.fetchall()

    for livro in resultado:
        print(f'Autor: {livro[2]}')
        print(f'ID: {livro[0]}')
        print(f'Título: {livro[1]}')
        print(f'Ano: {livro[3]}')
        print(f'Disponível: {livro[4]}')

    conexao.close()

def relatorio_disponivel_livro():
    conexao = sqlite3.connect('database/biblioteca')
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM livros
    WHERE disponivel = 1
    ORDER BY id_livro ASC
    """)

    resultado = cursor.fetchall()

    for livro in resultado:
        print(f'ID: {livro[0]}')
        print(f'Título: {livro[1]}')
        print(f'Autor: {livro[2]}')
        print(f'Ano: {livro[3]}')
        print(f'Disponível: {livro[4]}')
        print('-------------------')

    conexao.close()

def relatorio_indisponivel_livro():
    conexao = sqlite3.connect('database/biblioteca')
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM emprestimos
    WHERE disponivel = 0
    ORDER BY id_livro ASC
    """)

    resultado = cursor.fetchall()

    for livro in resultado:
        print(f'ID: {livro[0]}')
        print(f'Título: {livro[1]}')
        print(f'Autor: {livro[2]}')
        print(f'Ano: {livro[3]}')
        print(f'Disponível: {livro[4]}')
        print('-------------------')

    conexao.close()

##############################################################
# Relatórios Usuários:

def relatorio_padrao_usuario():
    conexao = sqlite3.connect('database/biblioteca')
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM usuarios
    """)

    resultado = cursor.fetchall()

    for usuario in resultado:
        print(f'ID: {usuario[0]}')
        print(f'NOME: {usuario[1]}')
        print(f'IDADE: {usuario[2]}')
        print(f'CPF: {usuario[3]}')
        print(f'NUMERO: {usuario[4]}')

    conexao.close()

def relatorio_ordem_alfabetica_usuario():
    conexao = sqlite3.connect('database/biblioteca')
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM usuarios
    ORDER BY nome ASC
    """)

def relatorio_id_usuario():
    conexao = sqlite3.connect('database/biblioteca')
    cursor = conexao.cursor()

    cursor.execut("""
    SELECT * FROM usuarios
    ORDER BY id_usuario ASC
    """)

    resultado = cursor.fetchall()

    for usuario in resultado:
        print(f'ID: {usuario[0]}')
        print(f'NOME: {usuario[1]}')
        print(f'IDADE: {usuario[2]}')
        print(f'CPF: {usuario[3]}')
        print(f'NUMERO: {usuario[4]}')

    conexao.close()

def relatorio_usuario_emprestimo():
    conexao = sqlite3.connect('database/biblioteca')
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT usuarios.nome,
    COUNT(emprestimos.id_emprestimo) FROM usuarios
    INNER JOIN emprestimos
        ON usuarios.id_usuario = emprestimos.id_usuario
    GROUP BY usuarios.id_usuario
    ORDER BY COUNT(emprestimos.id_emprestimo) DESC
    """)
    # INNER JOIN não retorna valores nulos

    resultado = cursor.fetchall()

    for usuario in resultado:
        print(f'Usuário: {usuario[0]}')
        print(f'Empréstimos: {usuario[1]}')
        print('--------------------')

    conexao.close()

def relatorio_usuario_sem_emprestimo():
    conexao = sqlite3.connect('database/biblioteca')
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT usuarios.nome FROM usuarios
    LEFT JOIN emprestimos
        ON usuarios.id_usuario = emprestimos.id_usuario
    WHERE emprestimos.id_usuario IS NULL
    """)
    # LEFT JOIN retorna valores que podem ser Nulos

    resultado = cursor.fetchall()

    for usuario in resultado:
        print(f'Usuário: {usuario[0]}')

    conexao.close()