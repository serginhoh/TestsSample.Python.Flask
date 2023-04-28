from src.app import app
from src.models.pessoa import Pessoa
from datetime import datetime
import pytest

app.testing = True
client = app.test_client()

def test_pessoa_router_v1_post_deve_retornar_http_201():
    #arrange
    data = {"nome": "teste", "aniversario": "2000-01-01"}
    result = '{"aniversario":"Sat, 01 Jan 2000 00:00:00 GMT","nome":"teste"}\n'

    #act
    response = client.post('/v1/pessoas', json=data)

    #assert
    assert response.status_code == 201
    assert response.get_data(as_text=True) == result

def test_pessoa_router_v1_post_deve_retornar_http_422():
    #arrange
    data = {"nome": "", "aniversario": "2000-01-01"}
    resultjson = '{"errors":[{"loc":["nome"],"msg":"Nome n\\u00e3o pode ser vazio","type":"value_error"}]}\n'

    #act
    response = client.post('/v1/pessoas', json=data)

    #assert
    assert response.status_code == 422
    assert response.get_data(as_text=True) == resultjson