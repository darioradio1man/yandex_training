def word_counter(file):
    counts = {}
    results = []
    words = [x.strip() for x in open(file, 'r', encoding='utf-8').read().split()]
    for word in words:
        counts.setdefault(word, 0)
        results.append(counts[word])
        counts[word] += 1
    return results


print(*word_counter('input.txt'))
