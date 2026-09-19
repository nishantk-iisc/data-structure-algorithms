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


# def insertion_sort(arr):
#     n = len(arr)
#     for i in range(1, n):
#         for j in range(i, 0, -1):
#             if arr[j-1] > arr[j]:
#                 arr[j-1], arr[j] = arr[j], arr[j-1]
#             else: 
#                 break

# insertion_sort(nums)
# print(nums)
