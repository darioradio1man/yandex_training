def max_product_with_three_nums(lst):
    max_nums = lst[:3]
    max_nums.sort()
    max_nums[0] = int(max_nums[0])
    max_nums[1] = int(max_nums[1])
    max_nums[2] = int(max_nums[2])

    min_nums = lst[:2]
    min_nums.sort(reverse=True)
    min_nums[0] = int(min_nums[0])
    min_nums[1] = int(min_nums[1])

    for i in range(2, len(lst)):
        lst[i] = int(lst[i])
        if i > 2:
            if lst[i] > max_nums[2]:
                max_nums[0], max_nums[1], max_nums[2] = max_nums[1], \
                                                        max_nums[2], lst[i]
            elif max_nums[1] < lst[i] <= max_nums[2]:
                max_nums[0], max_nums[1] = max_nums[1], lst[i]

            elif max_nums[0] < lst[i] <= max_nums[1]:
                max_nums[0] = lst[i]

        if lst[i] < min_nums[0]:
            min_nums[0], min_nums[1] = min_nums[1], lst[i]
        elif min_nums[0] < lst[i] < min_nums[1]:
            min_nums[1] = lst[i]

    if min_nums[0] < 0 and min_nums[1] < 0 and len(lst) > 3:
        if max_nums[0] * max_nums[1] * max_nums[2] \
                > min_nums[0] * min_nums[1] * max_nums[0]:
            print(max_nums[0], max_nums[1], max_nums[2])
        else:
            print(min_nums[0], min_nums[1], min_nums[2])
    else:
        print(max_nums[0], max_nums[1], max_nums[2])


the_list = list(map(int, input().split()))
max_product_with_three_nums(the_list)
