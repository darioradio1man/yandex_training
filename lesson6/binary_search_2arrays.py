def binary_search(this_list, key: int):
    step = 0
    left = 0
    right = len(this_list) - 1
    while left <= right:
        step += 1
        mid = (left+right)//2
        if key == this_list[mid]:
            return 'YES'
        if key > this_list[mid]:
            left = mid+1
        else:
            right = mid-1
    return 'NO'


def checker(list1, list2):
    checked = {}
    result = []
    for number in list2:
        if number in checked:
            result.append(checked[number])
            continue
        checked[number] = binary_search(list1, number)
        result.append(checked[number])
    return '\n'.join(result)


with open('input.txt') as file:
    lines = file.readlines()
    n, k = map(int, lines[0].split())
    first_list = sorted([int(number) for number in lines[1].split()])
    second_list = [int(number) for number in lines[2].split()]


with open('output.txt', 'w') as file:
    file.write(checker(first_list, second_list))

