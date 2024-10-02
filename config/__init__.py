import os

# Carregar variáveis de ambiente (se houver um arquivo .env ou outras fontes)
# Neste exemplo, usamos as variáveis já carregadas no ambiente
MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/captcha_solver')

# Se precisar de outras configurações globais, elas podem ser definidas aqui
