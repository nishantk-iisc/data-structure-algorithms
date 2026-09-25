# 0, 1, 1, 2, 3, 5, 8, 13 ...

# F(0) = 0, F(1) = 1 
# F(2) = F(0) + F(1) => 0 + 1 => 1 ...
import time
s = time.time()
## Recursive Solution
def fib(n):
    if n == 0: 
        return 0
    if n == 1: 
        return 1
    return(fib(n-2) + fib(n-1))

print(fib(6))
print(f"recursive: {(time.time() - s)} ms")

# Top Down Memoization  ==> Hash Map or dict ( cache )
#     Function calls 
#         f(4)   => 2^0
#         /   \
#     f(2)     f(3)  => 2^1
#     /   \    /   \
#  f(0)   f(1) f(2) f(3)  => 2^2

s = time.time()
def tp_dp_fib(n):
    memo = {0:0, 1:1}

    def f(x):
        if x in memo:
            return memo[x]
        else:
            memo[x] = f(x-1) + f(x-2)
            return memo[x]
    return f(n)

print(tp_dp_fib(6))
print(f"top down dp: {(time.time() - s)} ms")

# # Time : O(n)
# # Space: O(n)    

s = time.time()
## Bottom Up - tabulation
def bu_dp_fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    dp = [0]*(n+1)
    dp[0] = 0
    dp[1] = 1
    
    for i in range(2, n+1):
        dp[i] = dp[i-2] + dp[i-1]
    return dp[n]

print(bu_dp_fib(6))
print(f"bottom up dp: {(time.time() - s)} ms")

# # Time : O(n)
# # Space: O(n)    
