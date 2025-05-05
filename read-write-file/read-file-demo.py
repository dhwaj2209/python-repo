# Read & Write files in Python
import json
file_path = "../Sources/employee1.json"
person_dict1 = {'name': 'Bob',
'age': 12,
'country':'China'
}
with open(file_path, 'w') as json_file:
    json.dump(person_dict1, json_file)






