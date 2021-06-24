n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for num in b:
    l, r = 0, n - 1
    while r - l > 1:
        m = (r + l) // 2
        if a[m] < num:
            l = m
        else:
            r = m
    if num - a[l] <= a[r] - num:
        print(a[l])
    else:
        print(a[r])
