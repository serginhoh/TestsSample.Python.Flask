import pytest
from src.models.pessoa import Pessoa
from datetime import datetime

dtaniversario = datetime.strptime('01-01-2000', '%m-%d-%Y').date()

def test_pessoa_deve_retornar_sem_erros():
    #act
    pessoa = Pessoa(nome= 'teste', aniversario = dtaniversario)

    #assert
    assert isinstance(pessoa, Pessoa)

def test_pessoa_deve_retornar_erro_nome_null():
    #act
    with pytest.raises(ValueError):
        Pessoa(aniversario = dtaniversario)

def test_pessoa_deve_retornar_erro_nome_vazio():
    #act
    with pytest.raises(ValueError):
        Pessoa(nome = "", aniversario = dtaniversario)        

def test_pessoa_deve_retornar_erro_menor_18_anos():
    dtaniversario = datetime.today().date

    #act
    with pytest.raises(ValueError):
        Pessoa(nome= 'teste', aniversario = dtaniversario)
