from config.db import get_collections
from datetime import datetime

# Obter as coleções do MongoDB
logs_collection, train_collection = get_collections()

# Função para salvar os dados de treinamento no banco de dados
def save_training_data(training_data):
    train_collection.insert_many(training_data)

# Função para salvar logs no banco de dados
def save_log(level, message, captcha_id=None):
    log_entry = {
        "level": level,
        "message": message,
        "captcha_id": captcha_id,
        "timestamp": datetime.now()
    }
    logs_collection.insert_one(log_entry)
