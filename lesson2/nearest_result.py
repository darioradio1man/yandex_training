def nearest_count(the_list, value):
    found = the_list[0]
    for items in the_list:
        if abs(items - value) < abs(found - value):
            found = items
    return found


n = int(input())
lst = list(map(int, input().split()[:n]))
x = int(input())
print(nearest_count(lst, x))

