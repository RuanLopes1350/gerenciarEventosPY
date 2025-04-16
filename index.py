from database import banco
from criarTabelas import criarTabelaUsuarios, criarTabelaEventos
from adicionarUsuario import adicionar_usuarios
from adicionarEvento import adicionar_eventos
from listarUsuarios import listarUsuarios
from buscarUsuario import buscar_usuario_por_id

Gerenciador = True

criarTabelaUsuarios()
criarTabelaEventos()

while Gerenciador == True:
    print("\nO que gostaria de fazer?")
    print("1. Menu Eventos!")
    print("2. Menu Usuarios!")
    print("3. Sair do Sistema!")

    opcaoMenu = input("Digite a opção desejada: ")
    if opcaoMenu == "1":
        menuEventos = True
        while menuEventos == True:
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
        while menuUsuarios == True:
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
                adicionar_usuarios(
                    nome_do_usuario, email_do_usuario, senha_do_usuario)

            elif opcaoUsuarios == "2":
                print("\nListando Usuarios:")
                listarUsuarios()

            elif opcaoUsuarios == "3":
                id_string = input("Informe o ID do usuario que deseja buscar: ")
                id = int(id_string)
                buscar_usuario_por_id(id)

            elif opcaoUsuarios == "6":
                menuUsuarios = False

    if opcaoMenu == "3":
        Gerenciador = False
        print("Saindo do sistema...")
        banco.close()
