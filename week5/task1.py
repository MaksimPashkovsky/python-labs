"""
YAML генерация
"""

import json
import os
import yaml
from sys import argv


def walk_thru(startdir: str) -> list:
    a = list()
    for root, dirs, files in os.walk(startdir):
        s = root.replace(startdir, '')
        if not s:
            a.extend([file for file in files])
            a.extend([dir for dir in dirs])
        else:
            a.extend([s + '/' + file for file in files])
            a.extend([s + '/' + dir for dir in dirs])
    return a


def dir_tree_dict(startdir: str) -> dict:
    d = {}
    for item in dirs_and_files:
        p = d
        for x in item.split('/'):
            _, ext = os.path.splitext(item)
            if ext == '.txt':
                with open(startdir + item) as txt_file:
                    content = txt_file.read()
                p = p.setdefault(x, content)
            elif ext == '.yaml':
                with open(startdir + item) as yaml_file:
                    template = yaml.safe_load(yaml_file)
                p = p.setdefault(x, template)
            elif ext == '.json':
                with open(startdir + item) as json_file:
                    template = json.load(json_file)
                p = p.setdefault(x, template)
            elif ext == '':
                p = p.setdefault(x, {})
    return d


if __name__ == '__main__':
    startdir = argv[1] + '/'

    dirs_and_files = walk_thru(startdir)

    res = dir_tree_dict(startdir)

    res = {startdir.split('/')[-2]: res}

    with open('week5/res.yaml', 'w', newline='') as newfile:
        yaml.dump(res, newfile, default_flow_style=False)