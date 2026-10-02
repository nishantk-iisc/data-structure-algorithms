intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
# output: [[1, 6], [8, 10], [15, 18]]

def mergeIntervals(intervals):
    intervals.sort(key=lambda interval: interval[0])
    merged = []
    
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1] = [merged[-1][0], max(merged[-1][1], interval[1])]
        
    return merged

print(mergeIntervals(intervals))

# Time: O(n log n)
# Space: O(n)