class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

head = Node(12)
n1 = Node(24)
head.next = n1
n2 = Node(5)
n1.next = n2
n3 = Node(65)
n2.next = n3
n4 = Node(48)
n3.next = n4

# to display elements in list
# print('----------Elements in LinkedList---------')
def display(head):
    
    if head == None:
        return
    
    temp = head
    while temp != None:
        print(temp.value)
        temp = temp.next
# display(head)

# to add element at starting of LinkedList
def add_start(head, value):
    # print(f'----------Adding {value} at start in LinkedList---------')
    if head == None:
        return

    new_node = Node(value)
    new_node.next = head
    head = new_node
    return head

head = add_start(head, 518)
# display(head)


# to add element at end of LinkedList
def add_end(head, value):
    # print(f'----------Adding {value} at end in LinkedList---------')
    if head == None:
        new_val = Node(value)
        head = new_val
    
    temp = head
    while temp.next != None:
        temp = temp.next
    
    new_val = Node(value)
    temp.next = new_val
    return
add_end(head, 51)
# display(head)

# to delete an element from LinkedList
def delete_element(head, value):
    print(f'----------Deleting {value} from LinkedList---------')
    if head == None:
        return
    
    if head.value == value:
        head = head.next
        return

    temp = head
    old = None

    while head != None:
        if temp.value == value:
            old.next = temp.next
            return 
        old = temp
        temp = temp.next

delete_element(head, 48)
display(head)