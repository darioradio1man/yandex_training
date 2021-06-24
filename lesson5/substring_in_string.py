def substring(num: int, k: int, word: str):
    the_dict = dict.fromkeys(word, 0)
    temp_left, temp_right = 0, 0
    left_bound, right_bound = 0, 0
    while temp_right < num:
        if the_dict[word[temp_right]] < k:
            if temp_right - temp_left > right_bound - left_bound:
                left_bound, right_bound = temp_left, temp_right
            the_dict[word[temp_right]] += 1
            temp_right += 1
        else:
            temp_left = temp_right - k + 1
            the_dict = dict.fromkeys(the_dict, 0)
    return right_bound - left_bound + 1, left_bound + 1


n, k1 = map(int, input().split())
s = input()
print(*substring(n, k1, s))
