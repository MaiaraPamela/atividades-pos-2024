from xml.dom.minidom import parse

# Faz o parsing do arquivo XML
dom = parse('parsers/cardapio.xml')
cardapio = dom.documentElement

# Obtém todos os elementos "prato"
pratos = cardapio.getElementsByTagName('prato')

# Exibe o menu
print('MENU')
print('-=' * 30)
for id, prato in enumerate(pratos, start=1):
    nome = prato.getElementsByTagName('nome')[0].firstChild.nodeValue
    print(f"{id}. {nome}")
print('-=' * 30)

# Solicita ao usuário a escolha de um prato
prato_escolhido = int(input('Digite o ID do prato para saber mais detalhes: ')) - 1
print("")

# Obtém os detalhes do prato escolhido
prato = pratos[prato_escolhido]
nome = prato.getElementsByTagName('nome')[0].firstChild.nodeValue
descricao = prato.getElementsByTagName('descricao')[0].firstChild.nodeValue
ingredientes = prato.getElementsByTagName('ingredientes')[0].getElementsByTagName('ingrediente')
preco = prato.getElementsByTagName('preco')[0].firstChild.nodeValue
moeda = prato.getElementsByTagName('preco')[0].getAttribute('moeda')
calorias = prato.getElementsByTagName('calorias')[0].firstChild.nodeValue
tempo_preparo = prato.getElementsByTagName('tempoPreparo')[0].firstChild.nodeValue

# Exibe os detalhes do prato escolhido
print(f"Nome: {nome}")
print(f"Descrição: {descricao}")
print("Ingredientes:")
for ingrediente in ingredientes:
    print(f" - {ingrediente.firstChild.nodeValue}")
print(f"Preço: {moeda}{preco}")
print(f"Calorias: {calorias} kcal")
print(f"Tempo de Preparo: {tempo_preparo} minutos")
