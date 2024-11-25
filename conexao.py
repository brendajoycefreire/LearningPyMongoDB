from pymongo import MongoClient
from dotenv import dotenv_values

# Carrega variáveis do arquivo .env
config = dotenv_values(".env")

# Conecta ao MongoDB usando a URI do cluster fornecida no .env
try:
    client = MongoClient(config["ATLAS_URI"])
    # Tentativa de acessar informações do banco para verificar conexão
    client.server_info()  # Isso lança uma exceção se a conexão falhar
    print("Conexão bem-sucedida com o MongoDB!")
except Exception as e:
    print("Erro ao conectar ao MongoDB:", e)
finally:
    # Fecha a conexão com o cliente se ela foi estabelecida
    if 'client' in locals():
        client.close()
