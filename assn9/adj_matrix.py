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


    
verts = list(m1.labels.keys())

for label, index in m1.idx.items():
    if len(m1.neighbs(label)) >= 5:
        continue
    other_vert = random.choice(verts)
    # ah, I finally understand why Java made a do-while loop now
    while (len(m1.neighbs(other_vert)) >= 5) or (other_vert == label) or (other_vert in m1.neighbs(other_vert)):
        other_vert = random.choice(verts)
    m1.add_edge(label, other_vert)

print(m1.matrix)