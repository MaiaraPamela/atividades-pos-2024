import json

# Carrega os dados do arquivo JSON
with open('parsers/imobiliariaParse.json') as imobiliaria_json:
    imobiliaria_data = json.load(imobiliaria_json)

# Exibe o menu de opções de imóveis
print(10 * '-=' + ' MENU ' + '-=' * 10)
imoveis = imobiliaria_data['imobiliaria']
for idx, imovel in enumerate(imoveis, start=1):
    descricao = imovel['descricao']
    print(f'{idx}. {descricao}')
print('-=' * 20)
print('')

# Solicita ao usuário a escolha de um imóvel
imovel_escolhido = int(input('Digite o ID do imóvel para saber mais detalhes: ')) - 1
print('')

# Obtém os detalhes do imóvel escolhido
imovel = imoveis[imovel_escolhido]

descricao = imovel['descricao']
nome = imovel['nome']
email = imovel.get('email', [])
telefone = imovel.get('telefone', [])
rua = imovel['rua']
bairro = imovel['bairro']
cidade = imovel['cidade']
numero = imovel.get('numero', 'N/A')
tamanho = imovel['tamanho']
numQuartos = imovel['numQuartos']
numBanheiros = imovel['numBanheiros']
valor = imovel['valor']

# Exibe os detalhes do imóvel
print(f"Descrição: {descricao}")
print(f"Nome: {nome}")
if email:
    for e in email:
        print(f"Email: {e}")
else:
    print("Email: Não informado")
if telefone:
    for t in telefone:
        print(f"Telefone: {t}")
else:
    print("Telefone: Não informado")
print(f"Rua: {rua}")
print(f"Bairro: {bairro}")
print(f"Cidade: {cidade}")
print(f"Número: {numero}")
print(f"Tamanho: {tamanho} m²")
print(f"Número de Quartos: {numQuartos}")
print(f"Número de Banheiros: {numBanheiros}")
print(f"Valor: R${valor}")
