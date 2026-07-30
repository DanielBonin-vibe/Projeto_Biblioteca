from models.livro import Livro
from models.usuario import Usuario
from models.biblioteca import Biblioteca

biblioteca = Biblioteca()   # Criamos o objeto Biblioteca

livro1 = Livro("Dom Casmurro", "Machado de Assis", 1899)
livro2 = Livro("1984", "George Orwell", 1949)
livro3 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943)

usuario1 = Usuario("João", 20, "123.456.789-00", "81999999999")
usuario2 = Usuario("Maria", 22, "987.654.321-00", "81988888888")

while True:
    
    print('================= MENU =================')
    print('1- Cadastrar livro')
    print('2- Remover livro')
    print('3- Listar livro')
    print('4- Criar usuário')
    print('5- Remover usuário')
    print('6- Listar usuário')
    print('7- Emprestar livro')
    print('8 - Devolver livro')
    print('9 -  Sair')
    print()
    opcao = input('Digite a seleção desejada: ')

# Cadastrar livro:

    if opcao == '1':
        titulo_livro = input('Informe o titulo do livro: ')
        autor_livro = input("Digite o autror do livro: ")
        ano_livro = input('Digite o ano de lançamento: ')

        livro = Livro(titulo_livro, autor_livro, ano_livro)  # Aqui criamos o objeto que vai entrar na lista de lvirtos lá na biblioteca
        biblioteca.adicionar_livro(livro)
        # Não precisa de print, já que já temos na função em biblioteca

# Remover livro

    elif opcao == '2':
        livro_remover = int(input('Digite o Código de identificaçãodo livro a ser removido: '))
        for livro in biblioteca.livros:            # Para o livro no objeto biblioteca que tema  lista livros, faça:
            if livro.codigo == livro_remover:      # se livro.codigo for igual ao código informado, faça:
                biblioteca.remover_livro(livro)    # chamo o método do objeto biblioteca e remover o livro encontrado

# Listar Livros:

    elif opcao == '3':
        biblioteca.listar_livros()
    
# Criar Usuário:

    elif opcao == '4':
        nome_usuario = input('Digite o nome do cidadão a ser cadastrado: ')
        idade_usuario = int(input('Digite a idade do cidadão a ser cadastrado: '))
        cpf_usuario = input('Informe o CPF do cidadão: ')
        numero_usuario = input('Informe o número telefônico: ')

        usuario = Usuario(nome_usuario, idade_usuario, cpf_usuario, numero_usuario)   # Criamos o objeto usuario com as informações coletadas
        biblioteca.cadastrar_usuario(usuario)
        # print da função cadatsrar_usuario aqui.

# Remover Usuário:

    elif opcao == '5':
        
        buscar_id = int(input('Informe o ID de indentificação do usuário a ser removido: '))

        for usuario in biblioteca.usuarios:
            if usuario.id == buscar_id:
                biblioteca.remover_usuario(usuario)

# Listar Usuários:

    elif opcao == '6':
        biblioteca.listar_usuarios()

# Emprestar livro 

    elif opcao == '7':
        id_usuario_emprestimo = int(input('Informe o ID do usuário: '))
        id_livro_emprestimo = int(input('Informe o ID do livro: '))

        usuario_encontrado = None

        for usuario in biblioteca.usuarios:
            if usuario.id == id_usuario_emprestimo:
                usuario_encontrado = usuario
                break

        # Procurar o livro
        livro_encontrado = None

        for livro in biblioteca.livros:
            if livro.id_livro == id_livro_emprestimo:
                livro_encontrado = livro
                break

        # Verificar se ambos foram encontrados
        if usuario_encontrado and livro_encontrado:
            usuario_encontrado.pegar_livro(livro_encontrado)
        else:
            print("Usuário ou livro não encontrado.")

#######################################################################################

    elif opcao == '8':
        id_usuario_emprestimo = int(input('Informe o ID do usuário: '))
        id_livro_emprestimo = int(input('Informe o ID do livro: '))

        usuario_encontrado = None

        for usuario in biblioteca.usuarios:
            if id_livro_emprestimo == id.usuario:
                usuario_encontrado = usuario 
                break

        livro_encontrado = None
        for livro in biblioteca.livro:
            if id_livro_emprestimo == id.livro:
                livro_encontrado = livro
                break

        if usuario_encontrado and livro_encontrado:         # Se ambas as condições forem True
            usuario_encontrado.devolver_livro(livro_encontrado)
        else:
            print("Usuário ou livro não encontrado.")

    elif opcao == '9':
        print('Saindo...')
        break

    else:   
        print('Insira algo válido!')
   
    
