from fastapi import FastAPI
from pydantic import BaseModel
from utils import banco_de_dados
from typing import Literal

app = FastAPI()    # Cria um objeto da classe 'FastAPI' ;  Esse objeto 'app' sere para registrar rotas, configurações e etc. NEste momento ele está vazio de rotas
class Usuario(BaseModel): #  Estamos ensinando o modelo básico com Pydentic
    nome: str
    idade: int
    cpf: str
    numero: str

@app.post('/usuarios')
def salvar_usuario_api(usuario: Usuario):    # Estamos dizendo que o corpo da requisição deve seguir o modelo Usuario, 'usuario' é um objeto baseado na classe 'Usuario'

    banco_de_dados.salvar_usuario(usuario)

    return usuario

@app.delete('/usuarios/{id_usuario}')
def remover_usuario_api(id_usuario: int):
    banco_de_dados.remover_usuario(id_usuario)

    return {'Mensagem': 'Usuário removido com sucesso.'}

@app.get('/usuarios')
def listar_usuario_api():
    
    usuarios = banco_de_dados.listar_usuarios()

    return usuarios

########################################################################################

class Livro(BaseModel):
    titulo: str
    autor: str
    ano: int
    disponivel: Literal[0, 1]   # Só aceita 0 e 1, sendo 0 indisponível e 1 disponível

#

@app.post('/livros')
def cadastrar_livro_api(livro: Livro):

    banco_de_dados.cadastrar_livro(livro)

    return livro

#

@app.delete('/livros/{id_livro}')
def apagar_livro_api(id_livro: int):
    banco_de_dados.apagar_livro(id_livro)

    return {'mensagem': 'Usuário removido com sucesso.'}

#

@app.get('/livros')
def pecorrer_livros_api():

    livros = banco_de_dados.pecorrer_livros()

    return livros

#

@app.get('/livros')
def contar_livros_api():

    quantidade = banco_de_dados.contar_livros()

    return quantidade

#

@app.get('/livros')
def filtrar_livro_ano_api():
    filtro = banco_de_dados.filtrar_livro_ano()

    return filtro

#

@app.get('/livros')
def filtrar_livro_ordem_alfabetica_api():
    filtro = banco_de_dados.filtrar_livro_ordem_alfabetica()

    return filtro 

#

@app.get('/livros/{nome_pesquisado}')
def filtrar_encontrar_livro_nome_api(nome_pesquisado: str):
    filtro = banco_de_dados.filtrar_encontrar_livro_nome(nome_pesquisado)

    return filtro

##################################################################################################
class Emprestimo(BaseModel):
    id_usuario: int
    id_livro: int

@app.post('/emprestimos')
def cadastrar_emprestimo_api(emprestimo: Emprestimo):

    banco_de_dados.cadastrar_emprestimos(emprestimo)
    emprestimo.id_usuario,
    emprestimo.id_livro

    return emprestimo

#

@app.get('/emprestimos')
def listar_emprestimo_api():

    emprestimos = banco_de_dados.listar_emprestimos()

    return emprestimos

@ap.get('/emprestimos')
def devolver_emprestimo_api():

    banco_de_dados.