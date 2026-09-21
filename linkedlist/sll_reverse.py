from singlyLinkedList import SinglyLinkedList
sll = SinglyLinkedList()
nums = [5, 8, 7, 3, 2]
for num in nums:
  sll.appendlist(num)
sll.traversal()

## Brute force
# stack = list()
# curr_node = sll.head
# while curr_node:
#   stack.append(curr_node.data)
#   curr_node = curr_node.next

# curr_node = sll.head
# while stack:
#   curr_node.data = stack.pop()
#   curr_node = curr_node.next

# sll.traversal() 

## Optimal Solution
curr_node = sll.head
prev_node = None
while curr_node:
  front = curr_node.next
  curr_node.next = prev_node
  prev_node = curr_node
  curr_node = front

sll.head = prev_node
sll.traversal()

