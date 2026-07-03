
class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
#create nodes
head=node(10)
s=node(20)
t=node(30)
#connect nodes
head.next=s
s.prev=head

s.next=t
t.prev=s
#traverse forward
current=head
while current:
    print(current.data,end=" ")
    current=current.next
#traverse backward
print()
current=t
while current:
    print(current.data,end=" ")
    current=current.prev
 
 
 
 
#INSERTING AT BEGGINNING
def insert_beginning(head, data):
  new=node(data)
  if head is None:
        return new
 # new=node(5)
  new.next=head
  head.prev=new
  head=new
  current=head
  while current: 
      print(current.data,end=" ")
      current=current.next
  return head
# Call the function
print("\nAfter inserting at beginning:")
head = insert_beginning(head, 5)



#insertion at end
def insert_end(head, data):
    new=node(data)
    if head is None:
        return new
    current = head
    while current.next:
        current = current.next
    current.next = new
    new.prev = current
    return head

print("\nAfter inserting at end:")
head = insert_end(head, 40)
current = head
while current:
    print(current.data, end=" ")
    current = current.next
    
    
    
#insertion at specific position
def insert_spec(head, data, pos):
    new = node(data)
    if head is None or pos <= 0:
        if head:
            head.prev = new
            new.next = head
        return new
    current = head
    index = 0
    while current.next and index < pos - 1:
        current = current.next
        index += 1
    if current.next is None and index < pos - 1:
        current.next = new
        new.prev = current
    else:
        nxt = current.next
        current.next = new
        new.prev = current
        new.next = nxt
        if nxt:
            nxt.prev = new
    return head
print("\nAfter inserting at specific position:")
head = insert_spec(head, 25,pos=2)
current = head
while current:
    print(current.data, end=" ")
    current = current.next
    
    
    