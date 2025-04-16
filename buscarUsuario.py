from database import banco
from database import cursor

def buscar_usuario_por_id(id):
    try:
        cursor.execute("SELECT * FROM usuarios WHERE id = ?", (id,))
        usuario = cursor.fetchone()
        print(usuario)
    except Exception as erro:
        print(f"Erro ao buscar usuário: {erro}")
        banco.rollback()