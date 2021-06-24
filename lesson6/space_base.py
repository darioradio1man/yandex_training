def get_max_area(n, a, b, w, h):
    left, right = 0, min(w, h) + 1
    while left + 1 < right:
        mid = (left + right) // 2
        ad, bd = a + 2 * mid, b + 2 * mid
        ac, bc = w // ad, h // bd
        if ac * bc >= n:
            left = mid
        else:
            right = mid
    return left


n1, a1, b1, w1, h1 = map(int, input().split())
p1 = get_max_area(n1, a1, b1, w1, h1)
p2 = get_max_area(n1, b1, a1, w1, h1)
print(max(p1, p2))
