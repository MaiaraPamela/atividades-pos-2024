import requests
from xml.dom.minidom import parseString

def buscar_dado_pais(acao, codigo_pais):
    url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"
    cabecalhos = {
        "Content-Type": "text/xml; charset=utf-8",
        "SOAPAction": f"http://www.oorsprong.org/websamples.countryinfo/{acao}"
    }
    
    corpo_solicitacao = f"""<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
      <soap:Body>
        <{acao} xmlns="http://www.oorsprong.org/websamples.countryinfo">
          <sCountryISOCode>{codigo_pais}</sCountryISOCode>
        </{acao}>
      </soap:Body>
    </soap:Envelope>"""
    
    resposta = requests.post(url, data=corpo_solicitacao, headers=cabecalhos)
    resposta_xml = resposta.content.decode()
    
    # Analisa o XML de resposta
    dom = parseString(resposta_xml)
    
    # Verifica se a tag correspondente foi encontrada
    resultado = dom.getElementsByTagName(f"m:{acao}Result")
    if resultado:
        dado = resultado[0].childNodes[0].nodeValue
        return dado
    else:
        return f"'{acao}Result' não foi encontrado"

def buscar_nome_pais(codigo_pais):
    return buscar_dado_pais("CountryName", codigo_pais)

def buscar_continente_pais(codigo_pais):
    return buscar_dado_pais("ContinentName", codigo_pais)

def buscar_moeda_pais(codigo_pais):
    return buscar_dado_pais("CurrencyName", codigo_pais)

# Exemplo de uso
capital_nova_zelandia = buscar_dado_pais("CapitalCity", "NZ")
nome_nova_zelandia = buscar_nome_pais("NZ")
continente_nova_zelandia = buscar_continente_pais("NZ")
moeda_nova_zelandia = buscar_moeda_pais("NZ")

print(f"A capital da Nova Zelândia é {capital_nova_zelandia}")
print(f"O nome da Nova Zelândia é {nome_nova_zelandia}")
print(f"O continente da Nova Zelândia é {continente_nova_zelandia}")
print(f"A moeda da Nova Zelândia é {moeda_nova_zelandia}")
