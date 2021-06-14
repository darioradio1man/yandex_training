n, m, k = map(int, input().split())
mines = set(tuple(int(i) - 1 for i in input().split()) for _ in range(k))


def mines_neigbourhood(x, y):
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if i > -1 and j > -1:
                yield i, j


def mines_count(x, y):
    return sum((i, j) in mines for i, j in mines_neigbourhood(x, y))


for i in range(n):
    for j in range(m):
        if (i, j) not in mines:
            print(mines_count(i, j), end=' ')
        else:
            print('*', end=' ')
    print()
