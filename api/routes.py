from flask import request
from services import save_training_data, validate_image_size, process_image, save_log, get_images_with_empty_result
from api.responses import error_response, success_response

def configure_routes(app):

    @app.route("/captcha/train", methods=["POST"])
    def train_captcha_model():
      try:
        # Verificar se há arquivos e dados JSON na requisição
        if 'images' not in request.files:
            return error_response("Images are required", 400)

        images = request.files.getlist('images')

        # Validar a quantidade de imagens
        if len(images) > 10:
            return error_response(f"Maximum 10 images allowed per request", 400)

        training_data = []

        # Processar cada imagem
        for image_file in images:            

            # Validar o tamanho da imagem
            if not validate_image_size(image_file):
                return error_response(f"Image {image_file.filename} exceeds maximum size of 2MB", 400)

            # Processar a imagem (transformar, validar)
            processed_image = process_image(image_file)

            # Adicionar à lista de dados de treinamento
            training_data.append({
                "image_name": image_file.filename,
                "result": "",
                "image_data": processed_image
            })

        # Salvar os dados de treinamento no banco via serviço
        save_training_data(training_data)

        return success_response(f"Successfully uploaded {len(images)} images for training", 200)

      except Exception as e:
        save_log("ERROR", f"Error during training data upload: {str(e)}")
        return error_response(f"Error during training data upload: {str(e)}", 500)


    @app.route("/captcha/images/pending", methods=["GET"])
    def get_pending_images():
        try:
            # Obter imagens com campo result vazio
            pending_images = get_images_with_empty_result()

            if not pending_images:
                return success_response("No pending images found", 200)

            return success_response(pending_images, 200)

        except Exception as e:
            save_log("ERROR", f"Error retrieving pending images: {str(e)}")
            return error_response(f"Error retrieving pending images: {str(e)}", 500)