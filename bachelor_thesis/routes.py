from flask import Flask
from flask import render_template
from flask import redirect
from flask_http2_push import http2push
from flask_socketio import SocketIO
from flask_socketio import send
from flask_socketio import emit


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/http2/push')
@http2push('Path/to/Push_manifest')
def http_2_push():
    return render_template('push_it.html')

# HTML 5 preload Attribute used with the three different values


@app.route('/html_5/load/auto')
def html_5_load_it_auto():
    return render_template('load_it_auto.html')


@app.route('/html_5/load/metadata')
def html_5_load_it_metadata():
    return render_template('load_it_metadata.html')


@app.route('/html_5/load/none')
def html_5_load_it_none():
    return render_template('load_it_none.html')

# HTML 5 prefetch Tag for the <link> Attribute


@app.route('/html_5/fetch')
def html_5_push():
    return render_template('fetch_it.html')


@app.route('/javascript/client_loop?1')
def javascript_client_loop():
    return render_template('client_loop_it.html')


@app.route('/javascript/server_loop')
def javascript_server_loop():
    return redirect('http://bachelor.dev/javascript/server_loop_1')


@app.route('/javascript/server_loop_1')
def javascript_server_loop_1():
    return redirect('http://bachelor.dev/javascript/server_loop')


@app.route('/javascript/ajax')
def javascript_ajax():
    return render_template('ajax_it.html')


@app.route('/javascript/source.html')
def javascript_ajax_source():
    return render_template('source.html')


@app.route('/favicon')
def favicon():
    return render_template('favicon.html')


@socketio.on('message')
def handleMessage(msg):
    print('Message: ' + msg)
    send(msg, broadcast=True)


@socketio.on('connect')
def connect():
    i = 0
    while i < 20:
        emit('c_message', {'hello': "Hello, this is a Test!"})
        i = i + 1


@app.route('/websocket')
def websocket():
    return render_template('websocket.html')


if __name__ == "__main__":
    # app.run(debug=True)
    socketio.run(app)
