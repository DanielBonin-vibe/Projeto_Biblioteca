from utils import banco_de_dados

class Biblioteca:
    def __init__(self):
        ...

    def adicionar_livro(self, livro):      
        banco_de_dados.cadastrar_livro(livro)    
        print() 
        print(f'O livro "{livro.titulo}" foi adicionado à biblioteca.')

    def remover_livro(self, id_livro):
        quantidade = banco_de_dados.apagar_livro(id_livro)

        if quantidade > 0:
            print(f'Livro de ID {id_livro} removido da nossa coletânea.')
        else:
            print('Livro não encontrado.')

    def listar_livros(self):
        resultado = banco_de_dados.pecorrer_livros()
        print()
        print(resultado)
        print('Listagem completa.')

    def cadastrar_usuario(self, usuario):
        banco_de_dados.salvar_usuario(usuario)
        print()
        print(f'O usuário {usuario.nome} foi cadastrado.')

    def remover_usuario(self, id_usuario):
        banco_de_dados.remover_usuario(id_usuario)
        print()
        print(f'O usuário foi removido do nosso cadastro.')

    def listar_usuarios(self):
        resultado = banco_de_dados.listar_usuarios()
        print()
        print(resultado)
        print(f'Listagem completa.')

################################
# Barra de pesquisa:

    def filtro_ano(self):
        filtros = banco_de_dados.filtrar_livro_ano()
        print(filtros)

    def filtro_ordem_alfabetica(self):
        filtros = banco_de_dados.filtrar_livro_ordem_alfabetica()
        print(filtros)

    def filtro_encontrar_pelo_nome(self, nome_pesquisado):
        filtros = banco_de_dados.filtrar_encontrar_livro_nome(nome_pesquisado)
        print(filtros)

################## AÇÕES ##########################


    def emprestar_livro(self):
        id_usuario = int(input('Digite o ID do usuário: '))
        id_livro = int(input('Digite o ID do livro: '))

        livro = banco_de_dados.cadastrar_emprestimo(id_usuario, id_livro)

        if livro:
            print(f'Livro emprestado: {livro[1]}')
        else:
            print('Não foi possível realizar o empréstimo, pois o mesmo não está disponível.')

    def listar_emprestimos(self):
        emprestimos = banco_de_dados.listar_emprestimos()
        print(emprestimos)

    def devolver_emprestimo(self, id_emprestimo, id_livro):
        banco_de_dados.devolver_emprestimo(id_emprestimo, id_livro)