from .livro import Livro

class Usuario:
    # id = 0

    def __init__(self, nome, idade, cpf, numero):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf 
        self.numero = numero 
        self.livros_emprestados = []

    def apresentar(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'CPF: {self.cpf}')
        print(f'Número de telefone: {self.numero}')
        print(f'Livros emprestados: {self.livros_emprestados}')

    def pegar_livro(self, livro ):
        if livro.emprestar():          # Se livro.emprestar for True....
            self.livros_emprestados.append(livro)
            print('Livro emprestado!')

        else:
            print('Não podemos emprestar este títuolo no momento')

    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:

            if livro.devolver():          # Se livro.devolver for false...
                self.livros_emprestados.remove(livro)        
                print('Livro devolvido')

            else:
                print('O livro não pode ser devolvido.')

        else: 
            print('Você não tem nada a ser devolvido')
"""
    def to_dict(self):
        return {
        ['nome']: self.nome,
        ['idade']: self.idade,
        ['cpf']: self.cpf,
        ['numero']: self.numero,
        ['id']: self.id
        }

    @classmethod
    def from_dict(cls, dados):

        usuario = cls(
        dados['nome'],
        dados['idade'],
        dados['cpf'],
        dados['numero']
        )
        usuario.id = dados['id']
        return usuario
"""