import logging
from flask import request, jsonify

# Middleware que é executado antes de cada requisição
def request_middleware():
  # Aqui você pode adicionar verificações e validações globais
  logging.info(f"Interceptando requisição para: {request.path}")
  
  # Exemplo de validação para garantir que a requisição seja JSON quando apropriado
  if request.method == "POST" and not request.is_json:
    return jsonify({"status": "error", "message": "JSON body required"}), 400
