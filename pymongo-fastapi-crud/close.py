from pymongo import MongoClient
from dotenv import dotenv_values

# Carregar variáveis de ambiente do arquivo .env
config = dotenv_values(".env")

# Conectar ao MongoDB
client = MongoClient(config["ATLAS_URI"])

# Acessar o banco de dados e realizar operações
db = client[config["DB_NAME"]]
print("Conectado ao MongoDB!")

# Fechar a conexão após as operações
client.close()
print("Conexão com o MongoDB fechada.")
