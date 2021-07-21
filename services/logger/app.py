import socket
import flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from prometheus_client import make_wsgi_app
from core.database.log import create_log, get_logs
from core.config import SharedConfig

app = flask.Flask(__name__)
config = SharedConfig()
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})

@app.route('/logs', methods=['GET'])
def logs():
    count = 10
    page = 1

    if (flask.request.args.get('count') is not None):
        count = int(flask.request.args.get('count'))
    
    if (flask.request.args.get('page') is not None):
        page = int(flask.request.args.get('page'))

    logs = get_logs(count, page)
    return flask.jsonify(status=200, logs=logs), 200

@app.route('/logs', methods=['POST'])
def log():
    content = flask.request.get_json(silent=True)
    if content == None:
        return flask.jsonify(status=400, errors=['no body supplied']), 400

    host: str = content.get('host')
    message: str = content.get('message')
    
    if (len(host) == 0 or len(message) == 0):
        return flask.jsonify(status=400, errors=['Host and message are required']), 400

    id = create_log(host, message)

    return flask.jsonify(status=200, message='Log addeed successfully', id=id, logged_by=socket.gethostname()), 200

@app.route('/config')
def get_config():
    return config.to_json()