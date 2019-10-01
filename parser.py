from .log import Log

from pathlib import Path
import configparser


class Parser:

    log = Log()

    home_directory = str(Path.home())
    parser = configparser.ConfigParser()

    def __init__(self):  # Add specific directory, and .ini
        self.log.debug('Reading .stuff_config.ini from \'%s\'' %
                       (self.home_directory))
        self.parser.read("%s/.stuff_config.ini" % self.home_directory)

        pass

    def get_configuration_value(self, section, key):
        self.log.debug('Reading key \'%s\' from section \'%s\'' %
                       (key, section))
        return self.parser.parser.get(section, key)
