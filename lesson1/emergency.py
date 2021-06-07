k1, m, k2, p2, n2 = map(int, input().split())

if m != 1:
    for i in range(500):
        if i != 0 and n2 == ((k2 - 1) // i) + 1:
            p1 = (((k1 - 1) // i) // (m - 1)) + 1
            n1 = (((k1 - 1) // i) % (m - 1))
else:
    n1 = 1
    for i in range(500):
        if i != 0:
            while k1 % i != 0:
                k1 = k1 + 1
                p1 = k1 // i

if k2 < p2 * n2 or n2 > m or k2 // p2 < m:
    p1, n1 = -1, -1
if p2 == 1 and n2 == 1:
    p1 = -1
print(p1, n1)
