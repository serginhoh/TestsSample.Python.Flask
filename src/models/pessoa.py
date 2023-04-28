from datetime import date
from dateutil import relativedelta
from pydantic import BaseModel, validator

class Pessoa(BaseModel):
    nome: str
    aniversario: date

    @validator('nome')
    def nome_nao_deve_ser_vazio_ou_nulo(cls, v):
        if not v or not v.strip():
            raise ValueError('Nome não pode ser vazio')
        return v

    @validator('aniversario')
    def aniversario_deve_ser_maior_18_anos(cls, v):
        diff = relativedelta.relativedelta(date.today(), v)
        if diff.years < 18:
            raise ValueError('Pessoa deve ser maior de 18 anos.')
        return v