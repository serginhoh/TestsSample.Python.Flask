import pytest
from src.services.pessoa import PessoaService
from src.models.pessoa import Pessoa
from datetime import datetime

@pytest.mark.asyncio
async def test_adiciona_pessoa_deve_retornar_pessoa():
    #Arrange
    dtaniversario = datetime.strptime('01-01-2000', '%m-%d-%Y').date()
    pessoa = Pessoa(nome= 'teste', aniversario = dtaniversario)

    #act
    result = await PessoaService().adiciona_pessoa(pessoa)

    #assert
    assert pessoa == result
    assert isinstance(result, Pessoa)