# Read & Write files in Python
import json 
import csv

# Opening a file
file_path = "Sources/app-plain-text.txt"
f = open(file_path, 'r')
print(f.read())
f.close()

# Opening a file with context manager
with open(file_path, 'r') as file:
    print(file.read())
    file.close()

# Reading few bytes from file 
with open(file_path) as file:
    print(file.read(17))

# Reading one line at a time from file 
with open(file_path) as file:
    print(file.readline())

# Reading multiple lines from file 
with open(file_path) as file:
    lines = file.readlines()
    print(lines)
    print(type(lines))

# Creating new text file 
file_path1 = r'Sources/app-plain-text11.txt'
f = open(file_path1, "x")
f.write("New file..")
f.close()

# write data in file 
file_path = r'Sources/app-plain-text.txt'
file = open(file_path,"w")
L = ["This is first line \n","This is second line \n","This is third line \n"]
file.write("Hello Python \n")
file.writelines(L)
file.close()


# read CSV file    
file_path = "Sources/sampleData.csv"
with open(file_path) as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        print(row)


# write CSV file    
file_path = r'../Sources/SampleData.csv'
row1 = [8,"A8", "a8@test.com"]     
with open(file_path, "a") as file:
    wr = csv.writer(file)
    wr.writerow(row1)


# create CSV file    
import csv
file_path = r'../Sources/SampleData1.csv'
with open(file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["name", "age", "country"]
    writer.writerow(field)
    writer.writerow(["John", "40", "US"])
    writer.writerow(["Raj", "22", "India"])
    writer.writerow(["Anthony", "50", "UK"])

# read CSV file with Pandas library   
import pandas as pd
file_path = r'../Sources/SampleData.csv'
data = pd.read_csv(file_path)
print(data)

# read/write JSON files
import json
file_path = r'../Sources/employee.json'
with open(file_path) as f:
    content = json.load(f)
    print(content)

    
# Traversing the json file
for emp in content:
    print("Name: ", emp["emp_name"])
    print("Age: ", emp["age"])
    print("Country: ", emp["country"])

print(content[1]["emp_name"])

    
# Loads and Dumps methods with json
json_string = '{"name": "John", "age": "30", "country": "UK" }'
# Getting dictionary
person_dict = json.loads(json_string)
print(person_dict)
print(type(person_dict))
# Pretty Printing JSON string back
print(json.dumps(person_dict, indent = 8, sort_keys=True))


# Convert dictionart to JSON object
person_dict1 = {'name': 'Bob',
'age': 12,
'country':'China'
}
json_object = json.dumps(person_dict1)
print(type(json_object))
print(json_object)

# write data to JSON file
person_dict1 = {'name': 'Bob',
'age': 12,
'country':'China'
}
with open(file_path, 'w') as json_file:
  json.dump(person_dict1, json_file)
