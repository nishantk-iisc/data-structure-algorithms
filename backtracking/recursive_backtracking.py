"""
    - make decisions
    - recusion
    - base case
    - undo decisions

    => backtracking -> try something -> explore -> undo it -> try something else.
"""


## leetcode problem 78. subsets

## unique elements, return all possible subsets ==> (the power set)

nums = [1, 2, 3]
# output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

# def _subsets(nums):
#     n = len(nums)
#     res, sol= [], []

#     def backtrack(i):
#         if i == n:
#             res.append(sol[:])
#             return

#         # Don't pick nums[i]
#         backtrack(i+1)
    
#         # Pick nums[i]
#         sol.append(nums[i])
#         backtrack(i+1)
#         sol.pop()

#     backtrack(0)
#     return res

# print(_subsets(nums))

# ## time : O(2^n)
# ## space: O(n)

def _subsets(nums):
    result = []

    def backtrack(index, path):
        if index == len(nums):
            result.append(path.copy())
            return
        
        backtrack(index + 1, path)
        
        path.append(nums[index])
        backtrack(index + 1, path)
        path.pop()
    
    backtrack(0, [])
    return result

print(_subsets(nums))