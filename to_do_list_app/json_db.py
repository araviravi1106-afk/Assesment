import json
import os

file_name="task.json"

def file_createing():
    if not os.path.exists(file_name):
        with open(file_name, 'w') as f:
            json.dump([], f,indent=4)
            

def for_file_reading():
    with open(file_name, "r") as file:
        data = json.load(file)
    return data

def for_file_writing(data):
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)