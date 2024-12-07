import requests
from xml.dom.minidom import parseString

# Função para buscar dados de um país (como a capital, nome, continente e moeda)
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

# Funções específicas para buscar diferentes dados de um país
def buscar_nome_pais(codigo_pais):
    return buscar_dado_pais("CountryName", codigo_pais)

def buscar_continente_pais(codigo_pais):
    return buscar_dado_pais("ContinentName", codigo_pais)

def buscar_moeda_pais(codigo_pais):
    return buscar_dado_pais("CurrencyName", codigo_pais)

# Função para buscar a capital de um país (exemplo: Noruega)
capital_noruega = buscar_dado_pais("CapitalCity", "NO")
print(f"A capital da Noruega é {capital_noruega}")

# Função para converter número para extenso em inglês
def converter_numero_por_extenso(numero):
    # URL do WSDL da API de conversão de números
    wsdl_url = "https://www.dataaccess.com/webservicesserver/NumberConversion.wso"
    
    cabecalhos = {
        "Content-Type": "text/xml; charset=utf-8",
        "SOAPAction": "http://www.dataaccess.com/webservicesserver/NumberToWords"
    }
    
    corpo_solicitacao = f"""<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
      <soap:Body>
        <NumberToWords xmlns="http://www.dataaccess.com/webservicesserver/">
          <ubiNum>{numero}</ubiNum>
        </NumberToWords>
      </soap:Body>
    </soap:Envelope>"""
    
    # Faz a requisição POST para o serviço SOAP
    resposta = requests.post(wsdl_url, data=corpo_solicitacao, headers=cabecalhos)
    resposta_xml = resposta.content.decode()
    
    # Analisa o XML de resposta
    dom = parseString(resposta_xml)
    
    # Extrai o número por extenso
    resultado = dom.getElementsByTagName("m:NumberToWordsResult")
    if resultado:
        return resultado[0].childNodes[0].nodeValue
    else:
        return "Número não pôde ser convertido"

# Solicita ao usuário para digitar um número
numero = int(input("Digite um número para converter em extenso: "))
numero_extenso = converter_numero_por_extenso(numero)
print(f"O número {numero} por extenso em inglês é: {numero_extenso}")
