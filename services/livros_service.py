from database import livros_repository

def atualizar_livro(id_livro, titulo, autor, ano):
    resultado = livros_repository.atualizar_livro(id_livro, titulo, autor, ano)

    if resultado == 0:
        return 'livro_nao_encontrado'

    return 'livro_atualizado'

def remover_livro(id_livro):
    resultado = livros_repository.remover_livro(id_livro)

    if resultado == 0:
        return 'livro_nao_encontrado'

    return 'livro_removido'

def cadastrar_livro(titulo, autor, ano):
    resultado = livros_repository.cadastrar_livro(titulo, autor, ano)

    if resultado == 0:
        return 'livro_nao_encontrado'

    return 'livro_cadastrado'