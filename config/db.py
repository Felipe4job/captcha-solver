from pymongo import MongoClient
from config import MONGO_URI
from datetime import datetime

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

# Função para adicionar timestamps (created_at e updated_at)
def add_timestamps(data, is_update=True):
  now = datetime.now()
  data['updated_at'] = now

  if not is_update:
    data['created_at'] = now
    
  return data