import socket
import requests
import os
import json
from flask import Flask
from ..config import SharedConfig

app = Flask(__name__)
config = SharedConfig()

@app.route("/")
def index():
    result = log_request()
    hostname = socket.gethostname()
    return f"<p>Hello!</p><p>host: {hostname}</p><p>{result}</p>"

@app.route("/config")
def get_config():
    return config.to_json()

def log_request() -> str :
    # make request to logger service
    try:
        r = requests.post(
            f"{config.web.logger_address}/log", 
            json={"host": socket.gethostname(), "message": "request recieved"})

        # handle result
        if (r.status_code == 200):
            j = r.json()
            r.close()
            return f"log successful (id: {j['id']}, logged by: {j['logged_by']})"
        else:
            r.close()
            return "log unsuccessful"

    except Exception as err:
        print(f"an error occured while sending the log: {err}")
        return "log unsuccessful"

if (__name__ == "__main__"):
    app.run(host=config.web.address, port=config.web.port)