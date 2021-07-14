import os
import configparser
import json
from dataclasses import dataclass

class ConfigSectionMixin():
    
    def set_env_vars(self, prefix: str):
        # overrides fields with environment variables
        for f in self.__dataclass_fields__:
            setattr(self, f, os.getenv(f"{prefix.upper()}_{f.upper()}", default=getattr(self, f)))


@dataclass
class DatabaseConfig(ConfigSectionMixin):
    user: str
    password: str
    address: str
    db: str

    def __post_init__(self):
        self.set_env_vars("POSTGRES")
                
@dataclass
class WebConfig(ConfigSectionMixin):
    address: str
    port: str
    logger_address: str

    def __post_init__(self):
        self.set_env_vars("WEB")

@dataclass
class LoggerConfig(ConfigSectionMixin):
    address: str
    port: str

    def __post_init__(self):
        self.set_env_vars("LOGGER")


@dataclass(init=False)
class SharedConfig():
    raw_parser: configparser.SafeConfigParser
    database: DatabaseConfig
    web: WebConfig
    logger: LoggerConfig

    def __init__(self):
        # initialize parser
        self.raw_parser = configparser.SafeConfigParser()
        # read from configs, last overrides first
        self.raw_parser.read(["./src/defaults.ini", "./src/config.ini", "/shared_config.ini"])

        # set section values
        self.database = DatabaseConfig(**self.raw_parser['database'])    
        self.web = WebConfig(**self.raw_parser['web'])
        self.logger = LoggerConfig(**self.raw_parser['logger'])

    def to_json(self):
        model = {
            'database': self.database.__dict__,
            'logger': self.logger.__dict__,
            'web': self.web.__dict__
        }
        return json.dumps(model, skipkeys=True)
