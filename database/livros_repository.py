from database.conexao_postgre import conectar

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