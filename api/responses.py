from flask import jsonify

# Função para formatar respostas de sucesso
def success_response(message, status_code=200):
  response = {
      "status": "success",
      "message": message
  }
  return jsonify(response), status_code

# Função para formatar respostas de erro
def error_response(message, status_code=400):
  response = {
      "status": "error",
      "message": message
  }
  return jsonify(response), status_code
