from database import usuarios_repository

def atualizar_usuario(id_usuario, nome, idade, cpf, numero):
    resultado = usuarios_repository.atualizar_usuario(id_usuario, nome, idade, cpf, numero)

    if resultado == 0:
        return 'usuario_nao_encontrado'
    else:
        return 'usuario_atualizado'

def remover_usuario(id_usuario):
    resultado = usuarios_repository.remover_usuario(id_usuario)

    if resultado == 0:
        return 'erro_encontrado'

    else:
        return 'usuario_removido'

def cadastrar_usuario(nome, idade, cpf, numero):
    resultado = usuarios_repository.cadastrar_usuario(nome, idade, cpf, numero)

    if resultado == 0:
        return 'erro_ao_cadastrar'

    else:
        return 'usuario_cadastrado'

#