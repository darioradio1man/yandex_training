n, x, y = map(int, input().split())
left, right = 0, (n - 1) * max(x, y)
while right - left > 1:
    mid = (right + left) // 2
    res = (mid // x) + (mid // y)
    if res < n - 1:
        left = mid
    else:
        right = mid
print(right + min(x, y))
