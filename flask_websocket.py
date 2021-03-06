from flask import Flask, render_template
from flask_socketio import SocketIO
import time
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


# @socketio.on('message')
# def handle_message(message):
#     print(message["data"])

#     emit('response', {"response": [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]})
#     time.sleep(2)
#     
#     
@socketio.on('message')
def handle_message(message):
	"""线程开启任务"""
	socketio.start_background_task(task_even, message)

def task_even(message):
	"""定义任务"""
	print(message["data"])
	while True:
	    socketio.emit('response', {"response": [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)]})
	    socketio.sleep(2)


if __name__ == '__main__':
    socketio.run(app)
