from web.app import app
from core.config import SharedConfig

config = SharedConfig()

if (__name__ == '__main__'):
    app.run(host=config.web.address, port=config.web.port)