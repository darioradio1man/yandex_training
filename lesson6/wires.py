def wires_nums(num, length):
    lst = []
    l, r = 0, 10 ** 7 + 1
    for i in range(num):
        lst.append(int(input()))
    while l + 1 < r:
        m = (l + r) // 2
        count = 0
        for x in lst:
            count += x // m
        if count >= length:
            l = m
        else:
            r = m
    return l

n, k = map(int, input().split())
print(wires_nums(n, k))
