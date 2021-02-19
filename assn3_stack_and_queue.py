import copy

# A simple class stack that only allows pop and push operations
class Stack:

    def __init__(self, size):
        self.stack = size*[None] 
        self.top = -1
        self.size = size

    def push(self, node):
        if self.top == self.size -1:
            return  # overflow error
        else: 
            self.top += 1
            self.stack[self.top] = copy.deepcopy(node)
    
    def pop(self):
        if self.top == -1:
            return  # underflow error
        else:
            top_before_pop = self.top
            self.top -= 1
            return self.stack[top_before_pop]


# And a queue that only has enqueue and dequeue operations
class Queue:

    def __init__(self, size):
        self.queue = size*[None] 
        self.size = size
        self.numOfNodes = 0
        self.front = 0  # oldest
        self.rear = 0   # newest

    def enqueue(self, node):
        if self.numOfNodes == self.size:
            return  # overflow error
        else:
            self.numOfNodes += 1
            self.queue[self.rear] = copy.deepcopy(node)
            self.rear = (self.rear + 1) % self.size
            return node

    def dequeue(self):
        if self.numOfNodes == 0:
            return
        else:
            front_before_dq = self.front
            self.front = (self.front + 1) % self.size
            self.numOfNodes -= 1
            return self.queue[front_before_dq]
    
    def active_queue(self):
        if self.numOfNodes == 0:
            return []
        else: 
            in_queue = self.numOfNodes *[None]
            front = copy.deepcopy(self.front)
            for i in range(self.numOfNodes):
                in_queue[i] = self.queue[front]
                front = (front + 1) % self.size
            return in_queue
            



#region stack prints
print(15*"#")
print(f"{'#':<4}Stack{'#':>6}")
print(15*"#")

stack1 = Stack(3)
print('*Stack of Size 3*')
print(f"stack:\t {stack1.stack}")
print(f"top:\t {stack1.top}")
print()

stack1.push('joe')
print('*Push joe*')
print(f"stack:\t {stack1.stack}")
print(f"top:\t {stack1.top}")
print()

stack1.pop()
print('*Pop*')
print(f"stack:\t {stack1.stack}")
print(f"top:\t {stack1.top}")
print()

stack1.push('joannie')
print('*Push joannie*')
print(f"stack:\t {stack1.stack}")
print(f"top:\t {stack1.top}")
print()

#endregion

#region queue prints

print(15*"#")
print(f"{'#':<4}Queue{'#':>6}")
print(15*"#")

print('*Queue of Size 3*')
queue1 = Queue(3)
print(f"queue:\t {queue1.queue}")
print(f"num of nodes:\t {queue1.numOfNodes}")
print(f"front:\t {queue1.front}")
print(f"rear:\t {queue1.rear}")
print(f"active queue front to rear:\t {queue1.active_queue()}")
print()

print('*Enqueue joe*')
print(f"most recent enqueue:\t {queue1.enqueue('joe')}")
print(f"queue:\t {queue1.queue}")
print(f"num of nodes:\t {queue1.numOfNodes}")
print(f"front:\t {queue1.front}")
print(f"rear:\t {queue1.rear}")
print(f"active queue front to rear:\t {queue1.active_queue()}")
print()

print('*Dequeue*')
print(f"most recent dequeue:\t {queue1.dequeue()}")
print(f"queue:\t {queue1.queue}")
print(f"num of nodes:\t {queue1.numOfNodes}")
print(f"front:\t {queue1.front}")
print(f"rear:\t {queue1.rear}")
print(f"active queue front to rear:\t {queue1.active_queue()}")
print()

print('*Enqueue joannie*')
print(f"most recent enqueue:\t {queue1.enqueue('joannie')}")
print(f"queue:\t {queue1.queue}")
print(f"num of nodes:\t {queue1.numOfNodes}")
print(f"front:\t {queue1.front}")
print(f"rear:\t {queue1.rear}")
print(f"active queue front to rear:\t {queue1.active_queue()}")
print()

print('*Enqueue Maria, Evelyn, and Murphy ...overflow*')
print(f"most recent enqueue:\t {queue1.enqueue('Maria')}")
print(f"most recent enqueue:\t {queue1.enqueue('Evelyn')}")
print(f"most recent enqueue:\t {queue1.enqueue('Murphy')}")
print(f"queue:\t {queue1.queue}")
print(f"num of nodes:\t {queue1.numOfNodes}")
print(f"front:\t {queue1.front}")
print(f"rear:\t {queue1.rear}")
print(f"active queue front to rear:\t {queue1.active_queue()}")
print()

print('*Dequeue and then Enqueue Murphy*')
print(f"most recent dequeue:\t {queue1.dequeue()}")
print(f"most recent enqueue:\t {queue1.enqueue('Murphy')}")
print(f"queue:\t {queue1.queue}")
print(f"num of nodes:\t {queue1.numOfNodes}")
print(f"front:\t {queue1.front}")
print(f"rear:\t {queue1.rear}")
print(f"active queue front to rear:\t {queue1.active_queue()}")
print()

print('*Dequeue 4 times*')
print(f"most recent dequeue:\t {queue1.dequeue()}")
print(f"most recent dequeue:\t {queue1.dequeue()}")
print(f"most recent dequeue:\t {queue1.dequeue()}")
print(f"most recent dequeue:\t {queue1.dequeue()}")
print(f"queue:\t {queue1.queue}")
print(f"num of nodes:\t {queue1.numOfNodes}")
print(f"front:\t {queue1.front}")
print(f"rear:\t {queue1.rear}")
print(f"active queue front to rear:\t {queue1.active_queue()}")
print()

#endregion