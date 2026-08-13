from models.livro import Livro
from models.usuario import Usuario
from models.biblioteca import Biblioteca
biblioteca = Biblioteca()   # Criamos o objeto Biblioteca

while True:

    opcao_inicial = biblioteca.menu_principal()

    if opcao_inicial == 1:
        opcao_livro = biblioteca.menu_livros() 

        if opcao_livro == 1:
            titulo = input('Informe o título do livro: ')
            autor = input("Digite o autor do livro: ")
            ano = input('Digite o ano de lançamento: ')
            livro = Livro(titulo, autor, ano)  
            biblioteca.adicionar_livro(livro)
        
        elif opcao_livro == 2:
            id_livro = int(input('Digite o Código de identificação do livro a ser removido: '))
            biblioteca.remover_livro(id_livro)
 
        elif opcao_livro == 3:
            biblioteca.listar_livros()

###########################
    elif opcao_inicial == 2:

        opcao_usuarios = biblioteca.menu_usuarios()

        if opcao_usuarios == 1:
            nome_usuario = input('Digite o nome do cidadão a ser cadastrado: ')
            idade_usuario = int(input('Digite a idade do cidadão a ser cadastrado: '))
            cpf_usuario = input('Informe o CPF do cidadão: ')
            numero_usuario = input('Informe o número telefônico: ')
        
            usuario = Usuario(nome_usuario, idade_usuario, cpf_usuario, numero_usuario) 
            biblioteca.cadastrar_usuario(usuario)  
        
        elif opcao_usuarios == 2:
            id_usuario= int(input('Informe o ID de indentificação do usuário a ser removido: '))
            biblioteca.remover_usuario(id_usuario)

        elif opcao_usuarios == 3:
            biblioteca.listar_usuarios()

################################

    elif opcao_inicial == 3:
        opcao_acoes = biblioteca.menu_acoes()

        if opcao_acoes == 1:
            biblioteca.emprestar_livro()

        elif opcao_acoes == 2:
            biblioteca.listar_emprestimos()

        elif opcao_acoes == 3:
            id_emprestimo = int(input('Digite o ID do empréstimo: '))
            biblioteca.devolver_emprestimo(id_emprestimo)

#######################

    elif opcao_inicial == 4:
        opcao_pesquisa = biblioteca.barra_pesquisa()
        if opcao_pesquisa == 1:
            biblioteca.filtro_ano()

        elif opcao_pesquisa == 2:
            biblioteca.filtro_ordem_alfabetica

        elif opcao_pesquisa == 3:
            nome_pesquisado = input('Informe uma tentativa do nome')
            biblioteca.filtro_encontrar_pelo_nome(nome_pesquisado)
        
#################################################################################################################

    elif opcao_inicial == 5:

###################################################################################################

        elif opcao_acoes and opcao_usuarios and opcao_livro == 0:
            print('Saindo...')
            break

        else:   
            print('Insira algo válido!')
   
    
