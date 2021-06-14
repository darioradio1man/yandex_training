def is_weakly_ascending(A):
    checker_element = A[0]
    for i in range(1, len(A)):
        if A[i] >= checker_element:
            checker_element = A[i]
        else:
            return 0
    return "WEAKLY ASCENDING"


def is_weakly_descending(A):
    checker_element = A[0]
    for i in range(1, len(A)):
        if A[i] <= checker_element:
            checker_element = A[i]
        else:
            return 0
    return "WEAKLY DESCENDING"


def list_type(A):
    if all(A[i-1] < A[i] for i in range(1, len(A))):
        return "ASCENDING"
    elif all(A[i-1] == A[i] for i in range(1, len(A))):
        return "CONSTANT"
    elif all(A[i-1] > A[i] for i in range(1, len(A))):
        return "DESCENDING"
    elif is_weakly_ascending(A) != 0:
        return "WEAKLY ASCENDING"
    elif is_weakly_descending(A) != 0:
        return "WEAKLY DESCENDING"
    return "RANDOM"


matrix = []
while True:
    num = int(input())
    if num == -2 * 10 ** 9:
        break
    try:
        matrix.append(num)
    except:
        break

print(list_type(matrix))
