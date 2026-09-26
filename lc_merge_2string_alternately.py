word1 = "abc"
word2 = "pqrst"
# output = "apbqcrst"

def mergeAlternately(word1, word2):
    a, b = 0, 0
    A, B = len(word1), len(word2)
    result = []
    while a < A and b < B:
        if word1[a] < word2[b]:
            result.append(word1[a])
            a += 1
        else:
            result.append(word2[b])
            b += 1
    while a < A:
        result.append(word1[a])
        a += 1
    while b < B:
        result.append(word2[b])
        b += 1

    return "".join(result)

print(mergeAlternately(word1, word2))

# Time: O(A + B)
# Space: O(A + B)