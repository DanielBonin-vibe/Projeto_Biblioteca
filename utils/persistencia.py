import json

def salvar_alunos(alunos):

    dados = []

    for aluno in alunos:
        dados.append(aluno.to_dict())

    with open('dados/alunos.json', 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

def salvar_professores(professores):

    dados = []

    with open('dados/professores.json', 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)