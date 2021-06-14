def pigs(n):
    s = set()
    for i in range(n):
        inpt = list(map(int, input().split()))
        s.add(inpt[0])
    return len(list(s))


x = int(input())
print(pigs(x))
