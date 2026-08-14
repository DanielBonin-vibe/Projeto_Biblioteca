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
def salvar_usuario_api(usuario: Usuario):    # Estamos dizendo que o corpo da requisição deve seguir o modelo Usuario, 'usuario' é um objeto baseado na classe 'Usuario'

    banco_de_dados.salvar_usuario(usuario)

    return usuario;

@app.delete('/usuarios/{id_usuario}')
def remover_usuario_api(id_usuario: int):
    banco_de_dados.remover_usuario(id_usuario)

    return {'Mensagem': 'Usuário removido com sucesso.'}

@app.get('/usuarios')
def listar_usuario_api():
    
    usuarios = banco_de_dados.listar_usuarios()

    return usuarios

########################################################################################
