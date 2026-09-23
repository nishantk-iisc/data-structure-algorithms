nums = [-4, -1, 0, 3, 10]
# output = [0, 1, 9, 16, 100]

def sortedSquares(nums):
    left = 0
    right = len(nums) - 1
    result = []
    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            result.append(nums[left]**2)
            left += 1
        else:
            result.append(nums[right]**2)
            right -= 1
    
    result.reverse()
    return result

print(sortedSquares(nums))


# Time: O(n)
# Space: O(n)
