from flask import Flask, redirect

from .config import settings
from .routes import homeRoutes, userRoutes

def create_app():
  app = Flask(__name__)

  def status_401(error):
    return redirect('/login')

  def page_not_found(error):
    return "<h1>Not found page</h1>", 404

  app.config.from_object(settings['development'])
  app.register_blueprint(homeRoutes.main)
  app.register_blueprint(userRoutes.main)
  app.register_error_handler(401, status_401)
  app.register_error_handler(404, page_not_found)

  return app
