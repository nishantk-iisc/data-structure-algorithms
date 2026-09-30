## 2 string s and t => true if s is a subsequence of t or false otherwise.

# s, t = "abc", "ahbgdc"
s, t = "axc", "abcdef"

def isSubsequence(s, t):
    S = len(s)
    T = len(t)

    if s == "": return true
    if S > T: return false

    j = 0
    for i in range(T):
        if t[i] == s[j]:
            if j == S-1:
                return True 
            j += 1

    return False 

print(isSubsequence(s, t))

# Time: O(T)
# Space: O(1)