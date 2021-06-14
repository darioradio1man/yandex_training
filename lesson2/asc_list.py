def is_ascending_list(A):
    return all(A[i-1] < A[i] for i in range(1, len(A)))


the_list = list(map(int, input().split()))
print("YES" if is_ascending_list(the_list) else "NO")
