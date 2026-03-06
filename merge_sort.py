'''
Complexity:
  - TC = O(nlogn)
  - SC = O(n)
'''


def merge_array(left, right):
  result = []
  i, j = 0, 0
  n, m = len(left), len(right)

  while i < n and j < m:
    if left[i] > right[j]:
      result.append(right[j])
      j = j + 1
    else:
      result.append(left[i])
      i = i + 1
  if i < n:
    while i < n:
      result.append(left[i])
      i = i + 1
  if j < m:
    while j < m:
      result.append(right[j])
      j = j + 1  

  return result

def merge_sort(array):
  if len(array) <= 1:
    return array
  mid = len(array) // 2
  left_array = array[:mid]
  right_array = array[mid:]

  left = merge_sort(left_array)
  right = merge_sort(right_array)
  return merge_array(left, right)

print(merge_sort([5, 6, 1, 9, 0, 4, 3, 2, 8, 7]))
