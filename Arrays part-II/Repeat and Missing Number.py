from collections import Counter
def repeatedNumber(A):
    res = [0, 0]
    n = 1
    c = dict(Counter(A))
    n = 1
    for item in c:
        if c[item] >= 2:
            res[0] = item
    # checking for the missing number in A
    while n in c:
        n += 1
    res[1] = n
    return res

A = [3, 1, 2, 5, 3]
# Output:[3, 4] 
res = repeatedNumber(A=A)
print(res)