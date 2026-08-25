from database.conexao_postgre import conectar
######################################################

# Salvar usuários:
def salvar_usuario(usuario):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO usuarios(nome, idade, cpf, numero)
    VALUES(%s, %s, %s, %s) 
    """,(usuario.nome, usuario.idade, usuario.cpf, usuario.numero))

    conexao.commit()
    cursor.close()
    conexao.close()

    return {'Mensagem': 'Usuário cadastrado'}

def remover_usuario(usuario):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    DELETE FROM usuarios
    WHERE id_usuario = %s
    """,(usuario,))

    quantidade = cursor.rowcount

    conexao.commit()
    cursor.close()
    conexao.close()

    return quantidade

def listar_usuarios():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM usuarios
    """)

    usuarios = cursor.fetchall()

    cursor.close()
    conexao.close()

    return usuarios

def cadastrar_livro(livro):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO livros(titulo, autor, ano, disponivel)
    VALUES(%s, %s, %s, %s)
    """, (livro.titulo, livro.autor, livro.ano, livro.disponivel))

    conexao.commit()
    cursor.close()
    conexao.close()

    return {'Mensagem': 'Livro cadastrado'}

def apagar_livro(livro):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        """
        DELETE FROM livros
        WHERE id_livro = %s
        """,(livro,))

    resultado = cursor.rowcount
    
    conexao.commit()
    cursor.close()
    conexao.close()

    return resultado

def pecorrer_livros():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM livros
    """)

    livros = cursor.fetchall()

    cursor.close()
    conexao.close()

    return livros

def contar_livros():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT COUNT(*) FROM livros
    """)

    quantidade = cursor.fetchall()[0]

    cursor.close()
    conexao.close()

    return {'Quantidade': quantidade}

##################################################################################
# Filtros:

def filtrar_livro_ano():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT * FROM livros
        ORDER BY ano DESC;
    """)

    filtro = cursor.fetchall()

    cursor.close()
    conexao.close()

    return filtro 

def filtrar_livro_ordem_alfabetica():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM livros 
    ORDER BY titulo ASC
    """)

    filtro = cursor.fetchall()

    cursor.close()
    conexao.close()

    return filtro

def filtrar_encontrar_livro_nome(nome_pesquisado):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM livros
    WHERE titulo LIKE %s
    """, (f'%{nome_pesquisado}%',)
    )

    filtro = cursor.fetchall()

    cursor.close()
    conexao.close()

    return filtro

####################################################################################
# Empréstimos:

def cadastrar_emprestimo(id_usuario, id_livro):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
            SELECT id_livro, titulo, autor, ano, disponivel
            FROM livros
            WHERE id_livro = %s
        """, (id_livro,))

        livro = cursor.fetchone()

        if livro is None:
            return None

        if not livro[4]:
            return None

        cursor.execute("""
            INSERT INTO emprestimos (id_usuario, id_livro)
            VALUES (%s, %s)
        """, (id_usuario, id_livro))

        cursor.execute("""
            UPDATE livros
            SET disponivel = FALSE
            WHERE id_livro = %s
        """, (id_livro,))

        cursor.execute("""
            SELECT id_livro, titulo, autor, ano, disponivel
            FROM livros
            WHERE id_livro = %s
        """, (id_livro,))

        livro_emprestado = cursor.fetchone()

        conexao.commit()

        return livro_emprestado

    except Exception as erro:
        conexao.roolback()
        print(f'Erro ao cadastrar empréstimo: {erro}')
        return None

    finally:
        cursor.close()
        conexao.close()

def listar_emprestimos():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT emprestimos.id_emprestimo, emprestimos.data_emprestimo, usuarios.nome, livros.titulo FROM emprestimos 
    JOIN usuarios
        ON emprestimos.id_usuario = usuarios.id_usuario 
    JOIN livros
        ON emprestimos.id_livro = livros.id_livro
    WHERE emprestimos.status = 'ativo'
    ORDER BY emprestimos.id_emprestimo ASC
    """)

    emprestimos = cursor.fetchall()

    cursor.close()
    conexao.close()

    return emprestimos

def devolver_emprestimo(id_emprestimo):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        SELECT id_livro FROM emprestimos
        WHERE id_emprestimo = %s
            AND status = 'ativo'
        """, (id_emprestimo,))

        emprestimo = cursor.fetchone()

        if emprestimo is None:
            return None 

        id_livro = emprestimo[0]

        cursor.execute("""
        UPDATE livros
        SET disponivel = TRUE
        WHERE id_livro = %s
        """, (id_livro,))

        cursor.execute("""
            UPDATE emprestimos
            SET status = 'devolvido',
                data_devolucao = CURRENT_TIMESTAMP
            WHERE id_emprestimo = %s
        """, (id_emprestimo,))

        conexao.commit()

        return id_livro

    except Exception as erro:
        conexao.roolback()
        print(f"Erro ao devolver empréstimo: {erro}")
        return None

    finally:
        cursor.close()
        conexao.close()
    
#####################################################################
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