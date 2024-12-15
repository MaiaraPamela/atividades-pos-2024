import requests
from tabulate import tabulate

username = input("Digite sua Matricula: ")
password = input("Digite sua Senha: ")

auth_url = "https://suap.ifrn.edu.br/api/v2/autenticacao/token/"

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

def refresh_token(refresh_token):
    refresh_url = "https://suap.ifrn.edu.br/api/v2/autenticacao/token/refresh/"
    response = requests.post(refresh_url, data={"refresh": refresh_token})

    if response.status_code == 200:
        token_data = response.json()
        return token_data.get("access")
    else:
        print("Erro ao renovar o token:", response.status_code, response.text)
        return None
    
def get_boletim(api_key, ano_letivo, periodo_letivo):
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    boletim_url = f"https://suap.ifrn.edu.br/api/v2/minhas-informacoes/boletim/{ano_letivo}/{periodo_letivo}/"
    response = requests.get(boletim_url, headers=headers)

    if response.status_code == 401:  
        print("Token expirado. Tentando renovar...")
        api_key = refresh_token(refresh_token)
        if api_key: 
            headers["Authorization"] = f"Bearer {api_key}"
            response = requests.get(boletim_url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print("Erro ao obter o boletim:", response.status_code)
        return None

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

def main():
    api_key, refresh_token = authenticate()

    ano_letivo = int(input("Digite o Ano que Deseja Ver: ")) 
    periodo_letivo = 1  

    boletim_data = get_boletim(api_key, ano_letivo, periodo_letivo)
    if boletim_data:
        print("Boletim obtido com sucesso.")
        format_boletim(boletim_data=boletim_data)
    else:
        print("Nenhum dado encontrado.")

if __name__ == "__main__":
    main()
