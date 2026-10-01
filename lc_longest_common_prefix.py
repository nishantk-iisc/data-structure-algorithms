# strs = ["flower", "flow", "flight"]
# output = "fl"

strs = ["dog", "racecar", "car"]
# output = ""

def longestCommonPrefix(strs):
    min_length = float('inf')
    for s in strs:
        if len(s) < min_length:
            min_length = len(s)

    i = 0
    while i < min_length:
        for s in strs:
            if s[i] != strs[0][i]:
                return s[:i]
        i += 1
    if strs[0] == "":
        return ""

    return s[:i]
print(longestCommonPrefix(strs))


# Time: O(n*m)
# Space: O(1)