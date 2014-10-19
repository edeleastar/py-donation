from flask import Flask
from config import config

def create_app(config_name):
  app = Flask(__name__)
  app.config.from_object(config[config_name])
  config[config_name].init_app(app)

  from .controllers import accounts as account_blueprint
  app.register_blueprint(account_blueprint)

  from .controllers import donate as donate_blueprint
  app.register_blueprint(donate_blueprint)

  return app
