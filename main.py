from pymongo import MongoClient
import pandas as pd
import os

# Conectando com o MongoDB
mongo_client = MongoClient(os.environ.get("DB_STRING"))

# Criando base de dados 'escola'
mydb = mongo_client["escola"]

# Criando coleção 'alunos'
mycol = mydb["alunos"]

# Inserindo documento na coleção 'alunos'
mydict = {"nome": "Joaozinho",
          "ano": "Primeiro"}
x = mycol.insert_one(mydict)

# Mostrando a coleção 'alunos'
cursor = mycol.find({})
for document in cursor:
    print(document)

