n = int(input())
previous = float(input())
l, r = 30, 4000

for i in range(1, n):
    current, s = input().split()
    current = float(current)
    if current == previous:
        continue
    mid = (current + previous) / 2
    if current > previous and s == 'closer' or \
       current < previous and s != 'closer':
        l = max(l, mid)
    else:
        r = min(r, mid)
    previous = current
print(l, r)
