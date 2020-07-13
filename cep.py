import requests
class BuscaEndereco:
    def __init__(self, cep):
        cep = str(cep)
        if self.valida_cep(cep):
            self.cep = cep
        else:
            raise ValueError("Cep inválido!")

    def __str__(self):
        return self.formata_cep()

    def valida_cep(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def formata_cep(self):
        return f"{self.cep[:5]}-{self.cep[5:]}"

    @property
    def acessa_cep(self):
        url = f"https://viacep.com.br/ws/{self.cep}/json/"
        requisicao = requests.get(url)
        resposta = requisicao.json()
        return (
            resposta["cep"],
            resposta["logradouro"],
            resposta["bairro"]
        )
