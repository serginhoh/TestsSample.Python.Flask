from src.models.pessoa import Pessoa

class PessoaService:
    async def adiciona_pessoa(self, pessoa : Pessoa):
        return pessoa