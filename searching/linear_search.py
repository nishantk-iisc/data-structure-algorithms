nums = [6, 8, 2, 5, 7, 0, 1, 3, 4, 9]

def linear_search(arr, element):
    n = len(arr)
    for num in arr:
        if element == num:
            return True
    return False

print(linear_search(nums, 2))
