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
