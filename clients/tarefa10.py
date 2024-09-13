import requests
from xml.dom.minidom import parseString

def buscar_capital_pais(codigo_pais):
    url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"
    cabecalhos = {
        "Content-Type": "text/xml; charset=utf-8",
        "SOAPAction": "http://www.oorsprong.org/websamples.countryinfo/CapitalCity"
    }
    
    corpo_solicitacao = f"""<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
      <soap:Body>
        <CapitalCity xmlns="http://www.oorsprong.org/websamples.countryinfo">
          <sCountryISOCode>{codigo_pais}</sCountryISOCode>
        </CapitalCity>
      </soap:Body>
    </soap:Envelope>"""
    
    resposta = requests.post(url, data=corpo_solicitacao, headers=cabecalhos)
    resposta_xml = resposta.content.decode()
    
    # Analisa o XML de resposta
    dom = parseString(resposta_xml)
    
    # Verifica se a tag 'CapitalCityResult' foi encontrada
    capitais_encontradas = dom.getElementsByTagName("m:CapitalCityResult")
    if capitais_encontradas:
        capital = capitais_encontradas[0].childNodes[0].nodeValue
        return capital
    else:
        return "'CapitalCityResult' não foi encontrado"

def numero_por_extenso(numero):
    url = "https://www.dataaccess.com/webservicesserver/NumberConversion.wso"
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

    resposta = requests.post(url, data=corpo_solicitacao, headers=cabecalhos)
    resposta_xml = resposta.content.decode()

    dom = parseString(resposta_xml)

    resultado = dom.getElementsByTagName("m:NumberToWordsResult")
    if resultado:
        por_extenso = resultado[0].childNodes[0].nodeValue
        return por_extenso
    else:
        return "'NumberToWordsResult' não foi encontrado"

# Exemplo de uso
capital_noruega = buscar_capital_pais("NO")
print(f"A capital da Noruega é {capital_noruega}")

numero = int(input("Digite um número inteiro: "))
numero_extenso = numero_por_extenso(numero)
print(f"O número {numero} por extenso em inglês é: {numero_extenso}")
