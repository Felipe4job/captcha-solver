from flask import Flask
from .middleware import request_middleware
from .routes import configure_routes
from .responses import success_response, error_response

def create_app():
  app = Flask(__name__)

  # Registrar o middleware
  app.before_request(request_middleware)

  # Registrar as rotas
  configure_routes(app)

  return app
