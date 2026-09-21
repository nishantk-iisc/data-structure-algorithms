from singlyLinkedList import SinglyLinkedList
sll = SinglyLinkedList()
arr = [1, 3, 4, 7, 1, 2, 6]
N = 7
for num in arr:
  sll.appendlist(num)

sll.traversal()

## Brute force solution
# curr_node = sll.head
# length = 0
# while curr_node:
#   length += 1
#   curr_node = curr_node.next

# if length == N:
#   sll.head = sll.head.next
# else:
#   N = length - N
#   curr_node = sll.head
#   for i in range(N-1):
#     curr_node = curr_node.next
#   curr_node.next = curr_node.next.next

# sll.traversal() 

## Optimal Solution
first, second = sll.head, sll.head

for i in range(N):
  first = first.next

if first is None:
  sll.head = sll.head.next
else:
  while first.next:
    first = first.next
    second = second.next
  second.next = second.next.next

sll.traversal()