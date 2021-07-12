from flask import Flask
import socket
import requests

app = Flask(__name__)

@app.route("/")
def hello_world():
    log_request()
    hostname = socket.gethostname()
    return f"<p>Hello, World!</p><p>host: {hostname}</p>"

def log_request():
    try:
        r = requests.post(
            "http://logger:5001/log", 
            json={"host": socket.gethostname(), "message": "request recieved"})

        if (r.status_code != 200):
            print(r.json())
        else:
            print("log was successful")
        
        r.close()
    except Exception:
        print("an error occured while sending the log")

if (__name__ == "__main__"):
    app.run(host="0.0.0.0", port=5000)