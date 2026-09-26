nums = [-4, -2, 1, 0, 4, 8]
# output = 1

## nums = [2, -1, 1]
# output = 1

def findClosetNumber(nums):
    closest = nums[0]

    for x in nums:
        if abs(x) < abs(closest):
            closest = x

    if closest < 0 and abs(closest) in nums:
        return abs(closest)
    else:
        return closest
    
print(findClosetNumber(nums))

# Time : O(n)
# Space: O(1) 