from PIL import Image
from io import BytesIO

# Limite de tamanho de imagem
MAX_IMAGE_SIZE = 2 * 1024 * 1024  # 2 MB

# Função para validar o tamanho da imagem
def validate_image_size(image_file):
    return image_file.content_length <= MAX_IMAGE_SIZE

# Função para processar a imagem (pode incluir binarização, redimensionamento, etc.)
def process_image(image_file):
    image = Image.open(BytesIO(image_file.read()))
    image.verify()  # Verificar se a imagem é válida
    # Aqui você pode aplicar transformações na imagem se necessário
    return image
