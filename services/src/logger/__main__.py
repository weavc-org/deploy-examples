import socket
import flask
from ..database import create_log, get_logs

app = flask.Flask(__name__)

@app.route("/")
def logs():
    message = "";
    logs = get_logs()
    for log in logs:
        message += f"[{log.date}] {log.host}: {log.message}<br/>"

    return message

@app.route("/log", methods=["POST"])
def log():
    content = flask.request.get_json(silent=True)
    if content == None:
        return flask.jsonify(status=400, errors=["no body supplied"]), 400

    host: str = content.get("host")
    message: str = content.get("message")
    
    if (len(host) == 0 or len(message) == 0):
        return flask.jsonify(status=400, errors=["Host and message are required parameters"]), 400

    id = create_log(host, message)

    return flask.jsonify(status=200, message="Log addeed successfully", id=id, logged_by=socket.gethostname()), 200

if (__name__ == "__main__"):
    app.run(host="0.0.0.0", port=5001)