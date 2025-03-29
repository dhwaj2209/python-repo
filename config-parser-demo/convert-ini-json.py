# Python configparser
#1. Convert INI file to JSON format string.
#2. Convert INI file to JSON format file.

#INI to JSON String


import configparser
import json
config = configparser.ConfigParser()
file = open("../Sources/app_settings.ini","r")
config.read_file(file)
dict1=dict()
sections=config.sections()
for section in sections:
    items=config.items(section)
    dict1[section]=dict(items)

json_string=json.dumps(dict1)
print("JSON string is:")
print(json_string)
file.close()


#INI to JSON File

config = configparser.ConfigParser()
file = open("../Sources/app_settings.ini", "r")
config.read_file(file)
dict1 = dict()
sections = config.sections()
print(sections)
for section in sections:
    items = config.items(section)
    dict1[section] = dict(items)

json_file = open("../Sources/app_settings_jsonformat.json", "w")
json.dump(dict1, json_file)
json_file.close()
file.close()
