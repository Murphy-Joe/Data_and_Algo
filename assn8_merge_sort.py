import random
import copy

def merge_sort(ls):
    # base case -- a list of 0 or 1 is already "sorted"
    if len(ls) <= 1:
        return ls
    else:
        median_index = len(ls) // 2
        left = ls[:median_index]
        right = ls[median_index:]

        merge_sort(left)
        merge_sort(right)

        # actual sorting and merging
        merged = []
        while left and right:
            if left[0] < right[0]:
                merged.append(left[0])
                del left[0]
            else:
                merged.append(right[0])
                del right[0]

        merged.extend(left) 
        merged.extend(right)

        for i in range(len(merged)):
            ls[i] = merged[i]
        
        #ls = [i for i in merged]
        #ls = copy.deepcopy(merged)

        return ls


lis = [random.randint(1,50) for i in range(12)]
print(f"\nUnsorted: \t{lis}\n")
print(f"Merge Sorted: \t{merge_sort(lis)}\n")