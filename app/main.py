from fastapi import FastAPI
from pydantic import BaseModel
from utils import banco_de_dados

app = FastAPI()    # Cria um objeto da classe 'FastAPI' ;  Esse objeto 'app' sere para registrar rotas, configurações e etc. NEste momento ele está vazio de rotas
class Usuario(BaseModel): #  Estamos ensinando o modelo básico com Pydentic
    nome: str
    idade: int
    cpf: str
    numero: str

@app.post('/usuarios')
def criar_usuario(usuario: Usuario):    # Estamos dizendo que o corpo da requisição deve seguir o modelo Usuario, 'usuario' é um objeto baseado na classe 'Usuario'

    banco_de_dados.salvar_usuario(usuario)

    return usuario;
# http://127.0.0.1:8000/docs -> Acessamos o swagger