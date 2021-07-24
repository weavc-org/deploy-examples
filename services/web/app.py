import socket
import flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from prometheus_client import make_wsgi_app
from core.config import SharedConfig
from core.client.logger import log_request, get_logs_request

app = flask.Flask(__name__)
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})
config = SharedConfig()

@app.route('/', methods = ['GET', 'POST'])
def index():
    errors = []
    if (flask.request.method == 'POST'):
        message = flask.request.form['message']
        result = log_request(message)

        if (result[0]):
            success = f'Log successful (id: {result[1]["id"]}, logged by: {result[1]["logged_by"]})'
            return flask.render_template('log.html', success=success, hostname=socket.gethostname(), logs=get_logs())
        else:
            errors.append('An unexpected error occured while submitting the log')
    else:
        return flask.render_template('log.html', hostname=socket.gethostname(), logs=get_logs())

    return flask.render_template('log.html', errors=errors, hostname=socket.gethostname(), logs=get_logs())    

@app.route('/config')
def get_config():
    return config.to_json()

def get_logs() -> list:
    logsResult = get_logs_request()
    if (logsResult[0]):
        return logsResult[1]['logs']
    else: 
        return []