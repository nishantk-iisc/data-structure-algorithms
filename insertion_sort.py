nums = [3, 5, 6, 4, 8, 9, 10, 7, 1, 0, 2]

'''
Complexity 
- Worst Case - TC = O(n^2), SC = O(1)
- Best Case - TC = O(n), SC = O(1)
'''


for i in range(len(nums)):
  key = nums[i]
  j = i - 1
  while j>=0 and nums[j] > key:
    nums[j+1] = nums[j]
    j = j - 1
  nums[j+1] = key
print(nums)
