# TestsSample.Python.Flask

Projeto para demonstração em Python de Testes Unitários e de Integração utilizando Flask e pytest.


# Execução:

- criar diretório virtual para instalação dos packages
```
    python -m venv venv
```
- ativar
```
  .\venv\Scripts\activate

  Visual Studio Code

  Ctrl + Shift + P

  opção Selecionar o Interpretador 

  indicar o arquivo python.exe dentro do diretório virtual .\venv\Scripts
```
- instalar os pacotes
```
    pip install -r requirements.txt
```
- Execução 

  - Aplicação
  ```
      no diretório raiz
      
      flask --app src/app run --reload 

      RapiDoc -> http://127.0.0.1:5000/apidocs/
  ```
  - Testes
  ```
    no diretório raiz
    
    python -m pytest -v
  ```

# Referências

https://realpython.com/api-integration-in-python/#flask

https://docs.pytest.org/en/7.3.x/

https://docs.pydantic.dev/usage/validators/

https://github.com/adamsussman/flask-pydantic-api

https://understandingdata.com/posts/list-of-python-assert-statements-for-unit-tests/

https://rapidocweb.com/
