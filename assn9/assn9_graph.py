import random
from pprint import pprint

class Node:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.neighbors = []

    # calling node by it's object will return its name
    def __repr__(self):
        return self.name

    # so will node.get_name()
    def get_name(self):
        return self.name

    def get_neighbors(self):
        return self.neighbors

    def get_number(self):
        return self.number


    
class Graph: 
    def __init__(self, nodes=[], edges=[]):
        # skipping error catching step for wrong types given
        self.nodes = nodes
        self.edges = edges
        self.node_count = len(self.nodes)
        self.queue = []
        self.stack = []
        self.visited = []


    def add_node(self, node):
        self.nodes.append(node)
        self.node_count = len(self.nodes)
        
    def add_edge(self, node1, node2):
        self.edges.append((node1, node2))
        node1.neighbors.append(node2)
        node2.neighbors.append(node1)

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

    def structure(self):
        graph = {node.get_name(): node.get_neighbors() for node in self.all_nodes()}
        return graph


    def breadth_search(self, num_to_find, starting_num=None):
        if starting_num:
            starting_node = self.node_obj_from_value(starting_num)
        else:
            starting_node = random.choice(self.nodes)
        self.queue.append(starting_node)

        while self.queue:
            checking = self.queue.pop(0)
            self.visited.append(checking)
            if checking.get_number() == num_to_find:
                return f'Found {num_to_find} in {len(self.visited)} steps \nShortest path was {self.bfs_shortest()} steps'
            for neighbor in checking.get_neighbors():
                if neighbor not in self.visited and neighbor not in self.queue:
                    self.queue.append(neighbor)
        return "not found"


    def bfs_shortest(self):
        path_nodes = [self.visited[-1]]
        for node in reversed(self.visited):
            if node in path_nodes[-1].get_neighbors():
                path_nodes.append(node)
        return len(path_nodes)

    
    def depth_search(self, num_to_find, starting_num=None):
        if starting_num:
            starting_node = self.node_obj_from_value(starting_num)
        else:
            starting_node = random.choice(self.nodes)
        self.stack.insert(0,starting_node)

        while self.stack:
            checking = self.stack.pop(0)
            self.visited.append(checking)
            if checking.get_number() == num_to_find:
                return f'Found {num_to_find} in {len(self.visited)} steps \nCannot retrieve shortest path from depth search'
            for neighbor in checking.get_neighbors():
                if neighbor not in self.visited and neighbor not in self.stack:
                    self.stack.insert(0,neighbor)
        return "not found"     


graph1 = Graph()

num_nodes = 1000
max_rnd_num = 1000
num_choices = [i+1 for i in range(max_rnd_num)]

for i in range(num_nodes):
    rnd_num = random.choice(num_choices)
    num_choices.remove(rnd_num)
    new_node = Node(name=str(rnd_num), number=rnd_num)
    graph1.add_node(new_node)

nodes = graph1.all_nodes()

# create edges in graph, and thereby neighbors for nodes
for node in nodes:
    if len(node.neighbors) >= 5:
        continue
    other_node = random.choice(list(nodes))
    # ah, I finally understand why Java made a do-while loop now
    while (len(other_node.neighbors) >= 5) or (other_node == node) or (other_node in node.get_neighbors()):
        other_node = random.choice(list(nodes))
    graph1.add_edge(node, other_node)

#pprint(graph1.structure())
res = graph1.breadth_search(500)
print(res)



