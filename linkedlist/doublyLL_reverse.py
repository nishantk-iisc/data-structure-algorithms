from doublyLinkedList import DoublyLinkedList
dll = DoublyLinkedList()

elements = [5, 3, 2, 1, 9]
for ele in elements:
  dll.appendlist(ele)

dll.traversal()

### brute force solution
# stk = []
# curr_node = dll.head
# while curr_node:
#   stk.append((curr_node.data))
#   curr_node = curr_node.next

# curr_node = dll.head
# while stk:
#   curr_node.data = stk.pop()
#   curr_node = curr_node.next
# dll.traversal()


### optimal solution
curr_node = dll.head
prev_node = None

while curr_node:
  next_node = curr_node.next
  curr_node.prev = next_node
  curr_node.next = prev_node
  prev_node = curr_node
  curr_node = next_node

dll.head = prev_node
dll.traversal()