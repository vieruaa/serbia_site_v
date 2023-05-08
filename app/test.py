import json
from pathlib import Path, PosixPath
import os


house_number = 4
path = os.path.abspath(os.curdir)
with open(f'{path}/templates/static/assets/json/house_{house_number}.json', 'r', encoding='utf-8') as fp:
    src = json.load(fp)
    print(src)


# house_number = 5
# with open(f'templates/static/assets/json/house_{house_number}.json', 'r') as fp:
#     src = json.load(fp)


# with p.open('r', encoding='utf-8') as file:
#     print(file.read())
