import pytest
from io import BytesIO
from api import create_app

# Configuração do pytest para rodar o cliente de testes do Flask
@pytest.fixture
def client():
  app = create_app()
  app.config['TESTING'] = True
  with app.test_client() as client:
      yield client

def test_train_captcha_route(client):
  # Abrir as imagens de teste da pasta test_images
  with open('tests/images/captcha1.jfif', 'rb') as img1, open('tests/images/captcha1.jfif', 'rb') as img2:

    # Preparar os arquivos e dados do formulário
    data = {
        # 'results': ['12345', '67890'],  # Resultados correspondentes às imagens
        'images': [
            (img1, 'captcha1.png'),  # Arquivo de imagem
            (img2, 'captcha2.png')   # Arquivo de imagem
        ]
    }

    # Enviar a requisição POST com múltiplas imagens e resultados
    response = client.post(
        '/captcha/train',
        data=data,
        content_type='multipart/form-data'
    )

    # Exibir o status HTTP da resposta
    print(f"Status Code: {response.status_code}")

    # Exibir a mensagem de resposta (em formato JSON)
    response_data = response.get_json()
    print(f"Response Message: {response_data['message']}")

    # Verificar o status HTTP da resposta
    assert response.status_code == 200

    # Verificar o conteúdo da resposta
    assert 'Successfully uploaded' in response_data['message']

def test_get_pending_images_empty_response(client):
    # Fazer a requisição GET para obter imagens pendentes (campo 'result' vazio)
    response = client.get('/captcha/images/pending')

    # Exibir o status HTTP da resposta
    print(f"Status Code: {response.status_code}")

    # Exibir a mensagem de resposta (em formato JSON)
    response_data = response.get_json()
    print(f"Response Message: {response_data['message']}")

    # Verificar o status HTTP da resposta
    assert response.status_code == 200

    # Verificar que a resposta está vazia (sem imagens pendentes)
    response_data = response.get_json()
    assert response_data['message'] == "No pending images found"
    
