from database.conexao_postgre import conectar

def cadastrar_livro(livro):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        INSERT INTO livros(titulo, autor, ano, disponivel)
        VALUES(%s, %s, %s, %s)
        """, (livro.titulo, livro.autor, livro.ano, livro.disponivel))

        resultado = cursor.rowcount
        
        conexao.commit()

        return resultado

    except Exception as erro:
        conexao.rollback()
        print(f"Erro ao cadastrar livro: {erro}")
        return 0

    finally:
        cursor.close()
        conexao.close()

def remover_livro(id_livro):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """
            DELETE FROM livros
            WHERE id_livro = %s
            """,(id_livro,))

        resultado = cursor.rowcount
        
        conexao.commit()

        return resultado

    except Exception as erro:
        conexao.rollback()
        print(f"Erro ao remover livro: {erro}")
        return 0

    finally:
        cursor.close()
        conexao.close()


def atualizar_livro(id_livro, titulo, autor, ano):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        UPDATE livros
        SET titulo = %s, autor = %s, ano = %s
        WHERE id_livro = %s
        """, (titulo, autor, ano, id_livro))

        resultado = cursor.rowcount

        conexao.commit()

        return resultado

    except Exception as erro:
        conexao.rollback()
        print(f'Erro ao atualizar livro: {erro}')
        return 0

    finally:
        cursor.close()
        conexao.close()

def listar_livros():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
    SELECT * FROM livros
    """)

    livros = cursor.fetchall()

    cursor.close()
    conexao.close()

    return livros


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

def buscar_livro_por_id(id_livro):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id_livro, titulo, autor, ano, disponivel
        FROM livros
        WHERE id_livro = %s
    """, (id_livro,))

    livro = cursor.fetchone()

    cursor.close()
    conexao.close()

    return livro