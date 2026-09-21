from singlyLinkedList import SinglyLinkedList
sll = SinglyLinkedList()
arr = [5, 10, 27, 3, 99, 1]
for num in arr:
  sll.appendlist(num)
sll.traversal()
curr_node = sll.head

## brute force solution
# count = 0
# while curr_node:
#   count += 1
#   curr_node = curr_node.next
# mid = count // 2
# curr_node = sll.head
# for i in range(0, mid):
#   curr_node = curr_node.next
# print(curr_node.data)

## Optimal Solution
slow = curr_node
fast = curr_node
while fast and fast.next:
  fast = fast.next.next
  slow = slow.next
print(slow.data)