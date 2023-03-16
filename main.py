
url = "bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"
#print(url)

#Sanitização da URL
if type(url) == str:
    return url.strip()
else:
    return ""

#Validação da URL
if not url == "":
    raise ValueError("A URL está vazia")

#Separa a base e os parâmetros
indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:]

#Busca o valor de um parâmetro
parametro_busca = 'moedaDestino'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor )
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]
print(valor)


"""if "?" in url:
    print('Url válida')
    indice_interrogacao = url.find("?")
    url_base = url[:indice_interrogacao]
    print(f'Url base: {url_base}')
    url_parametros = url[indice_interrogacao+1:]
    print(f"Url parâmetos: {url_parametros}")
else:
    print('Url inválida')"""




