from singlyLinkedList import SinglyLinkedList

sll = SinglyLinkedList()
nums = [5, 9, 1, 7, 6, 4, 9, 2, 8]

for num in nums:
  sll.appendlist(num)

# create cycle
curr_node = sll.head
last = curr_node
while last.next:
  last = last.next
last.next = curr_node.next.next

## brute force solution
# curr_node = sll.head
# st = set()
# cycle = False
# while curr_node:
#   if curr_node in st:
#     cycle = True
#     break
#   st.add(curr_node)
#   curr_node = curr_node.next
# print("cycle started at:", curr_node) if cycle else print("cycle not present")

## Optimal solution
slow = sll.head
fast = sll.head
cycle = False
while fast and fast.next:
  slow = slow.next
  fast = fast.next.next
  if slow == fast:
    cycle = True
    break
if cycle:
  slow = sll.head
  while slow != fast:
    slow = slow.next
    fast = fast.next
  print("cycle started at:", slow.data)
else:
  print("cycle is not present!")