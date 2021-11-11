import os
from flask import Flask
from flask_socketio import SocketIO


app = Flask(
            __name__,
            static_url_path='',
            static_folder='www',
            template_folder='templates'
        )
app.config['SECRET_KEY'] = 'password'

socketio = SocketIO(app)

from appl import routes
from appl import hardware

app.hw = hardware.DummyHardware()

socketio.run(app)