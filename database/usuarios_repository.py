from database.conexao_postgre import conectar
######################################################

# Salvar usuários:
def cadastrar_usuario(nome, idade, cpf, numero):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        INSERT INTO usuarios(nome, idade, cpf, numero)
        VALUES(%s, %s, %s, %s) 
        """,(nome, idade, cpf, numero))

        resultado = cursor.rowcount

        conexao.commit()

        return resultado

    except Exception as erro:
        conexao.roolback()
        print(f'Erro ao cadastrar o usuário: {erro}')
        return 0
    finally:
        cursor.close()
        conexao.close()

    return 

def remover_usuario(usuario):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        DELETE FROM usuarios
        WHERE id_usuario = %s
        """,(usuario,))

        resultado = cursor.rowcount

        conexao.commit()

        return resultado

    except Exception as erro:
        conexao.roolback()
        print(f'Erro ao cadastrar o usuário: {erro}')
        return 0
    finally:
        cursor.close()
        conexao.close()


def atualizar_usuario(id_usuario, nome, idade, cpf, numero):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        UPDATE usuarios
        SET nome = %s, idade = %s, cpf = %s, numero = %s
        WHERE id_usuario = %s
        """, (nome, idade, cpf, numero, id_usuario))

        resultado = cursor.rowcount
        
        conexao.commit()

        return resultado

    except Exception as erro:
        conexao.rollback()
        print(f'Erro ao utilizar usuário: {erro}')
        return 0
    
    finally:
        cursor.close()
        conexao.close()


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
