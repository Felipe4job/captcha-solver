from config.db import get_collections, add_timestamps
from datetime import datetime
from utils.helpers import numpy_to_image_bytes
import base64
import numpy as np

# Obter as coleções do MongoDB
logs_collection, train_collection = get_collections()

# Função para salvar os dados de treinamento no banco de dados
def save_training_data(training_data):

    # Iterar sobre cada item em training_data e adicionar os timestamps
    for data in training_data:
        data['model_type'] = 'rec'

        # Converter o campo 'image_data' de numpy.ndarray para uma lista
        if isinstance(data["image_data"], np.ndarray):
            data["image_data"] = data["image_data"].tolist()

        add_timestamps(data, False)

    train_collection.insert_many(training_data)

# Função para salvar logs no banco de dados
def save_log(level, message, captcha_id=None):
    log_entry = {
        "level": level,
        "message": message,
        "captcha_id": captcha_id,
        "timestamp": datetime.now()
    }

    add_timestamps(log_entry, False)
    logs_collection.insert_one(log_entry)

# Função para buscar todas as imagens que têm o campo 'result' vazio
def get_images_with_empty_result():

    # Busca no banco de dados as imagens com campo result vazio ou nulo
    pending_images = train_collection.find({"result": {"$in": [None, ""]}})
    
    # Converte o resultado para uma lista de dicionários contendo os campos relevantes
    pending_images_list = []
    for image in pending_images:
        # Codifica a imagem em Base64 para que possa ser usada em JSON e no frontend
        # image_data_base64 = base64.b64encode(image.get("image_data")).decode('utf-8')

        # Recuperar a imagem que está armazenada em numpy (se for o caso)
        image_np = np.array(image.get("image_data"))

        # Converter a imagem numpy de volta para bytes
        image_bytes = numpy_to_image_bytes(image_np)

        # Codifica a imagem em Base64 para que possa ser usada em JSON e no frontend
        image_data_base64 = base64.b64encode(image_bytes).decode('utf-8')

        pending_images_list.append({
            "image_name": image.get("image_name"),
            "image_data": image_data_base64,
            "created_at": image.get("created_at")
        })
    
    return pending_images_list