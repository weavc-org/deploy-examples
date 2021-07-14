import socket
import flask
from ..database.log import create_log, get_logs
from ..config import SharedConfig

app = flask.Flask(__name__)
config = SharedConfig()

@app.route("/")
def logs():
    message = "";
    logs = get_logs()
    for log in logs:
        message += f"[{log.date}] {log.host}: {log.message}<br/>"

    return message

@app.route("/config")
def get_config():
    return config.to_json()

@app.route("/log", methods=["POST"])
def log():
    content = flask.request.get_json(silent=True)
    if content == None:
        return flask.jsonify(status=400, errors=["no body supplied"]), 400

    host: str = content.get("host")
    message: str = content.get("message")
    
    if (len(host) == 0 or len(message) == 0):
        return flask.jsonify(status=400, errors=["Host and message are required"]), 400

    id = create_log(host, message)

    return flask.jsonify(status=200, message="Log addeed successfully", id=id, logged_by=socket.gethostname()), 200

if (__name__ == "__main__"):
    app.run(host=config.logger.address, port=config.logger.port)