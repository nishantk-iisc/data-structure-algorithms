import random
nums = [random.randint(0, 21) for _ in range(0, 21)]
nums.sort()
print(nums)
target = random.sample(nums, 1)[0]
print(f"target: {target}")
n = len(nums)
low, high = 0, n-1

while low <= high:
  mid = (low + high)//2
  if nums[mid] == target:
    print(mid)
    break
  elif nums[mid] > target:
    high = mid - 1
  else:
    low = mid + 1
