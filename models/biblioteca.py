from database import usuarios_repository, livros_repository, emprestimos_repository
from services import emprestimos_service, livros_service, usuarios_service
class Biblioteca:

    def cadastrar_livro(self, titulo, autor, ano):      
        resultado = livros_service.cadastrar_livro(titulo, autor, ano) 

        if resultado == 'livro_nao_encontrado':
            print('O livro não foi localizado.')
        else:
            print('cadastro realizado com sucesso.')

    def remover_livro(self, id_livro):
        resultado = livros_service.remover_livro(id_livro)

        if resultado == 'livro_nao_encontrado':
            print(f'Livro não localizado.')
        else:
            print('Livro removido com sucesso.')

    def atualizar_livro(self, id_livro, titulo, autor, ano):
        resultado = livros_service.atualizar_livro(id_livro, titulo, autor, ano)

        if resultado == 'livro_nao_encontrado':
            print('Não foi possível localizar o livro.')
        else:
            print('Livro atualizado com sucesso.')

    def listar_livros(self):
        resultado = livros_repository.listar_livros()
        print()
        print(resultado)
        print('Listagem completa.')

#######################################################################################

    def cadastrar_usuario(self, nome, idade, cpf, numero):
        resultado = usuarios_service.cadastrar_usuario(nome, idade, cpf, numero)
        
        if resultado == 'erro_ao_cadastrar':
            print(f'Erro ao cadastrar.')
        else:
            print('Usuário cadastrado.')

    def remover_usuario(self, id_usuario):
        resultado = usuarios_service.remover_usuario(id_usuario)

        if resultado == 'erro_encontrado':
            print(f'Usuário não localizado.')
        else:
            print('Usuário removido.')

    def atualizar_usuario(self, id_usuario, nome, idade, cpf, numero):
        resultado = usuarios_service.atualizar_usuario(id_usuario, nome, idade, cpf, numero)
        print(resultado)

        if resultado == 'usuario_nao_encontrado':
            print('Usuário não encontrado')
        else:
            print('Usuário atualizado com sucesso.')

        
    def listar_usuarios(self):
        resultado = usuarios_repository.listar_usuarios()
        print()
        print(resultado)
        print(f'Listagem completa.')

################################
# Barra de pesquisa:

    def filtro_ano(self):
        filtros = livros_repository.filtrar_livro_ano()
        print(filtros)

    def filtro_ordem_alfabetica(self):
        filtros = livros_repository.filtrar_livro_ordem_alfabetica()
        print(filtros)

    def filtro_encontrar_pelo_nome(self, nome_pesquisado):
        filtros = livros_repository.filtrar_encontrar_livro_nome(nome_pesquisado)
        print(filtros)

################## AÇÕES ##########################


    def emprestar_livro(self):
        id_usuario = int(input('Digite o ID do usuário: '))
        id_livro = int(input('Digite o ID do livro: '))

        resultado = emprestimos_service.emprestar_livro(id_usuario, id_livro)

        if resultado == "livro_nao_encontrado":
            print('Livro não encontrado.')

        elif resultado == "livro_indisponivel":
            print('Não foi possível realizar o empréstimo, pois o livro não está disponível.')

        elif resultado is None:
            print('Não foi possível realizar o empréstimo.')

        else:
            print(f'Livro emprestado: {resultado[1]}')

    def listar_emprestimos(self):
        emprestimos = emprestimos_repository.listar_emprestimos()
        print(emprestimos)

    def devolver_emprestimo(self, id_emprestimo):
        resultado = emprestimos_service.devolver_livro(id_emprestimo)

        if resultado == "emprestimo_nao_encontrado":
            print("Empréstimo não encontrado ou já devolvido.")

        else:
            print(f"Livro de ID {resultado} devolvido com sucesso.")