from pprint import pprint
import random

""" matrix = [
    [0,1,0],
    [1,0,1],
    [1,1,0]
]

labels = {0:'a', 1:'b', 2:'c'}
idx = {'a':0, 'b':1, 'c':2} """

class Vertex:
    def __init__(self, label, index=None):
        self.label = label
        self.index = index

class Matrix:
    def __init__(self):
        self.matrix = [[]]
        self.idx = {}
        self.labels = {}
        self.listings = []


    def neighbs(self, label):
        index = self.idx[label]
        nbs = [self.labels[i] for i, row in enumerate(self.matrix) if row[index]]
        return nbs
    
    def get_edges(self, label):
        nbs = self.neighbs(label)
        edges = [(label, nb) for nb in nbs]
        return edges

    def add_edge(self, label1, label2):
        i1 = self.idx[label1]
        i2 = self.idx[label2]
        self.matrix[i1][i2], self.matrix[i2][i1] = 1, 1

    def del_edge(self, label1, label2):
        i1 = self.idx[label1]
        i2 = self.idx[label2]
        self.matrix[i1][i2], self.matrix[i2][i1] = 0, 0   

    def add_vertex(self, label):
        index = len(self.labels.keys())
        self.labels.setdefault(index, label)
        self.idx.setdefault(label, index)
        [row.append(0) for row in self.matrix]
        self.matrix.append([0]*(index+1))

    def del_vertex(self, label):
        index = self.idx[label]
        nbs = [self.idx[i] for i in self.neighbs(label)]
        for i in nbs:
            self.matrix[index][i], self.matrix[i][index] = 0,0

    def bfs_verts(self, goal_label, starting_label=None):
        if not starting_label:
            starting_label = random.choice(list(self.labels.values()))
        queue = []
        visited = []
        queue.append(starting_label)
        while queue:
            checking = queue.pop(0)
            visited.append(checking)
            if checking == goal_label:
                return visited
            queue.extend(self.neighbs(checking))

    def bfs_edges(self, goal_label, starting_label=None):
        if not starting_label:
            starting_label = random.choice(list(self.labels.values()))
        queue = []
        visited = []
        queue.extend(self.get_edges(starting_label))
        while queue:
            edge = queue.pop(0)
            visited.append(edge)
            checking = edge[1]
            if checking == goal_label:
                return visited
            queue.extend([(checking, nb) for nb in self.neighbs(checking)])

    def shortest(self,goal_label, starting_label=None):
        visited = self.bfs_edges(goal_label, starting_label)
        path = []
        path.append(visited[-1])
        for edge in reversed(visited):
            if edge[1] == path[-1][0]:
                path.append(edge)
        return len(path)

        



num_verts = 1000
max_rdm_num = 1000
num_choices = [i for i in range(max_rdm_num)]

m1 = Matrix()

for i in range(num_verts):
    rdm_num = random.choice(num_choices)
    num_choices.remove(rdm_num)
    lbl = str(rdm_num)
    m1.labels.setdefault(i, lbl)
    m1.idx.setdefault(lbl, i)
    m1.add_vertex(lbl)

verts = list(m1.labels.values())

for lbl, index in m1.idx.items():
    if len(m1.neighbs(lbl)) >= 5:
        continue
    other_vert = random.choice(verts)
    while (len(m1.neighbs(other_vert)) >= 5) or (other_vert == lbl) or (other_vert in m1.neighbs(lbl)):
        other_vert = random.choice(verts)
    m1.add_edge(lbl, other_vert)


print(m1.shortest('655'))