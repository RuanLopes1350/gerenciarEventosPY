from database import cursor
from database import banco


def adicionar_eventos(nome, data, usuario_ID):
    try:
        cursor.execute(
            "INSERT INTO eventos (nome, data, usuario_id) VALUES (?, ?, ?)", (nome, data, usuario_ID))
        banco.commit()
        print("Evento adicionado com sucesso!")
    except Exception as erro:
        print(f"Erro ao adicionar evento: {erro}")
        banco.rollback()