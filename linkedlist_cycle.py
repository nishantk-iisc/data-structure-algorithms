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

## Brute force
# st = set()
# cycle = False
# while curr_node:
#   if curr_node in st:
#     cycle = True
#     break  
#   st.add(curr_node)
#   curr_node = curr_node.next

# print(curr_node.data) if cycle else print("no cycle present")

## Optimal soution
slow = sll.head
fast = sll.head
cycle = False
while fast and fast.next:
  slow = slow.next
  fast = fast.next.next
  if slow == fast:
    print(slow.data, fast.data)
    cycle = True
    break

print("cycle is present.") if cycle else print("no cycle present")