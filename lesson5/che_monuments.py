def monuments(num_of_monuments, dist, lst):
    i, j, count = 0, 1, 0
    while j < len(lst) and i < len(lst) - 1:
        if lst[j] - lst[i] <= dist:
            j += 1
        else:
            count += num_of_monuments - j
            i += 1
    return count


n, r = map(int, input().split())
a = list(map(int, input().split()))
print(monuments(n, r, a))
