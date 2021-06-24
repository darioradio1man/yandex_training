from collections import *


def trees_interval(n, k, lst):
    left = 0
    segments = Counter()
    best_resolutions = [0, n]

    for right, color in enumerate(lst):
        segments[color] += 1
        if len(segments) == k:
            while segments[lst[left]] > 1:
                segments[lst[left]] -= 1
                left += 1
            if right - left < best_resolutions[1] - best_resolutions[0]:
                best_resolutions = (left, right)
    return best_resolutions[0] + 1, best_resolutions[1] + 1


n1, k1 = map(int, input().split())
lst1 = list(map(int, input().split()))
print(*trees_interval(n1, k1, lst1))
