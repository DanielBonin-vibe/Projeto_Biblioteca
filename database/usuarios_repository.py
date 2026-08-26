from database.conexao_postgre import conectar
######################################################

# Salvar usuários:
def cadastrar_usuario(usuario):
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

def atualizar_usuario(id_usuario, nome, idade, cpf, numero):
    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
        UPDATE usuarios
        SET nome = %s, idade = %s, cpf = %s, numero = %s
        WHERE id_usuario = %s
        """, nome, idade, cpf, numero, id_usuario)

        resultado = cursor.rowcount
        
        conexao.commit()

        return resultado

    except Exception as erro:
        conexao.rollback()
        print(f'erro ao utilizar usuário: {erro}')
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
