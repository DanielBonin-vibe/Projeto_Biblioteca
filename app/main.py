from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def inicio():
    return{'mensagem': 'API da biblioteca funcionando!'}

@app.get('/livros')
def listar_livros():
    return {
        'mensagem': 'Aqui serão listados os livros'
    }