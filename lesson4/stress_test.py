def test_dictionary(n):
    errors = 0
    accents = dict()
    for i in range(n):
        word = input()
        base_form = word.lower()
        if base_form not in accents:
            accents[base_form] = set()
        accents[base_form].add(word)
    for word in input().split():
        base_form = word.lower()
        if (base_form in accents and word not in accents[base_form]
                or len([l for l in word if l.isupper()]) != 1):
            errors += 1
    return errors


n1 = int(input())
print(test_dictionary(n1))
