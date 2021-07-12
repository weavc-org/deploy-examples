from flask import Flask
import socket
import requests
import os

app = Flask(__name__)

logger = os.getenv("LOGGER_ADDRESS", default="http://localhost:5001")
address = os.getenv("LADDRESS", default="0.0.0.0")
port = os.getenv("LPORT", default=5000)

@app.route("/")
def hello_world():
    result = log_request()
    hostname = socket.gethostname()
    return f"<p>Hello!</p><p>host: {hostname}</p><p>{result}</p>"

def log_request() -> str :
    # make request to logger service
    try:
        r = requests.post(
            f"{logger}/log", 
            json={"host": socket.gethostname(), "message": "request recieved"})

        # handle result
        if (r.status_code == 200):
            j = r.json()
            r.close()
            return f"log successful (id: {j['id']}, logged by: {j['logged_by']})"
        else:
            r.close()
            return "log unsuccessful"

    except Exception:
        print("an error occured while sending the log")
        return "log unsuccessful"

if (__name__ == "__main__"):
    app.run(host=address, port=port)