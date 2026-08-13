from Projeto_Biblioteca.utils import banco_de_dados

class Biblioteca:
    def __init__(self):
        """
        self.livros = persistencia.carregar_livros()
        self.usuarios = persistencia.carregar_usuarios()
        """
    def adicionar_livro(self, livro):      
        banco_de_dados.cadastrar_livro(livro)     
        print(f'O livro "{livro.titulo}" foi adicionado à biblioteca.')

        
    def remover_livro(self, livro):
        banco_de_dados.apagar_livro(livro)
        print(f'O livro {livro.titulo} foi removido da nossa coletânea')


    def listar_livros(self):
        banco_de_dados.pecorrer_livros()
        print('Listagem completa')

    def cadastrar_usuario(self, usuario):   # Recebe o objeto 'usuario' 
        banco_de_dados.salvar_usuario(usuario)
        print(f'O usuário {usuario.nome} foi cadastrado.')


    def remover_usuario(self, id_usuario):
        banco_de_dados.remover_usuario(id_usuario)
        print(f'O usuário foi removido do nosso cadastro.')

    def listar_usuarios(self):
        banco_de_dados.listar_usuarios()
        banco_de_dados.contar_livros()

    def filtro_ano(self):
        banco_de_dados.filtrar__livro_ano()

    def filtro_ordem_alfabetica(self):
        banco_de_dados.filtrar_livro_ordem_alfabetica()

    def filtro_encontrar_pelo_nome(self, nome_pesquisado):
        banco_de_dados.filtrar_encontrar_livro_nome(nome_pesquisado)

################## MENU ##########################

    def menu_principal(self):
        print('=' * 50)
        print(' ' * 14, 'Sistema De Biblioteca', ' ' * 20)
        print('=' * 50)
        print()
        print('1 - Livros')
        print('2 - Usuários')
        print('3 - Empréstimos')
        print('4 - Pesquisar')
        print('5 - Relatórios')
        print('0 - Sair')
        print()
        return int(input('Digite a seleção: '))

    def menu_livros(self):
        print()
        print('1 - Cadastrar livro')
        print('2 - Remover livro')
        print('3 - Listar livros')
        print('0 - Voltar')
        print()
        return int(input('Digite a seleção: '))

    def menu_usuarios(self):
        print()
        print('1 - Criar usuário')
        print('2 - Remover usuário')
        print('3 - Listar usuários')
        print()
        return int(input('Digite a seleção: '))

    def menu_acoes(self):
        print()
        print('1 - Emprestar livro')
        print('2 - Listar empréstimos')
        print('3 - Devolver livro')
        print('0 - Voltar')
        print()
        return int(input('Digite a ação requerida: '))

    def barra_pesquisa(self):
        print()
        print('1 - Descobrir nossa biblioteca por ano')
        print('2 - Descobrir nossa biblioteca por ordem alfabética')
        print('3 - Pesquisar pelo nome')
        print()
        return int(input('Informe a ação requerida: '))

        

################## AÇÕES ##########################


    def emprestar_livro(self):
        id_usuario = int(input('Digite o ID do usuário: '))
        id_livro = int(input('Digite o ID do livro: '))

        banco_de_dados.cadastrar_emprestimo(id_usuario, id_livro)

    def listar_emprestimos():
        banco_de_dados.listar_emprestimos()

    def devolver_emprestimo(self, id_emprestimo):
        banco_de_dados.devolver_emprestimo(id_emprestimo)