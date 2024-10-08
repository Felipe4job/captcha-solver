import logging
from flask import request, jsonify

# Middleware que é executado antes de cada requisição
def request_middleware():
  # Aqui você pode adicionar verificações e validações globais
  logging.info(f"Interceptando requisição para: {request.path}")
