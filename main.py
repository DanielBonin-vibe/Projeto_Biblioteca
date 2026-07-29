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

# Cadastrar livro

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
    

    elif opcao == '4':

    elif opcao == '5':

    elif opcao == '6':

    elif opcao == '7':

    elif opcao == '8':

    else:


   
    
