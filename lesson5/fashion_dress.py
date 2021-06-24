def closest_pair(arr_x, arr_y):
    i, j, min_arr_x, min_arr_y = 0, 0, -1, -1
    n, m = len(arr_x), len(arr_y)
    the_min = arr_x[n - 1] + arr_y[m - 1]
    while i < n and j < m:
        if abs(arr_x[i] - arr_y[j]) < the_min:
            the_min = abs(arr_x[i] - arr_y[j])
            min_arr_x, min_arr_y = arr_x[i], arr_y[j]
        if arr_x[i] > arr_y[j]:
            j += 1
        else:
            i += 1
    return min_arr_x, min_arr_y


n1 = int(input())
arr1 = list(map(int, input().split()))

m1 = int(input())
arr2 = list(map(int, input().split()))
print(*closest_pair(arr1, arr2))
