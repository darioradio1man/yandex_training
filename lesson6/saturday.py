n, r, c = map(int, input().split())
human_size = sorted([int(input()) for line in range(n)])
num = [human_size[i + c - 1] - human_size[i]
       for i in range(len(human_size) - c + 1)]


def results(the_count):
    h, u = 0, 0
    for i in range(len(num)):
        u -= 1
        if u < 1 and num[i] <= the_count:
            h += 1
            u = c
    if h >= r:
        return True
    return False


left = -1
right = human_size[-1] - human_size[0]
if r > 1:
    while left + 1 != right:
        mid = (left + right) // 2
        if results(mid):
            right = mid
        else:
            left = mid
    print(right)
else:
    print(min(num))
