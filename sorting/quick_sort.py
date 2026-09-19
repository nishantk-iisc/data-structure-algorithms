nums = [6, 8, 2, 5, 7, 0, 1, 3, 4, 9]

'''
Complexity
- TC = O(n^2)     - Worst Case
- TC = O(nlogn)   - Best and Average Case
- SC = O(log n)   - Average Case
- SC = O(n)       - Worst Case
'''

def partition(array, low, high):
    i, j = low, high
    pivot = array[low]

    while i < j:
        while i <= high - 1 and array[i] <= pivot:
            i += 1
        while j >= low + 1 and array[j] > pivot:
            j -= 1
        if i < j:
            array[i], array[j] = array[j], array[i]

    array[low], array[j] = array[j], array[low]

    return j


def qs(nums, low, high):
    if low < high:
        p_idx = partition(nums, low, high)
        qs(nums, low, p_idx - 1)
        qs(nums, p_idx + 1, high)

    return nums

print(qs(nums, 0, len(nums) - 1))