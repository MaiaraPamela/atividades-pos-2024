import requests
from tabulate import tabulate

# Credenciais do SUAP
username = input("Digite sua Matricula: ")
password = input("Digite sua Senha: ")

# URL do endpoint de autenticação
auth_url = "https://suap.ifrn.edu.br/api/v2/autenticacao/token/"

# Função para autenticar e obter o token
def authenticate():
    response = requests.post(auth_url, data={"username": username, "password": password})

    if response.status_code == 200:
        token_data = response.json()
        api_key = token_data.get("access")
        refresh_token = token_data.get("refresh")
        print("Token obtido com sucesso.")
        return api_key, refresh_token
    else:
        print("Erro ao obter o token:", response.status_code, response.text)
        exit(1)

# Função para renovar o token utilizando o refresh_token
def refresh_token(refresh_token):
    refresh_url = "https://suap.ifrn.edu.br/api/v2/autenticacao/token/refresh/"
    response = requests.post(refresh_url, data={"refresh": refresh_token})

    if response.status_code == 200:
        token_data = response.json()
        return token_data.get("access")
    else:
        print("Erro ao renovar o token:", response.status_code, response.text)
        return None

# Função para obter o boletim
def get_boletim(api_key, ano_letivo, periodo_letivo):
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    boletim_url = f"https://suap.ifrn.edu.br/api/v2/minhas-informacoes/boletim/{ano_letivo}/{periodo_letivo}/"
    response = requests.get(boletim_url, headers=headers)

    if response.status_code == 401:  # Se o token estiver expirado
        print("Token expirado. Tentando renovar...")
        api_key = refresh_token(refresh_token)
        if api_key:  # Se a renovação do token for bem-sucedida
            headers["Authorization"] = f"Bearer {api_key}"
            response = requests.get(boletim_url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print("Erro ao obter o boletim:", response.status_code)
        return None

# Função para formatar e exibir os dados do boletim
def format_boletim(boletim_data):
    if not boletim_data:
        print("Nenhum dado encontrado.")
        return

    tabela = []
    for disciplina in boletim_data:
        linha = [
            disciplina.get("disciplina", "N/A"),
            disciplina.get("nota_etapa_1", "N/A"),
            disciplina.get("nota_etapa_2", "N/A"),
            disciplina.get("nota_etapa_3", "N/A"),
            disciplina.get("nota_etapa_4", "N/A"),
            disciplina.get("media_disciplina", "N/A")
        ]
        tabela.append(linha)

    print(tabulate(tabela, headers=["Disciplina", "Nota 1", "Nota 2", "Nota 3", "Nota 4", "Média Final"], tablefmt="pretty"))

# Função principal para execução do script
def main():
    # Autenticando e obtendo os tokens
    api_key, refresh_token = authenticate()

    # Entrada para o ano letivo
    ano_letivo = int(input("Digite o Ano que Deseja Ver: ")) 
    periodo_letivo = 1  # Definido como 1, mas pode ser modificado para outro valor

    # Obtendo e formatando o boletim
    boletim_data = get_boletim(api_key, ano_letivo, periodo_letivo)
    if boletim_data:
        print("Boletim obtido com sucesso.")
        format_boletim(boletim_data=boletim_data)
    else:
        print("Nenhum dado encontrado.")

# Executando a função principal
if __name__ == "__main__":
    main()
