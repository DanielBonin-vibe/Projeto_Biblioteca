import menu, banco_de_dados

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


while True:
    opcao_relatorio = menu.menu_relatorio()

    if opcao_relatorio == 1:
        opcao_aluno = menu.menu_relatorio_aluno()

        if opcao_aluno == 1:
            banco_de_dados.relatorio_aluno_total()

        elif opcao_aluno ==  2:


            
#        elif opcao == 3:
            ...
#        elif opcao == 4:
            ...
#        elif opcao == 5:
            ...
#        else:
#            print('Opção inválida')
        