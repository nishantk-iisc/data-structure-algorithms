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
# my_dict = dict()
# travel = 0
# while curr_node and curr_node.next:
#   if curr_node in my_dict:
#     break
#   my_dict[curr_node] = travel
#   travel += 1
#   curr_node = curr_node.next
  
# print(travel - my_dict[curr_node])

## Optimal solution
fast = sll.head
slow = sll.head
cycle = False
while fast and fast.next:
  slow = slow.next
  fast = fast.next.next
  if slow == fast:
    cycle = True
    break
if cycle:
  slow = slow.next
  travel = 1
  while slow != fast:
    slow = slow.next
    travel += 1
  print(travel)
else:
  print("cycle is not present!")