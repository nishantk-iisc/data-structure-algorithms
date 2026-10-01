# sorted unique integer array nums.
nums = [0, 1, 2, 4, 5, 7]
# output: ["0->2", "4->5", "7"]

def summaryRanges(nums):
    ans = []
    n = len(nums)

    i = 0
    while i < n:
        start = nums[i]

        while i < n-1 and nums[i]+1 == nums[i+1]:
            i += 1
        
        if start != nums[i]:
            ans.append(str(start) + '->' + str(nums[i]))
        else:
            ans.append(str(nums[i]))
        i += 1
    
    return ans

print(summaryRanges(nums))
