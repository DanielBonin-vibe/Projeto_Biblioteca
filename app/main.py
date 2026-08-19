from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from utils import banco_de_dados
from typing import Literal

app = FastAPI()    

#####################################################
# Usuários:
class Usuario(BaseModel): 
    nome: str
    idade: int
    cpf: str
    numero: str

@app.post('/usuarios', status_code=201)
def salvar_usuario_api(usuario: Usuario):    

    banco_de_dados.salvar_usuario(usuario)

    return usuario

#

@app.delete('/usuarios/{id_usuario}', status_code=204)
def remover_usuario_api(id_usuario: int):

    quantidade = banco_de_dados.remover_usuario(id_usuario)

    if quantidade == 0:
        raise HTTPException(
            status_code=404,
            detail='usuário não encontrado'
        )

#

@app.get('/usuarios')
def listar_usuario_api():
    
    usuarios = banco_de_dados.listar_usuarios()

    return usuarios

########################################################################################
# Livros:
class Livro(BaseModel):
    titulo: str
    autor: str
    ano: int
    disponivel: Literal[0, 1]

#

@app.post('/livros', status_code=201)
def cadastrar_livro_api(livro: Livro):

    banco_de_dados.cadastrar_livro(livro)

    return livro

#

@app.delete('/livros/{id_livro}', status_code=204)
def apagar_livro_api(id_livro: int):

    resultado = banco_de_dados.apagar_livro(id_livro)

    if resultado == 0:
        raise HTTPException(
            status_code=404,
            detail='Livro não encontrado'
        )

#

@app.get('/livros')
def pecorrer_livros_api():

    livros = banco_de_dados.pecorrer_livros()

    return livros

#

@app.get('/livros/quantidade')
def contar_livros_api():

    quantidade = banco_de_dados.contar_livros()

    return quantidade

#

@app.get('/livros/por-ano')
def filtrar_livro_ano_api():
    filtro = banco_de_dados.filtrar_livro_ano()

    return filtro

#

@app.get('/livros/ordem-alfabetica')
def filtrar_livro_ordem_alfabetica_api():
    filtro = banco_de_dados.filtrar_livro_ordem_alfabetica()

    return filtro 

#

@app.get('/livros/pesquisa/{nome_pesquisado}')
def filtrar_encontrar_livro_nome_api(nome_pesquisado: str):
    filtro = banco_de_dados.filtrar_encontrar_livro_nome(nome_pesquisado)

    return filtro

##################################################################################################
# Empréstimos:
class Emprestimo(BaseModel):
    id_usuario: int
    id_livro: int

@app.post('/emprestimos', status_code=201)
def cadastrar_emprestimo_api(emprestimo: Emprestimo):

    resultado = banco_de_dados.cadastrar_emprestimos(emprestimo.id_usuario, emprestimo.id_livro)

    if resultado == 0:
        raise HTTPException(
            status_code=400
            detail='Livro indisponível ou não encontrado.'
        )

    return emprestimo

#

@app.get('/emprestimos')
def listar_emprestimo_api():

    emprestimos = banco_de_dados.listar_emprestimos()

    return emprestimos

#

@app.put('/emprestimos/devolver{id_emprestimo}')
def devolver_emprestimo_api(id_emprestimo: int):

    resultado = banco_de_dados.devolver_emprestimo(id_emprestimo)

    if resultado == 0:
        raise HTTPException(
            status_code=404,
            detail='Empréstimo não encontrado.'
        )

    return {'Mensagem': 'Livro devolvido com sucesso.'}