from xml.dom.minidom import parse
import json


dom = parse('parsers/imobiliaria.xml')
imobiliaria = dom.documentElement
imoveis = imobiliaria.getElementsByTagName('imovel')

list_imobiliaria = []
dict_imobiliaria = {}

for imovel in imoveis:
    imoveis_dict = {}

    imoveis_dict['descricao'] = imovel.getElementsByTagName('descricao')[0].firstChild.nodeValue

    proprietario = imovel.getElementsByTagName('proprietario')[0]
    imoveis_dict['nome'] = proprietario.getElementsByTagName('nome')[0].firstChild.nodeValue
    emails =  proprietario.getElementsByTagName('email')
    email_list = []
    for e in emails:
        email_list.append(e .firstChild.nodeValue)
        imoveis_dict['email'] = email_list
    telefones =  proprietario.getElementsByTagName('telefone')
    telefone_list = []
    for t in telefones:
        telefone_list.append(t.firstChild.nodeValue)
        imoveis_dict['telefone'] = telefone_list
        

    endereco = imovel.getElementsByTagName('endereco')[0]
    imoveis_dict['rua'] = endereco.getElementsByTagName('rua')[0].firstChild.nodeValue
    imoveis_dict['bairro'] = endereco.getElementsByTagName('bairro')[0].firstChild.nodeValue
    imoveis_dict['cidade'] = cidade = endereco.getElementsByTagName('cidade')[0].firstChild.nodeValue
    numeros = endereco.getElementsByTagName('numero')
    for n in numeros: 
        imoveis_dict['numero'] = n.firstChild.nodeValue

    caracteristicas = imovel.getElementsByTagName('caracteristicas')[0]
    imoveis_dict['tamanho'] = caracteristicas.getElementsByTagName('tamanho')[0].firstChild.nodeValue
    imoveis_dict['numQuartos'] = caracteristicas.getElementsByTagName('numQuartos')[0].firstChild.nodeValue
    imoveis_dict['numBanheiros'] = caracteristicas.getElementsByTagName('numBanheiros')[0].firstChild.nodeValue

    imoveis_dict['valor'] = imovel.getElementsByTagName('valor')[0].firstChild.nodeValue

    list_imobiliaria.append(imoveis_dict)

dict_imobiliaria['imobiliaria'] = list_imobiliaria

with open("parsers/imobiliariaParse.json", "w", encoding="utf-8") as json_file:
    json.dump(dict_imobiliaria, json_file, indent=4, ensure_ascii=False)