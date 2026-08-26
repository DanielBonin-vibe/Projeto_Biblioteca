from database import usuarios_repository, livros_repository, emprestimos_repository
class Biblioteca:

    def adicionar_livro(self, livro):      
        livros_repository.cadastrar_livro(livro)    
        print() 
        print(f'O livro "{livro.titulo}" foi adicionado à biblioteca.')

    def remover_livro(self, id_livro):
        quantidade = livros_repository.apagar_livro(id_livro)

        if quantidade > 0:
            print(f'Livro de ID {id_livro} removido da nossa coletânea.')
        else:
            print('Livro não encontrado.')

    def atualizar_livro(self, id_livro, titulo, autor, ano):
        resultado = livros_repository.atualizar_livro(id_livro, titulo, autor, ano)
        print(resultado)

    def listar_livros(self):
        resultado = livros_repository.listar_livros()
        print()
        print(resultado)
        print('Listagem completa.')

    def cadastrar_usuario(self, usuario):
        usuarios_repository.salvar_usuario(usuario)
        print()
        print(f'O usuário {usuario.nome} foi cadastrado.')

    def remover_usuario(self, id_usuario):
        usuarios_repository.remover_usuario(id_usuario)
        print()
        print(f'O usuário foi removido do nosso cadastro.')

    def atualizar_usuario(self, id_usuario, nome, idade, cpf, numero):
        resultado = usuarios_repository.atualizar_usuario(id_usuario, nome, idade, cpf, numero)
        print(resultado)

        if resultado == 0:
            print('Usuário não encontrado')
        else:
            print('Usuário atualziado com sucesso.')

        
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

        livro = emprestimos_repository.cadastrar_emprestimo(id_usuario, id_livro)

        if livro:
            print(f'Livro emprestado: {livro[1]}')
        else:
            print('Não foi possível realizar o empréstimo, pois o mesmo não está disponível.')

    def listar_emprestimos(self):
        emprestimos = emprestimos_repository.listar_emprestimos()
        print(emprestimos)

    def devolver_emprestimo(self, id_emprestimo):
        emprestimos_repository.devolver_emprestimo(id_emprestimo)