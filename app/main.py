from fastapi import FastAPI
from pydantic import BaseModel  # Pydantic serve para validar e estruturar os dados que entram na API

from utils import banco_de_dados

app = FastAPI()  # Criamos a aplicação FastAPI
 
# Vamos mostrar o que o usuário precisa possuir para o JSON
class Usuario(BaseModel):  # Serve para representar os dados que chegam pela API
    nome: str
    idade: int
    cpf: str
    numero: str

# Agora vamos criar a rota POST
# POST é um método HTTP, que é 'Criar', faz sentido, já que queremos cadastrar um novo usuário
@app.post('/usuarios') # Quando fizer uma requisição HTTP 'POST' para '/usuarios', execute a função abaixo. 
def salvar_usuarios(usuario: Usuario): # 'usuario' deve seguir o 'BaseModel' chamado 'Usuario'
    banco_de_dados.salvar_usuario(usuario)

    return{
        'mensagem': 'Usuário salvo com sucesso!'
    }

# Da onde veio 'usuario'