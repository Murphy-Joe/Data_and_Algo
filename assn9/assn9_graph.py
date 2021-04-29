import random
from pprint import pprint

class Node:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.neighbors = set()

    def __repr__(self):
        return self.name

    
class Graph: 
    def __init__(self, nodes=set(), edges=set()):
        # skipping error catching step for wrong types given
        self.nodes = nodes
        self.edges = edges
        self.node_count = len(self.nodes)

    def add_edge(self, node1, node2):
        self.edges.add((node1, node2))
        self.nodes.update([node1, node2])
        node1.neighbors.add(node2)
        node2.neighbors.add(node1)
        self.node_count = len(self.nodes)

    def find_node_from_value(self, value):
        # designed for a node who's name isn't just the string of its number
        for node in self.nodes:
            if node.number == value:
                return node
        return None

    def get_sorted_nodes(self):
        nds = list(self.nodes)
        srtd = sorted(nds, key=lambda x: x.number)
        return srtd

    def get_nodes_neighbors(self):
        nd_nb = {node:node.neighbors for node in self.get_sorted_nodes()}
        return nd_nb

    def get_profile(self):
        attrs = self.__dict__
        return attrs

nodes = set()
for i in range(1000):
    a = Node(str(i), i)
    nodes.add(a)

g = Graph(nodes)

def rand_node(max_nodes):
    val = random.randint(1,max_nodes-1)
    oth_node = g.find_node_from_value(val)
    return oth_node

# add edges to the Graph and thereby neighbors to Nodes
for node in nodes:
    if len(node.neighbors) >= 5:
        continue
    other_node = rand_node(1000)
    while len(other_node.neighbors) >= 5 or node == other_node:
        other_node = rand_node(1000)
    g.add_edge(node, other_node)

pprint(g.get_nodes_neighbors())
