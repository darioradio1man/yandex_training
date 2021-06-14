def bill(x):
    tmp = {}
    for i in x:
        prod, count = i
        if prod in tmp:
            tmp[prod] += int(count)
        else:
            tmp[prod] = int(count)
    return tmp


base = {}
while True:
    try:
        human, product, counts = input().split()
        if human in base:
            base[human].append((product, counts))
        else:
            base[human] = [(product, counts)]
    except:
        break

for i in sorted(base):
    print(i+':')
    for x, i in sorted(bill(base[i]).items()):
        print(x, i)
