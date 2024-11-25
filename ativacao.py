import os

# Verifica se a variável de ambiente VIRTUAL_ENV está definida
if 'VIRTUAL_ENV' in os.environ:
    print("O ambiente virtual está ativado!")
else:
    print("O ambiente virtual não está ativado.")