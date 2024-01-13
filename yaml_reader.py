# Using a library to read yaml file

import yaml
from basic import my_function

with open('file.yaml') as f:
    inp = yaml.safe_load(f)
    print(my_function(inp["input"]))
