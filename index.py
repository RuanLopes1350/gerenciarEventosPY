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

cursor.execute("CREATE TABLE IF NOT EXISTS usuarios ()")

Gerenciador = True

while Gerenciador == True:
    print("\nO que gostaria de fazer?")
    print("1. Menu Eventos!")
    print("2. Menu Usuarios!")

    opcaoMenu = input("Digite a opção desejada: ")
    if opcaoMenu == "1":
        menuEventos = True
        print("\nMenu Eventos")
        print("1. Cadastrar Evento")
        print("2. Listar Eventos")
        print("3. Buscar Evento por ID")
        print("4. Editar Evento")
        print("5. Excluir Evento")
        print("6. Voltar ao Menu anterior")
        opcaoEventos = input("Digite a opção desejada: ")

        if opcaoEventos == "1":
            print("Cadastrar Evento")
            nome_do_evento = input("Digite o nome do evento: ")

        elif opcaoEventos == "6":
            menuEventos = False

    if opcaoMenu == "2":
        menuUsuarios = True
        print("\nMenu Usuarios")
        print("1. Cadastrar Usuario")
        print("2. Listar Usuarios")
        print("3. Buscar Usuario por ID")
        print("4. Editar Usuario")
        print("5. Excluir Usuario")
        print("6. Voltar ao Menu anterior")
        opcaoUsuarios = input("Digite a opção desejada? ")
        if opcaoUsuarios == "1":
            print("Cadastrar Usuario")
            nome_do_usuario = input("Digite o nome do usuario: ")
            email_do_usuario = input("Digite o email do usuario: ")
            senha_do_usuario = input("Digite a senha do usuario: ")

        elif opcaoUsuarios == "6":
            menuUsuarios = False

    if opcaoMenu == "3":
        Gerenciador = False
        print("Saindo do sistema...")