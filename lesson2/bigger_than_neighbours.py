def count_of_bigger_than_neighbours(lst):
    counter = 0
    for i in range(1, len(lst) - 1):
        if a[i - 1] < a[i] > a[i + 1]:
            counter += 1
    return counter


a = [int(a) for a in input().split()]
print(count_of_bigger_than_neighbours(a))
