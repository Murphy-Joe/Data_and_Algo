import random
from pprint import pprint

num_verts = 10
g = {}
used = []
vertices = {i for i in range(1,num_verts+1)}

# subroutine: vertex may only be used as a neighbor by 3 other vertices AND it can't use itself as a neighbor
def eligible_neighbor(used_list, current_vertex):
    num = random.randint(1,num_verts)
    while used_list.count(num) >= 3 or num == current_vertex:
        num = random.randint(1,num_verts)
    used_list.append(num)
    return num

# subroutine: ensure all vertices get used as a neighbor at least once
def num_not_used(used_list): 
    num = random.randint(1,num_verts)
    while num in used_list:
        num = random.randint(1,num_verts)
    used_list.append(num)
    return num

# use subroutines to make neighbors limited by max amount
def unique_neighbors(used_list, current_vertex, num_neighbors):
    neighbs = []
    if len(set(used_list)) < num_verts:
        neighbs.append(num_not_used(used_list))
        num_neighbors = num_neighbors - 1

    while num_neighbors > 0:
        neighbs.append(eligible_neighbor(used_list, current_vertex))
        num_neighbors = num_neighbors - 1
    return neighbs

# give each vertex 1 or 2 neighbors each
for vertex in vertices:
    rand_range = random.randint(1,2)
    neighbors = unique_neighbors(used, vertex, rand_range)
    g.setdefault(vertex,neighbors)


pprint(g)






