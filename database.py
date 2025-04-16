import sqlite3
import os

DataBase_Path = './DataBase'

if not os.path.exists(DataBase_Path):
    os.makedirs(DataBase_Path)
    print(f"Diretório {DataBase_Path} criado com sucesso.")
else:
    print(f"Diretório {DataBase_Path} já existe.")

banco = sqlite3.connect('./DataBase/eventos.db')

cursor = banco.cursor()