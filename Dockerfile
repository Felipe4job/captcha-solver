# Use a imagem oficial do Python como base
FROM python:3.11-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o conteúdo da aplicação para o diretório de trabalho
COPY . .

# Expõe a porta 5000, que é onde o Flask vai rodar
EXPOSE 5000

# Define a variável de ambiente para evitar que o Flask rode em modo de produção
ENV FLASK_ENV=development
ENV FLASK_APP=main.py

# Comando para iniciar o servidor Flask com hot-reload
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000", "--reload"]
