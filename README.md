# LearningPyMongoDB

Requisitos
O projeto finalizado está disponível no Github . Você também pode seguir as instruções passo a passo para construir o projeto do zero. Para fazer isso, você precisará do seguinte:

Python 3.6+ — Você pode instalá-lo no site do Python .
Um cluster MongoDB Atlas — Você pode criar um cluster forever-free seguindo o guia Get Started with Atlas . Conclua as etapas no guia e localize sua string de conexão — você precisará dela para se conectar ao banco de dados a partir do aplicativo.

# Criar o ambiente virtual
python -m venv env-pymongo-fastapi-crud

# Ativar o ambiente virtual no Windows
env-pymongo-fastapi-crud\Scripts\activate

# um pequeno teste para saber se o ambiente está ativado

- crie um arquivo .py qualquer e cole este código:

import os

# Verifica se a variável de ambiente VIRTUAL_ENV está definida
if 'VIRTUAL_ENV' in os.environ:
    print("O ambiente virtual está ativado!")
else:
    print("O ambiente virtual não está ativado.")

- caso o ambiente virtual esteja ativado, a resposta será dada no terminal

# Agora que temos um ambiente virtual, podemos instalar os pacotes necessários. Usaremos pip—o instalador de pacotes para Python, que também está incluso na sua instalação do Python:
    python -m pip install 'fastapi[all]' 'pymongo[srv]' python-dotenv

# Em seguida, criaremos um diretório para nosso projeto, navegaremos até ele e criaremos o scaffold dos arquivos necessários para o projeto.

    # Criar o diretório
    mkdir pymongo-fastapi-crud

    # Entrar no diretório
    cd pymongo-fastapi-crud

    # Criar os arquivos
    echo.> main.py
    echo.> routes.py
    echo.> models.py
    echo.> .env

# Vamos começar implementando um /endpoint root simples que retorna uma mensagem de boas-vindas. Abra o main.pyarquivo no seu editor de código favorito e adicione o seguinte:

pymongo-fastapi-crud/main.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the PyMongo tutorial!"}

# Salve o arquivo e execute o aplicativo usando o uvicornpacote que foi instalado junto com o fastapipacote.

python -m uvicorn main:app --reload
