import configparser
import os


class ConfigReader:
    """
    Reads config.ini once and exposes values to the entire framework.
    No hardcoded URLs, browsers, or timeouts anywhere in the code.
    """

    def __init__(self):
        self.config = configparser.ConfigParser()
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        config_path = os.path.join(base_dir, "config", "config.ini")

        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Config file not found: {config_path}")

        self.config.read(config_path)

    def get(self, key, section="DEFAULT"):
        return self.config.get(section, key)

    def getint(self, key, section="DEFAULT"):
        return self.config.getint(section, key)

    def getboolean(self, key, section="DEFAULT"):
        return self.config.getboolean(section, key)