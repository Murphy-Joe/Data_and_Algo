import string

print(ord('a'), ord('z'))

class Node:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.neighbors = set()

    def __repr__(self):
        return self.name

nodes = []
for i in range(97,102):
    a = Node(str(i), i)
    nodes.append(a)
    print(a)

