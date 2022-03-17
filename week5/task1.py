"""
FILES to YAML
"""

import argparse
import json
import json.decoder
import os
from pathlib import Path
import yaml
import yaml.scanner


def walk_thru(startdir: str) -> list:
    p = Path(startdir)
    a = [str(el).replace('\\', '/').replace(startdir, '') for el in p.rglob('*')]
    return a


def read_file_content(filepath: str):
    with open(filepath) as file:
        content = file.read()

    try:
        template = yaml.safe_load(content)
        return template
    except yaml.scanner.ScannerError:
        pass

    try:
        template = json.loads(content)
        return template
    except json.decoder.JSONDecodeError:
        pass

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
    parser = argparse.ArgumentParser()
    parser.add_argument('startdir', type=str)
    args = parser.parse_args()
    startdir = args.startdir + '/'

    dirs_and_files = walk_thru(startdir)

    res = dir_tree_dict(startdir)

    res = {startdir.split('/')[-2]: res}

    with open('week5/res.yaml', 'w', newline='') as newfile:
        yaml.dump(res, newfile, default_flow_style=False)
