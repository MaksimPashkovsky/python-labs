import csv


class Node:
    def __init__(self, id, child_nodes):
        self.id = id
        self.child_nodes = child_nodes

    def __repr__(self):
        return f"Node(id = {self.id}, child_nodes = {self.child_nodes})"


nodes_dict = dict()


def find_node_by_id(id: int):
    return nodes_dict[id] if id in nodes_dict else None


if __name__ == "__main__":
    delimiter = ';'
    with open(r"D:\Python\pythonProject1\week2\tree2.csv", newline="", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=delimiter)
        for i, val in enumerate(reader):
            this_id, ch_id = int(val[0]), int(val[1])
            if this_id not in nodes_dict:
                nodes_dict[this_id] = Node(this_id, [ch_id])
            else:
                nodes_dict.get(this_id).child_nodes.append(ch_id)
            if ch_id not in nodes_dict:
                nodes_dict[ch_id] = Node(ch_id, [])
    print(nodes_dict)