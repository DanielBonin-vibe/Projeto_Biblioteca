class Livro:
    codigo = 1

    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = True
        self.codigo = Livro.codigo
        Livro.codigo += 1

    def exibir_informações(self):
        print(f'Título: {self.titulo}')
        print(f'Autor: {self.autor}')
        print(f'Ano: {self.ano}')
        print(f'Código de identificação: {self.codigo}')
        print(f'Disponível: {self.disponivel}')

    def emprestar(self):
        if self.disponivel == True:
            self.disponivel = False
            print(f'O {self.titulo} foi emprestado e agora estará indisponível')

        else:
            print(f' O {self.titulo} não está disponível para ser emprestado')

    def devolver(self):
        if self.disponjivel == False:
            self.disponivel = True
            print(f'O {self.titulo} foi devolvido e agora está disponível')

        else:
            print(f' O {self.titulo} já está em estoque....')