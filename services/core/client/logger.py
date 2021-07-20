import requests
import socket
from core.config import SharedConfig

config = SharedConfig()

def log_request(message: str) -> tuple():
    # make request to logger service
    try:
        r = requests.post(
            f"{config.web.logger_address}/logs", 
            json={"host": socket.gethostname(), "message": message})

        # handle result
        if (r.status_code == 200):
            j = r.json()
            r.close()
            return True, j
        else:
            r.close()
            return False, {}

    except Exception as err:
        print(f"an error occured while sending the log: {err}")
        return False, {}

def get_logs_request() -> tuple:
    # make request to logger service
    try:
        r = requests.get(
            f"{config.web.logger_address}/logs")

        # handle result
        if (r.status_code == 200):
            j = r.json()
            r.close()
            return True, j
        else:
            r.close()
            return False, {}

    except Exception as err:
        print(f"an error occured while sending the log: {err}")
        return False, {}