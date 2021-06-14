def turtles_truth(n: int) -> int:
    count = 0
    s = set()
    for _ in range(n):
        s.add(input())
    for i in s:
        j = list(map(int, i.split()))
        if j[0] + j[1] == n - 1 and j[0] >= 0 and j[1] >= 0:
            count += 1
    return count


n1 = int(input())
print(turtles_truth(n1))
