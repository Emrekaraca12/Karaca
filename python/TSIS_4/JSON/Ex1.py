import json

def parse_json_file(file_path):
    with open(file_path) as json_file:
        data = json.load(json_file)
    
    return data

print(parse_json_file)