## Create a Node
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

## Single Linked List
class SinglyLinkedList:
  def __init__(self):
    self.head = None
  
  def appendlist(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
    else:
      current = self.head
      while current.next:
        current = current.next
      current.next = new_node
  
  def traversal(self):
    if self.head is None:
      print("LL is empty!")
      return
    current = self.head
    while current:
      print(current.data, end="-->")
      current = current.next
    print("none")

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
    if index == 0:
      self.insert_at_beginning(data)
    else:
      new_node = Node(data)
      prev_node = None
      count = 0
      curr_node = self.head
      while curr_node.next and count < index:
        count += 1
        prev_node = curr_node
        curr_node = curr_node.next
      new_node.next = prev_node.next
      prev_node.next = new_node
    
  def delete_at_beginning(self):
    if self.head:
      temp = self.head
      self.head = self.head.next
      temp = None
    else:
      print("LL is empty!")
  
  def delete_at_end(self):
    if self.head is None:
      print('LL is empty!') 
      return 
   
    if self.head.next is None:
      self.head = None
      return
    
    curr_node = self.head
    while curr_node.next.next:
      curr_node = curr_node.next
    curr_node.next = None

  def delete_a_value(self, data):
    if self.head is None:
      print("LL is empty")
      return
    if self.head.data == data:
      self.head = self.head.next
      return
    curr_node = self.head
    while curr_node.next:
      if curr_node.next.data == data:
        curr_node.next = curr_node.next.next
        return
      curr_node = curr_node.next
    print(f"{data} is not present")


if __name__ == "__main__":
  sll = SinglyLinkedList()

  for data in range(0, 21, 4):
    sll.appendlist(data)
  sll.traversal()

  sll.insert_at_beginning(24)
  sll.traversal()

  sll.insert_at_end(25)
  sll.traversal()

  sll.insert_at_index(-1, 0)
  sll.traversal()

  sll.insert_at_index(-11, 3)
  sll.traversal()

  sll.delete_at_beginning()
  sll.traversal()

  sll.delete_at_end()
  sll.traversal()

  sll.delete_a_value(12)
  sll.traversal()

  sll.delete_a_value(7)
  sll.traversal()