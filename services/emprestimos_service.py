from database import livros_repository, emprestimos_repository

def emprestar_livro(id_usuario, id_livro):
    livro = livros_repository.buscar_livro_por_id(id_livro)

    if livro is None:
        return "livro_nao_encontrado"


    if not livro[4]:
        return "livro_indisponivel"

    resultado = emprestimos_repository.cadastrar_emprestimo(id_usuario, id_livro)

    return resultado

#

def devolver_livro(id_emprestimo):
    resultado = emprestimos_repository.devolver_emprestimo(id_emprestimo)

    if resultado is None:
        return 'emprestimo_nao_encontrado'

    return resultado