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

        left_srt = merge_sort(left)
        right_srt = merge_sort(right)

        # actual sorting and merging
        merged = []
        while left_srt and right_srt:
            if left_srt[0] < right_srt[0]:
                merged.append(left_srt.pop(0))
            else:
                merged.append(right_srt.pop(0))

        merged.extend(left_srt) 
        merged.extend(right_srt)

        return merged


lis = [random.randint(1,50) for i in range(12)]
print(f"\nUnsorted: \t{lis}\n")
print(f"Merge Sorted: \t{merge_sort(lis)}\n")