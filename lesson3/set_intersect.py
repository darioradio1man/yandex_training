def set_intersection(a: list, b: list) -> set:
    return sorted(set(a).intersection(set(b)))


list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
print(*set_intersection(list1, list2))
