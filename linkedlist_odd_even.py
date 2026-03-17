from singlyLinkedList import SinglyLinkedList
sll = SinglyLinkedList()
arr = [8, 7, 1, 5, 6, 4, 9]
for num in arr:
  sll.appendlist(num)
sll.traversal()

## brute force solution
# curr_node = sll.head
# odd = []
# even = []
# count = 1

# while curr_node:
#   if count % 2:
#     odd.append(curr_node.data)
#   else:
#     even.append(curr_node.data)
#   curr_node = curr_node.next
#   count += 1

# curr_node = sll.head
# for num in odd:
#   curr_node.data = num
#   curr_node = curr_node.next
# for num in even:
#   curr_node.data = num
#   curr_node = curr_node.next
# sll.traversal() 

## Optimal solution

if not sll.head or not sll.head.next:
  sll.traversal()
else:
  odd = sll.head
  even = odd.next
  even_head = even
  while even and even.next:
    odd.next =  odd.next.next
    even.next = even.next.next
    odd = odd.next
    even = even.next
  odd.next = even_head
  sll.traversal()

  
