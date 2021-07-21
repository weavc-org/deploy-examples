from logger.app import app
from core.config import SharedConfig

config = SharedConfig()

if (__name__ == '__main__'):
    app.run(host=config.logger.address, port=config.logger.port)