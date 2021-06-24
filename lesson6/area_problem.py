k = 0
n, m, t = int(input()), \
          int(input()), \
          int(input())
while t > 0 and n > 0 and m > 0:
    t -= (n - 2) * 2 + m * 2
    n -= 2
    m -= 2
    k += 1
if t == 0:
    print(k)
else:
    print(k - 1)
