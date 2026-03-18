## Create a linked list (SLL)
# [5, add] --> [10, add] --> [15, add] --> [20, add] --> None

## create node
from posixpath import curdir
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

## singly linked list
class SinglyLinkedList:
  def __init__(self):
    self.head = None
  
  def appended(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return
    
    current = self.head
    while current.next:
      current = current.next
    current.next = new_node
  
  def travesal(self):
    if self.head is None:
      print("Empty list")
      return
    current = self.head
    while current:
      print(current.data, end=" --> ")
      current = current.next
    print("None")

  def insert_at_beginning(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node
  
  def insert_at_end(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return
      
    current = self.head
    while current.next:
      current = current.next
    current.next = new_node

  def insert_at_index(self, data, index):
    new_node = Node(data)
    if index == 0:
      new_node.next = self.head
      self.head = new_node
      return
    current = self.head
    prev_node = None
    count = 0
    while current is not None and count < index:
      prev_node = current
      current = current.next
      count += 1
    prev_node.next = new_node
    new_node.next =  current
  
  def delete_at_begining(self):
    if self.head is None:
      return -1
    temp = self.head
    self.head = temp.next
    temp.next = None
  
  def delete_at_end(self):
    if self.head is None:
      return -1
    current = self.head
    while current.next.next:
      current = current.next
    current.next = None
  
  def delete_a_value(self, data):
    current = self.head
    if current is not None:
      if current.data == data:
        self.head = current.next
        return 
      else:
        found = False
        prev = None
        while current is not None:
          if current.data == data:
            found = True
            break
          prev = current
          current = current.next
        if found:
          prev.next = current.next
          return
        else:
          print("Node not found")
  
  def delete_at_index(self, index):
    if self.head is None:
      return -1
    if index == 0:
      self.delete_at_begining()
      return
    prev_node = None
    current = self.head
    count = 0
    while current.next and count < index:
      prev_node = current
      current = current.next
      count += 1
    prev_node.next = current.next
    current.next = None
    return

sll = SinglyLinkedList()
sll.delete_at_begining()

sll.travesal()
for i in range(1, 50, 5):
  sll.appended(i)
print("appended")
sll.travesal()
sll.insert_at_beginning(0)
print("inserted at begining")
sll.travesal()
sll.insert_at_end(100)  
print("inserted at end")
sll.travesal()
sll.insert_at_index(2, 2)
print("inserted at index")
sll.travesal()
sll.delete_at_begining()
print("deleted at begining")
sll.travesal()
sll.delete_at_end()
print("deleted at end")
sll.travesal()
sll.delete_a_value(7)
print("deleted at value")
sll.travesal()
sll.delete_a_value(26)
print("deleted at value")
sll.travesal()
sll.delete_at_index(2)
print("deleted at index")
sll.travesal()