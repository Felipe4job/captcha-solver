from pymongo import MongoClient
from config import MONGO_URI

# Função para conectar ao banco de dados
def get_db():
  client = MongoClient(MONGO_URI)
  db = client['captcha_solver']
  return db

# Função para obter as coleções de logs e dados de treinamento
def get_collections():
  db = get_db()
  logs_collection = db['logs']
  train_collection = db['train_data']
  return logs_collection, train_collection
