from utils import persistencia

class Biblioteca:
    def __init__(self):
        """
        self.livros = persistencia.carregar_livros()
        self.usuarios = persistencia.carregar_usuarios()
        """
    def adicionar_livro(self, livro):      
        persistencia.cadastrar_livro(livro)     
        print(f'O livro "{livro.titulo}" foi adicionado à biblioteca.')

        
    def remover_livro(self, livro):
        persistencia.apagar_livro(livro)
        print(f'O livro {livro.titulo} foi removido da nossa coletânea')


    def listar_livros(self):
        persistencia.pecorrer_livros()
        print('Listagem completa')

    def cadastrar_usuario(self, usuario):   # Recebe o objeto 'usuario' 
        persistencia.salvar_usuario(usuario)
        print(f'O usuário {usuario.nome} foi cadastrado.')


    def remover_usuario(self, id_usuario):
        persistencia.remover_usuario(id_usuario)
        print(f'O usuário foi removido do nosso cadastro.')

    def listar_usuarios(self):
        persistencia.listar_usuarios()
        persistencia.contar_livros()

    def filtro_ano(self):
        persistencia.filtrar__livro_ano()

    def filtro_ordem_alfabetica(self):
        persistencia.filtrar_livro_ordem_alfabetica()

    def filtro_encontrar_pelo_nome(self, nome_pesquisado):
        persistencia.filtrar_encontrar_livro_nome(nome_pesquisado)

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

        persistencia.cadastrar_emprestimo(id_usuario, id_livro)

    def listar_emprestimos():
        persistencia.listar_emprestimos()

    def devolver_emprestimo(self, id_emprestimo):
        persistencia.devolver_emprestimo(id_emprestimo)