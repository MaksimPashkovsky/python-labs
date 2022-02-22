import csv
from dataclasses import dataclass, field


@dataclass
class Node:
    data: ...
    id: int = None
    child_nodes: list = field(default_factory=list)


nodes_dict = dict()


def find_node_by_id(id: int) -> Node:
    return nodes_dict[id] if id in nodes_dict else None


if __name__ == "__main__":
    delimiter = ';'
    with open(r"week2\tree2.csv", newline="", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=delimiter)
        for i, val in enumerate(reader):
            this_id, ch_id = int(val[0]), int(val[1])
            if this_id not in nodes_dict:
                nodes_dict[this_id] = Node(this_id, this_id, [ch_id])
            else:
                nodes_dict.get(this_id).child_nodes.append(ch_id)
            if ch_id not in nodes_dict:
                nodes_dict[ch_id] = Node(ch_id, ch_id, [])
    print(nodes_dict)
