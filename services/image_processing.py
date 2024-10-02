from PIL import Image
from io import BytesIO

# Limite de tamanho de imagem
MAX_IMAGE_SIZE = 2 * 1024 * 1024  # 2 MB

# Função para validar o tamanho da imagem
def validate_image_size(image_file):
    return image_file.content_length <= MAX_IMAGE_SIZE

# Função para processar a imagem (pode incluir binarização, redimensionamento, etc.)
def process_image(image_file):
    # Abrir a imagem usando PIL
    image = Image.open(image_file)

    # Converter a imagem para bytes
    img_byte_arr = BytesIO()
    image.save(img_byte_arr, format='JPEG')  # Você pode escolher PNG ou outro formato, se preferir
    img_byte_arr = img_byte_arr.getvalue()

    return img_byte_arr
