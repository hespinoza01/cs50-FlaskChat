from flask import Flask
from .routes import routes
from .config import Config


app = Flask(__name__, static_folder='public')

app.config.from_object(Config)

app.register_blueprint(routes)
