def unique_cubes(a: list, b: list):
    print(len(set(a).intersection(b)))
    set_inter = sorted(set(a).intersection(b))
    print(*set_inter)
    print(len(set(a).difference(set(b))))
    diff1 = sorted(set(a).difference(set(b)))
    print(*diff1)
    print(len(set(b).difference(set(a))))
    diff2 = sorted(set(b).difference(set(a)))
    print(*diff2)


m, n = map(int, input().split())
a1, b1 = [], []
for i in range(m):
    a1.append(int(input()))
for i in range(n):
    b1.append(int(input()))
unique_cubes(a1, b1)
