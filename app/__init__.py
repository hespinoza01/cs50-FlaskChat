from flask import Flask
from flask_socketio import SocketIO, emit
from .routes import routes
from .config import Config


app = Flask(__name__, static_folder='public')

app.config.from_object(Config)
app.register_blueprint(routes)

server = SocketIO(app)

"""
@server.on('my event')
def on_my_event(res):
    print(res['data'])


@server.on('connect')
def on_connect():
    print('new client')
    emit('hello', {'data': 'Hello from server'})


@server.on('disconnect')
def on_disconnect():
    print('bye bye client')
"""