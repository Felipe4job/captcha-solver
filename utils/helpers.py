from PIL import Image
from io import BytesIO
import numpy as np

def numpy_to_image_bytes(image_np, format='PNG'):
  # Converter o array numpy de volta para uma imagem PIL
  image = Image.fromarray((image_np * 255).astype(np.uint8))  # Converte para 8-bit e normaliza
  
  # Salvar a imagem como bytes em memória
  img_byte_arr = BytesIO()
  image.save(img_byte_arr, format=format)
  img_byte_arr = img_byte_arr.getvalue()
  
  return img_byte_arr  # Retorna os bytes da imagem (pronto para enviar ou codificar em base64)