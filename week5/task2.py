"""
YAML to FILES
"""

import os
import yaml
from typing import Any


def traverse(d: dict, l: list[tuple[str, Any]]) -> list[tuple[str, Any]]:
    for key in list(d):
        if isinstance(d[key], dict):
            continue
        l.append((key, d[key]))
        del d[key]

    if not d:
        return l

    for key, value in d.items():
        d[key] = {key + '/' + k: v for k, v in value.items()}

    res = dict()

    for v in d.values():
        res.update(v)

    return traverse(res, l)


def create_files_and_dirs(startdir: str, template: dict):
    files_and_dirs = traverse(template, [])

    for rel_path, content in files_and_dirs:
        abs_path = startdir + rel_path
        if content is None:
            # empty directory
            os.mkdir(abs_path)
        else:
            *dirs, filename = abs_path.split('/')
            os.makedirs('/'.join(dirs), exist_ok=True)
            with open(abs_path, 'w') as file:
                file.write(str(content))


if __name__ == '__main__':
    file_path = 'week5/struct.yaml'
    startdir = 'D:/testdir2/'

    with open(file_path) as yaml_file:
        template = yaml.safe_load(yaml_file)

    create_files_and_dirs(startdir, template)
