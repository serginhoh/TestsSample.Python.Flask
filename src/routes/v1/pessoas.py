from src.app import app
from flask_pydantic_api import pydantic_api
from src.services.pessoa import PessoaService
from src.models.pessoa import Pessoa
from datetime import datetime

@app.route('/v1/pessoas', methods=['POST'])
@pydantic_api(
        name="Post Pessoas",        # Name of path operation in OpenAPI schema
        tags=["Pessoas"],           # OpenAPI tags
        success_status_code=201
   )
async def add_pessoa(pessoa: Pessoa):
    return await PessoaService().adiciona_pessoa(pessoa) 