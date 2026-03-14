# nums = [2,7,11,15]
# target = 9

nums = [3,3]
target = 6
n = len(nums)
# hash = dict()
# for i in range(n):
#   val = target - nums[i]
#   if val in hash:
#     ans = [hash[val], i]
#   hash[nums[i]] = i
# print(ans)

for i in range(n):
  for j in range(i+1, n):
    if nums[i] + nums[j] == target:
      temp = [i, j]
print(temp)