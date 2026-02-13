class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0 #push할때마다 +1 pop 할때마다 -1
    
    def push(self, data):
        new_node = Node(data)
        
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            current = self.tail
            current.next = new_node
            self.tail = new_node
            
        self.count += 1
        
    def empty(self):
        return self.head == None
            
            
    def pop(self):
        if self.empty():
            self.tail = None
            self.count = 0
            return -1
        
        current = self.head
        self.head = current.next
        self.count -= 1
        return current.data
            
    
    def size2(self):
        return self.count
    
    
    def front(self):
        if self.head == None:
            return -1
        return self.head.data
    
    def back(self):
        if self.tail == None:
            return -1
        return self.tail.data
    
q = Queue()


N = int(input())

for i in range(N):
    q.push(i+1)
    
while q.size2() > 1:
    print(q.pop(), end=" ")
    q.push(q.pop())




print(q.pop())
    
    
    
