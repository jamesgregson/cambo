from flask import render_template
from flask_socketio import send, emit

from appl import app, socketio

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@socketio.on('my event')
def handle_message(json):
    print('Received message: ' + str(json) )

@socketio.on('set_pwm')
def handle_message(json):
    app.hw.left_pwm  = json['pwmL']
    app.hw.right_pwm = json['pwmR'] 
    emit( 'status', {'quaternion': app.hw.quaternion} )