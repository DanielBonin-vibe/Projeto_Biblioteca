from models.livro import Livro
from models.usuario import Usuario
from models.biblioteca import Biblioteca
from relatorios import relatorios
from utils import menu
biblioteca = Biblioteca()

while True:

    opcao_inicial = menu.menu_principal()

    if opcao_inicial == 1:
        opcao_livro = menu.menu_livros() 

        if opcao_livro == 1:
            titulo = input('Informe o título do livro: ')
            autor = input("Digite o autor do livro: ")
            ano = input('Digite o ano de lançamento: ')
 
            biblioteca.cadastrar_livro(titulo, autor, ano)
        
        elif opcao_livro == 2:
            id_livro = int(input('Digite o código de identificação do livro a ser removido: '))
            biblioteca.remover_livro(id_livro)

        elif opcao_livro == 3:
            id_livro = int(input('Digite o código de identificação do livro a ser atualizado: '))
            titulo = input('Digite o novo título: ')
            autor = input('Digite o novo autor: ')
            ano = input('Digite o novo ano: ')

            biblioteca.atualizar_livro(id_livro, titulo, autor, ano)
 
        elif opcao_livro == 4:
            biblioteca.listar_livros()

        elif opcao_livro == 5:
            biblioteca.filtro_ano()

        elif opcao_livro == 6:
            biblioteca.filtro_ordem_alfabetica()

        elif opcao_livro == 7:
            nome_pesquisado = input('Informe uma tentativa do nome: ')
            biblioteca.filtro_encontrar_pelo_nome(nome_pesquisado)

###########################
    elif opcao_inicial == 2:

        opcao_usuarios = menu.menu_usuarios()

        if opcao_usuarios == 1:
            nome = input('Digite o nome do cidadão a ser cadastrado: ')
            idade = int(input('Digite a idade do cidadão a ser cadastrado: '))
            cpf = input('Informe o CPF do cidadão: ')
            numero = input('Informe o número telefônico: ')
    
            biblioteca.cadastrar_usuario(nome, idade, cpf, numero)  
        
        elif opcao_usuarios == 2:
            id_usuario= int(input('Informe o ID de indentificação do usuário a ser removido: '))
            biblioteca.remover_usuario(id_usuario)

        elif opcao_usuarios == 3:
            id_usuario = int(input('Informe o ID do usuário a ser atualizado: '))
            nome = input('Informe o novo nome do usuário: ')
            idade = int(input('Informe a nova idade: '))
            cpf = input('Informe o novo CPF: ')
            numero = input('Informe o novo número telefônico: ')

            biblioteca.atualizar_usuario(id_usuario, nome, idade, cpf, numero)

        elif opcao_usuarios == 4:
            biblioteca.listar_usuarios()

################################

    elif opcao_inicial == 3:
        opcao_acoes = menu.menu_acoes()

        if opcao_acoes == 1:
            biblioteca.emprestar_livro()

        elif opcao_acoes == 2:
            biblioteca.listar_emprestimos()

        elif opcao_acoes == 3:
            id_emprestimo = int(input('Digite o ID do empréstimo: '))
            biblioteca.devolver_emprestimo(id_emprestimo)

        
#################################################################################################################

    elif opcao_inicial == 4:

        acesso = relatorios.menu_senha_relatorio()

        if acesso:
            relatorios.executar_relatorio()

###################################################################################################

    elif opcao_acoes and opcao_usuarios and opcao_livro == 0:
        print('Saindo...')
        break

    else:   
        print('Insira algo válido!')
   
    
