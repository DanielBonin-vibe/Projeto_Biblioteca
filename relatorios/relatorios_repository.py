from database.conexao_postgre import conectar

# Relatórios livro:

def relatorio_livro_total():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT COUNT(*) FROM livros
    """)

    contagem = cursor.fetchone()
    print(f'O total de livros cadastrados é: {contagem}')

    cursor.execute("""
    SELECT * FROM livros
    """)

    resultado = cursor.fetchall()

    for livro in resultado:
        print(f'ID: {livro[0]}')
        print(f'Título: {livro[1]}')
        print(f'Autor: {livro[2]}')
        print(f'Ano: {livro[3]}')
        print(f'Disponível: {livro[4]}')

    cursor.close()
    conexao.close()

    return resultado

def relatorio_livro_ordem_alfabetica():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM livros
    ORDER BY titulo ASC
    """)

    resultado = cursor.fetchall()

    for livro in resultado:
        print(f'ID: {livro[0]}')
        print(f'Título: {livro[1]}')
        print(f'Autor: {livro[2]}')
        print(f'Ano: {livro[3]}')
        print(f'Disponível: {livro[4]}')

    cursor.close()
    conexao.close()

    return resultado

def relatorio_id_livro():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM livros
    ORDER BY id_livro ASC
    """)

    resultado = cursor.fetchall()

    for livro in resultado:
        print(f'ID: {livro[0]}')
        print(f'Título: {livro[1]}')
        print(f'Autor: {livro[2]}')
        print(f'Ano: {livro[3]}')
        print(f'Disponível: {livro[4]}')

    cursor.close()
    conexao.close()

    return resultado

def relatorio_autor_livro():
    conexao = conectar()
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

    cursor.close()
    conexao.close()

    return resultado

def relatorio_disponivel_livro():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM livros
    WHERE disponivel = TRUE
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

    cursor.close()
    conexao.close()

    return resultado

def relatorio_indisponivel_livro():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM livros
    WHERE disponivel = FALSE
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

    cursor.close()
    conexao.close()

    return resultado

##############################################################
# Relatórios Usuários:

def relatorio_padrao_usuario():
    conexao = conectar()
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
        print(f'NÙMERO: {usuario[4]}')

    cursor.close()
    conexao.close()

    return resultado

def relatorio_ordem_alfabetica_usuario():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM usuarios
    ORDER BY nome ASC
    """)

    resultado = cursor.fetchall()

    for usuario in resultado:
        print(f'ID: {usuario[0]}')
        print(f'NOME: {usuario[1]}')
        print(f'IDADE: {usuario[2]}')
        print(f'CPF: {usuario[3]}')
        print(f'NÙMERO: {usuario[4]}')

    cursor.close()
    conexao.close()

    return resultado

def relatorio_id_usuario():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
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

    cursor.close()
    conexao.close()

    return resultado 

def relatorio_usuario_emprestimo():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT usuarios.nome,
    COUNT(emprestimos.id_emprestimo) FROM usuarios
    JOIN emprestimos
        ON usuarios.id_usuario = emprestimos.id_usuario
    GROUP BY usuarios.id_usuario
    ORDER BY COUNT(emprestimos.id_emprestimo) DESC
    """)

    resultado = cursor.fetchall()

    for usuario in resultado:
        print(f'Usuário: {usuario[0]}')
        print(f'Empréstimos: {usuario[1]}')
        print('--------------------')

    cursor.close()
    conexao.close()

    return resultado

def relatorio_usuario_sem_emprestimo():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT usuarios.nome FROM usuarios
    JOIN emprestimos
        ON usuarios.id_usuario = emprestimos.id_usuario
    WHERE emprestimos.id_usuario IS NULL
    """)

    resultado = cursor.fetchall()

    for usuario in resultado:
        print(f'Usuário: {usuario[0]}')

    cursor.close()
    conexao.close()

    return resultado