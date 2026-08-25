import psycopg 


def conectar():
    conexao = psycopg.connect(
        host='localhost',
        port='5432',
        dbname='projeto_academia',
        user='postgres',
        password='B@nin180506'
    )

    return conexao