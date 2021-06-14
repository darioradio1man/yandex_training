def most_common_word(counter):
    m, word = 0, ''
    for key, value in counter.items():
        if value > m:
            m, word = value, key
        elif value == m:
            if key < word:
                word = key
    return word


txt = open('input.txt').read().split()
dct = {}
for words in txt:
    if words in dct:
        dct[words] += 1
    else:
        dct[words] = 1
print(most_common_word(dct))
