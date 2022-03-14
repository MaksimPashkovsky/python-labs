"""
FILES to YAML
"""

import json
import json.decoder
import os
import yaml
import yaml.scanner
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


def read_file_content(filepath: str):
    with open(filepath) as yaml_file:
        try:
            template = yaml.safe_load(yaml_file)
            return template
        except (yaml.scanner.ScannerError, UnicodeDecodeError):
            pass
    with open(filepath) as json_file:
        try:
            template = json.load(json_file)
            return template
        except (json.decoder.JSONDecodeError, UnicodeDecodeError):
            pass
    with open(filepath, mode='r+b') as file:
        content = file.read()
    return content


def dir_tree_dict(startdir: str) -> dict:
    d = {}
    for item in dirs_and_files:
        p = d
        for x in item.split('/'):
            if os.path.isdir(startdir + item):
                p = p.setdefault(x, {})
            else:
                content = read_file_content(startdir + item)
                p = p.setdefault(x, content)
    return d


if __name__ == '__main__':
    startdir = argv[1] + '/'

    dirs_and_files = walk_thru(startdir)

    res = dir_tree_dict(startdir)

    res = {startdir.split('/')[-2]: res}

    with open('week5/res.yaml', 'w', newline='') as newfile:
        yaml.dump(res, newfile, default_flow_style=False)
