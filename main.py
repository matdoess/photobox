import configparser

config = configparser.ConfigParser()
config.read('./config/global-config.ini')

private_config = configparser.ConfigParser()
private_config.read('./config/private-config.ini')

from kivy.config import Config
Config.read(config['kivy']['config_file'])

import sys
import settings


# Environment festlegen
env = sys.argv[1] if len(sys.argv) > 1 else 'raspberrypi'

# Environment in globale Liste schreiben
settings.myList["env"] = env

# Config in globale Variable schreiben
settings.myList['config'] = config._sections

# Private_Config in globale Variable schreiben
settings.myList['private_config'] = private_config._sections

from ScreenManagerApp import ScreenManagerApp

if __name__ == '__main__':
    screenManagerApp = ScreenManagerApp()
    screenManagerApp.run()