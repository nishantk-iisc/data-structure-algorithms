# Selection Sort
nums = [5, 7, 8, 4, 1, 6, 9, 2]

# Ascending Order --> TC - O(n^2), SC - O(1)
# for i in range(len(nums)):  
#   print(i)
#   min_idx = i
#   for j in range(i+1, len(nums)):
#     if nums[min_idx] > nums[j]:
#       min_idx = j
#   nums[i], nums[min_idx] = nums[min_idx], nums[i]

# print(nums)

# Descending Order 
for i in range(len(nums)):  
  print(i)
  max_idx = i
  for j in range(i+1, len(nums)):
    if nums[max_idx] < nums[j]:
      max_idx = j
  nums[i], nums[max_idx] = nums[max_idx], nums[i]

print(nums)
