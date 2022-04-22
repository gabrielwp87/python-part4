import re # Regular Expression -- RegEx
class ExtratorURL:
    def __init__(self, url):
        """Salva a url em atributo do objeto (self.url = url) e verifica se a url é válida."""
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        """Retorna a url removendo espaços em branco."""
        return url.strip()

    def valida_url(self):
        """Valida se a url está vazia."""
        if not self.url:
            raise ValueError("A URL está vazia")

        padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError("A URL não é válida.")



    def get_url_base(self):
        """Retorna a base da url."""
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        """Retorna os parâmetros da url."""
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        """Retorna o valor do parâmetro 'parametro_busca'."""
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return "URL: " + self.url + "\n" + "URL Base: " + self.get_url_base() + "\n" +  "Parâmetros: " + self.get_url_parametros()

    def __eq__(self, other):
        return self.url == other.url





url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
extrator_url = ExtratorURL(url)
extrator_url_2 = ExtratorURL(url)

valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print(valor_quantidade)

valor_de_origem = extrator_url.get_valor_parametro("moedaOrigem")
print(valor_de_origem)

valor_de_destino = extrator_url.get_valor_parametro("moedaDestino")
print(valor_de_destino)


print(extrator_url)

print(extrator_url == extrator_url_2) # extrator_url.__eq__(extrator_url_2)

print("O endereço de memória do extrator_url é: {}".format(id(extrator_url)))
print("O endereço de memória do extrator_url_2 é: {}".format(id(extrator_url_2)))

#para fazer comparação de identidades (localização na memória) usa-se o "is", exemplo:

print(extrator_url is extrator_url_2)
