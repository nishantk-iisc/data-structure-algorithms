from doublyLinkedList import DoublyLinkedList
dll = DoublyLinkedList()

elements = [1, 2, 2, 3, 2, 4, 2, 5]
for ele in elements:
  dll.appendlist(ele)

dll.traversal()

key = 2

## brute force
# st = set()
# curr_node = dll.head
# while curr_node:
#   if curr_node.data != key:
#     st.add(curr_node.data)
#   curr_node = curr_node.next

# curr_node = dll.head
# while st:
#   curr_node.data = st.pop()
#   if not st:
#     curr_node.next = None
#   curr_node = curr_node.next
# dll.traversal()

## optimal solution
curr_node = dll.head
prev_node = None
new_head = dll.head
while curr_node:
  if curr_node.data == key:
    if prev_node is not None:
      prev_node.next = curr_node.next
    if curr_node.next is not None:
      curr_node.next.prev = prev_node
    if curr_node == new_head:
      new_head = curr_node.next
  
  if curr_node.data == key:
    curr_node = curr_node.next
  else:
    prev_node = curr_node
    curr_node = curr_node.next

dll.head = new_head
dll.traversal()


