arr = [-1, 0, 1, 2, -1, -4]
n = len(arr)
## Brute Force
# my_set = set()
# for i in range(0, n):
#   for j in range(i+1, n):
#     for k in range(j+1, n):
#       if arr[i] + arr[j] + arr[k] == 0:
#         temp = [arr[i], arr[j], arr[k]]
#         temp.sort()
#         my_set.add(tuple(temp))
# print(my_set)

## Better Solution
result = set()
for i in range(0, n):
  my_set = set()
  for j in range(i+1, n):
    my_set.add(arr[j])
    val = -(arr[i] + arr[j])
    if val in my_set:
      temp = [arr[i], arr[j], val]
      temp.sort()
      result.add(tuple(temp))

print(result) 