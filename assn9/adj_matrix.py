matrix = [
    [0,1,0],
    [1,0,1],
    [1,1,0]
]

labels = {0:'a', 1:'b', 2:'c'}

def idx_from_label(label):
    for k,v in labels.items():
        if v == label:
            return k

def neighbs(label):
    nbs = []
    column_idx = idx_from_label(label)
    for i, row in enumerate(matrix):
        if row[column_idx]:
            nb = labels[i]
            nbs.append(nb)
    return nbs

print(neighbs('c'))
