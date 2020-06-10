class Graph():
    def __init__(self, tree):
        self.nodes = {}
        for relationship in tree:
            r = list(relationship)
            if not r[0] in self.nodes:
                self.add_node(r[0])
            if not r[1] in self.nodes:
                self.add_node(r[1])
            self.add_child(r[0], r[1])

    def add_node(self, node_num):
        self.nodes[node_num] = set()

    def add_child(self, parent, child):
        if parent in self.nodes and child in self.nodes:
            self.nodes[parent].add(child)
        else:
            raise IndexError("Vertex does not exist")

    def get_children(self, node_num):
        return self.nodes[node_num]


def earliest_ancestor(ancestors, starting_node):
    g = Graph(ancestors)
    print(g.nodes)


if __name__ == '__main__':
    test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                      (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    print(earliest_ancestor(test_ancestors, 3))
