def generate(numRows: int) -> list[list[int]]:
    res = [[1]]
    for i in range(numRows-1):
        temp = [0] + res[-1] + [0]
        sub_arr = []
        for j in range(1, len(temp)):
            sub_arr.append(temp[j-1] + temp[j])
        res.append(sub_arr)
    return res

res = generate(5)
print(res)