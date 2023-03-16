import re


class ExtratorURL:
    def __init__(self,url):
        self.url = self.sanitiza_url(url)
        self.index_separa_parametro = self.url.find('?')
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia")
        #self.valida_url_base()

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(url)
        if not match:
            raise ValueError("A URL não é válida")
        print("URl é válida")


    #def valida_url_base(self): #Verificar https e /cambio
    #    self.url_base()
    #    if not self.url_base().startswith('https://'):
    #        raise ValueError(f"Erro HTTPS")
    #    if not self.url_base().endswith("/cambio"):
    #        raise ValueError(f"Página não encontrada")

    def url_base(self):
        url_base = self.url [:self.index_separa_parametro]
        return url_base

    def url_parametros(self):
        url_parametros = self.url[self.index_separa_parametro + 1:]
        return url_parametros

    def busca_valor_parametro(self, parametro_busca):
        indice_parametro = self.url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.url_parametros()[indice_valor:]
        else:
            valor = self.url_parametros()[indice_valor:indice_e_comercial]
        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + "\n" + 'Parâmetros: ' + self.url_parametros() + "\n" + 'Base: ' + self.url_base()

url = 'https://bytebank.com/cambio?moedaDestino=real&moedaOrigem=dolar&quantidade=115'
extrator_url = ExtratorURL(url)
valor_url = extrator_url.busca_valor_parametro('moedaDestino') #Parâmetro de busca
#print(valor_url)
print("O tamanho da URL é: ", len(extrator_url))
print(extrator_url)


### DESAFIO ###
# Conversão de dólar para real
VALOR_DOLAR = 5.50  # 1 dólar = 5.50 reais
moeda_origem = extrator_url.busca_valor_parametro("moedaOrigem")
moeda_destino = extrator_url.busca_valor_parametro("moedaDestino")
quantidade = extrator_url.busca_valor_parametro("quantidade")

if moeda_origem == 'real' and moeda_destino == 'dolar':
    valor_conversao = int(quantidade)/VALOR_DOLAR
    print("O valor de R$" + int(quantidade) + "reais é igual a $" + str(valor_conversao) + "$ dólares.")
elif moeda_origem == 'dolar' and moeda_destino == 'real':
    valor_conversao = int(quantidade)*VALOR_DOLAR
    print("O valor de $" + quantidade + " dólares é igual a R$" + str(valor_conversao) + " reais.")
else:
    print(f"Câmbio de {moeda_origem} para {moeda_destino} não está disponível.")
