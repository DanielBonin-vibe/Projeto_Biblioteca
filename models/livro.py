class Livro:
    # id = 1

    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = True

    def exibir_informações(self):
        print(f'Título: {self.titulo}')
        print(f'Autor: {self.autor}')
        print(f'Ano: {self.ano}')
        print(f'Disponível: {self.disponivel}')

    def emprestar(self):
        if self.disponivel == True:
            self.disponivel = False
            print(f'O {self.titulo} foi emprestado e agora estará indisponível')

        else:
            print(f' O {self.titulo} não está disponível para ser emprestado')

    def devolver(self):
        if self.disponivel == False:
            self.disponivel = True
            print(f'O {self.titulo} foi devolvido e agora está disponível')

        else:
            print(f' O {self.titulo} já está em estoque....')
"""
    def to_dict(self):
        return {
        ['titulo']: self.titulo,
        ['autor']: self.autor,
        ['ano']: self.ano,
        ['disponivel']: self.disponivel,
        ['id']: self.id
        }

    @classmethod
    def from_dict(cls, dados):
        livro = cls(
        dados['titulo'],
        dados['autor'],
        dados['ano'],
        )
        livro.disponivel = dados['disponivel']
        livro.id = dados['id']
        return livro
"""