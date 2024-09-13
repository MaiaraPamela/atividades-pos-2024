import requests
import argparse

BASE_URL = "https://jsonplaceholder.typicode.com"

def listar_usuarios():
    response = requests.get(f'{BASE_URL}/users')
    if response.status_code == 200:
        usuarios = response.json()
        for usuario in usuarios:
            print(f"ID: {usuario['id']}, Nome: {usuario['name']}, Email: {usuario['email']}")
    else:
        print('Erro ao listar usuários')

def listar_tarefas_usuario(user_id):
    response = requests.get(f'{BASE_URL}/users/{user_id}/todos')
    if response.status_code == 200:
        todos = response.json()
        if todos:
            for tarefa in todos:
                status = 'Concluída' or 'Pendente'
                print(f"ID: {tarefa['id']}, Tarefa: {tarefa['title']}, Status: {status}")
        else:
            print(f"O usuário {user_id} não tem tarefas.")
    else:
        print(f"Erro ao listar tarefas do usuário {user_id}")

def criar_usuario(nome, username, email):
    novo_usuario = {
        "name": nome,
        "username": username,
        "email": email
    }
    response = requests.post(f'{BASE_URL}/users', json=novo_usuario)
    if response.status_code == 201:
        print(f"Usuário criado com sucesso: {response.json()}")
    else:
        print('Erro ao criar usuário')

def ler_usuario(user_id):
    response = requests.get(f'{BASE_URL}/users/{user_id}')
    if response.status_code == 200:
        usuario = response.json()
        print(f"ID: {usuario['id']}, Nome: {usuario['name']}, Email: {usuario['email']}")
    else:
        print(f"Erro ao buscar o usuário {user_id}")

def atualizar_usuario(user_id, nome=None, username=None, email=None):
    dados_atualizados = {}
    if nome:
        dados_atualizados['name'] = nome
    if username:
        dados_atualizados['username'] = username
    if email:
        dados_atualizados['email'] = email

    response = requests.put(f'{BASE_URL}/users/{user_id}', json=dados_atualizados)
    if response.status_code == 200:
        print(f"Usuário {user_id} atualizado com sucesso: {response.json()}")
    else:
        print(f"Erro ao atualizar o usuário {user_id}")

def deletar_usuario(user_id):
    response = requests.delete(f'{BASE_URL}/users/{user_id}')
    if response.status_code == 200:
        print(f"Usuário {user_id} deletado com sucesso.")
    else:
        print(f"Erro ao deletar o usuário {user_id}")

def main():
    parser = argparse.ArgumentParser(description="CLI para gerenciar usuários da API JSONPlaceholder")
    subparser = parser.add_subparsers(dest='comando')


    subparser.add_parser('listar')

    parser_tarefas = subparser.add_parser('tarefas')
    parser_tarefas.add_argument('user_id', type=int, help='ID do usuário para listar as tarefas')

    parser_criar = subparser.add_parser('criar')
    parser_criar.add_argument('nome', help='Nome do usuário')
    parser_criar.add_argument('username', help='Username do usuário')
    parser_criar.add_argument('email', help='Email do usuário')

    parser_ler = subparser.add_parser('ler')
    parser_ler.add_argument('user_id', type=int, help='ID do usuário')

    parser_atualizar = subparser.add_parser('atualizar')
    parser_atualizar.add_argument('user_id', type=int, help='ID do usuário')
    parser_atualizar.add_argument('--nome', help='Novo nome do usuário')
    parser_atualizar.add_argument('--username', help='Novo username do usuário')
    parser_atualizar.add_argument('--email', help='Novo email do usuário')

    parser_deletar = subparser.add_parser('deletar')
    parser_deletar.add_argument('user_id', type=int, help='ID do usuário a ser deletado')

    args = parser.parse_args()

    if args.comando == 'listar':
        listar_usuarios()
    elif args.comando == 'tarefas':
        listar_tarefas_usuario(args.user_id)
    elif args.comando == 'criar':
        criar_usuario(args.nome, args.username, args.email)
    elif args.comando == 'ler':
        ler_usuario(args.user_id)
    elif args.comando == 'atualizar':
        atualizar_usuario(args.user_id, args.nome, args.username, args.email)
    elif args.comando == 'deletar':
        deletar_usuario(args.user_id)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
