class Node:
    def __init__(self,data):#__init__ is a special method that runs automatically when you create an object.
        self.data=data
        self.next=None
def print_list(head):
    current = head
 
    while current:#Keep looping as long as current is not None.
       print(current.data,end="->")
       current=current.next
    print("None")
head=Node(10)
s=Node(20)
t=Node(30)
head.next = s
s.next = t
current = head
print_list(head)

#insertion at beginning
new_node=Node(5)
new_node.next=head
head=new_node
print_list(head)

#insertion at end
new_node = Node(40)
current = head

while current.next:
    current=current.next
current.next=new_node
print_list(head)

#insertion at given place
current=head
while current.data != 20:
    current = current.next

new_node = Node(25)
new_node.next = current.next
current.next = new_node

print("\nAfter Insertion After 20:")
print_list(head)

#deletion at beggining
head = head.next
print_list(head)
#deletion at end
current = head

while current.next.next:
    current = current.next
current.next = None
print_list(head)
#deletion at given place
current = head

while current.next.data != 20:
    current = current.next

current.next = current.next.next
print_list(head)