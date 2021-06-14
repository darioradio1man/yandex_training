def alien_genoms_set(a: str, b: str) -> int:
    x1, x2 = set(), set()
    count = 0
    for i in range(len(a) - 1):
        x1.add(a[i:i+2])
    for i in range(len(b) - 1):
        x2.add(b[i:i+2])
    intrsct = x1.intersection(x2)
    for i in range(len(a) - 1):
        if a[i:i+2] in intrsct:
            count += 1
    return count


a1, b1 = input(), input()
print(alien_genoms_set(a1, b1))
