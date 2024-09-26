import logging
import os
from flask import Flask, request, jsonify
from pymongo import MongoClient
from datetime import datetime

# Configuração do MongoDB
mongo_uri = os.getenv('MONGO_URI', 'mongodb://localhost:27017/captcha_solver')
client = MongoClient(mongo_uri)
db = client['captcha_solver']
logs_collection = db['logs']

# Configurando o logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s', handlers=[
    logging.FileHandler("captcha_solver.log"),
    logging.StreamHandler()
])

# Função para salvar logs no MongoDB
def save_log(level, message, captcha_id=None):
    log_entry = {
        "level": level,
        "message": message,
        "captcha_id": captcha_id,
        "timestamp": datetime.now()
    }
    logs_collection.insert_one(log_entry)

app = Flask(__name__)

# Rota para verificar se a API está funcionando
@app.route("/health", methods=["GET"])
def health_check():
    logging.info("Health check request received.")
    return jsonify({"status": "success", "message": "API is running."}), 200

# Rota para processar captchas
@app.route("/captcha/solve", methods=["POST"])
def solve_captcha():
    try:
        # Verifica se a requisição contém uma imagem
        if 'captcha_image' not in request.files:
            error_message = f"No captcha image found in request."
            logging.error(error_message)
            save_log("ERROR", error_message)
            return jsonify({"status": "error", "message": "Captcha image not provided"}), 400

        captcha_image = request.files['captcha_image']

        # Simulação de processamento do captcha
        logging.info("Captcha image received for processing.")
        # Aqui você adicionaria o código de processamento da imagem

        # Simulação de resposta (resposta correta fictícia)
        response = {
            "status": "success",
            "message": "Captcha processed successfully",
            "solution": "12345"  # Exemplo de solução fictícia
        }
        logging.info(f"Captcha processed successfully. Solution: {response['solution']}")
        return jsonify(response), 200

    except Exception as e:
        logging.error(f"Error processing captcha: {str(e)}")
        return jsonify({"status": "error", "message": "Internal server error"}), 500

# Rota para receber feedback sobre o captcha (acerto ou erro)
@app.route("/captcha/feedback", methods=["POST"])
def feedback_captcha():
    try:
        data = request.get_json()

        if not data or 'captcha_id' not in data or 'correct_solution' not in data:
            logging.error("Invalid feedback data received.")
            save_log("ERROR", "Invalid feedback data received.")
            return jsonify({"status": "error", "message": "Invalid feedback data"}), 400

        captcha_id = data['captcha_id']
        correct_solution = data['correct_solution']

        # Aqui você adicionaria a lógica de aprendizado com base no feedback

        logging.info(f"Feedback received for captcha {captcha_id}. Correct solution: {correct_solution}")
        return jsonify({"status": "success", "message": "Feedback received"}), 200

    except Exception as e:
        logging.error(f"Error processing feedback: {str(e)}")
        return jsonify({"status": "error", "message": "Internal server error"}), 500

# Iniciar o servidor Flask
if __name__ == "__main__":
    logging.info("Starting Captcha Solver API server...")
    app.run(debug=True, host='0.0.0.0', port=5000)
