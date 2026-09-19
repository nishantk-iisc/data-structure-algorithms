nums = [5, 1, 6, 8, 2, 4, 9, 0]

# Complexity 
# Worst Case - TC = O(n), SC = O(1)
# Best Case - Array already sorted - TC = O(n), SC = O(1)

n = len(nums)
for i in range(n, -1, -1):
    for j in range(0, i-1):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
    
print(nums)


# def bubble_sort(arr):
#     n = len(arr)
#     flag = True
#     while flag:
#         flag = False
#         for i in range(1, n):
#             if arr[i-1] > arr[i]:
#                 flag = True
#                 arr[i-1], arr[i] = arr[i], arr[i-1]

# bubble_sort(nums)
# print(nums)

