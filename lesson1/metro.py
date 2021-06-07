def waiting_metro_in_minutes(a, b, n, m):
    min_way1 = (a + 1) * n - a
    max_way1 = (a + 1) * n + a
    min_way2 = (b + 1) * m - b
    max_way2 = (b + 1) * m + b
    total_min, total_max = max(min_way1, min_way2), min(max_way1, max_way2)
    if total_min > total_max:
        print(-1)
    else:
        print(total_min, total_max)


a1, b1, m1, n1 = int(input()), \
                 int(input()), \
                 int(input()), \
                 int(input())
waiting_metro_in_minutes(a1, b1, m1, n1)
