from flask import Flask
from flask_socketio import SocketIO, emit, send
from .routes import routes, session
from .config import Config


app = Flask(__name__, static_folder='public')

app.config.from_object(Config)
app.register_blueprint(routes)

server = SocketIO(app)


@server.on('message', namespace='/')
def on_my_event(res):
    emit('sendmessage', res, broadcast=True)
    print("received message: %s" %str(res))


@server.on('connect')
def on_connect():
    print('new client')
    nick = session.get('nickname') or 'none'
    emit('joined', {'user': nick}, broadcast=True)


@server.on('disconnect')
def on_disconnect():
    print('bye bye client')
