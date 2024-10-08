from PIL import Image
import numpy as np
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

    # Converter a imagem para escala de cinza (remover cores)
    image = image.convert('L')  # 'L' mode converte para escala de cinza

     # Aplicar binarização (usar um threshold para definir preto e branco)
    threshold = 128
    image = image.point(lambda p: p > threshold and 255)  # Binariza a imagem

    # Converter a imagem para um array numpy para facilitar o uso na rede neural
    image_np = np.array(image)  # Converte a imagem para uma matriz numpy

    # Normalizar os valores dos pixels para o intervalo [0, 1]
    image_np = image_np / 255.0

    # Converter a imagem para bytes
    # img_byte_arr = BytesIO()
    # image.save(img_byte_arr, format='PNG')  # Você pode escolher PNG ou outro formato, se preferir
    # img_byte_arr = img_byte_arr.getvalue()

    return image_np
