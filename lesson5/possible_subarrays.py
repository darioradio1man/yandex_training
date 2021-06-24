def nums_of_subarray_for_required_sum(lst, x):
    count, curr_sum, start, i = 0, lst[0], 0, 1
    while i <= len(lst):
        while curr_sum > x and start < i - 1:
            curr_sum = curr_sum - lst[start]
            start += 1
        if curr_sum == x:
            count += 1
        if i < len(lst):
            curr_sum = curr_sum + lst[i]
        i += 1
    return count


nums, y = map(int, input().split())
lst_new = list(map(int, input().split()))
print(nums_of_subarray_for_required_sum(lst_new, y))
