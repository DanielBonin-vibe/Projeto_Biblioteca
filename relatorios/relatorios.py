from . import relatorios_repository
from utils import menu

def menu_senha_relatorio():
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


def executar_relatorio():
    while True:
        opcao_relatorio = menu.menu_relatorio()

        if opcao_relatorio == 1:
            opcao_livro = menu.menu_relatorio_livro()

            if opcao_livro == 1:
                relatorios_repository.relatorio_livro_total()

            elif opcao_livro ==  2:
                relatorios_repository.relatorio_livro_ordem_alfabetica()

            elif opcao_livro == 3:
                relatorios_repository.relatorio_id_livro()

            elif opcao_livro == 4:
                relatorios_repository.relatorio_autor_livro()

            elif opcao_livro == 5:
                relatorios_repository.relatorio_disponivel_livro()

            elif opcao_livro == 6:
                relatorios_repository.relatorio_indisponivel_livro()
            else:
                break


        elif opcao_relatorio == 2:
            opcao_usuario = menu.menu_relatorio_usuario()

            if opcao_usuario == 1:
                relatorios_repository.relatorio_padrao_usuario()

            elif opcao_usuario == 2:
                relatorios_repository.relatorio_ordem_alfabetica_usuario()

            elif opcao_usuario == 3:
                relatorios_repository.relatorio_id_usuario()

            elif opcao_usuario == 4:
                relatorios_repository.relatorio_usuario_emprestimo()

            elif opcao_usuario == 5:
                relatorios_repository.relatorio_usuario_sem_emprestimo()

            else:
                break
            