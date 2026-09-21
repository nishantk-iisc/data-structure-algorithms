nums = [5, 3, 2, 1, 3, 3, 7, 2, 2]

# Time complexity: O(n+k) where k is the range of data
# Space: O(k)
# Note: Positive arrays only

def counting_sort(arr):
    n = len(arr)
    N = max(arr)
    count = [0]* (N+1)
    for i in nums:
        count[i] = count[i] + 1

    i = 0
    for c in range(len(count)):
        while count[c] > 0:
            arr[i] = c
            i += 1
            count[c] -= 1

    print(arr)
        
counting_sort(nums)