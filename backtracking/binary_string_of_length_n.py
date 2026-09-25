"""
    Find all possible solution or a valid solution among many possibilities.
    Example: 1
        nums = [1, 2, 3]
        output => Generate all possible arrangements -> [123, 132, 213, 231, 312, 321]
    
    Example: 2
        nums = [0, 1]
        output => [00, 01, 10, 11]
"""

# def generate(n):
#     result = []

#     def backtrack(path):
#         if len(path) == n:
#             result.append(path)
#             return

#         for choice in ["0", "1"]:
#             backtrack(path + choice)

#     backtrack("")
#     return result

# print(generate(2))



## Actual backtracking step

def generate(n):
    result = []

    def backtrack(path):
        if len(path) == n:
            result.append(path.copy())
            return
        
        for choice in [0, 1]:
            path.append(choice)
            backtrack(path)
            path.pop()
        
    backtrack([])
    return result

print(generate(2))