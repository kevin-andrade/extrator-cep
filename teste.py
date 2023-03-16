
url = "bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"

#Separa a base e os parâmetros
indice_interrogacao = url.find('?') #Retorna o numero do indice onde está
url_base = url[:indice_interrogacao] # Procura do inicio até o indice_interrogacao, lembrando que o indice é exclusivo, aparece seu antecessor
url_parametros = url[indice_interrogacao+1:] # Separa os parâmetros, começando depois do indice_interrogacao, retornando tudo até o fim
#print(url_base)
#print(url_parametros)

#Busca o valor de um parâmetro
parametro_busca = 'moedaOrigem' #Busca feita na url
indice_parametro = url_parametros.find(parametro_busca) #Procura o indice da busca, retornando o começo
indice_valor = indice_parametro + len(parametro_busca) + 1 #Percorrer o parametro até o =, somando +1 para chegar ao indice do valor
indice_e_comercial = url_parametros.find('&', indice_valor)  #retornar o indice, argumento: Procurando do indice_valor até achar o indice_e_comercial
if indice_e_comercial == -1:  #Caso a procura ultrapasse
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]

print(valor)