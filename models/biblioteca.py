

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def adicionar_livro(self, livro):      # Vai receber o objeto Livro 
        self.livros.append(livro)          # Adiciona a lista 'self.livros' o objeto livro criado em livros.py
        print(f'O livro "{livro.titulo}" foi adicionado à biblioteca.')

        
    def remover_livro(self, livro):
        self.livros.remove(livro)
        print(f'O livro {livro.titulo} foi removido da nossa coletânea')


    def listar_livros(self):
        for livro in self.livros:
          livro.exibir_informações()

    def cadastrar_usuario(self, usuario):   # Recebe o objeto 'usuario' 
        self.usuarios.append(usuario)       # Adiciona o objeto usuario a lista de usuarios 'self.usuarios'
        print(f'O usuário {usuario.nome} foi cadastrado.')

    def remover_usuario(self, usuario):
        self.usuarios.remove(usuario)
        print(f'O usuário {usuario.nome} foi removido do nosso cadastrado.')

    def listar_usuarios(self):
        for usuario in self.usuarios:
            usuario.apresentar()
