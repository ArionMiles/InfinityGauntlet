import os
import configparser


class Configurer:
    def __init__(self, filename="config.ini"):
        print("initialised configurations")
        self.abs_filename = self.get_abs_filename(filename)
        self.config = configparser.ConfigParser()
        self.config.read(self.abs_filename)
        self.sections = self.config.sections()

    @staticmethod
    def get_abs_filename(filename):
        return os.path.abspath(os.path.join(os.path.dirname(__file__), filename))

    def get_configuration(self, key, section="REDDIT"):
        try:
            value = self.config[section][key]
        except KeyError:
            print("API KEYS FOR '%s' is not provided in the config.ini file."
                  " Refer back to the docs" % key)
            return False
        if value:
            return value
        print("The correct API KEY wasn't provided for %s" % key)
        return False


config = Configurer()
