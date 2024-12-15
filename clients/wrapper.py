import requests

BASE_URL = "https://jsonplaceholder.typicode.com/users"

def list_users():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        return response.json()
    else:
        return f"Erro ao listar usuários: {response.status_code}"

def create_user(name, username, email):
    new_user = {
        "name": name,
        "username": username,
        "email": email
    }
    response = requests.post(BASE_URL, json=new_user)
    if response.status_code == 201:
        return response.json()
    else:
        return f"Erro ao criar usuário: {response.status_code}"

def read_user(user_id):
    response = requests.get(f"{BASE_URL}/{user_id}")
    if response.status_code == 200:
        return response.json()
    else:
        return f"Erro ao buscar usuário: {response.status_code}"

def update_user(user_id, name=None, username=None, email=None):
    updated_data = {}
    if name:
        updated_data["name"] = name
    if username:
        updated_data["username"] = username
    if email:
        updated_data["email"] = email

    response = requests.put(f"{BASE_URL}/{user_id}", json=updated_data)
    if response.status_code == 200:
        return response.json()
    else:
        return f"Erro ao atualizar usuário: {response.status_code}"

def delete_user(user_id):
    response = requests.delete(f"{BASE_URL}/{user_id}")
    if response.status_code == 200:
        return f"Usuário {user_id} deletado com sucesso."
    else:
        return f"Erro ao deletar usuário: {response.status_code}"