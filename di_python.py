import re
import json

with open('./inventory', 'r') as f:
    contents = f.read()

#print(contents)
matches = re.findall(f'\[(.*)\]\nansible_host=(.*)', contents)
host_dict = {}
for match in matches:
    host_dict[match[0]] = {'ansible_host': match[1]}

json_data = {'all': {'hosts': host_dict}}

with open("inventory.json", "w") as file:
    json.dump(json_data, file, indent=4)
#print(json.dumps(json_data, indent=4))