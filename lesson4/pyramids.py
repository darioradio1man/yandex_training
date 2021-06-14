dicts = {}

for a in range(int(input())):
    h, w = map(int, input().split(" "))
    dicts[h] = max(dicts.get(h, w), w)
print(sum(dicts.values()))
