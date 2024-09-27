from flask import request
from services import save_training_data, validate_image_size, process_image, save_log
from api import error_response, success_response

def configure_routes(app):

    @app.route("/captcha/train", methods=["POST"])
    def train_captcha_model():
      try:
        # Verificar se há arquivos e dados JSON na requisição
        if 'images' not in request.files or 'results' not in request.form:
            return error_response("Images and results are required", 400)

        images = request.files.getlist('images')
        results = request.form.getlist('results')

        # Validar a quantidade de imagens
        if len(images) > 10:
            return error_response(f"Maximum 10 images allowed per request", 400)

        # Verificar se o número de imagens corresponde ao número de resultados
        if len(images) != len(results):
            return error_response("Each image must have a corresponding result", 400)

        training_data = []

        # Processar cada imagem
        for i, image_file in enumerate(images):
            # Validar o tamanho da imagem
            if not validate_image_size(image_file):
                return error_response(f"Image {image_file.filename} exceeds maximum size of 2MB", 400)

            # Processar a imagem (transformar, validar)
            try:
                processed_image = process_image(image_file)
            except Exception as e:
                return error_response(f"Invalid image {image_file.filename}: {str(e)}", 400)

            # Adicionar à lista de dados de treinamento
            training_data.append({
                "image_name": image_file.filename,
                "result": results[i],
                "image_data": processed_image
            })

        # Salvar os dados de treinamento no banco via serviço
        save_training_data(training_data)

        return success_response(f"Successfully uploaded {len(images)} images for training", 200)

      except Exception as e:
        save_log("ERROR", f"Error during training data upload: {str(e)}")
        return error_response("Internal server error", 500)
