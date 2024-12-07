import argparse
import clients.users_wrapper as users

# Função principal da CLI usando argparse
def main():
    parser = argparse.ArgumentParser(description="CLI para gerenciar usuários usando a API JSONPlaceholder")
    subparser = parser.add_subparsers(dest='comando')

    # Comando para listar usuários
    subparser.add_parser('listar')

    # Comando para criar um usuário
    parser_criar = subparser.add_parser('criar')
    parser_criar.add_argument('nome', help='Nome do usuário')
    parser_criar.add_argument('username', help='Username do usuário')
    parser_criar.add_argument('email', help='Email do usuário')

    # Comando para ler um usuário específico
    parser_ler = subparser.add_parser('ler')
    parser_ler.add_argument('user_id', type=int, help='ID do usuário')

    # Comando para atualizar um usuário
    parser_atualizar = subparser.add_parser('atualizar')
    parser_atualizar.add_argument('user_id', type=int, help='ID do usuário')
    parser_atualizar.add_argument('--nome', help='Novo nome do usuário')
    parser_atualizar.add_argument('--username', help='Novo username do usuário')
    parser_atualizar.add_argument('--email', help='Novo email do usuário')

    # Comando para deletar um usuário
    parser_deletar = subparser.add_parser('deletar')
    parser_deletar.add_argument('user_id', type=int, help='ID do usuário a ser deletado')

    args = parser.parse_args()

    if args.comando == 'listar':
        usuarios = users.list_users()
        if isinstance(usuarios, list):
            for user in usuarios:
                print(f"ID: {user['id']}, Nome: {user['name']}, Email: {user['email']}")
        else:
            print(usuarios)

    elif args.comando == 'criar':
        resultado = users.create_user(args.nome, args.username, args.email)
        print(resultado)

    elif args.comando == 'ler':
        usuario = users.read_user(args.user_id)
        if isinstance(usuario, dict):
            print(f"ID: {usuario['id']}, Nome: {usuario['name']}, Email: {usuario['email']}")
        else:
            print(usuario)

    elif args.comando == 'atualizar':
        resultado = users.update_user(args.user_id, args.nome, args.username, args.email)
        print(resultado)

    elif args.comando == 'deletar':
        resultado = users.delete_user(args.user_id)
        print(resultado)

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
