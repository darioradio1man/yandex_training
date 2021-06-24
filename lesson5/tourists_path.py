def tourists(pts, tr):
    the_results = []
    left = [0] + [None] * (len(pts) - 1)
    right = [None] * (len(pts) - 1) + [0]
    for i in range(1, len(pts)):
        left[i] = left[i - 1] + max(pts[i][1] - pts[i - 1][1], 0)
        right[len(pts) - i - 1] =\
            right[len(pts) - i] + max(pts[len(pts) - i - 1][1] - pts[len(pts) - i][1], 0)
    for track in tr:
        if track[0] < track[1]:
            the_results.append(left[track[1] - 1] - left[track[0] - 1])
        else:
            the_results.append(right[track[1] - 1] - right[track[0] - 1])
    return the_results


n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
m = int(input())
tracks = [tuple(map(int, input().split())) for _ in range(m)]
results = tourists(points, tracks)
for result in results:
    print(result)
