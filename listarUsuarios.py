from database import banco
from database import cursor

def listarUsuarios():
    try:
        cursor.execute("SELECT * FROM usuarios")
        for linha in cursor.fetchall():
            print(linha)
    except Exception as erro:
        print(f"Erro ao listar usuários: {erro}")