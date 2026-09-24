## fixed length sliding window problem

nums = [1, 12, -5, -6, 50, 3]
k = 4

# output : 12.7500 => (12  - 5 - 6 + 50) / 4 => 51/4 => 12.7500


def findMaxAverage(nums, k):
    n = len(nums)
    cur_sum = 0
    for i in range(k):
        cur_sum += nums[i]
    
    max_avg = cur_sum / k

    for i in range(k, n):
        cur_sum += nums[i]
        cur_sum -= nums[i-k]

        avg = cur_sum / k
        max_avg = max(max_avg, avg)
    return max_avg

print(findMaxAverage(nums, k))