w, h, n = map(int, input().split())
left = max(w, h)
right = left * n
while right - left > 1:
    mid = (right + left) // 2
    res = (mid // w) * (mid // h)
    if res < n:
        left = mid
    else:
        right = mid
print(right)
