def synonims_in_dict(dct: dict, word: str) -> str:
    for k in dct:
        if dct[k] == word:
            return k
        elif k == word:
            return dct[k]


new_dict = {}
n = int(input())
for i in range(n):
    key, value = input().split()
    new_dict[key] = value
this_word = input()
print(synonims_in_dict(new_dict, this_word))
