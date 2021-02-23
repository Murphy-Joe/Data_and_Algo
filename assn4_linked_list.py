import copy

class Node: 
   
    # Initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None

    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next

    def set_next(self, node):
        self.next = node


   

class LinkedList: 
     
    # Initialize the Linked List object
    def __init__(self):  
        self.head = None

    def print(self):
        walker = self.head # which is a node object
        while walker:
            print(walker.get_data())
            walker = walker.get_next()

    def print_w_address(self):
        walker = self.head # which is a node object
        while walker:
            print(f"{walker.get_data()} {walker}")
            walker = walker.get_next()

    def final_node_index(self):
        walker = self.head
        i = -1
        while walker:
            walker = walker.get_next()
            i += 1
        return i

    def walk_indices(self, index):
        walker = self.head
        i = 0
        while walker:
            if index == i:
                return walker
            else:
                i += 1
                walker = walker.get_next()
        return None

    
    def data_val_to_index(self, data_val):
        walker = self.head
        i = 0
        while walker and walker.get_data() != data_val:
            walker = walker.get_next()
            i += 1
        if walker:
            return i
        else:
            return

    def data_val_to_node(self, data_val):
        walker = self.head
        while walker and walker.get_data() != data_val:
            walker = walker.get_next()
        if walker:
            return walker
        else:
            return

    def insert_node(self, index, new_node):
        if index == 0:
            new_node.set_next(self.head)
            self.head = new_node
        elif index == self.final_node_index() + 1:
            prev_node = self.walk_indices(index - 1)
            prev_node.set_next(new_node)
            new_node.set_next(None)
        elif 0 < index <= self.final_node_index():
            prev_node = self.walk_indices(index - 1)
            new_node.set_next(prev_node.get_next())
            prev_node.set_next(new_node)
        
    def delete_node(self, index):
        if index == 0:
            self.head = self.head.get_next()
        elif index == self.final_node_index():
            prev_node = self.walk_indices(index - 1)
            prev_node.set_next(None)
        elif 0 < index <= self.final_node_index():
            prev_node = self.walk_indices(index - 1)
            node_to_del = prev_node.get_next()
            prev_node.set_next(node_to_del.get_next())
        
    def update_or_replace_node(self, index, new_node):
        if index == 0:
            new_node.set_next(self.head.get_next())
            self.head = new_node
        elif index == self.final_node_index():
            prev_node = self.walk_indices(index - 1)
            prev_node.set_next(new_node)
        elif 0 < index <= self.final_node_index():
            prev_node = self.walk_indices(index - 1)
            node_to_replace = prev_node.get_next()
            prev_node.set_next(new_node)
            new_node.set_next(node_to_replace.get_next())


    def ascend_nodes_by_data_val(self):
        num_of_nodes = self.final_node_index()+1
        temp_list = num_of_nodes*[None]

        # create list of data values
        for i in range(num_of_nodes):
            node = self.walk_indices(i)
            data_val = node.get_data()
            temp_list[i] = data_val

        # bubble sort data values
        swapped = 1
        while swapped > 0:
            swapped = 0
            for i in range(num_of_nodes-1):
                if temp_list[i] > temp_list[i+1]:
                    placeholder = temp_list[i]
                    temp_list[i] = temp_list[i+1]
                    temp_list[i+1] = placeholder
                    swapped += 1

        # assign node objects from the sorted values using data_val_to_node
        new_llist = LinkedList()
        for i in range(num_of_nodes):
            data_val = temp_list[i]
            node = self.data_val_to_node(data_val)
            node_copy = copy.deepcopy(node)
            if i == 0:
                new_llist.head = node_copy
            elif 0 < i <= self.final_node_index():
                new_llist.insert_node(i, node_copy)
            
        return new_llist
                
            


# Start with the empty list 
llist = LinkedList() 
first = Node(1)
second = Node(2) 
third = Node(3) 

llist.head = first
first.next = second
second.next = third

print('Original Nodes')
llist.print()
print('\nInsert Node with data value 4 at position 2')
fourth = Node(4)
llist.insert_node(2, fourth)
llist.print()

print('\nDelete whatever Node holds position 0')
llist.delete_node(0)
llist.print()

print("\nReturn a Node's index based on its data value (value = 3)")
index_of_val = llist.data_val_to_index(3)
print(index_of_val)

print("\nUpdate whatever Node is at position 1 (Node w/ data 4 will be replace by Node w/ data 5)")
fifth = Node(5)
llist.update_or_replace_node(1, fifth)
llist.print()

print("\nAdd more nodes for the sorting test")
llist.insert_node(0,fourth)
llist.insert_node(4, first)
llist.print()

print("\nSort the linked list in ascending order by data value")
sorted_llist = llist.ascend_nodes_by_data_val()
sorted_llist.print_w_address()









