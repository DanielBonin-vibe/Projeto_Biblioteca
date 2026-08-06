from models.livro import Livro
from models.usuario import Usuario
from models.biblioteca import Biblioteca


biblioteca = Biblioteca()   # Criamos o objeto Biblioteca


while True:

    opcao_inicial = biblioteca.menu_principal()

    if opcao_inicial == 1:
        opcao_livro = biblioteca.menu_livros() 

        if opcao_livro == 1:
            titulo_livro = input('Informe o título do livro: ')
            autor_livro = input("Digite o autor do livro: ")
            ano_livro = input('Digite o ano de lançamento: ')
        
            livro = Livro(titulo_livro, autor_livro, ano_livro)  
            biblioteca.adicionar_livro(livro)
        
        # Remover livro
        elif opcao_livro == 2:
            buscar_id = int(input('Digite o Código de identificação do livro a ser removido: '))
            usuario_encontrado = biblioteca.verificar_id_livro(buscar_id) 

            if usuario_encontrado:                  
                biblioteca.remover_livro(livro)    
        
         # Listar Livros:
            elif opcao_livro == 3:
                biblioteca.listar_livros()
        
##############################################################################################################
    elif opcao_inicial == 2:
        opcao_usuarios = biblioteca.menu_usuarios()

        if opcao_usuarios == 1:
            nome_usuario = input('Digite o nome do cidadão a ser cadastrado: ')
            idade_usuario = int(input('Digite a idade do cidadão a ser cadastrado: '))
            cpf_usuario = input('Informe o CPF do cidadão: ')
            numero_usuario = input('Informe o número telefônico: ')
        
            usuario = Usuario(nome_usuario, idade_usuario, cpf_usuario, numero_usuario) 
            biblioteca.cadastrar_usuario(usuario)  
        
        # Remover Usuário:
        elif opcao_usuarios == 2:
            id_usuario= int(input('Informe o ID de indentificação do usuário a ser removido: '))
            biblioteca.remover_usuario(id_usuario)
        
            # Listar Usuários:
        elif opcao_usuarios == 3:
            biblioteca.listar_usuarios()

#################################################################################################################
    elif opcao_inicial == 3:
        opcao_acoes = biblioteca.menu_acoes()

    # Emprestar livro 
        if opcao_acoes == 1:
            buscar_id_usuario = int(input('Informe o ID do usuário: '))
            buscar_id_livro = int(input('Informe o ID do livro: '))

            usuario_encontrado = biblioteca.verificar_id_usuario(buscar_id_usuario)  # Procura usuário
            livro_encontrado = biblioteca.verificar_id_livro(buscar_id_livro)        # Procura livro

            if usuario_encontrado and livro_encontrado:             # Se ambos forem True
                usuario_encontrado.pegar_livro(livro_encontrado)
            else:
                print("Usuário ou livro não encontrado.")

    # Devolver livro
        elif opcao_acoes == 2:
            buscar_id_usuario = int(input('Informe o ID do usuário: '))
            buscar_id_livro = int(input('Informe o ID do livro: '))

            usuario_encontrado = biblioteca.verificar_id_usuario(buscar_id_usuario)  # Procura usuário
            
            livro_encontrado = biblioteca.verificar_id_livro(buscar_id_livro)        # Procura livro

            if usuario_encontrado and livro_encontrado:         # Se ambas as condições forem True
                usuario_encontrado.devolver_livro(livro_encontrado)
            else:
                print("Usuário ou livro não encontrado.")

    # Sair
        elif opcao_acoes and opcao_usuarios and opcao_livro == 0:
            print('Saindo...')
            break

    # Digitou algo inválido
        else:   
            print('Insira algo válido!')
   
    
