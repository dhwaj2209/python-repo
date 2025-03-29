# configparser in Python
import configparser
config = configparser.ConfigParser()
config.read(['app_settings.ini'])
general = config["General"]
val = general.get("app_name")
print(val)

val = general.get("app_name", fallback = "test")
print(val)




