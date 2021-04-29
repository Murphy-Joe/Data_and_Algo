import random
from pprint import pprint

class Node:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.neighbors = set()

    # calling node by it's object will return its name
    def __repr__(self):
        return self.name

    # so will node.get_name()
    def get_name(self):
        return self.name

    def get_neighbors(self):
        return list(self.neighbors)

    def get_number(self):
        return self.number


    
class Graph: 
    def __init__(self, nodes=set(), edges=set()):
        # skipping error catching step for wrong types given
        self.nodes = nodes
        self.edges = edges
        self.node_count = len(self.nodes)

    def add_node(self, node):
        self.nodes.add(node)
        self.node_count = len(self.nodes)
        

    def add_edge(self, node1, node2):
        self.edges.add((node1, node2))
        self.nodes.update([node1, node2])
        node1.neighbors.add(node2)
        node2.neighbors.add(node1)
        self.node_count = len(self.nodes)

    def node_obj_from_value(self, value):
        # designed for a node who's name isn't just the string of its number
        for node in self.nodes:
            if node.number == value:
                return node
        return None

    def all_nodes(self):
        nds = list(self.nodes)
        srtd = sorted(nds, key=lambda x: x.number)
        return srtd

    def all_edges(self):
        return list(self.edges)

    def all_nodes_neighbors(self):
        nd_nb = {node:node.neighbors for node in self.all_nodes()}
        return nd_nb

    def profile(self):
        attrs = self.__dict__
        return attrs

graph1 = Graph()

for i in range(1000):
    rnd_num = random.randint(1,100000)
    new_node = Node(name=str(rnd_num), number=rnd_num)
    graph1.add_node(new_node)

nodes = graph1.all_nodes()

# create edges in graph, and thereby neighbors for nodes
for node in nodes:
    if len(node.neighbors) >= 5:
        continue
    # ah, I finally understand why Java made a do-while loop now
    other_node = random.choice(list(nodes))
    while len(other_node.neighbors) >= 5 or other_node == node or other_node in node.get_neighbors():
        other_node = random.choice(list(nodes))
    graph1.add_edge(node, other_node)

pprint(graph1.all_nodes_neighbors())


