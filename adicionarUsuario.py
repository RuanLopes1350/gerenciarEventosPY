from database import cursor
from database import banco


def adicionar_usuarios(nome, email, senha):
    try:
        cursor.execute(
            "INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)", (nome, email, senha))
        banco.commit()
        print("Usuário adicionado com sucesso!")
    except Exception as erro:
        print(f"Erro ao adicionar usuário: {erro}")
        banco.rollback()
