def merge(intervals: list[list[int]]) -> list[list[int]]:
    n = len(intervals)
    intervals.sort(key=lambda x:x[0], reverse=False)
    prev = intervals[0]
    res = []
    for i in range(1, n):
        pres = intervals[i]
        if prev[1] < pres[0]:
            res.append(prev)
            prev = pres
        else:
            if prev[1] >= pres[1]:
                prev = prev
            else:
                prev = [prev[0], pres[1]]
    res.append(prev)
    return res

intervals = [[1,3],[2,6],[8,10],[15,18]] # Output: [[1,6],[8,10],[15,18]]
res = merge(intervals=intervals)
print(res)