def count_of_numbers(the_list: list) -> int:
    return len(set(the_list))


list1 = list(map(int, input().split()))
print(count_of_numbers(list1))
