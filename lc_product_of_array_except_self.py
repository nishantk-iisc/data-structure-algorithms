nums = [1, 2, 3, 4]
# output: [24, 12, 8, 6]

# nums = [-1, -1, 0, -3, -3]
# output: [0, 0, 9, 0, 0]

def productExceptSelf(nums):
    ## Brute force: Time: O(N*2), Space: O(N)
    # ans = []
    # for i in range(len(nums)):
    #     val = 1
    #     for j in range(len(nums)):
    #         if i != j:
    #             val *= nums[j]
    #     ans.append(val)
    # return ans
    

    ## Optimal Solution: Time: O(N), Space: O(N)
    l_mult = 1
    r_mult = 1
    n = len(nums)
    l_arr = [0]*n
    r_arr = [0]*n

    for i in range(n):
        j = -i - 1
        l_arr[i] = l_mult
        r_arr[j] = r_mult
        l_mult *= nums[i]
        r_mult *= nums[j]

    return [l*r for l, r in zip(l_arr, r_arr)]
 


print(productExceptSelf(nums))
