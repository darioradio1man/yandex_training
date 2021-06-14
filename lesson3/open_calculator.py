def open_calc(x: int, y: int, z: int, count: int) -> int:
    set1 = {x, y, z}
    set2 = set(map(int, str(count)))
    if set1 == set2:
        return 0
    return len(set2.difference(set1))


a, b, c = map(int, input().split())
num = int(input())
print(open_calc(a, b, c, num))
