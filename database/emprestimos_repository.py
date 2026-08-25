from database.conexao_postgre import conectar

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