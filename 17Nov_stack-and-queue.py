# Stack: Last In First Out ------------------------------------------------------------------
class Stack():
    def __init__(self):
        self.list1 = []

    def is_empty(self):
        return len(self.list1) == 0
    
    def peek(self):
        if len(self.list1) == 0:
            raise Exception ('no elements in stack')

        end_ind = len(self.list1) - 1
        return self.list1[end_ind]

    def size(self):
        return len(self.list1)
    
    def push(self, ele):
        return self.list1.append(ele)
    
    def pop(self):
        if len(self.list1) == 0:
            raise Exception ('no elements in stack')
        
        return self.list1.pop()

s1 = Stack()
s1.push(5)              # [5]
print(s1.peek())        # 5
s1.push(5)              # [5, 5]
s1.push(54)             # [5, 5, 54]
s1.push(21)             # [5, 5, 54, 21]
s1.push(254)            # [5, 5, 54, 21, 254]
s1.push(58721)          # [5, 5, 54, 21, 254, 58721]
print(s1.peek())        # 58721, top element in stack
print(s1.is_empty())    # false
print(s1.size())        # 6
print(s1.pop())         # removed from stack: 58721, elements remained in stack:[5, 5, 54, 21, 254]
print(s1.pop())         # removed from stack: 254, elements remained in stack:[5, 5, 54, 21]
print(s1.size())        # 4


# Queue: First In First Out ----------------------------------------------------------------------------

class Queue():
    def __init__(self):
        self.list1 = []

    def is_empty(self):
        return len(self.list1) == 0
    
    def peek(self):
        if len(self.list1) == 0:
            raise Exception ('no elements in stack')

        return self.list1[0]

    def size(self):
        return len(self.list1)
    
    def push(self, ele):
        return self.list1.insert(0, ele)
    
    def pop(self):
        if len(self.list1) == 0:
            raise Exception ('no elements in stack')
        
        return self.list1.pop()

q1 = Queue()
q1.push(5)              # [5]
print(q1.peek())        # 5
q1.push(5)              # [5, 5]
q1.push(54)             # [54, 5, 5]
q1.push(21)             # [21, 54, 5, 5]
q1.push(254)            # [254, 21, 54, 5, 5]
q1.push(58721)          # [58721, 254, 21, 54, 5, 5]
print(q1.peek())        # 58721
print(q1.is_empty())    # false
print(q1.size())        # 6
print(q1.pop())         # first element entered stack is 5, 5 removed: [58721, 254, 21, 54, 5]
print(q1.pop())         # first element entered stack is 5, 5 removed: [58721, 254, 21, 54]
print(q1.size())        # 4