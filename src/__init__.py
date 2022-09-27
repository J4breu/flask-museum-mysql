from flask import Flask, redirect

from .config import settings
from .routes import homeRoutes, userRoutes, employeeRoutes, artRoutes


def createApp():
  app = Flask(__name__)

  def status401(error):
    return redirect("/login")

  def pageNotFound(error):
    return "<h1>Not found page</h1>", 404

  app.config.from_object(settings["development"])
  app.register_blueprint(homeRoutes.main)
  app.register_blueprint(userRoutes.main)
  app.register_blueprint(employeeRoutes.main)
  app.register_blueprint(artRoutes.main)
  app.register_error_handler(401, status401)
  app.register_error_handler(404, pageNotFound)

  return app