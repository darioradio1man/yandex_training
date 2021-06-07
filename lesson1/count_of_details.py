def details_count(n, k, m):
    result = 0
    if m <= k:
        while n >= k:
            num_pattern = int(n / k)
            rest_from_pattern = n % k
            det_from_patten = int(k / m)
            rest_from_details = k % m
            result += num_pattern * det_from_patten
            n = rest_from_pattern + (rest_from_details * num_pattern)
    return result


n1, k1, m1 = map(int, input().split())
print(details_count(n1, k1, m1))
