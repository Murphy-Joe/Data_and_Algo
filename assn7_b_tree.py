import copy

class NodeTree:
    def __init__(self, value):
        self.value = value


    def __init__(self, values: list):
        values = sorted(values)
        self.values = values
        length = len(values)
        self.left_child = None
        self.right_child = None
    
        if length == 1:
            self.value = values[0]
        elif length == 2:
            min = min(values)
            max = max(values)
            self.value = max
            self.left_child = NodeTree(min)
        else:
            median = int(length/2)
            left_list = copy.deepcopy(values[:median])
            right_list = copy.deepcopy(values[median+1:])
            self.value = values[median]
            # recursive part -- new instance goes back through the list-as-value constructor
            if left_list:
                self.left_child = NodeTree(left_list)
            if right_list:
                self.right_child = NodeTree(right_list)

    def binary_search_digits(self, val):
        if val == self.value:
            return f"Value of {val} found at Node Object {self}"
        elif val > self.value:
            return self.right_child.binary_search_digits(val)
        elif val < self.value:
            return self.left_child.binary_search_digits(val)

                

digit_tree1 = NodeTree([1,2,3,4,5,6,7])
res1 = digit_tree1.binary_search_digits(2)
print(res1)

digit_tree2 = NodeTree([7,1,6,2,5,3,4])
res2 = digit_tree2.binary_search_digits(2)
print(res2)









    

