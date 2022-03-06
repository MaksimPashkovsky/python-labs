from task1 import Node


class Graph:
    @staticmethod
    def create_from_nodes(nodes: list):
        return Graph(nodes)

    def __init__(self, nodes = None):
        self.adjacency_matrix = [[0] * len(nodes) for _ in range(len(nodes))]
        self.nodes = nodes
        for i in range(len(self.nodes)):
            self.nodes[i].cur_id = i

    def connect_two(self, node1, node2, weight = 1):
        n1_index = self.get_index_from_node(node1)
        n2_index = self.get_index_from_node(node2)
        self.adjacency_matrix[n1_index][n2_index] = weight

    def connect(self, node1, node2, weight = 1):
        self.connect_two(node1, node2, weight)
        self.connect_two(node2, node1, weight)

    def get_index_from_node(self, node):
        if isinstance(node, int):
            return node
        else:
            return node.cur_id

    def connections_from(self, node):
        node = self.get_index_from_node(node)
        return [
                (self.nodes[col_num], self.adjacency_matrix[node][col_num])
                for col_num in range(len(self.adjacency_matrix[node]))
                if self.adjacency_matrix[node][col_num] != 0
                ]

    def print_adjacency_matrix(self):
        for row in self.adjacency_matrix:
            print(row)

    def dijkstra(self, node : Node):
        nodenum = self.get_index_from_node(node)
        dist = [None] * len(self.nodes)
        for i in range(len(dist)):
            dist[i] = [float("inf")]
            dist[i].append([self.nodes[nodenum]])

        dist[nodenum][0] = 0

        queue = [i for i in range(len(self.nodes))]
        seen = set()
        while len(queue) > 0:
            min_dist = float("inf")
            min_node = None
            for n in queue:
                if dist[n][0] < min_dist and n not in seen:
                    min_dist = dist[n][0]
                    min_node = n

            queue.remove(min_node)
            seen.add(min_node)
            connections = self.connections_from(min_node)

            for node, weight in connections:
                tot_dist = weight + min_dist
                if tot_dist < dist[node.cur_id][0]:
                    dist[node.cur_id][0] = tot_dist
                    dist[node.cur_id][1] = list(dist[min_node][1])
                    dist[node.cur_id][1].append(node)
        return dist

    def distance(self, node):
        res = [(weight, [n.data for n in node]) for weight, node in graph.dijkstra(node)]
        d = dict()
        for w, path in res:
            d[path[-1]] = w, path
        return d


if __name__ == "__main__":
    a = Node("A")
    b = Node("B")
    c = Node("C")
    d = Node("D")
    e = Node("E")
    f = Node("F")

    graph = Graph.create_from_nodes([a, b, c, d, e, f])

    graph.connect(a, b, 14)
    graph.connect(a, c, 9)
    graph.connect(a, f, 7)
    graph.connect(b, d, 9)
    graph.connect(b, c, 2)
    graph.connect(c, e, 11)
    graph.connect(c, f, 10)
    graph.connect(d, e, 6)
    graph.connect(e, f, 15)

    from_a = graph.distance(a)
    from_d = graph.distance(d)

    # tests
    assert from_a['A'][0] == 0
    assert from_a['B'][0] == 11
    assert from_a['C'][0] == 9
    assert from_a['D'][0] == 20
    assert from_a['E'][0] == 20
    assert from_a['F'][0] == 7

    assert from_d['A'][0] == 20
    assert from_d['B'][0] == 9
    assert from_d['C'][0] == 11
    assert from_d['D'][0] == 0
    assert from_d['E'][0] == 6
    assert from_d['F'][0] == 21
    print("All tests passed")
