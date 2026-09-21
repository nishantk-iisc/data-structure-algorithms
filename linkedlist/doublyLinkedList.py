## Create Node
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None
  
class DoublyLinkedList:
  def __init__(self):
    self.head = None

  def insert_at_head(self, data):
    new_node = Node(data)
    if not self.head:
      self.head = new_node
    else:
      new_node.next = self.head
      self.head.prev = new_node
      self.head = new_node

  def appendlist(self, data):
    new_node = Node(data) 
    if self.head is None:
      self.head = new_node
      return
    curr_node = self.head
    while curr_node.next :
      curr_node = curr_node.next
    curr_node.next = new_node
    new_node.prev = curr_node
  
  def traversal(self):
    if self.head is None:
      print("DLL is empty!")
      return
    curr_node = self.head
    while curr_node:
      print(curr_node.data, end=" <==> ")
      curr_node = curr_node.next
    print(None)

  def insert_at_end(self, data):
    new_node = Node(data)
    if not self.head:
      self.head = new_node
      return
    curr_node = self.head
    while curr_node.next:
      curr_node = curr_node.next
    curr_node.next = new_node
    new_node.prev = curr_node

  def insert_at_index(self, data, index):
    new_node = Node(data)
    if index == 0:
      self.insert_at_head(data)
      return
    curr_node= self.head
    count =  0
    while curr_node and count < index - 1:
      curr_node = curr_node.next
      count += 1
    
    if not curr_node:
      print(f"position {index} out of bound!")
      return
    
    new_node.next = curr_node.next
    new_node.prev = curr_node

    if curr_node.next:
      curr_node.next.prev = new_node
    curr_node.next = new_node

  def delete_head(self):
    if self.head is None:
      return
    if not self.head.next:
      self.head = None
      return
    curr_node = self.head
    self.head = curr_node.next
    curr_node.next = None
    self.head.prev = None
  
  def delete_last(self):
    if not self.head:
      return
    if not self.head.next:
      self.delete_head()
      return
    curr_node = self.head
    while curr_node.next.next:
      curr_node = curr_node.next
    curr_node.next.prev = None
    curr_node.next = curr_node.next.next

  def delete_at_index(self, index):
    if index == 0:
      self.delete_head()
      return
    curr_node = self.head
    count = 0
    while curr_node and count < index:
      curr_node = curr_node.next
      count += 1
    curr_node.prev.next = curr_node.next
    curr_node.next.prev = curr_node.prev
    curr_node.next = None
    curr_node.prev = None


if __name__=="__main__": 
  dll = DoublyLinkedList()

  print("# append a element")
  dll.appendlist(-5)
  dll.traversal()
  dll.delete_last()
  print("# delete head")
  dll.delete_head()
  dll.traversal()

  print("# append elements")
  for num in range(0, 41, 5):
    dll.appendlist(num)
  dll.traversal()

  print("# Insert at head")
  dll.insert_at_head(-10)
  dll.traversal()

  print("# insert at end")
  dll.insert_at_end(45)
  dll.traversal()

  print("# insert a position 100")
  dll.insert_at_index(0, 100)

  print("# insert a position 0")
  dll.insert_at_index(-1, 0)
  dll.traversal()

  print("# insert a position 3")
  dll.insert_at_index(-7, 3)
  dll.traversal()

  print("# delete head")
  dll.delete_head()
  dll.traversal()

  print("# delete last element")
  dll.delete_last()
  dll.traversal()

  print("# delete at index 0")
  dll.delete_at_index(0)
  dll.traversal()

  print("# delete at index 2")
  dll.delete_at_index(2) 
  dll.traversal()