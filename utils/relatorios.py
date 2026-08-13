import sqlite3

def menu_senha_relatorio(self):
    senha_correta = '1234'
    tentativas = 3

    while tentativas > 0:
        print()
        print('=' * 20, 'ACESSO RESTRITO', '=' * 20)
        print()
        senha = input('Informe a senha de acesso: ')

        if senha == senha_correta:
            print('Acesso autorizado')
            return True
        
        else:
            tentativas -= 1
            print('Senha incorreta')
            print(f'Tentativas restantes: {tentativas}')

    print('Acesso bloqueado')
    return False

def menu_relatorio(self):
    while True:
        print()
        print('=' * 20, 'RELATÓRIOS', '=' * 20)
        print()
        print('1 - ')
        print('2 - ')
        print('3 - ')
        print('4 - ')
        print('5 - ')
        opcao = int(input('Escolha uma opcao: '))

        if opcao == 1:
            ...
        elif opcao ==  2:
            ...
        elif opcao == 3:
            ...
        elif opcao == 4:
            ...
        elif opcao == 5:
            ...
        else:
            print('Opção inválida')