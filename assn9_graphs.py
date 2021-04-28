import random
import string

g = {}
used = []
vertices = {i for i in range(1,1001)}

def unique_neighbor(used_list):
    num = random.randint(1,1001)
    while used_list.count(num) >= 5:
        num = random.randint(1,1001)
    used_list.append(num)
    return num

for vertex in vertices:
    neighbors = []
    rand_range = random.randint(1,5)
    for i in range(rand_range):
        neighbors.append(unique_neighbor(used))
    g.setdefault(vertex,neighbors)

